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
        GrilHappyQMW.resize(1120, 689)
        GrilHappyQMW.setMinimumSize(QtCore.QSize(0, 0))
        GrilHappyQMW.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/girl/img/birthday_girl_128px_1292266_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GrilHappyQMW.setWindowIcon(icon)
        GrilHappyQMW.setIconSize(QtCore.QSize(64, 64))
        GrilHappyQMW.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        GrilHappyQMW.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(GrilHappyQMW)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(159, 159, 159, 255))\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setContentsMargins(80, 20, 80, 20)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border:1px solid #ffffff;\n"
"    border-radius:4px;\n"
"    padding:10px 30px;\n"
"    background-color:rgba(202, 202, 202, 50);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border:1px solid #ffffff;\n"
"    border-radius:4px;\n"
"    padding:10px 30px;\n"
"    background-color:rgba(202, 202, 202, 50);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border:1px solid #ffffff;\n"
"    border-radius:4px;\n"
"    padding:10px 30px;\n"
"    background-color:rgba(202, 202, 202, 50);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border:1px solid #ffffff;\n"
"    border-radius:4px;\n"
"    padding:10px 30px;\n"
"    background-color:rgba(202, 202, 202, 50);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 52pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"黑体\";\n"
"\n"
"\n"
"")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border:1px solid #ffffff;\n"
"    border-radius:2px;\n"
"    padding:10px 36px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 4)
        self.verticalLayout_5.setStretch(2, 4)
        self.verticalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.videoLayout = QtWidgets.QVBoxLayout()
        self.videoLayout.setObjectName("videoLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.videoLayout.addItem(spacerItem4)
        self.horizontalLayout_5.addLayout(self.videoLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(40, 20, 40, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 12pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;")
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(170, 0))
        self.label_7.setStyleSheet("font: 25 8pt \"Microsoft YaHei UI\";\n"
"color: rgb(220, 220, 220);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(40, 20, 40, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 12pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(170, 0))
        self.label.setStyleSheet("font: 25 8pt \"Microsoft YaHei UI\";\n"
"color: rgb(220, 220, 220);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(40, 20, 40, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 12pt \"黑体\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(170, 0))
        self.label_5.setStyleSheet("font: 25 8pt \"Microsoft YaHei UI\";\n"
"color: rgb(220, 220, 220);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addWidget(self.widget)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        GrilHappyQMW.setCentralWidget(self.centralwidget)

        self.retranslateUi(GrilHappyQMW)
        QtCore.QMetaObject.connectSlotsByName(GrilHappyQMW)

    def retranslateUi(self, GrilHappyQMW):
        _translate = QtCore.QCoreApplication.translate
        GrilHappyQMW.setWindowTitle(_translate("GrilHappyQMW", "MainWindow"))
        self.label_6.setText(_translate("GrilHappyQMW", "EIE.201"))
        self.pushButton.setText(_translate("GrilHappyQMW", "文档"))
        self.pushButton_2.setText(_translate("GrilHappyQMW", "母鸡"))
        self.pushButton_3.setText(_translate("GrilHappyQMW", "啊这"))
        self.pushButton_5.setText(_translate("GrilHappyQMW", "关于"))
        self.label_2.setText(_translate("GrilHappyQMW", "在这里,在现在.."))
        self.label_3.setText(_translate("GrilHappyQMW", "女生节快乐!"))
        self.label_4.setText(_translate("GrilHappyQMW", "也许机器的语言不够浪漫， 但请相信我们默默守候的心.\n"
"千言浓情满天星,\n"
"万行代码与君依。"))
        self.pushButton_4.setText(_translate("GrilHappyQMW", "Let\'s GO"))
        self.pushButton_8.setText(_translate("GrilHappyQMW", "颜色调节"))
        self.label_7.setText(_translate("GrilHappyQMW", "TextLabel"))
        self.pushButton_6.setText(_translate("GrilHappyQMW", "温度调节"))
        self.label.setText(_translate("GrilHappyQMW", "TextLabel"))
        self.pushButton_7.setText(_translate("GrilHappyQMW", "生成hex"))
        self.label_5.setText(_translate("GrilHappyQMW", "TextLabel"))

import gril_rc
