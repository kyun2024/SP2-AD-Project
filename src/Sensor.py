import sys
from PyQt5.Qt import QWidget, QApplication, QPushButton, QGridLayout


class Sensor(QWidget):
    def __init__(self,slot):
        super().__init__();
        btn = QPushButton("Send Signal")
        btn.setMinimumSize(200,100)
        btn.pressed.connect(slot)
        layout = QGridLayout()
        layout.addWidget(btn);
        layout.setSpacing(20);
        self.setLayout(layout)
        self.show()
        pass

if __name__ == '__main__':
    q = QApplication(sys.argv)
    s = Sensor(lambda :print("Pressed"));
    sys.exit(q.exec_())
