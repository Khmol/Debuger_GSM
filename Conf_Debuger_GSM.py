#coding: utf8
from PyQt5.QtCore import QBasicTimer

class Conf_Debuger_GSM(object):

    def __init__(self):
        self.mode = ['TEST']    #тестовый режим
        #self.mode = ['WORK']    #рабочий режим

        #определяем переменные для работы основной программы
        self.status_new = 0 #текущее состояние
        self.status_old = 0 #прошлое состояние
        self.transmit_off = True    #флаг выключеной передачи (файл закрыт)
        self.flag_rx_ok = False #флаг успешного приема
        #словарь для ID1
        self.ID1 = {
            "SETUP_GSM_REQ": 0x07, # Настройки, GSM запрос
            "SETUP_GSM_RESP": 0x08, # Настройки, GSM ответ
        }
        #словарь для ID2
        self.ID2 = {
            "IDLE": 0,
            "TRAMP_BEGIN_READ": 0x01,
            "TRAMP_BEGIN_WRITE": 0x02,
            "TRAMP_END_READ": 0x03,
            "TRAMP_END_WRITE": 0x04,
            "DTMF_SET_GUARD_CMD_READ": 0x05,
            "DTMF_SET_GUARD_CMD_WRITE": 0x06,
            "DTMF_RESET_GUARD_CMD_READ": 0x07,
            "DTMF_RESET_GUARD_CMD_WRITE": 0x08,
            "DTMF_CLEAR_ALARM_CMD_READ": 0x09,
            "DTMF_CLEAR_ALARM_CMD_WRITE": 0x0A,
            "CONF_SET_GUARD_SMS_READ": 0x0B,
            "CONF_SET_GUARD_SMS_WRITE": 0x0C,
            "CONF_ALARM_SMS_READ": 0x0D,
            "CONF_ALARM_SMS_WRITE": 0x0E,
            "CONF_ALARM_CALL_READ": 0x0F,
            "CONF_ALARM_CALL_WRITE": 0x10,
            "SMS_SET_GUARD_CMD_READ":   0x11,
            "SMS_SET_GUARD_CMD_WRITE":   0x12,
            "SMS_RESET_GUARD_CMD_READ": 0x13,
            "SMS_RESET_GUARD_CMD_WRITE": 0x14,
            "ALARM_TEXT_READ": 0x15,
            "ALARM_TEXT_WRITE": 0x16,
            "CLEAR_ALARM_TEXT_READ": 0x17,
            "CLEAR_ALARM_TEXT_WRITE": 0x18,
            "TEXT_GUARD_SET_READ": 0x19,
            "TEXT_GUARD_SET_WRITE": 0x1A,
            "GSM_SETUP_U_READ": 0x1B,
            "GSM_SETUP_U_WRITE": 0x1C,
            "SIM900_USER_PHONE_NUMBER_READ": 0x1D,
            "SIM900_USER_PHONE_NUMBER_WRITE": 0x1E,
            "SIM900_USER_TIMEOUT_READ": 0x1F,
            "SIM900_USER_TIMEOUT_WRITE": 0x20,
            "MIN_BALANCE_CALL_READ": 0x21,
            "MIN_BALANCE_CALL_WRITE": 0x22,
            "MIN_BALANCE_SMS_READ": 0x23,
            "MIN_BALANCE_SMS_WRITE": 0x24,
            }
        self.BAUDRATES = ['1200', '9600', '19200', '38400', '57600', '115200']    #возможные значения скоростей для RS-232
        self.READ_BYTES = 100    #количество байт для чтения
        self.OK_ANSWER = bytearray('OK'.encode('latin-1')) #OK
        self.MAX_WAIT_BYTES = 200    #максимальное количество байт в буфере порта на прием
        self.NUMBER_SCAN_PORTS = 5  #количество портов для сканирования
        self.SET = 1
        self.IN_NUMBER = ['1', '2', '3', '4', '5']  # входы
        self.RESET_GUARD_NUMBER = ['1', '2']      # команды снятия с охраны
        self.SET_GUARD_NUMBER = ['1', '2', '3', '4', '5']      # команды установки на охрану

        #значения для парсинга пакета
        self.NOMBER_LENGTH = 13  #длина номера с "+"
        self.NOM_FROM = 7    #пакет READ_NOM - номер байта с которого идет номер телефона
        self.NOM_TO = 20     #пакет READ_NOM - номер байта до которого идет номер телефона
        self.NUM_ABONENTS = 9     # количество пользователей - 1, поскольку счет с 0


    # установка нового значения переменным STATUS
    def Set_Status(self, new_status):
        self.status_old = self.status_new
        self.status_new = new_status

    def Check_Last_Char(self, str_data):
        '''
        проверка на равенство 0 последнего символа str_data
        param str_data: str - данные
        return: str_data без последнего символа если 0, str_data если не 0
        '''
        if isinstance(str_data, str):
            # проверка последний символ на равенство 0
            if ord(str_data[-1]) == 0x00 :
                return str_data[:-1]
            else:
                return str_data
