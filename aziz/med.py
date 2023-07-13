from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication







def play():
    n=windows.m.text()
    a=verif(n)
    windows.r.setText(a)











app=QApplication([])
windows=loadUi("med1.ui")
windows.show()
windows.r.clicked.connect(play)
app.exec_()