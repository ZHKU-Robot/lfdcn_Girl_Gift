# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grilHappy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GrilHappyQMW(object):
    def setupUi(self, GrilHappyQMW):
        GrilHappyQMW.setObjectName("GrilHappyQMW")
        GrilHappyQMW.resize(198, 198)
        GrilHappyQMW.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/q/birthday_girl_128px_1292266_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GrilHappyQMW.setWindowIcon(icon)
        GrilHappyQMW.setIconSize(QtCore.QSize(64, 64))
        GrilHappyQMW.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        GrilHappyQMW.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(GrilHappyQMW)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        GrilHappyQMW.setCentralWidget(self.centralwidget)

        self.retranslateUi(GrilHappyQMW)
        QtCore.QMetaObject.connectSlotsByName(GrilHappyQMW)

    def retranslateUi(self, GrilHappyQMW):
        _translate = QtCore.QCoreApplication.translate
        GrilHappyQMW.setWindowTitle(_translate("GrilHappyQMW", "MainWindow"))

import gril_rc
