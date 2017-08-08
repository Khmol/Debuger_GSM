#coding: utf8

import sys
import serial
import Debuger_GSM
from CRC16 import *

class RS_Commands(object):

    def __init__(self, in_app: Debuger_GSM):
        self.app = in_app

    #*********************************************************************
    #определение свободных COM портов
    #*********************************************************************
    def scan_COM_ports(self):
        """scan for available ports. return a list of tuples (num, name)"""
        available = []
        for i in range(self.app.NUMBER_SCAN_PORTS):
            try:
                s = serial.Serial(i)
                available.append((s.portstr))
                s.close()   # explicit close 'cause of delayed GC in java
            except serial.SerialException:
                pass
        return available

    #*********************************************************************
    #настройка порта со значением выбранным в comboBox_COM
    #{int} baudrate - скорость работы порта
    #{str} nom_com - номер ком порта
    #*********************************************************************
    #pyuic5 Serial_Qt.ui -o Serial_Qt_Form.py - для обновления главной формы
    def Serial_Config(self,baudrate, nom_com):
        # configure the serial connections (the parameters differs on the device you are connecting to)
        self.ser = serial.Serial(nom_com,#'COM25',
                    baudrate=baudrate,#9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=0,
                    bytesize=serial.EIGHTBITS,
                    xonxoff=0)
        if baudrate == 115200:
            self.TIME_TO_RX = 30#
        elif baudrate == 57600:
            self.TIME_TO_RX = 40#
        elif baudrate == 38400:
            self.TIME_TO_RX = 60#
        elif baudrate == 19200:
            self.TIME_TO_RX = 100#
        elif baudrate == 9600:
            self.TIME_TO_RX = 150#
        elif baudrate == 1200:
            self.TIME_TO_RX = 1200#
        #начальные данные для передатчика
        self.RS_START = bytearray([0x55, 0xAA])   #стартовая последовательность для RS
        self.pack_size_TX = 0    #размер передаваемого пакета в байтах
        self.pack_seq_TX = 0     #номер пакета в последовательности
        self.ID1_TX = 0           #ID1 передаваемой команды
        self.ID2_TX = 0           #ID2 передаваемой команды
        self.DATA_TX = bytearray([0x00]) #данные для передачи
        #начальные данные для приемника
        self.pack_size_RX = 0    #размер принятого пакета в байтах
        self.pack_seq_RX = 0     #номер принятого пакета в последовательности
        self.ID_RX = 0           #ID принятой команды
        return ['Ok']

    #*********************************************************************
    # закрываем порт RS
    #*********************************************************************
    def Serial_Close(self):
        # закрываем порт если он открыт
        if self.ser.isOpen():
            self.ser.close()

    #*********************************************************************
    # передача пакета в RS
    #*********************************************************************
    def Transmit_RS_Data (self):
        try:
            #установка начальног значения CRC16
            crc = INITIAL_MODBUS
            #проверка открыт ли порт
            if self.ser.isOpen():
                #полезные данные для передачи
                useful_data = self.pack_seq_TX.to_bytes(1,'little') + \
                              self.ID1_TX.to_bytes(1,'little') + \
                              self.ID2_TX.to_bytes(1,'little') + \
                              self.DATA_TX
                #определяем длину полезных данных
                self.pack_size_TX = len(useful_data)+6 #2 - преамбула, 2 - это CRC и 2 это размер поля длина пакета
                self.pack_seq_TX += 1   #увеличиваем счетчик последовательности
                #обнуляем счетчик последовательности
                if self.pack_seq_TX == 256:
                    self.pack_seq_TX = 0
                self.rs_send_pack = self.RS_START + \
                                    self.pack_size_TX.to_bytes(2,'little') + \
                                    useful_data
                #производим рассчет CRC16 для self.rs_send_pack
                for ch in self.rs_send_pack:
                    crc = calcByte(ch,crc)
                self.rs_send_pack = self.rs_send_pack + crc.to_bytes(2, byteorder='little')
                print("Передан пакет")
                for i in range(0,len(self.rs_send_pack)):
                    print(i,': ', hex(self.rs_send_pack[i]),' ;',chr(self.rs_send_pack[i]))
                self.ser.write(self.rs_send_pack)
                return ['Ok']
            else:
                return ['Error']
        except:
            return ['Error']
        #ps_pack_int = int.from_bytes(rs_pack_bytes, byteorder='little')
        #self.ser.write(self.rs_tx_buffer.encode('utf-8'))
        #pack_size_TX = len(rs_pack_seq_TX.to_bytes(1,'little') + rs_ID.to_bytes(1,'little') + rs_DATA)



    #*********************************************************************
    #проверка наличия данных в буфере RS
    #*********************************************************************
    def Recieve_RS_Data(self):
        RX_Data = ''  #данных нет
        while self.ser.inWaiting() > 0:
            RX_Data = self.ser.read(self.app.MAX_WAIT_BYTES)
        return RX_Data


    def Send_Command(self, new_status, id1, id2, timer_ms, data = 0x00):
        '''
        проверить текущий состояние, установить новое состояние, отправить команду
        param new_status: int - новове состояние в котором бедет производится отправка данных
        id1: int - значение id1 для отправки
        id2: int - значение id2 для отправки
        data - bin или str - данные для отправки
        return: Ok - при успешном выполении, Error - при ошибке
        '''
        self.app.Set_Status(new_status)
        if isinstance(data, bytes) or isinstance(data, bytearray):
            # данные в формате bytes
            self.DATA_TX = data
        elif isinstance(data, str):
            # данные в формате str
            self.DATA_TX = bytearray(b'')
            for d in data:
              self.DATA_TX += ord(d).to_bytes(1,'little')
        elif isinstance(data, int):
            self.DATA_TX = data.to_bytes(1,'little')
        else:
            # данные в другом формате
            return ['Error_Tx']
        self.ID1_TX = id1
        self.ID2_TX = id2
        #передаем данные в порт
        if self.Transmit_RS_Data() == ['Ok']:
            self.app.timer_RX_RS.start(timer_ms, self.app) #ждем ответ в течении self.TIME_TO_RX мс
            return ['Ok']
        return ['Error_Tx']

    #*********************************************************************
    #отправить запрос чтения номера телефона
    #*********************************************************************
    def Send_Get_Phone_Number(self, currentRow):
        if self.app.status_new == self.app.ID1["IDLE"]:
            self.app.status_old = self.app.status_new
            self.app.status_new = self.app.ID1["READ_NOM"]
            self.ID1_TX = self.app.ID1["READ_NOM"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = currentRow.to_bytes(1,'little') #данных READ_NOM
            self.Transmit_RS_Data() #передаем данные в порт
        return

    def Send_Get_Phone_Number_test(self):
        if self.app.status_new == self.app.ID1["IDLE"]:
            self.app.status_old = self.app.status_new
            self.app.status_new = self.app.ID1["READ_NOM"]
            self.ID1_TX = self.app.ID1["READ_NOM"]
            self.ID2_TX = self.app.ID1["IDLE"]
            param = '+380501234567'
            self.DATA_TX = bytearray(self.app.NOMBER_LENGTH)
            for i in range (0,self.app.NOMBER_LENGTH):
                self.DATA_TX[i] = ord(param[i]) #переводим данные в bytes для передачи по RS
            self.Transmit_RS_Data() #передаем данные в порт
        return

    #*********************************************************************
    #утановка номера телефона абонента
    #*********************************************************************
    def Send_Set_Phone_Number(self, currentRow, param):
        if self.app.status_new == self.app.ID1["IDLE"]:
            try:
                #проверка на длину введенного текста
                if len(param) == self.app.NOMBER_LENGTH:
                    #проверка что вначале номера есть знак '+'
                    if param[0] == '+':
                        self.app.status_old = self.app.status_new
                        self.app.status_new = self.app.ID1["WRITE_NOM"]
                        self.ID1_TX = self.app.ID1["WRITE_NOM"]
                        self.ID2_TX = self.app.ID1["IDLE"]
                        self.DATA_TX = bytearray(self.app.NOMBER_LENGTH+1)
                        self.DATA_TX[0] = currentRow
                        #проверка правильности ввода номера
                        for i in range (0,self.app.NOMBER_LENGTH):
                            #проверка на то, что введена цифра
                            if i>0:
                                int(param[i])
                            #записываем данные в буфер
                            self.DATA_TX[i+1] = ord(param[i]) #переводим данные в bytes для передачи по RS

                        #передаем пакет в порт
                        self.Transmit_RS_Data() #передаем данные в порт
                        return ['Ok']
                    else:
                        #выход с ошибкой - количество знаков в номере не правильное
                        return ['Error']
                else:
                    #выход с ошибкой - количество знаков в номере не правильное
                    return ['Error']
            except:
                #возврат в исходное состояние
                self.app.status_old = self.app.status_new
                self.app.status_new = self.app.ID1["IDLE"]
                return ['Error']

    def Send_Set_Phone_Number_test(self, currentRow, param):
        if self.app.status_new == self.app.ID1["IDLE"]:
            try:
                #проверка на длину введенного текста
                if len(param) == self.app.NOMBER_LENGTH:
                    #проверка что вначале номера есть знак '+'
                    if param[0] == '+':
                        self.app.status_old = self.app.status_new
                        self.app.status_new = self.app.ID1["WRITE_NOM"]
                        self.ID1_TX = self.app.ID1["WRITE_NOM"]
                        self.ID2_TX = self.app.ID1["IDLE"]
                        self.DATA_TX = bytearray(self.app.NOMBER_LENGTH)
                        #проверка правильности ввода номера
                        for i in range (0,self.app.NOMBER_LENGTH):
                            #проверка на то, что введена цифра
                            if i>0:
                                int(param[i])
                            #записываем данные в буфер
                            self.DATA_TX[i] = ord(param[i]) #переводим данные в bytes для передачи по RS

                        #передаем пакет в порт
                        self.Transmit_RS_Data() #передаем данные в порт
                        return ['Ok']
                    else:
                        #выход с ошибкой - количество знаков в номере не правильное
                        return ['Error']
                else:
                    #выход с ошибкой - количество знаков в номере не правильное
                    return ['Error']
            except:
                #возврат в исходное состояние
                self.app.status_old = self.app.status_new
                self.app.status_new = self.app.ID1["IDLE"]
                return ['Error']

    #*********************************************************************
    #отправить запрос чтения бинарных настроек вкладки "Пользователи"
    #*********************************************************************
    def Send_Get_Users_Flags(self, currentRow):
            self.ID1_TX = self.app.ID1["READ_ABON_FLAGS"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = currentRow.to_bytes(1,'little') #данных READ_NOM
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Get_Users_Flags_test(self, currentRow):
            self.ID1_TX = self.app.ID1["READ_ABON_FLAGS"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = 0x0055.to_bytes(2,'little') #данных READ_NOM
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']


    #*********************************************************************
    #отправить команду записи бинарных настроек вкладки "Пользователи"
    #*********************************************************************
    def Send_Set_Users_Flags(self, currentRow, data):
            self.ID1_TX = self.app.ID1["WRITE_ABON_FLAGS"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = currentRow.to_bytes(1,'little') #данных READ_NOM
            self.DATA_TX = self.DATA_TX + data.to_bytes(2,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Set_Users_Flags_test(self, currentRow, data):
            self.ID1_TX = self.app.ID1["WRITE_ABON_FLAGS"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('O').to_bytes(1,'little') + ord('K').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']


    #*********************************************************************
    #отправить команду чтения значения минимального остатка на счету для СМС    #*********************************************************************
    def Send_Min_Balance_SMS_Read(self, data):
        self.ID1_TX = self.app.ID1["SETUP_GSM_REQ"]
        self.ID2_TX = self.app.ID2["MIN_BALANCE_SMS_READ"]
        self.DATA_TX = data.to_bytes(1,'little')
        self.Transmit_RS_Data() #передаем данные в порт
        return ['Ok']

    #*********************************************************************
    #отправить команду записи значения минимального остатка на счету
    #*********************************************************************
    def Send_Min_Balance_SMS_Write(self, data):
        self.ID1_TX = self.app.ID1["SETUP_GSM_REQ"]
        self.ID2_TX = self.app.ID2["MIN_BALANCE_SMS_WRITE"]
        self.DATA_TX = data.to_bytes(2,'little')
        self.Transmit_RS_Data() #передаем данные в порт
        return ['Ok']


    #*********************************************************************
    #отправить команду чтения секретного номера для снятия/установки на охрану
    #*********************************************************************
    def Send_Get_Security_Number(self, data):
            self.ID1_TX = self.app.ID1["READ_SECURITY_NUMBER"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = data.to_bytes(1,'little')    #данных нет
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Get_Security_Number_test(self, data):
            self.ID1_TX = self.app.ID1["READ_SECURITY_NUMBER"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = 0x0102.to_bytes(2,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    #*********************************************************************
    #отправить команду записи секретного номера для снятия/установки на охрану
    #*********************************************************************
    def Send_Set_Security_Number(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SECURITY_NUMBER"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = data.to_bytes(2,'little')    #данных нет
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Set_Security_Number_test(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SECURITY_NUMBER"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('O').to_bytes(1,'little') + ord('K').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    #*********************************************************************
    #отправить команду чтения СМС установки на охрану
    #*********************************************************************
    def Send_Get_SMS_Set_Guard(self, data):
            self.ID1_TX = self.app.ID1["READ_SMS_SET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = data.to_bytes(1,'little')    #данных нет
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Get_SMS_Set_Guard_test(self, data):
            self.ID1_TX = self.app.ID1["READ_SMS_SET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('T').to_bytes(1,'little') + ord('e').to_bytes(1,'little') + \
                           ord('x').to_bytes(1,'little') + ord('t').to_bytes(1,'little') + \
                           ord('1').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    #*********************************************************************
    #отправить команду чтения СМС снятия с охраны
    #*********************************************************************
    def Send_Get_SMS_Set_Guard(self, data):
            self.ID1_TX = self.app.ID1["READ_SMS_RESET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = data.to_bytes(1,'little')    #данных нет
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Get_SMS_Reset_Guard_test(self, data):
            self.ID1_TX = self.app.ID1["READ_SMS_RESET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('T').to_bytes(1,'little') + ord('e').to_bytes(1,'little') + \
                           ord('x').to_bytes(1,'little') + ord('t').to_bytes(1,'little') + \
                           ord('2').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    #*********************************************************************
    #отправить команду записи СМС установки на охрану
    #*********************************************************************
    def Send_Set_SMS_Guard_On(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SMS_SET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = b''
            for i in range(0, len(data)):
                self.DATA_TX = self.DATA_TX + ord(data[i]).to_bytes(1,'little')    #преобразуем данные из string в bytes
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Set_SMS_Guard_On_test(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SMS_SET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('O').to_bytes(1,'little') + ord('K').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    #*********************************************************************
    #отправить команду записи СМС снятия с охраны
    #*********************************************************************
    def Send_Set_SMS_Guard_Off(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SMS_RESET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = b''
            for i in range(0, len(data)):
                self.DATA_TX = self.DATA_TX + ord(data[i]).to_bytes(1,'little')    #преобразуем данные из string в bytes
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

    def Send_Set_SMS_Guard_Off_test(self, data):
            self.ID1_TX = self.app.ID1["WRITE_SMS_RESET_GUARD"]
            self.ID2_TX = self.app.ID1["IDLE"]
            self.DATA_TX = ord('O').to_bytes(1,'little') + ord('K').to_bytes(1,'little')
            self.Transmit_RS_Data() #передаем данные в порт
            return ['Ok']

