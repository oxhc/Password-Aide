# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imgs/logo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(440, 156))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.open_pw = QtWidgets.QPushButton(self.groupBox_4)
        self.open_pw.setDefault(True)
        self.open_pw.setFlat(True)
        self.open_pw.setObjectName("open_pw")
        self.horizontalLayout_4.addWidget(self.open_pw)
        self.generate = QtWidgets.QPushButton(self.groupBox_4)
        self.generate.setDefault(True)
        self.generate.setFlat(True)
        self.generate.setObjectName("generate")
        self.horizontalLayout_4.addWidget(self.generate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_button = QtWidgets.QPushButton(self.groupBox_4)
        self.import_button.setMinimumSize(QtCore.QSize(320, 0))
        self.import_button.setDefault(True)
        self.import_button.setFlat(True)
        self.import_button.setObjectName("import_button")
        self.horizontalLayout.addWidget(self.import_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.entop = QtWidgets.QPushButton(self.groupBox_4)
        self.entop.setMinimumSize(QtCore.QSize(0, 68))
        self.entop.setMaximumSize(QtCore.QSize(83, 16777215))
        self.entop.setDefault(False)
        self.entop.setFlat(True)
        self.entop.setObjectName("entop")
        self.verticalLayout_4.addWidget(self.entop)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(440, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.g_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.g_name.setObjectName("g_name")
        self.horizontalLayout_9.addWidget(self.g_name)
        self.copy_name = QtWidgets.QPushButton(self.groupBox_3)
        self.copy_name.setDefault(True)
        self.copy_name.setFlat(True)
        self.copy_name.setObjectName("copy_name")
        self.horizontalLayout_9.addWidget(self.copy_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.g_url = QtWidgets.QLineEdit(self.groupBox_3)
        self.g_url.setObjectName("g_url")
        self.horizontalLayout_8.addWidget(self.g_url)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.g_username = QtWidgets.QLineEdit(self.groupBox_3)
        self.g_username.setReadOnly(False)
        self.g_username.setObjectName("g_username")
        self.horizontalLayout_3.addWidget(self.g_username)
        self.username_combo = QtWidgets.QComboBox(self.groupBox_3)
        self.username_combo.setFrame(False)
        self.username_combo.setObjectName("username_combo")
        self.horizontalLayout_3.addWidget(self.username_combo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.p_ged = QtWidgets.QLineEdit(self.groupBox_3)
        self.p_ged.setObjectName("p_ged")
        self.horizontalLayout_5.addWidget(self.p_ged)
        self.copy_pass = QtWidgets.QPushButton(self.groupBox_3)
        self.copy_pass.setDefault(True)
        self.copy_pass.setFlat(True)
        self.copy_pass.setObjectName("copy_pass")
        self.horizontalLayout_5.addWidget(self.copy_pass)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.insert = QtWidgets.QPushButton(self.groupBox_3)
        self.insert.setAutoDefault(False)
        self.insert.setDefault(True)
        self.insert.setFlat(True)
        self.insert.setObjectName("insert")
        self.horizontalLayout_7.addWidget(self.insert)
        self.copy_user = QtWidgets.QPushButton(self.groupBox_3)
        self.copy_user.setAutoDefault(False)
        self.copy_user.setDefault(True)
        self.copy_user.setFlat(True)
        self.copy_user.setObjectName("copy_user")
        self.horizontalLayout_7.addWidget(self.copy_user)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.confirm = QtWidgets.QPushButton(self.groupBox_3)
        self.confirm.setAutoDefault(False)
        self.confirm.setDefault(True)
        self.confirm.setFlat(True)
        self.confirm.setObjectName("confirm")
        self.verticalLayout_3.addWidget(self.confirm)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(293, 77))
        self.groupBox.setMaximumSize(QtCore.QSize(440, 76))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(30, 26))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/imgs/search_stu.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.keyword = QtWidgets.QLineEdit(self.groupBox)
        self.keyword.setText("")
        self.keyword.setObjectName("keyword")
        self.horizontalLayout_2.addWidget(self.keyword)
        self.search_button = QtWidgets.QPushButton(self.groupBox)
        self.search_button.setAutoDefault(False)
        self.search_button.setDefault(True)
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_2.addWidget(self.search_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.file_menu = QtWidgets.QAction(MainWindow)
        self.file_menu.setObjectName("file_menu")
        self.exit_menu = QtWidgets.QAction(MainWindow)
        self.exit_menu.setObjectName("exit_menu")
        self.about_menu = QtWidgets.QAction(MainWindow)
        self.about_menu.setObjectName("about_menu")
        self.cur_status = QtWidgets.QAction(MainWindow)
        self.cur_status.setObjectName("cur_status")
        self.logout = QtWidgets.QAction(MainWindow)
        self.logout.setObjectName("logout")
        self.pw_menu = QtWidgets.QAction(MainWindow)
        self.pw_menu.setObjectName("pw_menu")
        self.dorm_menu = QtWidgets.QAction(MainWindow)
        self.dorm_menu.setObjectName("dorm_menu")
        self.repair_menu = QtWidgets.QAction(MainWindow)
        self.repair_menu.setObjectName("repair_menu")
        self.repair_submit_menu = QtWidgets.QAction(MainWindow)
        self.repair_submit_menu.setObjectName("repair_submit_menu")
        self.normal_import_menu = QtWidgets.QAction(MainWindow)
        self.normal_import_menu.setObjectName("normal_import_menu")
        self.menu.addAction(self.file_menu)
        self.menu.addAction(self.exit_menu)
        self.menu_2.addAction(self.pw_menu)
        self.menu_4.addAction(self.cur_status)
        self.menu_4.addAction(self.logout)
        self.menu_5.addAction(self.about_menu)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Aide"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Entries"))
        self.open_pw.setText(_translate("MainWindow", "Passwd Manage"))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.import_button.setText(_translate("MainWindow", "Import from xls or xlsx file"))
        self.entop.setText(_translate("MainWindow", "Not\n"
                                                    "Top"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Generator"))
        self.label_4.setText(_translate("MainWindow", "name:"))
        self.copy_name.setText(_translate("MainWindow", "copy"))
        self.label_3.setText(_translate("MainWindow", "url: "))
        self.label.setText(_translate("MainWindow", "username:"))
        self.g_username.setText(_translate("MainWindow", "default  ->"))
        self.g_username.setPlaceholderText(_translate("MainWindow", "username(default)"))
        self.label_2.setText(_translate("MainWindow", "password:"))
        self.p_ged.setPlaceholderText(_translate("MainWindow", "password(auto)"))
        self.copy_pass.setText(_translate("MainWindow", "copy"))
        self.insert.setText(_translate("MainWindow", "Save"))
        self.copy_user.setText(_translate("MainWindow", "copy username"))
        self.confirm.setText(_translate("MainWindow", "Copy Password and Save"))
        self.groupBox.setTitle(_translate("MainWindow", "Password Search"))
        self.keyword.setPlaceholderText(_translate("MainWindow", "Input keyword here"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menu_2.setTitle(_translate("MainWindow", "Info Manage"))
        self.menu_4.setTitle(_translate("MainWindow", "Administrator"))
        self.menu_5.setTitle(_translate("MainWindow", "About"))
        self.file_menu.setText(_translate("MainWindow", "Import from xls file"))
        self.exit_menu.setText(_translate("MainWindow", "退出"))
        self.about_menu.setText(_translate("MainWindow", "About software"))
        self.cur_status.setText(_translate("MainWindow", "Present: Super Administrator"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.pw_menu.setText(_translate("MainWindow", "Password Manage"))
        self.dorm_menu.setText(_translate("MainWindow", "管理宿舍信息"))
        self.repair_menu.setText(_translate("MainWindow", "查看报修信息"))
        self.repair_submit_menu.setText(_translate("MainWindow", "添加报修"))
        self.normal_import_menu.setText(_translate("MainWindow", "导入学生(通用模式)"))


import img_rc