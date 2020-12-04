import random
import sys
import time
from PyQt5.QtGui import QMovie, QRegion, QPixmap, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,  QDialog, QHBoxLayout, QLabel, \
 QSizePolicy, QColorDialog
from PyQt5.QtCore import Qt, QRect,  QTimer, QPropertyAnimation, QPoint, QUrl
from qtpy import QtCore
from grilHappy import Ui_GrilHappyQMW
PRELOAD = 0
class MainWindow(QMainWindow, Ui_GrilHappyQMW):
    """
    记录鼠标
    """
    mxPos1 = 0
    myPos1 = 0
    mxPos2 = 1
    myPos2 = 1
    r1=0
    g1=0
    b1=0
    r2=159
    g2=159
    b2=159
    myWheel = 255

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle('Grils HappyToo!!!')
        self.setVisible(0)
        self.preloadDialog = QDialog()
        self.screen = QDesktopWidget().screenGeometry()
        self.setMouseTracking(1)
        self.centralwidget.setMouseTracking(1)

        """
        gif开场动画
        """
        if PRELOAD:
            self.movie = QMovie(":/girl/img/showheart.gif")

            self.movie.updated.connect(self.gifFinished)
            self.movie.destroyed.connect(self.showMainWindow)
            self.movie.setSpeed(100)
            """
            开场dialog
            """
            self.preloadDialog.setWindowFlag(Qt.FramelessWindowHint)
            self.preloadDialog.move((self.screen.width() - 200) / 2, (self.screen.height() - 200) / 2)
            self.preloadDialog.setMinimumWidth(199)
            self.preloadDialog.setMinimumHeight(198)
            gifLayout = QHBoxLayout()
            gifLayout.setContentsMargins(0, 0, 0, 0)
            gifLayout.setSpacing(0)
            gifLabel = QLabel()

            gifLabel.setMovie(self.movie)
            gifLayout.addWidget(gifLabel)

            self.preloadDialog.setLayout(gifLayout)

            self.preloadDialog.setVisible(1)
            self.movie.start()
        else:
            self.showMainWindow()

    def showMainWindow(self):
        self.move((self.screen.width() - self.width()) / 2, (self.screen.height() - self.height()) / 2)
        self.meidaPlayer = QMediaPlayer()

        self.playlist = QMediaPlaylist()
        self.playlist.setCurrentIndex(1);
        self.playlist.addMedia(QMediaContent(QUrl().fromLocalFile("video/Radio-Digital-Scheme-Live-Wallpaper~1.mp4")))
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.meidaPlayer.setPlaylist(self.playlist)

        videoWidget = QVideoWidget()

        videoWidget.setAspectRatioMode(Qt.IgnoreAspectRatio)
        videoWidget.setAutoFillBackground(True)
        videoWidget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        # videoWidget.setMinimumSize(videoWidget.size())
        self.meidaPlayer.setVideoOutput(videoWidget)
        self.videoLayout.insertWidget(0, videoWidget)
        self.meidaPlayer.play()

        # self.pushButton_4.clicked.connect(self.showColorDialog)
        self.pushButton_4.installEventFilter(self)
        # self.pushButton.setGeometry()
        self.setVisible(1)
    def eventFilter(self, a0, a1) -> bool:

        if a1.type() == QtCore.QEvent.MouseButtonPress:
            self.pushButton_4.setStyleSheet("""
            QPushButton#pushButton_4{
            border:1px solid #ffffff;
            border-radius:2px;
            padding:10px 36px;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
            color: rgb(255, 255, 255);
}
            """)
            t=QTimer()
            t.timeout.connect(lambda :self.pushButton_4.setStyleSheet("""
                                QPushButton#pushButton_4{
                                border:1px solid #ffffff;
                                border-radius:2px;
                                padding:10px 36px;
                                background-color: rgba(255, 255, 255, 0);
                                color: rgb(255, 255, 255);
                    }
                                """))
            t.start(50)
            t.setSingleShot(1)
            self.showColorDialog()
            return 1
        else:
            return 0
    def showColorDialog(self):
        #QColor QColorDialog::getColor(const QColor &initial = Qt::white, QWidget *parent = Q_NULLPTR, const QString &title = QString(), ColorDialogOptions options = ColorDialogOptions())
        self.r1,self.g1,self.b1,a=QColorDialog().getColor(QColor(0,0,0),self,"选择第一种渐变颜色",QColorDialog.ShowAlphaChannel).getRgb()
        self.r2,self.g2,self.b2,a=QColorDialog().getColor(QColor(255,255,255),self,"选择第二种渐变颜色",QColorDialog.ShowAlphaChannel).getRgb()
        self.centralwidget.setStyleSheet("""
        QWidget#centralwidget{background-color:qlineargradient(spread:pad, x1:%f, y1:%f, x2:%f, y2:%f, stop:0 rgba(%d, %d, %d, 255), stop:1 rgba(%d, %d, %d, %d));
        }""" % (self.mxPos1, self.myPos1, self.mxPos2, self.myPos2,self.r1,self.g1,self.b1, self.r2,self.g2,self.b2,self.myWheel))

    def wheelEvent(self, a0) -> None:
        angle = a0.angleDelta().y() / 8
        if self.myWheel < 255 and angle > 0:
            self.myWheel += 1
        elif self.myWheel > 0 and angle < 0:
            self.myWheel -= 1
        self.centralwidget.setStyleSheet("""
        QWidget#centralwidget{background-color:qlineargradient(spread:pad, x1:%f, y1:%f, x2:%f, y2:%f, stop:0 rgba(%d, %d, %d, 255), stop:1 rgba(%d, %d, %d, %d));
        }""" % (self.mxPos1, self.myPos1, self.mxPos2, self.myPos2,self.r1,self.g1,self.b1, self.r2,self.g2,self.b2,self.myWheel))
    def mousePressEvent(self, a0) -> None:
        """
        这里需要加上btn的..那个padding
        """
        if not self.pushButton.geometry().contains(a0.pos()):
            label = QLabel(parent=self)
            self.centralwidget.setStyleSheet("""
            QWidget#centralwidget{background-color:qlineargradient(spread:pad, x1:%f, y1:%f, x2:%f, y2:%f, stop:0 rgba(%d, %d, %d, 255), stop:1 rgba(%d, %d, %d, %d));
            }""" % (
            self.mxPos1, self.myPos1, self.mxPos2, self.myPos2, self.r1, self.g1, self.b1, self.r2, self.g2, self.b2,
            self.myWheel))
            if (a0.button() == Qt.LeftButton):
                self.mxPos1 = a0.x() / self.width()
                self.myPos1 = a0.y() / self.height()
                # s ="也许机器的语言不够浪漫， 但请相信我默默守候的心，千言浓情满天星万行代码与君依。"
            elif (a0.button() == Qt.RightButton):
                self.mxPos2 = a0.x() / self.width()
                self.myPos2 = a0.y() / self.height()

            s = "女生节快乐"
            label.setText(s)
            label.raise_()
            label.setMaximumWidth(13*6)
            label.setStyleSheet("""
            font: 87 12pt "黑体";
            color: rgb({}, {}, {});
            """.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            label.setAttribute(Qt.WA_TranslucentBackground)
            label.show()
            ani = QPropertyAnimation(label, b'pos', self)
            ani.setDuration(2000)
            x = a0.pos().x()
            y = a0.pos().y()
            ani.setStartValue(QPoint(x, y))
            ani.setEndValue(QPoint(x, y + 40))
            ani.finished.connect(label.deleteLater)
            ani.start()

    def mouseMoveEvent(self, a0) -> None:
        label = QLabel(parent=self)
        s = random.choice("女生节快乐")
        label.setText(s)
        label.raise_()
        label.setMaximumWidth(13)
        label.setStyleSheet("""
        font: 87 10pt "Arial";
        color: rgba({}, {}, {},{});
        """.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),random.randint(0,255)))
        label.setAttribute(Qt.WA_TranslucentBackground)
        label.show()
        ani = QPropertyAnimation(label, b'pos', self)
        ani.setDuration(500)
        x = a0.pos().x()
        y = a0.pos().y()
        rx = random.randint(-20, 20)
        ry = random.randint(-20, 20)
        ani.setStartValue(QPoint(x, y))
        ani.setEndValue(QPoint(x + rx, y + ry))
        ani.finished.connect(label.deleteLater)
        ani.start()

    def codeRain(self):

        label = QLabel(parent=self)
        s = ''.join([word + '\n' for word in list("我们的每一天，都无法重来，将管理学书籍读遍依旧管不了因你悸动的心。")])
        label.setText(s)
        label.raise_()
        label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        label.setMaximumWidth(12)
        label.setMaximumHeight(len(s) * 10)
        label.setMinimumHeight(len(s) * 10)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignTop)
        label.setStyleSheet("""
        font: 87 10pt "Arial";
        color: rgb(0, 49, 79);
        """)
        label.setAttribute(Qt.WA_TranslucentBackground)
        label.show()
        ani = QPropertyAnimation(label, b'pos', self)

        ani.setDuration(10000)
        xr = random.randint(0, self.label.width())
        yr = random.randint(0, self.height())
        ani.setStartValue(QPoint(xr, -self.width()))
        ani.setEndValue(QPoint(xr, self.height()))
        ani.finished.connect(label.deleteLater)
        ani.start()

    def gifFinished(self):
        if (self.movie.currentFrameNumber() == self.movie.frameCount() - 1):
            self.preloadDialog.close()
            self.movie.stop()
            self.showPreload()

    def showPreload(self):

        self.preloadDialog = QDialog()
        self.preloadImage = QPixmap(':/girl/img/preload.png')
        size = self.preloadImage.size()
        self.move((self.screen.width() - size.width()) / 2, (self.screen.height() - size.height()) / 2)
        self.preloadDialog.setMinimumSize(size)

        layout = QHBoxLayout()
        label = QLabel()
        label.setPixmap(self.preloadImage)

        layout.addWidget(label)

        self.preloadDialog.setLayout(layout)
        self.preloadDialog.setMask(QRegion(QRect(self.preloadImage.rect().x() + 15, self.preloadImage.rect().y() + 15,
                                                 self.preloadImage.rect().width() - 20,
                                                 self.preloadImage.rect().height() - 35)))

        self.timer = QTimer()
        self.preloadDialog.show()
        self.timer.timeout.connect(self.faded)
        self.timer.start(3000)
        self.timer.setInterval(50)
        self.opacity = 100

    def faded(self):
        self.preloadDialog.setWindowOpacity(self.opacity / 100)
        if self.opacity <= 0:
            self.preloadDialog.close()
            self.showMainWindow()
            self.timer.stop()
        else:
            self.opacity -= 1

    def closeEvent(self, a0) -> None:

        for i in range(100, 0, -1):
            self.setWindowOpacity(i / 100)
            time.sleep(0.002)
        self.close()


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setWindowFlag(Qt.SplashScreen)
    # win.setWindowFlag(Qt.WindowStaysOnTopHint)
    # win.setVisible(1)
    # win.setWindowOpacity(0)

    sys.exit(app.exec_())
