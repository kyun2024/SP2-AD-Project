import sys
from PyQt5.Qt import QWidget, QPixmap, QPainter, QLabel, QVBoxLayout, QApplication, QPushButton

class Scene(QWidget):
    def __init__(self,uri):
        super().__init__()
        #define pixmap
        img = QPixmap(uri)
        label = QLabel()
        label.setPixmap(img)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    q = QApplication(sys.argv)
    #Need Environment Variable
    scene = Scene("./assets/images/grad_img.jpeg")
    sys.exit(q.exec_())