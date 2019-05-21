# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 127)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 10, 51, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(70, 40, 291, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 61, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 291, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(220, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(290, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 10, 111, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Esp MicroPython Flasher"))
        self.pushButton.setText(_translate("Form", "Flash"))
        self.label.setText(_translate("Form", "Com Port"))
        self.label_3.setText(_translate("Form", "Firmware"))
        self.checkBox.setText(_translate("Form", "Erase"))
        self.checkBox_3.setText(_translate("Form", "Advanced"))
        self.label_2.setText(_translate("Form", "Board"))
