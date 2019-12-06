import sys
from PyQt5.QtWidgets import (
    QStackedWidget, QGridLayout, QWidget, QLabel,
    QPushButton, QApplication, QVBoxLayout,
    QLCDNumber,
)
from PyQt5.QtCore import QTimer

class Game(QWidget):
    def __init__(self):
        super()
        self.initUI()

    def initUI(self):
        pass

class InitScene(QWidget):
    def __init__(self,st):
        super().__init__()
        self.initUI()
        self.stw = st

    def changeScene(self):
        #self.stw = QStackedWidget()
        self.stw.setCurrentIndex(1)
        self.stw.currentWidget().initGame()

    def initUI(self):
        self.setGeometry(0,0,360,640)

        label = QLabel('BASKETBALL GAME')
        label.setStyleSheet('font-size: 42px')

        btn = QPushButton('PLAY')
        btn.setStyleSheet('font-size:36px')



        btn.pressed.connect(self.changeScene)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()
        layout.addStretch()
        layout.addWidget(btn)
        layout.addStretch()

        self.setLayout(layout)
        #self.show()

class PlayScene(QWidget):
    def __init__(self,st):
        super().__init__()
        self.stw = st
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.remainTime = 60
        self.timer.timeout.connect(self.changeTime)

        self.initUI()

    def changeTime(self):
        self.remainTime -= 1
        self.lcd.display(self.remainTime)

    def initUI(self):
        self.lcd = QLCDNumber()
        self.lcd.display(self.remainTime)
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        self.setLayout(layout)
        #self.show()
        pass

    def initGame(self):
        self.game_start = False
        self.remainTime = 60
        self.timer.stop()
        self.timer.start()

if __name__ == "__main__":
    q = QApplication(sys.argv)
    st = QStackedWidget()
    st.setGeometry(0,0,360,640)
    st.addWidget(InitScene(st))
    st.addWidget(PlayScene(st))
    st.show()
    sys.exit(q.exec_())