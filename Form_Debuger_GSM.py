# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Debuger_GSM.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Debuger_GSM(object):
    def setupUi(self, Debuger_GSM):
        Debuger_GSM.setObjectName("Debuger_GSM")
        Debuger_GSM.resize(667, 456)
        Debuger_GSM.setMinimumSize(QtCore.QSize(667, 456))
        Debuger_GSM.setMaximumSize(QtCore.QSize(667, 456))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("touchscreen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Debuger_GSM.setWindowIcon(icon)
        Debuger_GSM.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(Debuger_GSM)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_Baudrate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Baudrate.setGeometry(QtCore.QRect(89, 28, 74, 20))
        self.comboBox_Baudrate.setObjectName("comboBox_Baudrate")
        self.comboBox_COM = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_COM.setGeometry(QtCore.QRect(9, 28, 74, 20))
        self.comboBox_COM.setObjectName("comboBox_COM")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_open_COM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_COM.setGeometry(QtCore.QRect(169, 27, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_open_COM.setFont(font)
        self.pushButton_open_COM.setObjectName("pushButton_open_COM")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 661, 351))
        self.tabWidget.setMinimumSize(QtCore.QSize(661, 351))
        self.tabWidget.setMaximumSize(QtCore.QSize(661, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.users = QtWidgets.QWidget()
        self.users.setObjectName("users")
        self.list_users_nom = QtWidgets.QListWidget(self.users)
        self.list_users_nom.setEnabled(False)
        self.list_users_nom.setGeometry(QtCore.QRect(0, 0, 51, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.list_users_nom.setFont(font)
        self.list_users_nom.setObjectName("list_users_nom")
        self.lineEdit_Telephone_Number = QtWidgets.QLineEdit(self.users)
        self.lineEdit_Telephone_Number.setEnabled(False)
        self.lineEdit_Telephone_Number.setGeometry(QtCore.QRect(70, 30, 151, 20))
        self.lineEdit_Telephone_Number.setObjectName("lineEdit_Telephone_Number")
        self.label_Example_Tel_Number = QtWidgets.QLabel(self.users)
        self.label_Example_Tel_Number.setEnabled(True)
        self.label_Example_Tel_Number.setGeometry(QtCore.QRect(72, 8, 281, 16))
        self.label_Example_Tel_Number.setObjectName("label_Example_Tel_Number")
        self.pushButton_Read_Users = QtWidgets.QPushButton(self.users)
        self.pushButton_Read_Users.setEnabled(False)
        self.pushButton_Read_Users.setGeometry(QtCore.QRect(200, 290, 80, 25))
        self.pushButton_Read_Users.setObjectName("pushButton_Read_Users")
        self.pushButton_Write_Users = QtWidgets.QPushButton(self.users)
        self.pushButton_Write_Users.setEnabled(False)
        self.pushButton_Write_Users.setGeometry(QtCore.QRect(290, 290, 80, 25))
        self.pushButton_Write_Users.setObjectName("pushButton_Write_Users")
        self.checkBox_SMS_set_guard = QtWidgets.QCheckBox(self.users)
        self.checkBox_SMS_set_guard.setEnabled(False)
        self.checkBox_SMS_set_guard.setGeometry(QtCore.QRect(70, 58, 331, 18))
        self.checkBox_SMS_set_guard.setObjectName("checkBox_SMS_set_guard")
        self.checkBox_SMS_alarm = QtWidgets.QCheckBox(self.users)
        self.checkBox_SMS_alarm.setEnabled(False)
        self.checkBox_SMS_alarm.setGeometry(QtCore.QRect(70, 78, 241, 18))
        self.checkBox_SMS_alarm.setObjectName("checkBox_SMS_alarm")
        self.checkBox_call_back_alarm = QtWidgets.QCheckBox(self.users)
        self.checkBox_call_back_alarm.setEnabled(False)
        self.checkBox_call_back_alarm.setGeometry(QtCore.QRect(70, 98, 371, 18))
        self.checkBox_call_back_alarm.setChecked(False)
        self.checkBox_call_back_alarm.setObjectName("checkBox_call_back_alarm")
        self.spinBox_sim900_user_timeout = QtWidgets.QSpinBox(self.users)
        self.spinBox_sim900_user_timeout.setEnabled(False)
        self.spinBox_sim900_user_timeout.setGeometry(QtCore.QRect(70, 128, 51, 22))
        self.spinBox_sim900_user_timeout.setMaximum(255)
        self.spinBox_sim900_user_timeout.setObjectName("spinBox_sim900_user_timeout")
        self.label_Max_Time_Talk = QtWidgets.QLabel(self.users)
        self.label_Max_Time_Talk.setEnabled(False)
        self.label_Max_Time_Talk.setGeometry(QtCore.QRect(130, 130, 321, 16))
        self.label_Max_Time_Talk.setObjectName("label_Max_Time_Talk")
        self.tabWidget.addTab(self.users, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_in_number = QtWidgets.QComboBox(self.tab)
        self.comboBox_in_number.setEnabled(False)
        self.comboBox_in_number.setGeometry(QtCore.QRect(10, 30, 74, 20))
        self.comboBox_in_number.setObjectName("comboBox_in_number")
        self.label_in_number = QtWidgets.QLabel(self.tab)
        self.label_in_number.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_in_number.setFont(font)
        self.label_in_number.setObjectName("label_in_number")
        self.pushButton_Read_In = QtWidgets.QPushButton(self.tab)
        self.pushButton_Read_In.setEnabled(False)
        self.pushButton_Read_In.setGeometry(QtCore.QRect(200, 290, 80, 25))
        self.pushButton_Read_In.setObjectName("pushButton_Read_In")
        self.pushButton_Write_In = QtWidgets.QPushButton(self.tab)
        self.pushButton_Write_In.setEnabled(False)
        self.pushButton_Write_In.setGeometry(QtCore.QRect(290, 290, 80, 25))
        self.pushButton_Write_In.setObjectName("pushButton_Write_In")
        self.lineEdit_in_alarm_text = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_in_alarm_text.setEnabled(False)
        self.lineEdit_in_alarm_text.setGeometry(QtCore.QRect(90, 30, 151, 20))
        self.lineEdit_in_alarm_text.setObjectName("lineEdit_in_alarm_text")
        self.label_in_number_2 = QtWidgets.QLabel(self.tab)
        self.label_in_number_2.setGeometry(QtCore.QRect(90, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_in_number_2.setFont(font)
        self.label_in_number_2.setObjectName("label_in_number_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(10, 10, 641, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox_Reset_Guard = QtWidgets.QComboBox(self.frame)
        self.comboBox_Reset_Guard.setEnabled(False)
        self.comboBox_Reset_Guard.setGeometry(QtCore.QRect(10, 100, 51, 20))
        self.comboBox_Reset_Guard.setObjectName("comboBox_Reset_Guard")
        self.label_File_Name_3 = QtWidgets.QLabel(self.tab_3)
        self.label_File_Name_3.setGeometry(QtCore.QRect(340, 90, 221, 16))
        self.label_File_Name_3.setObjectName("label_File_Name_3")
        self.lineEdit_clear_alarm_text = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_clear_alarm_text.setEnabled(False)
        self.lineEdit_clear_alarm_text.setGeometry(QtCore.QRect(340, 110, 201, 20))
        self.lineEdit_clear_alarm_text.setObjectName("lineEdit_clear_alarm_text")
        self.label_File_Name_4 = QtWidgets.QLabel(self.tab_3)
        self.label_File_Name_4.setGeometry(QtCore.QRect(180, 20, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_File_Name_4.setFont(font)
        self.label_File_Name_4.setObjectName("label_File_Name_4")
        self.label_sms_reset_guard_cmd_1 = QtWidgets.QLabel(self.tab_3)
        self.label_sms_reset_guard_cmd_1.setGeometry(QtCore.QRect(110, 90, 201, 16))
        self.label_sms_reset_guard_cmd_1.setObjectName("label_sms_reset_guard_cmd_1")
        self.lineEdit_sms_reset_guard_cmd = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_sms_reset_guard_cmd.setEnabled(False)
        self.lineEdit_sms_reset_guard_cmd.setGeometry(QtCore.QRect(100, 110, 200, 20))
        self.lineEdit_sms_reset_guard_cmd.setText("")
        self.lineEdit_sms_reset_guard_cmd.setObjectName("lineEdit_sms_reset_guard_cmd")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 641, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_File_Name_5 = QtWidgets.QLabel(self.frame_2)
        self.label_File_Name_5.setGeometry(QtCore.QRect(170, 10, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_File_Name_5.setFont(font)
        self.label_File_Name_5.setObjectName("label_File_Name_5")
        self.lineEdit_text_guard_set = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_text_guard_set.setEnabled(False)
        self.lineEdit_text_guard_set.setGeometry(QtCore.QRect(20, 210, 181, 20))
        self.lineEdit_text_guard_set.setObjectName("lineEdit_text_guard_set")
        self.label_File_Name_2 = QtWidgets.QLabel(self.tab_3)
        self.label_File_Name_2.setGeometry(QtCore.QRect(20, 190, 221, 16))
        self.label_File_Name_2.setObjectName("label_File_Name_2")
        self.pushButton_Read_SMS = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Read_SMS.setEnabled(False)
        self.pushButton_Read_SMS.setGeometry(QtCore.QRect(200, 290, 80, 25))
        self.pushButton_Read_SMS.setObjectName("pushButton_Read_SMS")
        self.pushButton_Write_SMS = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Write_SMS.setEnabled(False)
        self.pushButton_Write_SMS.setGeometry(QtCore.QRect(290, 290, 80, 25))
        self.pushButton_Write_SMS.setObjectName("pushButton_Write_SMS")
        self.label_sms_reset_guard_cmd_2 = QtWidgets.QLabel(self.tab_3)
        self.label_sms_reset_guard_cmd_2.setGeometry(QtCore.QRect(20, 90, 71, 16))
        self.label_sms_reset_guard_cmd_2.setObjectName("label_sms_reset_guard_cmd_2")
        self.label_sms_reset_guard_cmd_3 = QtWidgets.QLabel(self.tab_3)
        self.label_sms_reset_guard_cmd_3.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label_sms_reset_guard_cmd_3.setObjectName("label_sms_reset_guard_cmd_3")
        self.label_sms_reset_guard_cmd_4 = QtWidgets.QLabel(self.tab_3)
        self.label_sms_reset_guard_cmd_4.setGeometry(QtCore.QRect(110, 50, 201, 16))
        self.label_sms_reset_guard_cmd_4.setObjectName("label_sms_reset_guard_cmd_4")
        self.lineEdit_sms_Set_Guard_Cmd = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_sms_Set_Guard_Cmd.setEnabled(False)
        self.lineEdit_sms_Set_Guard_Cmd.setGeometry(QtCore.QRect(100, 70, 200, 20))
        self.lineEdit_sms_Set_Guard_Cmd.setText("")
        self.lineEdit_sms_Set_Guard_Cmd.setObjectName("lineEdit_sms_Set_Guard_Cmd")
        self.comboBox_Set_Guard = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_Set_Guard.setEnabled(False)
        self.comboBox_Set_Guard.setGeometry(QtCore.QRect(20, 70, 51, 20))
        self.comboBox_Set_Guard.setObjectName("comboBox_Set_Guard")
        self.tabWidget.addTab(self.tab_3, "")
        self.general_config = QtWidgets.QWidget()
        self.general_config.setObjectName("general_config")
        self.label_File_Name_7 = QtWidgets.QLabel(self.general_config)
        self.label_File_Name_7.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label_File_Name_7.setObjectName("label_File_Name_7")
        self.spinBox_min_balance_SMS = QtWidgets.QSpinBox(self.general_config)
        self.spinBox_min_balance_SMS.setEnabled(False)
        self.spinBox_min_balance_SMS.setGeometry(QtCore.QRect(10, 30, 51, 22))
        self.spinBox_min_balance_SMS.setMaximum(255)
        self.spinBox_min_balance_SMS.setObjectName("spinBox_min_balance_SMS")
        self.pushButton_Read_GS = QtWidgets.QPushButton(self.general_config)
        self.pushButton_Read_GS.setEnabled(False)
        self.pushButton_Read_GS.setGeometry(QtCore.QRect(200, 290, 80, 25))
        self.pushButton_Read_GS.setObjectName("pushButton_Read_GS")
        self.pushButton_Write_GS = QtWidgets.QPushButton(self.general_config)
        self.pushButton_Write_GS.setEnabled(False)
        self.pushButton_Write_GS.setGeometry(QtCore.QRect(290, 290, 80, 25))
        self.pushButton_Write_GS.setObjectName("pushButton_Write_GS")
        self.spinBox_min_balance_call = QtWidgets.QSpinBox(self.general_config)
        self.spinBox_min_balance_call.setEnabled(False)
        self.spinBox_min_balance_call.setGeometry(QtCore.QRect(160, 30, 51, 22))
        self.spinBox_min_balance_call.setMaximum(255)
        self.spinBox_min_balance_call.setObjectName("spinBox_min_balance_call")
        self.label_File_Name_8 = QtWidgets.QLabel(self.general_config)
        self.label_File_Name_8.setGeometry(QtCore.QRect(160, 10, 281, 16))
        self.label_File_Name_8.setObjectName("label_File_Name_8")
        self.checkBox_let_set_guard_nom = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_let_set_guard_nom.setEnabled(False)
        self.checkBox_let_set_guard_nom.setGeometry(QtCore.QRect(10, 220, 411, 18))
        self.checkBox_let_set_guard_nom.setObjectName("checkBox_let_set_guard_nom")
        self.checkBox_let_set_guard_no_nom = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_let_set_guard_no_nom.setEnabled(False)
        self.checkBox_let_set_guard_no_nom.setGeometry(QtCore.QRect(10, 200, 411, 18))
        self.checkBox_let_set_guard_no_nom.setObjectName("checkBox_let_set_guard_no_nom")
        self.checkBox_rep_sms_self = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_rep_sms_self.setEnabled(False)
        self.checkBox_rep_sms_self.setGeometry(QtCore.QRect(10, 180, 541, 18))
        self.checkBox_rep_sms_self.setObjectName("checkBox_rep_sms_self")
        self.checkBox_rep_call_back_self = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_rep_call_back_self.setEnabled(False)
        self.checkBox_rep_call_back_self.setGeometry(QtCore.QRect(10, 160, 571, 18))
        self.checkBox_rep_call_back_self.setChecked(False)
        self.checkBox_rep_call_back_self.setObjectName("checkBox_rep_call_back_self")
        self.checkBox_send_sms_always = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_send_sms_always.setEnabled(False)
        self.checkBox_send_sms_always.setGeometry(QtCore.QRect(10, 240, 301, 18))
        self.checkBox_send_sms_always.setChecked(False)
        self.checkBox_send_sms_always.setObjectName("checkBox_send_sms_always")
        self.checkBox_call_back_always = QtWidgets.QCheckBox(self.general_config)
        self.checkBox_call_back_always.setEnabled(False)
        self.checkBox_call_back_always.setGeometry(QtCore.QRect(10, 260, 301, 18))
        self.checkBox_call_back_always.setChecked(False)
        self.checkBox_call_back_always.setObjectName("checkBox_call_back_always")
        self.label_dtmf_alarm_off = QtWidgets.QLabel(self.general_config)
        self.label_dtmf_alarm_off.setGeometry(QtCore.QRect(340, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_dtmf_alarm_off.setFont(font)
        self.label_dtmf_alarm_off.setObjectName("label_dtmf_alarm_off")
        self.lineEdit_dtmf_clear_alarm_cmd = QtWidgets.QLineEdit(self.general_config)
        self.lineEdit_dtmf_clear_alarm_cmd.setEnabled(False)
        self.lineEdit_dtmf_clear_alarm_cmd.setGeometry(QtCore.QRect(340, 30, 151, 20))
        self.lineEdit_dtmf_clear_alarm_cmd.setText("")
        self.lineEdit_dtmf_clear_alarm_cmd.setObjectName("lineEdit_dtmf_clear_alarm_cmd")
        self.lineEdit_dtmf_set_guard = QtWidgets.QLineEdit(self.general_config)
        self.lineEdit_dtmf_set_guard.setEnabled(False)
        self.lineEdit_dtmf_set_guard.setGeometry(QtCore.QRect(90, 130, 151, 20))
        self.lineEdit_dtmf_set_guard.setObjectName("lineEdit_dtmf_set_guard")
        self.label_dtmf_set_guard_2 = QtWidgets.QLabel(self.general_config)
        self.label_dtmf_set_guard_2.setGeometry(QtCore.QRect(90, 110, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_dtmf_set_guard_2.setFont(font)
        self.label_dtmf_set_guard_2.setObjectName("label_dtmf_set_guard_2")
        self.label_dtmf_set_guard = QtWidgets.QLabel(self.general_config)
        self.label_dtmf_set_guard.setGeometry(QtCore.QRect(10, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_dtmf_set_guard.setFont(font)
        self.label_dtmf_set_guard.setObjectName("label_dtmf_set_guard")
        self.comboBox_dtmf_set_guard = QtWidgets.QComboBox(self.general_config)
        self.comboBox_dtmf_set_guard.setEnabled(False)
        self.comboBox_dtmf_set_guard.setGeometry(QtCore.QRect(10, 130, 74, 20))
        self.comboBox_dtmf_set_guard.setObjectName("comboBox_dtmf_set_guard")
        self.comboBox_dtmf_reset_guard = QtWidgets.QComboBox(self.general_config)
        self.comboBox_dtmf_reset_guard.setEnabled(False)
        self.comboBox_dtmf_reset_guard.setGeometry(QtCore.QRect(340, 130, 74, 20))
        self.comboBox_dtmf_reset_guard.setObjectName("comboBox_dtmf_reset_guard")
        self.label_dtmf_reset_guard = QtWidgets.QLabel(self.general_config)
        self.label_dtmf_reset_guard.setGeometry(QtCore.QRect(340, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_dtmf_reset_guard.setFont(font)
        self.label_dtmf_reset_guard.setObjectName("label_dtmf_reset_guard")
        self.label_dtmf_reset_guard_2 = QtWidgets.QLabel(self.general_config)
        self.label_dtmf_reset_guard_2.setGeometry(QtCore.QRect(420, 110, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_dtmf_reset_guard_2.setFont(font)
        self.label_dtmf_reset_guard_2.setObjectName("label_dtmf_reset_guard_2")
        self.lineEdit_dtmf_reset_guard = QtWidgets.QLineEdit(self.general_config)
        self.lineEdit_dtmf_reset_guard.setEnabled(False)
        self.lineEdit_dtmf_reset_guard.setGeometry(QtCore.QRect(420, 130, 151, 20))
        self.lineEdit_dtmf_reset_guard.setObjectName("lineEdit_dtmf_reset_guard")
        self.lineEdit_trump_begin = QtWidgets.QLineEdit(self.general_config)
        self.lineEdit_trump_begin.setEnabled(False)
        self.lineEdit_trump_begin.setGeometry(QtCore.QRect(10, 80, 151, 20))
        self.lineEdit_trump_begin.setText("")
        self.lineEdit_trump_begin.setObjectName("lineEdit_trump_begin")
        self.label_rtump_begin = QtWidgets.QLabel(self.general_config)
        self.label_rtump_begin.setGeometry(QtCore.QRect(10, 60, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_rtump_begin.setFont(font)
        self.label_rtump_begin.setObjectName("label_rtump_begin")
        self.lineEdit_trump_end = QtWidgets.QLineEdit(self.general_config)
        self.lineEdit_trump_end.setEnabled(False)
        self.lineEdit_trump_end.setGeometry(QtCore.QRect(340, 80, 151, 20))
        self.lineEdit_trump_end.setText("")
        self.lineEdit_trump_end.setObjectName("lineEdit_trump_end")
        self.label_rtump_end = QtWidgets.QLabel(self.general_config)
        self.label_rtump_end.setGeometry(QtCore.QRect(340, 60, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_rtump_end.setFont(font)
        self.label_rtump_end.setObjectName("label_rtump_end")
        self.label_rtump_end_2 = QtWidgets.QLabel(self.general_config)
        self.label_rtump_end_2.setGeometry(QtCore.QRect(190, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_rtump_end_2.setFont(font)
        self.label_rtump_end_2.setObjectName("label_rtump_end_2")
        self.tabWidget.addTab(self.general_config, "")
        self.pushButton_close_COM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close_COM.setEnabled(False)
        self.pushButton_close_COM.setGeometry(QtCore.QRect(266, 27, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_close_COM.setFont(font)
        self.pushButton_close_COM.setObjectName("pushButton_close_COM")
        Debuger_GSM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Debuger_GSM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 18))
        self.menubar.setObjectName("menubar")
        Debuger_GSM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Debuger_GSM)
        self.statusbar.setObjectName("statusbar")
        Debuger_GSM.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(Debuger_GSM)
        self.action.setObjectName("action")

        self.retranslateUi(Debuger_GSM)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Debuger_GSM)

    def retranslateUi(self, Debuger_GSM):
        _translate = QtCore.QCoreApplication.translate
        Debuger_GSM.setWindowTitle(_translate("Debuger_GSM", "Настройка сигнализации"))
        self.label_2.setText(_translate("Debuger_GSM", "Выбор порта"))
        self.pushButton_open_COM.setText(_translate("Debuger_GSM", "Открыть порт"))
        self.label_Example_Tel_Number.setText(_translate("Debuger_GSM", "Номер телефона (например +380504777777)"))
        self.pushButton_Read_Users.setText(_translate("Debuger_GSM", "Прочитать"))
        self.pushButton_Write_Users.setText(_translate("Debuger_GSM", "Установить"))
        self.checkBox_SMS_set_guard.setText(_translate("Debuger_GSM", "SMS оповещение об установке на охрану"))
        self.checkBox_SMS_alarm.setText(_translate("Debuger_GSM", "SMS оповещение при аварии"))
        self.checkBox_call_back_alarm.setText(_translate("Debuger_GSM", "Обратный звонок при аварии"))
        self.label_Max_Time_Talk.setText(_translate("Debuger_GSM", "максимальная продолжительность разговора, секунд"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.users), _translate("Debuger_GSM", "Пользователи"))
        self.label_in_number.setText(_translate("Debuger_GSM", "№ входа"))
        self.pushButton_Read_In.setText(_translate("Debuger_GSM", "Прочитать"))
        self.pushButton_Write_In.setText(_translate("Debuger_GSM", "Установить"))
        self.label_in_number_2.setText(_translate("Debuger_GSM", "Текст СМС при срабатывании"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Debuger_GSM", "Входы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Debuger_GSM", "Выходы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Debuger_GSM", "Брелки"))
        self.label_File_Name_3.setText(_translate("Debuger_GSM", "Снятие аварии"))
        self.label_File_Name_4.setText(_translate("Debuger_GSM", "СМС от абонента к сигнализации"))
        self.label_sms_reset_guard_cmd_1.setText(_translate("Debuger_GSM", "Снятие с охраны"))
        self.label_File_Name_5.setText(_translate("Debuger_GSM", "СМС от сигнализации к абоненту"))
        self.label_File_Name_2.setText(_translate("Debuger_GSM", "Охрана установлена"))
        self.pushButton_Read_SMS.setText(_translate("Debuger_GSM", "Прочитать"))
        self.pushButton_Write_SMS.setText(_translate("Debuger_GSM", "Установить"))
        self.label_sms_reset_guard_cmd_2.setText(_translate("Debuger_GSM", "№ режима"))
        self.label_sms_reset_guard_cmd_3.setText(_translate("Debuger_GSM", "№ режима"))
        self.label_sms_reset_guard_cmd_4.setText(_translate("Debuger_GSM", "Установка на охрану"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Debuger_GSM", "СМС"))
        self.label_File_Name_7.setText(_translate("Debuger_GSM", "Лимит денег для СМС"))
        self.pushButton_Read_GS.setText(_translate("Debuger_GSM", "Прочитать"))
        self.pushButton_Write_GS.setText(_translate("Debuger_GSM", "Установить"))
        self.label_File_Name_8.setText(_translate("Debuger_GSM", "Лимит денег для звонков"))
        self.checkBox_let_set_guard_nom.setText(_translate("Debuger_GSM", "Установка на охрану по звонку с донабором защитного кода"))
        self.checkBox_let_set_guard_no_nom.setText(_translate("Debuger_GSM", "Установка на охрану по звонку без донабора защитного кода"))
        self.checkBox_rep_sms_self.setText(_translate("Debuger_GSM", "Передавать СМС уведомление о постановке на охрану тому, кто поставил на охрану"))
        self.checkBox_rep_call_back_self.setText(_translate("Debuger_GSM", "Обратный звонок как уведомление о постановке на охрану тому, кто поставил на охрану"))
        self.checkBox_send_sms_always.setText(_translate("Debuger_GSM", "Отправлять СМС даже при низком балансе"))
        self.checkBox_call_back_always.setText(_translate("Debuger_GSM", "Обратный звонок даже при низком балансе"))
        self.label_dtmf_alarm_off.setText(_translate("Debuger_GSM", " DTMF для снятия аварии"))
        self.label_dtmf_set_guard_2.setText(_translate("Debuger_GSM", "DTMF код установки на охрану"))
        self.label_dtmf_set_guard.setText(_translate("Debuger_GSM", "№ режима"))
        self.label_dtmf_reset_guard.setText(_translate("Debuger_GSM", "№ режима"))
        self.label_dtmf_reset_guard_2.setText(_translate("Debuger_GSM", "DTMF код снятия с охраны"))
        self.label_rtump_begin.setText(_translate("Debuger_GSM", "Начало команды \"Перезвони мне\""))
        self.label_rtump_end.setText(_translate("Debuger_GSM", "Конец команды \"Перезвони мне\""))
        self.label_rtump_end_2.setText(_translate("Debuger_GSM", "<- номер телефона ->"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_config), _translate("Debuger_GSM", "Общие настройки"))
        self.pushButton_close_COM.setText(_translate("Debuger_GSM", "Закрыть порт"))
        self.action.setText(_translate("Debuger_GSM", "Закрыть"))

