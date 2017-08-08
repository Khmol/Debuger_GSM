# class Application(object):
#
#     def __init__(self, in_app):
#         self.main_app = in_app

ID2_POS = 6     # номер ID2 в полученном пакете
ID1_POS = 5     # номер ID1 в полученном пакете
DATA_FROM = 7   # начало данных
SIZE_POS = 2    # номер Size в полученном пакете
SIZE_MAX = 100  # максимальная длина пакета

def ArrBite_to_ArrChar( data, data_from, size, size_max):
    '''
    #*********************************************************************
    # извлечение номера в формате str из данных в формате byte
    # [data] - данные в формате byte
    # [data_from] - индекс начала для обработки
    # [size] - длина данных для обработки
    # [size_max] - максимально допустимая длина данных
    #*********************************************************************
    '''
    if (size > 0) and (size < size_max):
        data_to = size - 2
        text = ''
        for i in range(data_from, data_to):
            text += chr(data[i])
        return text


def Parsing_Rx_Pack(data_in):
    """
    парсинг полученного пакета
    param: data_in: {bytes}
    return: [size, crc_rx_int, id1, id2, str_data, bin_data, err]:
    """
    err = False
    str_data = ''
    bin_data = bytearray(b'')
    # выделяем полученную в пакете длину - size
    size = int.from_bytes(data_in[SIZE_POS:SIZE_POS+2], byteorder='little') #преобразуем в int
    # проверка соответствует ли длина реальной
    if size != len(data_in):
        err = True
        id1 = 0
        id2 = 0
        crc_rx_int = 0
    else:
        # выделяем полученное значение ID1
        id1 = int.from_bytes(data_in[ID1_POS:ID1_POS+1], byteorder='little') #преобразуем в int
        id2 = int.from_bytes(data_in[ID2_POS:ID2_POS+1], byteorder='little') #преобразуем в int
        # вылеояем лаееые из принятого пакета
        data_to = size - 2
        for i in range(DATA_FROM, data_to):
            str_data += chr(data_in[i])
            bin_data += data_in[i].to_bytes(1,'little')
        # выделяем полученное CRC
        crc_rx = data_in[size - 2:]   #выделяем CRC
        crc_rx_int = int.from_bytes(crc_rx, byteorder='little') #преобразуем в int
        # bin_data = bytearray(reversed(bin_data))
    return size, crc_rx_int, id1, id2, str_data, bin_data, err


def ReverseBytearray(arr_in):
    arr_out = bytearray()
    for i in reversed(arr_in):
        arr_out += i
    return arr_out

def Convert_To_User_Num(data, max_num):
    '''
    :param data: {int} данные для обработки
    :return: {int} - номер абонента если 0 абонент это 10 бит, а 10 абонент - 0 бит
    '''
    ret_val = max_num
    for i in range(max_num + 1):
        if i == data:
            return ret_val
        ret_val -= 1

def Convert_Str_to_Bytearray(text_in):
    '''
    :param text_in:
    :param bytearray_out:
    :return:
    '''
    if isinstance(text_in, str):
        bytearray_out = bytearray(b'')
        for data in text_in:
            bytearray_out += ord(data).to_bytes(1,'little')
        return bytearray_out
    else:
        return None