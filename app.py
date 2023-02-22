from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from led import setPIn,setVAL
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
    
    def turnON(self):
        setPIn("23")
        setVAL("1")

    def turnOFF(self):
        setPIn("23")
        setVAL("0")
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Control LED")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("turn ON")
        self.b1.clicked.connect(self.turnON )

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("turn OFF")
        self.b2.move(100,0)
        self.b2.clicked.connect(self.turnOFF)

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
