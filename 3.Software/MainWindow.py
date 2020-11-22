import os
import sys
import time

from PyQt5 import sip
from PyQt5.QtGui import QMovie, QRegion, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget
from PyQt5.QtCore import Qt, QRect, QSize, QTimer
from PyQt5.uic.properties import QtGui

from grilHappy import Ui_GrilHappyQMW

class MainWindow(QMainWindow, Ui_GrilHappyQMW):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Grils HappyToo!!!')
        self.movie=QMovie("showheart.gif")
        self.movie.updated.connect(self.gifFinished)
        self.movie.destroyed.connect(self.showMainWindow)
        self.label.setMovie(self.movie)
        self.region=QRegion(QRect(9,9,198,198))
        self.setMask(self.region)
        self.movie.setSpeed(88)
        self.movie.start()

        # self.setWindowFlag(Qt.FramelessWindowHint )
        # self.setWindowFlag(Qt.WindowCloseButtonHint )
    def gifFinished(self):
        if(self.movie.currentFrameNumber()==self.movie.frameCount()-1):
            self.clearMask()
            sip.delete(self.movie)

    def showMainWindow(self):
        self.preloadImage=QPixmap('preload.png')
        # self.setMask(self.preloadImage.mask())
        size = self.preloadImage.size()
        self.label.setPixmap(self.preloadImage)
        screen = QDesktopWidget().screenGeometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.setMask(QRegion(QRect(self.preloadImage.rect().x()+9,self.preloadImage.rect().y()+9,self.preloadImage.rect().width(),self.preloadImage.rect().height()-1)))
        self.timer = QTimer()
        self.timer.timeout.connect(self.faded)
        self.timer.start(3000)
        self.timer.setInterval(60)
        self.opacity = 100

    def faded(self):
        self.setWindowOpacity(self.opacity / 100)
        if self.opacity <= 0:
            self.timer.stop()
            self.setVisible(0)
        else:
            self.opacity -= 1


    def closeEvent(self, a0) -> None:
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    qss="""/*
Neon Style Sheet for QT Applications (QpushButton)
Author: Jaime A. Quiroga P.
Company: GTRONICK
Last updated: 24/10/2020, 15:42.
Available at: https://github.com/GTRONICK/QSS/blob/master/NeonButtons.qss
*/
QPushButton{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #d3dae3;
	padding: 2px;
	background-color: #100E19;
}
QPushButton::default{
	border-style: solid;
	border-color: #050a0e;
	border-width: 1px;
	border-radius: 5px;
	color: #FFFFFF;
	padding: 2px;
	background-color: #151a1e;
}
QPushButton:hover{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}
QPushButton:pressed{
	border-style: solid;
	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);
	border-width: 2px;
    border-radius: 1px;
	color: #d3dae3;
	padding: 2px;
}"""
    win = MainWindow()
    win.setStyleSheet(qss)
    # win.setWindowFlag(Qt.SplashScreen)
    # win.setWindowFlag(Qt.WindowStaysOnTopHint)
    # win.setVisible(1)
    # win.setWindowOpacity(0)
    win.show()
    sys.exit(app.exec_())
