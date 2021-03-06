import sys

import pyperclip
from PyQt5.QtCore import QObject, Qt, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

import controller
from PasswordWindow import PasswordWindow
from qt_utils import ThreadProxy, msg
from ui.about import Ui_About
from ui.index import Ui_MainWindow
from ui.login import Ui_Login


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.main_window = None
        self.bind()

    def check_login(self):
        user_name = self.ui.user_name.text()
        password = self.ui.password.text()
        if password:
            self.hide()
            if self.main_window is None:
                self.main_window = MainWindow()
                self.main_window.parent_window = self
            self.main_window.show()
        else:
            QMessageBox.information(self,
                                    "错误",
                                    "用户名或密码错误",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        return

    def guest_login(self):
        self.close()
        if self.main_window is None:
            self.main_window = MainWindow()
            self.main_window.parent_window = self
        self.main_window.show()

    def bind(self):
        self.ui.login_button.clicked.connect(self.check_login)
        self.ui.guest_button.clicked.connect(self.guest_login)


class AboutWindow(QDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MwSignals(QObject):
    open_PasswordWindow = pyqtSignal(bool)
    generate = pyqtSignal(str)
    usernames = pyqtSignal(list)
    insert_res = pyqtSignal(bool)


class MainWindow(QMainWindow):
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()
        self.c = MwSignals()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent_window = None
        self.about_window = None
        self.password_window = None
        self.bind()
        self.setAttribute(Qt.WA_QuitOnClose, True)

        self.top = False
        self.flags = self.windowFlags()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.thread = ThreadProxy(func=controller.get_default_username, signal=self.c.usernames)
        self.thread.start()

    @pyqtSlot()
    def on_insert_clicked(self):
        combo = self.ui.username_combo.currentText()
        if combo == 'other':
            combo = self.ui.g_username.text()
        self.thread = ThreadProxy(func=lambda: controller.add(
            self.ui.g_name.text(),
            self.ui.g_url.text(),
            combo,
            self.ui.p_ged.text()
        ), signal=self.c.insert_res)
        self.thread.start()

    def default_username(self, usernames):
        self.ui.username_combo.addItems(usernames)
        self.ui.username_combo.addItem('other')

    def openPasswordWindow(self, search=False):
        if self.password_window:
            if search:
                self.password_window.c.receive_keyword.emit(self.ui.keyword.text())
        else:
            self.password_window = PasswordWindow()
            print(self.ui.keyword.text())
            if search:
                self.password_window.c.receive_keyword.emit(self.ui.keyword.text())
            self.password_window.ui.search_button.clicked.emit(True)
        self.password_window.show()

    def bind(self):
        self.ui.open_pw.clicked.connect(self.openPasswordWindow)
        self.c.generate.connect(self.ui.p_ged.setText)
        self.ui.copy_pass.clicked.connect(lambda: pyperclip.copy(self.ui.p_ged.text()))

        def func(widget):
            combo = widget.ui.username_combo.currentText()
            if combo == 'other':
                combo = self.ui.g_username.text()
            return combo

        self.ui.copy_user.clicked.connect(lambda: pyperclip.copy(func(self)))
        self.ui.copy_name.clicked.connect(lambda: self.ui.g_name.setText(pyperclip.paste()))
        self.c.usernames.connect(self.default_username)
        self.c.insert_res.connect(lambda x: msg(self, x))
        self.ui.search_button.clicked.connect(lambda: self.openPasswordWindow(search=True))
        self.ui.keyword.returnPressed.connect(self.ui.search_button.clicked.emit)

    @pyqtSlot()
    def on_entop_clicked(self):
        if self.top:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.ui.entop.setText("Not\nTop")
            self.top = False
        else:
            self.setWindowFlags(self.flags)
            self.ui.entop.setText("Stay\nTop")
            self.top = True
        self.show()

    @pyqtSlot()
    def on_generate_clicked(self):
        self.thread = ThreadProxy(func=lambda: controller.gen(10), signal=self.c.generate)
        self.thread.start()

    @pyqtSlot()
    def on_about_menu_triggered(self):
        if self.about_window is not None:
            self.about_window.show()
            return
        self.about_window = AboutWindow()
        self.about_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = MainWindow()
    login_window.show()
    sys.exit(app.exec_())
