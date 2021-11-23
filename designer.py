# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerGraphicsbCFyqS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import os


class Ui_Validator(object):
    def setupUi(self, Validator):
        if not Validator.objectName():
            Validator.setObjectName(u"Validator")
        Validator.resize(458, 258)
        self.centralwidget = QWidget(Validator)
        self.centralwidget.setObjectName(u"centralwidget")
        centralwidget.setWindowIcon(QtGui.QIcon("Validator_logo.png"))
        self.sections_label = QLabel(self.centralwidget)
        self.sections_label.setObjectName(u"sections_label")
        self.sections_label.setGeometry(QRect(20, 40, 101, 41))
        font = QFont()
        font.setFamily(u"Amazon Ember")
        font.setPointSize(11)
        self.sections_label.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 100, 111, 41))
        self.label.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(140, 40, 291, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.textEdit.setFont(font1)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(140, 100, 291, 31))
        self.textEdit_2.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 160, 91, 41))
        font2 = QFont()
        font2.setFamily(u"Bookerly")
        font2.setPointSize(11)
        self.pushButton.setFont(font2)
        Validator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Validator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 22))
        Validator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Validator)
        self.statusbar.setObjectName(u"statusbar")
        Validator.setStatusBar(self.statusbar)

        self.retranslateUi(Validator)

        QMetaObject.connectSlotsByName(Validator)
    # setupUi

    def retranslateUi(self, Validator):
        Validator.setWindowTitle(QCoreApplication.translate("Validator", u"Validator", None))
        self.sections_label.setText(QCoreApplication.translate("Validator", u"Sections Json", None))
        self.label.setText(QCoreApplication.translate("Validator", u"Questions Json", None))
        self.pushButton.setText(QCoreApplication.translate("Validator", u"Validate", None))
        Validator.setWindowIcon(QtGui.QIcon('Validator_logo.png'))
        Validator.setFixedSize(458, 258)
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    centralwidget = QtWidgets.QMainWindow()
    ui = Ui_Validator()
    ui.setupUi(centralwidget)
    centralwidget.show()
    sys.exit(app.exec_())
