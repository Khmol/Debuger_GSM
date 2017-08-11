import Debuger_GSM
from PyQt5 import QtWidgets

class Form_Events(object):

    def __init__(self, main_app: Debuger_GSM):
        self.app = main_app

    def Init_Widgets(self):
        '''
        настройка действий по кнопкам
        None :return:
        '''

        # обраотка кнопки открытие порта RS - pushButton_open_COM
        self.app.ui.pushButton_open_COM.clicked.connect(self.pb_Open_COM_Header)
        # обраотка кнопки закрытие порта RS - pushButton_close_COM
        self.app.ui.pushButton_close_COM.clicked.connect(self.pb_Close_COM_Header)

        # вкладка пользователи
        # обраотка кнопки прочиать общие настройки - pushButton_Read_GS
        self.app.ui.pushButton_Read_GS.clicked.connect(self.pb_Read_GS_Header)
        # обраотка кнопки записать общие настройки - pushButton_Write_GS
        self.app.ui.pushButton_Write_GS.clicked.connect(self.pb_Write_GS_Header)


        # чтение телефонного номера пользователя
        self.app.ui.pushButton_Read_Users.clicked.connect(self.pb_Read_Users_Header)
        # установка телефонного номера пользователя
        self.app.ui.pushButton_Write_Users.clicked.connect(self.pb_Write_Users_Header)

        # вкладка "СМС"
        self.app.ui.pushButton_Read_SMS.clicked.connect(self.pb_Read_SMS_Header)
        self.app.ui.pushButton_Write_SMS.clicked.connect(self.pb_Write_SMS_Header)

        # вкладка "общие настройки"
        self.app.ui.list_users_nom.currentRowChanged.connect(self.Disable_Widget_User_Page)

        # вкладка "Входы"
        self.app.ui.pushButton_Read_In.clicked.connect(self.pb_Read_In_Header)
        self.app.ui.pushButton_Write_In.clicked.connect(self.pb_Write_In_Header)

        # перечень доступных портов
        list_com_ports = ''
        # проверка какие порты свободны
        for s in self.app.rs.scan_COM_ports():
            list_com_ports += s + ' '
        # установка номеров списка пользователей
        for i in range (1,10):
            self.app.ui.list_users_nom.addItem(str(i))
        self.app.ui.list_users_nom.setCurrentRow(0) #установка 0 значения по умолчанию

        # настройка списка для выбора порта
        # добавляем свободные порты в comboBox_COM
        self.app.ui.comboBox_COM.addItems(list_com_ports.split())
        self.app.ui.comboBox_COM.setCurrentIndex(1)
        # добавляем нужные скорости в comboBox_Baudrate
        self.app.ui.comboBox_Baudrate.addItems(self.app.BAUDRATES)
        self.app.ui.comboBox_Baudrate.setCurrentIndex(5)
        # добавляем список входов в comboBox_in_number
        self.app.ui.comboBox_in_number.addItems(self.app.IN_NUMBER)
        self.app.ui.comboBox_in_number.setCurrentIndex(0)
        # добавляем список входов в comboBox_Reset_Guard
        self.app.ui.comboBox_Reset_Guard.addItems(self.app.RESET_GUARD_NUMBER)
        self.app.ui.comboBox_Reset_Guard.setCurrentIndex(0)
        # добавляем список входов в comboBox_Set_Guard
        self.app.ui.comboBox_Set_Guard.addItems(self.app.SET_GUARD_NUMBER)
        self.app.ui.comboBox_Set_Guard.setCurrentIndex(0)
        # добавляем список входов в comboBox_Reset_Guard
        self.app.ui.comboBox_dtmf_reset_guard.addItems(self.app.RESET_GUARD_NUMBER)
        self.app.ui.comboBox_dtmf_reset_guard.setCurrentIndex(0)
        # добавляем список входов в comboBox_Set_Guard
        self.app.ui.comboBox_dtmf_set_guard.addItems(self.app.SET_GUARD_NUMBER)
        self.app.ui.comboBox_dtmf_set_guard.setCurrentIndex(0)


    def Enable_Widget_User_Page(self):
        '''
        #*********************************************************************
        # выключить все элементы вкладки Абоненты
        #*********************************************************************
        :return:
        '''
        self.app.ui.checkBox_SMS_set_guard.setEnabled(1)
        self.app.ui.checkBox_SMS_alarm.setEnabled(1)
        self.app.ui.checkBox_call_back_alarm.setEnabled(1)
        self.app.ui.lineEdit_Telephone_Number.setEnabled(1)
        self.app.ui.spinBox_sim900_user_timeout.setEnabled(1)
        self.app.ui.label_Max_Time_Talk.setEnabled(1)
        self.app.ui.pushButton_Write_Users.setEnabled(1)


    def Disable_Widget_User_Page(self):
        '''
        #*********************************************************************
        # выключить все элементы вкладки Абоненты
        #*********************************************************************
        :return:
        '''
        self.app.ui.checkBox_SMS_set_guard.setDisabled(1)
        self.app.ui.checkBox_SMS_alarm.setDisabled(1)
        self.app.ui.checkBox_call_back_alarm.setDisabled(1)
        self.app.ui.lineEdit_Telephone_Number.setDisabled(1)
        self.app.ui.spinBox_sim900_user_timeout.setDisabled(1)
        self.app.ui.label_Max_Time_Talk.setDisabled(1)


    def Enable_Widget_In_Page(self):
        '''
        #*********************************************************************
        # активировать все элементы вкладки "Входы"
        #*********************************************************************
        :return:
        '''
        self.app.ui.comboBox_in_number.setEnabled(1)
        self.app.ui.lineEdit_in_alarm_text.setEnabled(1)
        self.app.ui.pushButton_Write_In.setEnabled(1)


    def Disable_Widget_In_Page(self):
        '''
        #*********************************************************************
        # деактивировать все элементы вкладки "Входы"
        #*********************************************************************
        :return:
        '''
        self.app.ui.pushButton_Read_In.setDisabled(1)
        self.app.ui.pushButton_Write_In.setDisabled(1)
        self.app.ui.comboBox_in_number.setDisabled(1)
        self.app.ui.lineEdit_in_alarm_text.setDisabled(1)
        self.app.ui.lineEdit_sms_Set_Guard_Cmd.setDisabled(1)
        self.app.ui.comboBox_Set_Guard.setDisabled(1)


    def Enable_Widget_SMS_Page(self):
        '''
        #*********************************************************************
        # активирация элементов вкладки "СМС"
        #*********************************************************************
        :return:
        '''
        self.app.ui.lineEdit_text_guard_set.setEnabled(1)
        self.app.ui.lineEdit_sms_reset_guard_cmd.setEnabled(1)
        self.app.ui.lineEdit_clear_alarm_text.setEnabled(1)
        self.app.ui.comboBox_Reset_Guard.setEnabled(1)
        self.app.ui.lineEdit_sms_Set_Guard_Cmd.setEnabled(1)
        self.app.ui.comboBox_Set_Guard.setEnabled(1)
        self.app.ui.pushButton_Write_SMS.setEnabled(1)


    def Disable_Widget_SMS_Page(self):
        '''
        #*********************************************************************
        # деактивируем элементов вкладки "СМС"
        #*********************************************************************
        :return:
        '''
        self.app.ui.lineEdit_text_guard_set.setDisabled(1)
        self.app.ui.lineEdit_sms_reset_guard_cmd.setDisabled(1)
        self.app.ui.lineEdit_clear_alarm_text.setDisabled(1)
        self.app.ui.comboBox_Reset_Guard.setDisabled(1)
        self.app.ui.pushButton_Read_SMS.setDisabled(1)
        self.app.ui.pushButton_Write_SMS.setDisabled(1)


    def Enable_Widget_General_Page(self):
        '''
        #*********************************************************************
        # активируем элементы вкладки "Общие настройки"
        #*********************************************************************
        :return:
        '''
        self.app.ui.spinBox_min_balance_SMS.setEnabled(1)
        self.app.ui.spinBox_min_balance_call.setEnabled(1)
        self.app.ui.checkBox_rep_call_back_self.setEnabled(1)
        self.app.ui.checkBox_rep_sms_self.setEnabled(1)
        self.app.ui.checkBox_let_set_guard_no_nom.setEnabled(1)
        self.app.ui.checkBox_let_set_guard_nom.setEnabled(1)
        self.app.ui.checkBox_send_sms_always.setEnabled(1)
        self.app.ui.checkBox_call_back_always.setEnabled(1)
        self.app.ui.lineEdit_dtmf_clear_alarm_cmd.setEnabled(1)
        self.app.ui.comboBox_dtmf_set_guard.setEnabled(1)
        self.app.ui.lineEdit_dtmf_set_guard.setEnabled(1)
        self.app.ui.comboBox_dtmf_reset_guard.setEnabled(1)
        self.app.ui.lineEdit_dtmf_reset_guard.setEnabled(1)
        self.app.ui.lineEdit_trump_begin.setEnabled(1)
        self.app.ui.lineEdit_trump_end.setEnabled(1)
        self.app.ui.pushButton_Write_GS.setEnabled(1)


    def Disable_Widget_General_Page(self):
        '''
        #*********************************************************************
        # деактивируем элементы вкладки "Общие настройки"
        #*********************************************************************
        :return:
        '''
        self.app.ui.spinBox_min_balance_SMS.setDisabled(1)
        self.app.ui.spinBox_min_balance_call.setDisabled(1)
        self.app.ui.checkBox_rep_call_back_self.setDisabled(1)
        self.app.ui.checkBox_rep_sms_self.setDisabled(1)
        self.app.ui.checkBox_let_set_guard_no_nom.setDisabled(1)
        self.app.ui.checkBox_let_set_guard_nom.setDisabled(1)
        self.app.ui.checkBox_send_sms_always.setDisabled(1)
        self.app.ui.checkBox_call_back_always.setDisabled(1)
        self.app.ui.pushButton_Read_GS.setDisabled(1)
        self.app.ui.pushButton_Write_GS.setDisabled(1)
        self.app.ui.lineEdit_dtmf_clear_alarm_cmd.setDisabled(1)
        self.app.ui.comboBox_dtmf_set_guard.setDisabled(1)
        self.app.ui.lineEdit_dtmf_set_guard.setDisabled(1)
        self.app.ui.comboBox_dtmf_reset_guard.setDisabled(1)
        self.app.ui.lineEdit_dtmf_reset_guard.setDisabled(1)
        self.app.ui.lineEdit_trump_begin.setDisabled(1)
        self.app.ui.lineEdit_trump_end.setDisabled(1)


    def pb_Open_COM_Header(self):
        '''
        #*********************************************************************
        # обработчик кнопки открыть порт - pushButton_open_COM
        #*********************************************************************
        :return:
        '''
        # читаем значения для конфигурирования порта
        baudrate = int(self.app.ui.comboBox_Baudrate.currentText())
        nom_com_port = self.app.ui.comboBox_COM.currentText()
        # конфигурируем порт RS
        self.app.rs.Serial_Config(baudrate, nom_com_port)
        # активация кнопок после выбора порта и скорости
        self.app.ui.pushButton_open_COM.setDisabled(1)
        self.app.ui.pushButton_close_COM.setEnabled(1)
        #вкладка "Пользователи"
        self.app.ui.pushButton_Read_Users.setEnabled(1)
        self.app.ui.list_users_nom.setEnabled(1)
        #вкладка "СМС"
        self.app.ui.pushButton_Read_SMS.setEnabled(1)
        #вкладка "Общие настройки"
        self.app.ui.pushButton_Read_GS.setEnabled(1)
        #вкладка "Входы"
        self.app.ui.pushButton_Read_In.setEnabled(1)

        return True


    def pb_Close_COM_Header(self):
        '''
        #*********************************************************************
        # обработчик кнопки закрыть порт - pushButton_close_COM
        #*********************************************************************
        :return:
        '''
        # деактивация кнопок открытия порта
        self.app.ui.pushButton_open_COM.setEnabled(1)
        self.app.ui.pushButton_close_COM.setDisabled(1)
        #вкладка "Пользователи"
        self.Disable_Widget_User_Page()
        self.app.ui.pushButton_Read_Users.setDisabled(1)
        self.app.ui.pushButton_Write_Users.setDisabled(1)
        self.app.ui.list_users_nom.setDisabled(1)
        #вкладка "Общие настройки"
        self.Disable_Widget_General_Page()
        #вкладка "СМС"
        self.Disable_Widget_SMS_Page()
        #вкладка "Входы"
        self.Disable_Widget_In_Page()
        # закрытие порта
        self.app.rs.Serial_Close()


    def pb_Read_Users_Header(self):
        '''
        # обработчик кнопки pushButton_Read_Users - чтение настроек абонентов
        return: ['Ok'] - при успешном выполении, ['Error'] - при ошибке
        '''
        #включаем все элементы вкладки Абоненты
        self.Enable_Widget_User_Page()
        # отправляем SIM900_USER_TIMEOUT_READ
        if self.app.rs.Send_Command(  self.app.ID2["SIM900_USER_TIMEOUT_READ"],
                                  self.app.ID1["SETUP_GSM_REQ"],
                                  self.app.ID2["SIM900_USER_TIMEOUT_READ"],
                                  self.app.rs.TIME_TO_RX,
                                  self.app.ui.list_users_nom.currentRow()) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Write_Users_Header(self):
        '''
        # обработчик кнопки pushButton_Write_Users - запись настроек абонентов
        return: ['Ok'] - при успешном выполении, ['Error'] - при ошибке
        '''
        #включаем все элементы вкладки Абоненты
        self.Enable_Widget_User_Page()
        data = self.app.ui.list_users_nom.currentRow().to_bytes(1,'little')
        data += self.app.ui.spinBox_sim900_user_timeout.value().to_bytes(2,'little')
        # отправляем SIM900_USER_TIMEOUT_WRITE
        if self.app.rs.Send_Command(  self.app.ID2["SIM900_USER_TIMEOUT_WRITE"],
                                  self.app.ID1["SETUP_GSM_REQ"],
                                  self.app.ID2["SIM900_USER_TIMEOUT_WRITE"],
                                  self.app.rs.TIME_TO_RX,
                                  data) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Read_SMS_Header(self):
        '''
        # обработчик кнопки pushButton_Read_SMS - чтение настроек абонентов
        return: ['Ok'] - при успешном выполении, ['Error'] - при ошибке
        '''
        #включаем все элементы вкладки Абоненты
        self.Enable_Widget_SMS_Page()
        # отправляем ALARM_TEXT_READ
        if self.app.rs.Send_Command( self.app.ID2["TEXT_GUARD_SET_READ"],
                                 self.app.ID1["SETUP_GSM_REQ"],
                                 self.app.ID2["TEXT_GUARD_SET_READ"],
                                 self.app.rs.TIME_TO_RX) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Write_SMS_Header(self):
        '''
        # обработчик кнопки pushButton_Write_SMS - чтение настроек абонентов
        return: ['Ok'] - при успешном выполении, ['Error'] - при ошибке
        :return:
        '''
        if self.app.rs.Send_Command(   self.app.ID2["TEXT_GUARD_SET_WRITE"],
                                   self.app.ID1["SETUP_GSM_REQ"],
                                   self.app.ID2["TEXT_GUARD_SET_WRITE"],
                                   self.app.rs.TIME_TO_RX,
                                   self.app.ui.lineEdit_text_guard_set.text()) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Read_In_Header(self):
        '''
        #*********************************************************************
        # обраотка кнопки прочиать настройки входов - pushButton_Read_In
        #*********************************************************************
        ['Ok']/['Error'] :return:
        '''
        self.Enable_Widget_In_Page()
        # начинаем опрос - чтение денежного лимита ALARM_TEXT_READ
        if self.app.rs.Send_Command(   self.app.ID2["ALARM_TEXT_READ"],
                                       self.app.ID1["SETUP_GSM_REQ"],
                                       self.app.ID2["ALARM_TEXT_READ"],
                                       self.app.rs.TIME_TO_RX,
                                       self.app.ui.comboBox_in_number.currentIndex()) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Write_In_Header(self):
        '''
        #*********************************************************************
        # обраотка кнопки записать настройки входов - pushButton_Write_In
        #*********************************************************************
        ['Ok']/['Error'] :return:
        '''
        data = chr(self.app.ui.comboBox_in_number.currentIndex()) + self.app.ui.lineEdit_in_alarm_text.text()
        if self.app.rs.Send_Command(  self.app.ID2["ALARM_TEXT_WRITE"],
                                  self.app.ID1["SETUP_GSM_REQ"],
                                  self.app.ID2["ALARM_TEXT_WRITE"],
                                  self.app.rs.TIME_TO_RX,
                                  data) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Read_GS_Header(self):
        '''
        #*********************************************************************
        # обраотка кнопки прочиать общие настройки - pushButton_Read_GS
        #*********************************************************************
        :return:
        '''
        # активация элементов вкладки
        self.Enable_Widget_General_Page()
        # начинаем опрос - чтение денежного лимита MIN_BALANCE_SMS_READ
        if self.app.rs.Send_Command(  self.app.ID2["MIN_BALANCE_SMS_READ"],
                               self.app.ID1["SETUP_GSM_REQ"],
                               self.app.ID2["MIN_BALANCE_SMS_READ"],
                               self.app.rs.TIME_TO_RX) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def pb_Write_GS_Header(self):
        '''
        #*********************************************************************
        # обраотка кнопки записать общие настройки - pushButton_Write_GS
        #*********************************************************************
        :return:
        '''
        # активация элементов вкладки
        self.Enable_Widget_General_Page()
        if self.app.rs.Send_Command(  self.app.ID2["MIN_BALANCE_SMS_WRITE"],
                                  self.app.ID1["SETUP_GSM_REQ"],
                                  self.app.ID2["MIN_BALANCE_SMS_WRITE"],
                                  self.app.rs.TIME_TO_RX,
                                  self.app.ui.spinBox_min_balance_SMS.value().to_bytes(2,'little')) == ['Ok']:
            return ['Ok']
        else:
            return ['Error']


    def Show_Warning_TX_OK(self, number, start_index, length_number):
        '''
        #*********************************************************************
        # вывод сообщения - "данные _номер_ записаны успешно"
        # [number] - массив данных
        # [start_index] - индекс начала номера в массиве для вывода в сообщение
        #*********************************************************************
        :param number:
        :param start_index:
        :param length_number:
        :return:
        '''
        s = ''
        for i in range (start_index,start_index + length_number):
            s = s+chr(number[i]) # извлекаем номер абонента
        out_str = "Номер " + s + " успешно записан"
        QtWidgets.QMessageBox.warning(self.app, 'Сообщение',out_str , QtWidgets.QMessageBox.Ok)
        return True


    def Check_Bit(self, data, bit_num):
        '''
        #*********************************************************************
        # проверка значения бита переменной int
        # [data] - данные
        # [bit_num] - номер бита для установки
        #*********************************************************************
        :param data:
        :param bit_num:
        :return: 1 если установлен, 0 если не установлен, None если данные не распознаны
        '''
        if isinstance(data, int):
            return (data >> bit_num) & 1
        elif isinstance(data, bytearray) or isinstance(data, bytes):
            return (int.from_bytes(data, byteorder='little') >> bit_num) & 1
        else:
            return None


    def Set_Bit(self, data, bit_num):
        '''
        #*********************************************************************
        # установка значения бита переменной int
        # [data] - данные
        # [bit_num] - номер бита для установки
        #*********************************************************************
        :param data:
        :param bit_num:
        :return: данные data с установленным битом
        '''
        if isinstance(data, int):
            return ( data | (1 << bit_num))
        elif isinstance(data, bytearray) or isinstance(data, bytes):
            data_len = len(data)
            data = int.from_bytes(data, byteorder='little') | (1 << bit_num)
            return data.to_bytes(data_len,'little')
        else:
            return None


    def Reset_Bit(self, data, bit_num):
        '''
        #*********************************************************************
        # установка значения бита переменной int и byte
        # [data] - данные
        # [bit_num] - номер бита для установки
        #*********************************************************************
        :param data:
        :param bit_num:
        :return: данные data с установленным битом
        '''
        mask = 0
        if isinstance(data, int):
            len_data_bin = len(bin(data))-2
            for i in range(len_data_bin):
                mask = (mask << 1)
                mask += 1
            mask = mask ^ ( 1 << bit_num)
            return (data & mask)
        elif isinstance(data, bytearray) or isinstance( data, bytes ):
            data_len = len(data)
            data = int.from_bytes(data, byteorder='little')
            len_data_bin = len(bin(data))-2
            for i in range(len_data_bin):
                mask = (mask << 1)
                mask += 1
            mask = mask ^ ( 1 << bit_num)
            return (data & mask).to_bytes(data_len,'little')
        else:
            return None


    def Reload_Widget_General_Page(self, data):
        '''
        обновление значений setChecked на вкладке "Общие настройки"
        param data: int - 4 байта полученных данных
        return: Ok - при успешном выполении, Error - при ошибке
        '''
        try:
            # Установка на охрану по звонку без донабора защитного кода
            if self.Check_Bit(data[0],1):
                self.app.ui.checkBox_let_set_guard_no_nom.setChecked(1)
            else:
                self.app.ui.checkBox_let_set_guard_no_nom.setChecked(0)
            # Установка на охрану по звонку с донабором защитного кода
            if self.Check_Bit(data[0],2):
                self.app.ui.checkBox_let_set_guard_nom.setChecked(1)
            else:
                self.app.ui.checkBox_let_set_guard_nom.setChecked(0)
            # Передавать СМС уведомление о постановке на охрану тому, кто поставил на охрану
            if self.Check_Bit(data[0],3):
                self.app.ui.checkBox_rep_sms_self.setChecked(1)
            else:
                self.app.ui.checkBox_rep_sms_self.setChecked(0)
            # Обратный звонок как уведомление о постановке на охрану тому, кто поставил на охрану
            if self.Check_Bit(data[0],4):
                self.app.ui.checkBox_rep_call_back_self.setChecked(1)
            else:
                self.app.ui.checkBox_rep_call_back_self.setChecked(0)
            # Отправлять СМС даже при низком балансе
            if self.Check_Bit(data[0],5):
                self.app.ui.checkBox_send_sms_always.setChecked(1)
            else:
                self.app.ui.checkBox_send_sms_always.setChecked(0)
            # Обратный звонок даже при низком балансе
            if self.Check_Bit(data[0],6):
                self.app.ui.checkBox_call_back_always.setChecked(1)
            else:
                self.app.ui.checkBox_call_back_always.setChecked(0)
            # успешный выход
            return ['Ok']
        except:
            return ['Error']


    def Read_Widget_General_Page(self):
        '''
        #*********************************************************************
        # прочитать информацию на вкладке "Общие настройки"
        #*********************************************************************
        :return:
        '''
        # проверяем значения всех checkBox на вкладке "Общие настройки"
        # Установка на охрану по звонку без донабора защитного кода
        data = 0
        if self.app.ui.checkBox_let_set_guard_no_nom.checkState() == 2:
            data = self.Set_Bit(data, 1)
        # Установка на охрану по звонку с донабором защитного кода
        if self.app.ui.checkBox_let_set_guard_nom.checkState() == 2:
            data = self.Set_Bit(data, 2)
        # Передавать СМС уведомление о постановке на охрану тому, кто поставил на охрану
        if self.app.ui.checkBox_rep_sms_self.checkState() == 2:
            data = self.Set_Bit(data, 3)
        # Обратный звонок как уведомление о постановке на охрану тому, кто поставил на охрану
        if self.app.ui.checkBox_rep_call_back_self.checkState() == 2:
            data = self.Set_Bit(data, 4)
        # Отправлять СМС даже при низком балансе
        if self.app.ui.checkBox_send_sms_always.checkState() == 2:
            data = self.Set_Bit(data, 5)
        # Обратный звонок даже при низком балансе
        if self.app.ui.checkBox_call_back_always.checkState() == 2:
            data = self.Set_Bit(data, 6)
        return data


    def Read_Widget_Users(self, user_num):
        '''
        #*********************************************************************
        # прочитать информацию на вкладке "Пользователи"
        #*********************************************************************
        :return: {bytearray} Данные флагов
        0 бит - checkBox_SMS_alarm - разрешения/запрещения звонка при аварии
        '''
        # проверяем значения всех checkBox на вкладке "Общие настройки"
        # Установка на охрану по звонку без донабора защитного кода
        data = 0
        if self.app.ui.checkBox_SMS_alarm.checkState() == 2:
            data = self.Set_Bit(data, 0)
        return data


    def Show_RX_DATA(self):
        '''
        #*********************************************************************
        #вывести полученный пакет из rs_receive_pack
        #*********************************************************************
        :return:
        '''
        print("Принят пакет")
        for i in range(0,len(self.app.rs_receive_pack)):
            print(i,': ', hex(self.app.rs_receive_pack[i]),' ;',chr(self.app.rs_receive_pack[i]))

