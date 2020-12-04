import os
import random
import sys
import time

from PyQt5 import sip
from PyQt5.QtGui import QMovie, QRegion, QPixmap, QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QDialog, QHBoxLayout, QLabel, \
    QPushButton, QLayout, QSizePolicy
from PyQt5.QtCore import Qt, QRect, QSize, QTimer, QPropertyAnimation, QPoint, QUrl
from PyQt5.uic.properties import QtGui

from grilHappy import Ui_GrilHappyQMW

class MainWindow(QMainWindow, Ui_GrilHappyQMW):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle('Grils HappyToo!!!')
        self.setVisible(0)
        self.preloadDialog = QDialog()
        self.screen = QDesktopWidget().screenGeometry()

        """
        gif开场动画
        """
        self.movie=QMovie(":/girl/img/showheart.gif")

        self.movie.updated.connect(self.gifFinished)
        self.movie.destroyed.connect(self.showMainWindow)
        self.movie.setSpeed(1111)
        """
        开场dialog
        """


        self.preloadDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.preloadDialog.setMask(QRegion(12,12,190,190))
        self.preloadDialog.move(( self.screen.width()-200) / 2, ( self.screen.height()-200) / 2)
        gifLayout=QHBoxLayout()
        gifLabel=QLabel()

        gifLabel.setMovie(self.movie)
        gifLayout.addWidget(gifLabel)

        self.preloadDialog.setLayout(gifLayout)


        self.preloadDialog.setVisible(1)
        self.movie.start()
    def showMainWindow(self):
        self.move((self.screen.width() - self.width()) / 2, (self.screen.height() - self.height()) / 2)
        self.meidaPlayer=QMediaPlayer()

        self.playlist=QMediaPlaylist()
        self.playlist.setCurrentIndex(1);
        self.playlist.addMedia(QMediaContent(QUrl().fromLocalFile("video/Radio-Digital-Scheme-Live-Wallpaper~1.mp4")))
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.meidaPlayer.setPlaylist(self.playlist)

        videoWidget = QVideoWidget()

        videoWidget.setAspectRatioMode(Qt.IgnoreAspectRatio)
        videoWidget.setAutoFillBackground(True)
        videoWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        # videoWidget.setMinimumSize(videoWidget.size())

        self.meidaPlayer.setVideoOutput(videoWidget)

        self.verticalLayout_2.insertWidget(0,videoWidget)
        self.meidaPlayer.play()
        self.setVisible(1)


    def codeRain(self):

        label=QLabel(parent=self)
        s=''.join([word+'\n' for word in list("我们的每一天，都无法重来，将管理学书籍读遍依旧管不了因你悸动的心。")])
        label.setText(s)
        label.raise_()
        label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        label.setMaximumWidth(12)
        label.setMaximumHeight(len(s)*10)
        label.setMinimumHeight(len(s)*10)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignTop)
        label.setStyleSheet("""
        font: 87 10pt "Arial";
        color: rgb(0, 49, 79);
        """)
        label.setAttribute(Qt.WA_TranslucentBackground)
        label.show()
        ani=QPropertyAnimation(label, b'pos', self)

        ani.setDuration(10000)
        xr=random.randint(0,self.label.width())
        yr=random.randint(0,self.height())
        ani.setStartValue(QPoint(xr,-self.width()))
        ani.setEndValue(QPoint(xr,self.height()))
        ani.finished.connect(label.deleteLater)
        ani.start()




    def gifFinished(self):
        if(self.movie.currentFrameNumber()==self.movie.frameCount()-1):
            self.preloadDialog.close()
            self.movie.stop()
            self.showPreload()

    def showPreload(self):
        self.preloadDialog = QDialog()
        self.preloadImage=QPixmap(':/girl/img/preload.png')
        size = self.preloadImage.size()
        self.move(( self.screen.width() - size.width()) / 2, ( self.screen.height() - size.height()) / 2)
        self.preloadDialog.setMinimumSize(size)

        layout=QHBoxLayout()
        label=QLabel()
        label.setPixmap(self.preloadImage)

        layout.addWidget(label)

        self.preloadDialog.setLayout(layout)
        self.preloadDialog.setMask(QRegion(QRect(self.preloadImage.rect().x()+15,self.preloadImage.rect().y()+15,self.preloadImage.rect().width()-20,self.preloadImage.rect().height()-35)))

        self.timer = QTimer()
        self.preloadDialog.show()
        self.timer.timeout.connect(self.faded)
        self.timer.start(3000)
        self.timer.setInterval(10)
        self.opacity = 100

    def faded(self):
        self.preloadDialog.setWindowOpacity(self.opacity / 100)
        if self.opacity <= 0:

            self.preloadDialog.close()
            """
            开启代码雨
            """
            self.showMainWindow()
            self.codeTimer=QTimer()
            self.codeTimer.timeout.connect(self.codeRain)
            self.codeTimer.start(1000)
            self.codeTimer.setInterval(5000)
            self.timer.stop()
        else:
            self.opacity -= 13


    def closeEvent(self, a0) -> None:
        self.codeTimer.stop()
        for i in range(100,0,-1):
            self.setWindowOpacity(i/100)
            time.sleep(0.002)

if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setWindowFlag(Qt.SplashScreen)
    # win.setWindowFlag(Qt.WindowStaysOnTopHint)
    # win.setVisible(1)
    # win.setWindowOpacity(0)

    sys.exit(app.exec_())
