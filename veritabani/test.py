from PyQt5 import QtWidgets,uic
import sys


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("veritabani/ogrenci.ui")
        self.show()

app = QtWidgets.QApplication(sys.argv)
window=UI() 
app.exec_()   