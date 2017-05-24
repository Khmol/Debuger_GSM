# -*- encoding: utf-8 -*-

import unittest
from Debuger_GSM import *
from PyQt5 import QtWidgets #QtCore, QtGui,

class TestUM(unittest.TestCase):
    def setUp(self):
        self.widg = QtWidgets.QApplication(sys.argv)
        self.app = Debuger_GSM()
        list = 0x55, 0xaa, 0x17, 0x00, 0xe, 0x8, 0x1d, 0x2b, 0x33, 0x38, 0x30, 0x35, 0x30,\
               0x34, 0x37, 0x33, 0x35, 0x33, 0x35, 0x37, 0x0, 0x6c, 0xe2
        self.rs_receive_pack = bytearray(list)

    def test_Check_Bit_1_ok(self):
        res = self.app.event.Check_Bit(0x01,0)
        self.assertEqual(res, 1)

    def test_Check_Bit_1_no(self):
        res = self.app.event.Check_Bit(0x01,2)
        self.assertEqual(res, 0)

    def test_Set_Bit(self):
        res = self.app.event.Set_Bit(0x01,2)
        self.assertEqual(res, 5)

    def test_Show_Warning_TX_OK(self):
        start_index = 7
        length = 13
        res = self.app.event.Show_Warning_TX_OK(self.rs_receive_pack, start_index, length)
        self.assertTrue(res)

    def test_Reload_Widget_General_Page(self):
        data = (0,0,0,0xFF)
        res = self.app.event.Reload_Widget_General_Page(data)
        self.assertTrue(res)

    def test_Send_Command(self):
        self.app.rs.Serial_Config(115200, 'COM2')
        res = self.app.rs.Send_Command(self.app.ID2["MIN_BALANCE_SMS_READ"],
                                       self.app.ID1["SETUP_GSM_REQ"],
                                       self.app.ID2["MIN_BALANCE_SMS_READ"],
                                       self.app.rs.TIME_TO_RX)
        self.app.rs.Serial_Close()
        self.app.timer_RX_RS.stop() #выключаем таймер
        self.assertEqual(res, ['Ok'])

    def test_Enable_Disable_Widgets(self):
        res = self.app.event.Init_Widgets()
        self.assertEqual(res, None)
        res = self.app.event.Enable_Widget_In_Page()
        self.assertEqual(res, None)
        res = self.app.event.Disable_Widget_In_Page()
        self.assertEqual(res, None)
        res = self.app.event.Enable_Widget_User_Page()
        self.assertEqual(res, None)
        res = self.app.event.Disable_Widget_User_Page()
        self.assertEqual(res, None)
        res = self.app.event.Enable_Widget_SMS_Page()
        self.assertEqual(res, None)
        res = self.app.event.Disable_Widget_SMS_Page()
        self.assertEqual(res, None)
        res = self.app.event.Enable_Widget_General_Page()
        self.assertEqual(res, None)
        res = self.app.event.Disable_Widget_General_Page()
        self.assertEqual(res, None)


    def test_Convert_To_User_Num(self):
        res = Convert_To_User_Num(0, 9)
        self.assertEqual(res, 9)
        res = Convert_To_User_Num(9, 9)
        self.assertEqual(res, 0)

    def test_Reset_Bit(self):
        d = 2789
        res = self.app.event.Reset_Bit(d.to_bytes(2,'big'), 6)
        self.assertEqual(int.from_bytes(res, byteorder='big'), 2725)
        res = self.app.event.Reset_Bit(2789, 9)
        self.assertEqual(res, 2277)
        res = self.app.event.Reset_Bit(2, 1)
        self.assertEqual(res, 0)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
