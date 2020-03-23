from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox, QPushButton


def msg(parent, flag, op=None, m=None, diy=None):
    if not op:
        op = 'opreation'
    if diy:
        res = diy
    else:
        res = str.title(op) + ' succeed' if flag else ' faild'
    if not m:
        m = res
    QMessageBox.information(parent,
                            res, m,
                            QMessageBox.Yes)


if __name__ == '__main__':
    msg(True, 'delete')


def comfirm(op, count=None):
    def check(func):
        def ff(*args, **kwargs):
            reply = QMessageBox.information(args[0],
                                            "请确认",
                                            "是否进行%s操作" % op,
                                            QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if count:
                    args = args[:count]
                func(*args, **kwargs)

        return ff

    return check


class ThreadProxy(QThread):
    def __init__(self, func=None, args=None, signal=None):
        super().__init__()
        self.func = func
        self.args = args
        self.signal = signal

    def run(self):
        if self.func is not None:
            if self.args is not None:
                res = self.func(self.args)
            else:
                res = self.func()
            print(res)
            if self.signal is not None:
                self.signal.emit(res)


class MyBtn(QPushButton):
    def __init__(self, name, data1, s=None):
        super().__init__(name)
        self.data1 = data1
        self.data2 = s
