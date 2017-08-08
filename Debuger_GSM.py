#coding: utf8
# import sys, serial
from Form_Debuger_GSM import *
from PyQt5 import QtWidgets #QtCore, QtGui,
from RS_Commands import *
from Application import *
from Conf_Debuger_GSM import *
import Form_Events

class Debuger_GSM(QtWidgets.QMainWindow, Conf_Debuger_GSM):
    # инициализация окна
    # pyuic5 Form_Debuger_GSM.ui -o Form_Debuger_GSM.py
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Conf_Debuger_GSM.__init__(self)
        #инициализация интерфейса
        self.ui = Ui_Debuger_GSM()      #инициализация графического интерфейса
        self.ui.setupUi(self)
        #определяем таймер
        self.timer_RX_RS = QBasicTimer()
        self.timer_RX_RS.stop()
        #подключаем модули
        self.rs = RS_Commands(self)               #подключение функций работы по RS
        self.event = Form_Events.Form_Events(self)   #определение обработчиков событий

        # настройка действий по кнопкам
        self.event.Init_Widgets()

    def analyze_pack(self):
        '''
        #*********************************************************************
        # анализ принятых данных из RS
        #*********************************************************************
        :return:
        '''
        # проверка на стартовую посылку
        if self.rs_receive_pack[0:2] == self.rs.RS_START:
            #показать принятые данные
            self.event.Show_RX_DATA()
            #производим рассчет CRC16 для self.rs_send_pack без последних двух байт
            size, crc_rx, id1, id2, str_data, bin_data, err = Parsing_Rx_Pack(self.rs_receive_pack)
            # проверка была ли ошибка длины в принятых данных
            if err == True:
                return ['Error']
            #вычисляем непосредственно CRC
            crc = INITIAL_MODBUS
            for ch in self.rs_receive_pack[:size-2]:
                crc = calcByte(ch,crc)
            #сравниваем полученное CRC с расчитанным
            if crc == crc_rx:
                #CRC сошлось, проводим проверку тела данных
                if id1 == self.ID1["SETUP_GSM_RESP"]:

                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # чтение/запись вкладки "пользователи"
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    if self.status_new == self.ID2["SIM900_USER_TIMEOUT_READ"] and id2 == self.ID2["SIM900_USER_TIMEOUT_READ"]\
                            or self.status_new == self.ID2["SIM900_USER_TIMEOUT_WRITE"] and id2 == self.ID2["SIM900_USER_TIMEOUT_WRITE"]:
                        # выводим полученные данные в окно вывода
                        tmp = int.from_bytes(bin_data, byteorder='little')
                        self.ui.spinBox_sim900_user_timeout.setValue(tmp)
                        return ['Ok']
                    elif self.status_new == self.ID2["SIM900_USER_PHONE_NUMBER_READ"] and id2 == self.ID2["SIM900_USER_PHONE_NUMBER_READ"]\
                            or self.status_new == self.ID2["SIM900_USER_PHONE_NUMBER_WRITE"] and id2 == self.ID2["SIM900_USER_PHONE_NUMBER_WRITE"]:
                        # выводим полученные данные в окно вывода
                        self.ui.lineEdit_Telephone_Number.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif self.status_new == self.ID2["CONF_ALARM_CALL_READ"] and id2 == self.ID2["CONF_ALARM_CALL_READ"]\
                            or self.status_new == self.ID2["CONF_ALARM_CALL_WRITE"] and id2 == self.ID2["CONF_ALARM_CALL_WRITE"]:
                        # выводим полученные данные в окно вывода
                        self.user_bit_num = Convert_To_User_Num(self.ui.list_users_nom.currentRow(), self.NUM_ABONENTS)
                        self.conf_alarm_call_flags = bin_data   # переменная текущего значения флагов CONF_ALARM_CALL
                        if self.event.Check_Bit(bytearray(reversed(bin_data)), self.user_bit_num):
                            self.ui.checkBox_call_back_alarm.setChecked(1)
                        else:
                            self.ui.checkBox_call_back_alarm.setChecked(0)
                        return ['Ok']
                    elif self.status_new == self.ID2["CONF_ALARM_SMS_READ"] and id2 == self.ID2["CONF_ALARM_SMS_READ"]\
                            or self.status_new == self.ID2["CONF_ALARM_SMS_WRITE"] and id2 == self.ID2["CONF_ALARM_SMS_WRITE"]:
                        # выводим полученные данные в окно вывода
                        self.user_bit_num = Convert_To_User_Num(self.ui.list_users_nom.currentRow(), self.NUM_ABONENTS)
                        self.conf_alarm_sms_flags = bin_data   # переменная текущего значения флагов CONF_ALARM_SMS
                        if self.event.Check_Bit(bytearray(reversed(bin_data)), self.user_bit_num):
                            self.ui.checkBox_SMS_alarm.setChecked(1)
                        else:
                            self.ui.checkBox_SMS_alarm.setChecked(0)
                        return ['Ok']
                    elif self.status_new == self.ID2["CONF_SET_GUARD_SMS_READ"] and id2 == self.ID2["CONF_SET_GUARD_SMS_READ"]\
                            or self.status_new == self.ID2["CONF_SET_GUARD_SMS_WRITE"] and id2 == self.ID2["CONF_SET_GUARD_SMS_WRITE"]:
                        # выводим полученные данные в окно вывода
                        self.user_bit_num = Convert_To_User_Num(self.ui.list_users_nom.currentRow(), self.NUM_ABONENTS)
                        self.sms_set_guard_flags = bin_data   # переменная текущего значения флагов CONF_ALARM_SMS
                        if self.event.Check_Bit(bytearray(reversed(bin_data)), self.user_bit_num):
                            self.ui.checkBox_SMS_set_guard.setChecked(1)
                        else:
                            self.ui.checkBox_SMS_set_guard.setChecked(0)
                        return ['Ok']

                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # чтение/запись вкладки "Входы"
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif self.status_new == self.ID2["ALARM_TEXT_READ"] and id2 == self.ID2["ALARM_TEXT_READ"]\
                            or self.status_new == self.ID2["ALARM_TEXT_WRITE"] and id2 == self.ID2["ALARM_TEXT_WRITE"]:
                        # выводим полученные данные в окно вывода
                        self.ui.lineEdit_in_alarm_text.setText(self.Check_Last_Char(str_data))
                        return ['Ok']

                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # чтение/запись вкладки "СМС"
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif (self.status_new == self.ID2["TEXT_GUARD_SET_READ"] and id2 == self.ID2["TEXT_GUARD_SET_READ"])\
                            or (self.status_new == self.ID2["TEXT_GUARD_SET_WRITE"] and id2 == self.ID2["TEXT_GUARD_SET_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_text_guard_set.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif (self.status_new == self.ID2["CLEAR_ALARM_TEXT_READ"] and id2 == self.ID2["CLEAR_ALARM_TEXT_READ"])\
                            or (self.status_new == self.ID2["CLEAR_ALARM_TEXT_WRITE"] and id2 == self.ID2["CLEAR_ALARM_TEXT_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_clear_alarm_text.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif (self.status_new == self.ID2["SMS_RESET_GUARD_CMD_READ"] and id2 == self.ID2["SMS_RESET_GUARD_CMD_READ"])\
                            or (self.status_new == self.ID2["SMS_RESET_GUARD_CMD_WRITE"] and id2 == self.ID2["SMS_RESET_GUARD_CMD_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_sms_reset_guard_cmd.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif (self.status_new == self.ID2["SMS_SET_GUARD_CMD_READ"] and id2 == self.ID2["SMS_SET_GUARD_CMD_READ"])\
                            or (self.status_new == self.ID2["SMS_SET_GUARD_CMD_WRITE"] and id2 == self.ID2["SMS_SET_GUARD_CMD_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_sms_Set_Guard_Cmd.setText(self.Check_Last_Char(str_data))
                        return ['Ok']

                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    # чтение/запись вкладки "Общие настройки"
                    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif    (self.status_new == self.ID2["MIN_BALANCE_SMS_READ"] and id2 == self.ID2["MIN_BALANCE_SMS_READ"])\
                            or (self.status_new == self.ID2["MIN_BALANCE_SMS_WRITE"] and id2 == self.ID2["MIN_BALANCE_SMS_WRITE"]):
                        # проверка дины полученных данных
                        if len(bin_data) == 2:
                            #обновляем значение в окне вывода
                            self.ui.spinBox_min_balance_SMS.setValue(int.from_bytes(bin_data, byteorder='little'))
                            return ['Ok']
                    elif    (self.status_new == self.ID2["MIN_BALANCE_CALL_READ"] and id2 == self.ID2["MIN_BALANCE_CALL_READ"])\
                            or (self.status_new == self.ID2["MIN_BALANCE_CALL_WRITE"] and id2 == self.ID2["MIN_BALANCE_CALL_WRITE"]):
                        # проверка дины полученных данных
                        if len(bin_data) == 2:
                            #обновляем значение в окне вывода
                            self.ui.spinBox_min_balance_call.setValue(int.from_bytes(bin_data, byteorder='little'))
                            return ['Ok']
                    elif    (self.status_new == self.ID2["GSM_SETUP_U_READ"] and id2 == self.ID2["GSM_SETUP_U_READ"])\
                            or (self.status_new == self.ID2["GSM_SETUP_U_WRITE"] and id2 == self.ID2["GSM_SETUP_U_WRITE"]):
                        # проверка дины полученных данных
                        if len(bin_data) == 4:
                            # установка нужных флагов в окне вывода
                            if self.event.Reload_Widget_General_Page(bin_data) == ['Ok']:
                                return ['Ok']
                    elif    (self.status_new == self.ID2["DTMF_CLEAR_ALARM_CMD_READ"] and id2 == self.ID2["DTMF_CLEAR_ALARM_CMD_READ"])\
                            or (self.status_new == self.ID2["DTMF_CLEAR_ALARM_CMD_WRITE"] and id2 == self.ID2["DTMF_CLEAR_ALARM_CMD_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_dtmf_clear_alarm_cmd.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif    (self.status_new == self.ID2["DTMF_RESET_GUARD_CMD_READ"] and id2 == self.ID2["DTMF_RESET_GUARD_CMD_READ"])\
                            or (self.status_new == self.ID2["DTMF_RESET_GUARD_CMD_WRITE"] and id2 == self.ID2["DTMF_RESET_GUARD_CMD_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_dtmf_reset_guard.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif    (self.status_new == self.ID2["DTMF_SET_GUARD_CMD_READ"] and id2 == self.ID2["DTMF_SET_GUARD_CMD_READ"])\
                            or (self.status_new == self.ID2["DTMF_SET_GUARD_CMD_WRITE"] and id2 == self.ID2["DTMF_SET_GUARD_CMD_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_dtmf_set_guard.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif    (self.status_new == self.ID2["TRAMP_END_READ"] and id2 == self.ID2["TRAMP_END_READ"])\
                            or (self.status_new == self.ID2["TRAMP_END_WRITE"] and id2 == self.ID2["TRAMP_END_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_trump_end.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                    elif    (self.status_new == self.ID2["TRAMP_BEGIN_READ"] and id2 == self.ID2["TRAMP_BEGIN_READ"])\
                            or (self.status_new == self.ID2["TRAMP_BEGIN_WRITE"] and id2 == self.ID2["TRAMP_BEGIN_WRITE"]):
                        #обновляем значение в окне вывода
                        self.ui.lineEdit_trump_begin.setText(self.Check_Last_Char(str_data))
                        return ['Ok']
                else:
                    return ['Error']

            #иначе возвращаем Error
            return ['Error']
        else:
            return ['Error']

    #*********************************************************************
    # обработка событий по таймеру
    #*********************************************************************
    def timerEvent(self, e):
        self.timer_RX_RS.stop() #выключаем таймер
        self.rs_receive_pack = self.rs.Recieve_RS_Data()    #получаем аднные
        #есть ли принятые данные
        if self.rs_receive_pack != '':
            # анализируем полученные данные
            self.result_analyze = self.analyze_pack()
            #данные есть, проверяем что с ними нужно сделать
            if self.result_analyze == ['Ok']:
                if self.status_new == self.ID2["IDLE"]:
                    #ничего не делаем в состоянии IDLE
                    self.flag_rx_ok = False

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # чтение вкладки "Входы"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["ALARM_TEXT_READ"]:
                    #переходим к отправке запроса защитного кода MIN_BALANCE_CALL_READ
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки входов прочитаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим к исходному состоянию IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # запись вкладки "Входы"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["ALARM_TEXT_WRITE"]:
                    #переходим к отправке запроса защитного кода MIN_BALANCE_CALL_READ
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки входов записаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим к исходному состоянию IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # чтение вкладки "Пользователи"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["SIM900_USER_TIMEOUT_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["SIM900_USER_PHONE_NUMBER_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["SIM900_USER_PHONE_NUMBER_READ"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.list_users_nom.currentRow().to_bytes(1,'little'))
                elif self.status_new == self.ID2["SIM900_USER_PHONE_NUMBER_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["CONF_ALARM_CALL_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["CONF_ALARM_CALL_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["CONF_ALARM_CALL_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["CONF_ALARM_SMS_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["CONF_ALARM_SMS_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["CONF_ALARM_SMS_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["CONF_SET_GUARD_SMS_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["CONF_SET_GUARD_SMS_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["CONF_SET_GUARD_SMS_READ"]:
                    #переходим к отправке запроса защитного кода MIN_BALANCE_CALL_READ
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки абонента прочитаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим к исходному состоянию IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # запись вкладки "Пользователи"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["SIM900_USER_TIMEOUT_WRITE"]:
                    # проверяем данные в строке ввода на соответствие номеру
                    text = self.ui.lineEdit_Telephone_Number.text()
                    if text[0] != '+':
                        self.result_analyze = ['Error_First_Char']
                    else:
                        try:
                            for t in text[1:]:# проверяем весь текст кроме первого символа
                                if ((int(t)) >= 0):
                                    continue
                            data_all = bytearray(b'')
                            data_all += self.ui.list_users_nom.currentRow().to_bytes(1,'little') + \
                                        Convert_Str_to_Bytearray(text)
                            # отправляем запрос SIM900_USER_PHONE_NUMBER_WRITE
                            self.result_analyze = self.rs.Send_Command(self.ID2["SIM900_USER_PHONE_NUMBER_WRITE"],
                                                                       self.ID1["SETUP_GSM_REQ"],
                                                                       self.ID2["SIM900_USER_PHONE_NUMBER_WRITE"],
                                                                       self.rs.TIME_TO_RX,
                                                                       data_all)
                        except:
                            self.result_analyze = ['Error_Number']
                elif self.status_new == self.ID2["SIM900_USER_PHONE_NUMBER_WRITE"]:
                    if self.ui.checkBox_call_back_alarm.checkState() == 2:
                        self.conf_alarm_call_flags = self.event.Set_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    else:
                        self.conf_alarm_call_flags = self.event.Reset_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    # data_all = self.ui.list_users_nom.currentRow().to_bytes(1,'little')
                    self.result_analyze = self.rs.Send_Command(self.ID2["CONF_ALARM_CALL_WRITE"],
                                                               self.ID1["SETUP_GSM_REQ"],
                                                               self.ID2["CONF_ALARM_CALL_WRITE"],
                                                               self.rs.TIME_TO_RX,
                                                               self.conf_alarm_call_flags)
                elif self.status_new == self.ID2["CONF_ALARM_CALL_WRITE"]:
                    if self.ui.checkBox_SMS_alarm.checkState() == 2:
                        self.conf_alarm_sms_flags = self.event.Set_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    else:
                        self.conf_alarm_sms_flags = self.event.Reset_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    self.result_analyze = self.rs.Send_Command(self.ID2["CONF_ALARM_SMS_WRITE"],
                                                               self.ID1["SETUP_GSM_REQ"],
                                                               self.ID2["CONF_ALARM_SMS_WRITE"],
                                                               self.rs.TIME_TO_RX,
                                                               self.conf_alarm_sms_flags)
                elif self.status_new == self.ID2["CONF_ALARM_SMS_WRITE"]:
                    if self.ui.checkBox_SMS_set_guard.checkState() == 2:
                        self.sms_set_guard_flags = self.event.Set_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    else:
                        self.sms_set_guard_flags = self.event.Reset_Bit(self.conf_alarm_call_flags, self.user_bit_num)
                    self.result_analyze = self.rs.Send_Command(self.ID2["CONF_SET_GUARD_SMS_WRITE"],
                                                               self.ID1["SETUP_GSM_REQ"],
                                                               self.ID2["CONF_SET_GUARD_SMS_WRITE"],
                                                               self.rs.TIME_TO_RX,
                                                               self.sms_set_guard_flags)
                elif self.status_new == self.ID2["CONF_SET_GUARD_SMS_WRITE"]:
                    s = self.ui.list_users_nom.currentRow()
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки '+(str(s+1))+' абонента записаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # чтение вкладки "СМС"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["TEXT_GUARD_SET_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["CLEAR_ALARM_TEXT_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["CLEAR_ALARM_TEXT_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["CLEAR_ALARM_TEXT_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["SMS_RESET_GUARD_CMD_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["SMS_RESET_GUARD_CMD_READ"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.comboBox_Reset_Guard.currentIndex())
                elif self.status_new == self.ID2["SMS_RESET_GUARD_CMD_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["SMS_SET_GUARD_CMD_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["SMS_SET_GUARD_CMD_READ"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.comboBox_Set_Guard.currentIndex())
                elif self.status_new == self.ID2["SMS_SET_GUARD_CMD_READ"]:
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки СМС прочитаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим в IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # запись вкладки "СМС"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["TEXT_GUARD_SET_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(   self.ID2["CLEAR_ALARM_TEXT_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["CLEAR_ALARM_TEXT_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.lineEdit_clear_alarm_text.text())
                elif self.status_new == self.ID2["CLEAR_ALARM_TEXT_WRITE"]:
                    data_all = bytearray(b'')
                    data_all += self.ui.comboBox_Reset_Guard.currentIndex().to_bytes(1,'little') + \
                                Convert_Str_to_Bytearray(self.ui.lineEdit_sms_reset_guard_cmd.text())
                    self.result_analyze = self.rs.Send_Command(   self.ID2["SMS_RESET_GUARD_CMD_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["SMS_RESET_GUARD_CMD_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   data_all)
                elif self.status_new == self.ID2["SMS_RESET_GUARD_CMD_WRITE"]:
                    data_all = bytearray(b'')
                    data_all += self.ui.comboBox_Set_Guard.currentIndex().to_bytes(1,'little') + \
                                Convert_Str_to_Bytearray(self.ui.lineEdit_sms_Set_Guard_Cmd.text())
                    self.result_analyze = self.rs.Send_Command(   self.ID2["SMS_SET_GUARD_CMD_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["SMS_SET_GUARD_CMD_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   data_all)
                elif self.status_new == self.ID2["SMS_SET_GUARD_CMD_WRITE"]:
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Настройки СМС записаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим в IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # чтение вкладки "Общие настройки"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["MIN_BALANCE_SMS_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["MIN_BALANCE_CALL_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["MIN_BALANCE_CALL_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["MIN_BALANCE_CALL_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["GSM_SETUP_U_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["GSM_SETUP_U_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["GSM_SETUP_U_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_CLEAR_ALARM_CMD_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_CLEAR_ALARM_CMD_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["DTMF_CLEAR_ALARM_CMD_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_RESET_GUARD_CMD_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_RESET_GUARD_CMD_READ"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.comboBox_dtmf_reset_guard.currentIndex())
                elif self.status_new == self.ID2["DTMF_RESET_GUARD_CMD_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_SET_GUARD_CMD_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_SET_GUARD_CMD_READ"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.comboBox_dtmf_set_guard.currentIndex())
                elif self.status_new == self.ID2["DTMF_SET_GUARD_CMD_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["TRAMP_END_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["TRAMP_END_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["TRAMP_END_READ"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["TRAMP_BEGIN_READ"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["TRAMP_BEGIN_READ"],
                                                                   self.rs.TIME_TO_RX)
                elif self.status_new == self.ID2["TRAMP_BEGIN_READ"]:
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Общие настройки прочитаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим в IDLE
                    self.Set_Status(self.ID2["IDLE"])

                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                # запись вкладки "Общие настройки"
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                elif self.status_new == self.ID2["MIN_BALANCE_SMS_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["MIN_BALANCE_CALL_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["MIN_BALANCE_CALL_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.ui.spinBox_min_balance_call.value().to_bytes(2,'little'))
                elif self.status_new == self.ID2["MIN_BALANCE_CALL_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["GSM_SETUP_U_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["GSM_SETUP_U_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   self.event.Read_Widget_General_Page().to_bytes(4,'little'))
                elif self.status_new == self.ID2["GSM_SETUP_U_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_CLEAR_ALARM_CMD_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_CLEAR_ALARM_CMD_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   Convert_Str_to_Bytearray(self.ui.lineEdit_dtmf_clear_alarm_cmd.text()))
                elif self.status_new == self.ID2["DTMF_CLEAR_ALARM_CMD_WRITE"]:
                    data_all = bytearray(b'')
                    data_all += self.ui.comboBox_dtmf_reset_guard.currentIndex().to_bytes(1,'little') + \
                                Convert_Str_to_Bytearray(self.ui.lineEdit_dtmf_reset_guard.text())
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_RESET_GUARD_CMD_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_RESET_GUARD_CMD_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   data_all)
                elif self.status_new == self.ID2["DTMF_RESET_GUARD_CMD_WRITE"]:
                    data_all = bytearray(b'')
                    data_all += self.ui.comboBox_dtmf_set_guard.currentIndex().to_bytes(1,'little') + \
                                Convert_Str_to_Bytearray(self.ui.lineEdit_dtmf_set_guard.text())
                    self.result_analyze = self.rs.Send_Command(    self.ID2["DTMF_SET_GUARD_CMD_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["DTMF_SET_GUARD_CMD_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   data_all)
                elif self.status_new == self.ID2["DTMF_SET_GUARD_CMD_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["TRAMP_END_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["TRAMP_END_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   Convert_Str_to_Bytearray(self.ui.lineEdit_trump_end.text()))
                elif self.status_new == self.ID2["TRAMP_END_WRITE"]:
                    self.result_analyze = self.rs.Send_Command(    self.ID2["TRAMP_BEGIN_WRITE"],
                                                                   self.ID1["SETUP_GSM_REQ"],
                                                                   self.ID2["TRAMP_BEGIN_WRITE"],
                                                                   self.rs.TIME_TO_RX,
                                                                   Convert_Str_to_Bytearray(self.ui.lineEdit_trump_begin.text()))
                elif self.status_new == self.ID2["TRAMP_BEGIN_WRITE"]:
                    QtWidgets.QMessageBox.warning(self, 'Информация', 'Общие настройки записаны успешно',
                                                  QtWidgets.QMessageBox.Ok)
                    #переходим в IDLE
                    self.Set_Status(self.ID2["IDLE"])


            # обработка ошибок
            if self.result_analyze == ['Error_Number']:
                QtWidgets.QMessageBox.warning(self, 'Информация', 'Ошибка - в номере должны быть только цифры',
                                              QtWidgets.QMessageBox.Ok)
                #переходим в IDLE
                self.Set_Status(self.ID2["IDLE"])
            elif self.result_analyze == ['Error_First_Char']:
                QtWidgets.QMessageBox.warning(self, 'Информация', 'Первый символ номера должен быть +', QtWidgets.QMessageBox.Ok)
                #переходим в IDLE
                self.Set_Status(self.ID2["IDLE"])
            elif self.result_analyze == ['Error']:
                QtWidgets.QMessageBox.warning(self, 'Ошибка',"Ошибка приема", QtWidgets.QMessageBox.Ok)
                #переходим в IDLE
                self.Set_Status(self.ID2["IDLE"])
        #принятых данных нет
        else:
            #ответ не получен
            QtWidgets.QMessageBox.warning(self, 'Ошибка',"Нет ответа от модуля.", QtWidgets.QMessageBox.Ok)
            #переходим в IDLE
            self.Set_Status(self.ID2["IDLE"])
        return



if __name__ == "__main__":
    widg = QtWidgets.QApplication(sys.argv)
    myapp = Debuger_GSM()
    myapp.show()
    sys.exit(widg.exec_())
