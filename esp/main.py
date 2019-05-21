#!/usr/bin/env python
# coding: utf-8
'''
@File   :erase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import esp.control
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from esp.mainWindow import Ui_Form
from PyQt5.QtCore import QTimer
import threading
mutex = threading.Lock()

class MyWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main)
        self.checkBox_3.stateChanged.connect(self.disable_op)

        # self.comboBox.highlighted.connect(self.get_com)
        # self.comboBox.activated.connect(self.get_com)

        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        # self.setWindowIcon(QIcon('./image/icon.ico'))
        self.statusBar().showMessage("Put the firmware in the same directory can be burning")

        self.list_serial = []

        self.get_com()
        self.get_bin()
        self.get_borad()
        self.get_config()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_com)
        self.timer.start(3000)

    def get_config(self):
        import esp.config
        config = esp.config.get_confg_dict()

        if 'erase' in config:
            self.checkBox.setCheckState(config['erase'] == 'True')

        if 'advanced' in config:
            self.checkBox_3.setCheckState(config['advanced'] == 'True')

        if 'auto' in config and config['auto'] == 'True':
            self.main()

    def disable_op(self):
        if self.checkBox_3.isChecked():
            self.comboBox_2.setDisabled(True)
            self.comboBox_3.setDisabled(True)
            self.checkBox.setDisabled(True)
        else:
            self.comboBox_2.setDisabled(False)
            self.comboBox_3.setDisabled(False)
            self.checkBox.setDisabled(False)

    def get_com(self):
        tmp = esp.control.list_serial()
        # print(tmp)
        if len(tmp) != len(self.list_serial):
            self.list_serial = tmp
            self.comboBox.clear()
            self.comboBox.addItems(tmp)
            # print(self.comboBox.count())

    def check_com(self):
        result = len(self.com) > 1  # and open(com) test
        if result is False:
            self.statusBar().showMessage('The selected serial port is not exist')
        return result

    def get_bin(self):
        self.comboBox_2.addItems(esp.control.list_bin())

    def get_borad(self):
        self.comboBox_3.addItems(esp.control.list_board())

    def erase(self):
        self.statusBar().showMessage('Start to erase firmware...')
        self.statusBar().showMessage(esp.control.flash_erase(self.com))
        time.sleep(1)
        self.flash()

    def flash(self):
        self.statusBar().showMessage('Start to flash firmware...')
        try:
            self.statusBar().showMessage(esp.control.flash_bin(self.board, self.com, self.firmware))
        finally:
            self.pushButton.setDisabled(False)
            self.statusBar().showMessage('Ready To GO')

    def flash_adv(self):
        self.statusBar().showMessage('Start to advanced flash...')
        try:
            import esp.advanced
            self.statusBar().showMessage(esp.advanced.flash_bin(self.com))
        finally:
            self.pushButton.setDisabled(False)
            self.statusBar().showMessage('Ready To GO')

    def main(self):
        self.com = self.comboBox.currentText().split(" - ", 1)[0]
        self.firmware = self.comboBox_2.currentText()
        if self.check_com():
            self.board = self.comboBox_3.currentText()
            print(self.com,self.firmware,self.board)
            self.pushButton.setDisabled(True)
            with mutex:
                task = self.flash_adv if self.checkBox_3.isChecked() else self.erase if self.checkBox.isChecked() else self.flash
                threading.Thread(target=task).start()

def run():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()