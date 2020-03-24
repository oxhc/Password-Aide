from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QTableWidgetItem

import controller
from qt_utils import msg, comfirm, ThreadProxy, MyBtn
from ui.ui_student import Ui_Students


class PasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Students()
        self.ui.setupUi(self)
        self.c = PwSignals()
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.thread = None
        self.bind()
        self.ui.info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.info_table.verticalHeader().setVisible(False)
        self.ui.info_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.ui.info_table.setColumnWidth(4, 70)
        self.ui.info_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.info_table.setColumnWidth(5, 70)
        self.page = 1
        self.btns = []
        self.maxPage = None

    def msg_fresh(self, flag, op=None):
        msg(self, flag, op=op)
        self.search()

    def bind(self):
        self.c.passwords.connect(self.fresh_table)
        self.ui.search_button.clicked.connect(self.search)

        self.c.flag_signal.connect(lambda x: self.msg_fresh(x, 'add'))
        self.c.del_signal.connect(lambda x: self.msg_fresh(x, 'delete'))

        self.ui.add_button.clicked.connect(self.add)
        self.ui.next_page.clicked.connect(self.nextPage)
        self.ui.before_page.clicked.connect(self.beforePage)
        self.ui.index_page.clicked.connect(self.firstPage)
        self.ui.clear_button.clicked.connect(self.clear)
        self.c.receive_keyword.connect(lambda x: self.ui.search_input.setText(x))
        self.ui.search_input.returnPressed.connect(self.ui.search_button.clicked.emit)

    def changePage(self, p_text):
        self.page = int(p_text)

    @comfirm('清空表', count=1)
    def clear(self):
        self.thread = ThreadProxy(func=lambda: controller.clear())
        self.thread.start()
        QMessageBox.information(self, '成功', '清除成功', QMessageBox.Yes)
        self.fresh()

    def nextPage(self):
        if self.maxPage is not None and self.page == self.maxPage:
            return
        self.page = self.page + 1
        self.ui.page_input.setText(str(self.page))
        self.fresh()

    def firstPage(self):
        self.page = 1
        self.ui.page_input.setText(str(self.page))
        self.fresh()

    def beforePage(self):
        if self.page == 1:
            return
        self.page = self.page - 1
        self.ui.page_input.setText(str(self.page))
        self.fresh()

    @comfirm('删除')
    def del_stu(self, id):
        self.thread = ThreadProxy(func=lambda: controller.del_(id), signal=self.c.del_signal)
        self.thread.start()

    def add(self):
        name = self.ui.stu.text()
        url = self.ui.name.text()
        username = self.ui.build.text()
        password = self.ui.password.text()
        self.thread = ThreadProxy(func=lambda: controller.add(name, url, username, password), signal=self.c.flag_signal)
        self.thread.start()

    def search(self):
        self.page = 1
        self.ui.page_input.setText(str(self.page))
        self.fresh()

    def fresh(self):
        keyword = self.ui.search_input.text()
        try:
            page = int(self.page)
        except Exception:
            page = 1
        keyword = None if keyword == '' else keyword
        self.thread = ThreadProxy(func=lambda: controller.get(keyword, page=page), signal=self.c.passwords)
        self.thread.start()

    @comfirm('修改')
    def update_table(self, row, sno):
        print(row)
        name = self.ui.info_table.item(row, 1).text()
        build = self.ui.info_table.item(row, 2).text()
        room = self.ui.info_table.item(row, 3).text()
        bed = self.ui.info_table.item(row, 4).text()
        password = self.ui.info_table.item(row, 5).text()

        self.thread = ThreadProxy(func=lambda x: x, signal=self.c.op_signal)
        self.thread.start()

    def fresh_table(self, passwords):
        print(passwords)
        self.ui.info_table.setRowCount(len(passwords))
        print(len(passwords))
        if len(passwords) < 50:
            self.maxPage = self.page
        else:
            self.maxPage = None
        for key, passwd in enumerate(passwords):
            print(passwd.name)
            self.ui.info_table.setItem(key, 0, QTableWidgetItem(passwd.name))
            self.ui.info_table.setItem(key, 1, QTableWidgetItem(passwd.url))
            self.ui.info_table.setItem(key, 2, QTableWidgetItem(passwd.username))
            self.ui.info_table.setItem(key, 3, QTableWidgetItem(passwd.password))
            searchBtn = MyBtn("EDIT", key, passwd.id)
            searchBtn.setStyleSheet("border:none;background-color:#00b894;padding:5px;color:white;")
            searchBtn.clicked.connect(lambda: self.update_table(self.sender().data1, self.sender().data2))
            self.ui.info_table.setCellWidget(key, 4, searchBtn)
            deleteBtn = MyBtn("DEL", passwd.id)
            deleteBtn.setStyleSheet("border:none;background-color:#ff7675;padding:5px;color:white;")
            deleteBtn.clicked.connect(lambda: self.del_stu(self.sender().data1))
            self.ui.info_table.setCellWidget(key, 5, deleteBtn)  #


class PwSignals(QObject):
    passwords = pyqtSignal(list)
    flag_signal = pyqtSignal(bool)
    del_signal = pyqtSignal(bool)
    op_signal = pyqtSignal(bool)
    receive_keyword = pyqtSignal(str)
