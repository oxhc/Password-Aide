# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(266, 259)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color:white;")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(100, 10, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgs/login_av.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.user_name = QtWidgets.QLineEdit(Login)
        self.user_name.setGeometry(QtCore.QRect(70, 90, 151, 20))
        self.user_name.setObjectName("user_name")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 31, 21))
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(Login)
        self.password.setGeometry(QtCore.QRect(70, 130, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        self.password.setFont(font)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setReadOnly(False)
        self.password.setObjectName("password")
        self.guest_button = QtWidgets.QPushButton(Login)
        self.guest_button.setGeometry(QtCore.QRect(140, 180, 71, 23))
        self.guest_button.setAutoFillBackground(False)
        self.guest_button.setAutoDefault(True)
        self.guest_button.setDefault(True)
        self.guest_button.setFlat(True)
        self.guest_button.setObjectName("guest_button")
        self.login_button = QtWidgets.QPushButton(Login)
        self.login_button.setEnabled(True)
        self.login_button.setGeometry(QtCore.QRect(50, 180, 71, 23))
        self.login_button.setCheckable(False)
        self.login_button.setAutoDefault(True)
        self.login_button.setDefault(True)
        self.login_button.setFlat(True)
        self.login_button.setObjectName("login_button")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "管理员登录"))
        self.label_2.setText(_translate("Login", "账号:"))
        self.label_3.setText(_translate("Login", "密码:"))
        self.guest_button.setText(_translate("Login", "访客"))
        self.login_button.setText(_translate("Login", "登录"))


import img_rc
