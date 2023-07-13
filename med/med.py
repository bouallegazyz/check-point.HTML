from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def vérif(N):
    if not(N>0):
        msg="verifié"
    else:
        msg="non super"
        x=str(N)
        if(N%2==0 and int(x[0])%2==0):
            msg="super"
    return msg




def play():
    n=int(windows.m.text())
    a=vérif(n)
    windows.r.setText(a)

app=QApplication([])
windows=loadUi("med1.ui")
windows.show()
windows.pushButton.clicked.connect(play)
app.exec_()