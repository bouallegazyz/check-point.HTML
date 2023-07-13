from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def vérif(ch):
    if not(int(ch)>100):
        msg="vérifie votre nombre"
    else:
        msg="non ondulant"
        i=0
        while not(ch[i]==ch[i+2],i>=len(ch)-1):
            i=i+1
            msg="le nombre est  ondulant"
    return msg
def play():
    a=windows.t2.text()
    x=vérif(a)
    windows.t3.setText(x)


app=QApplication([])
windows=loadUi("azizB.ui")
windows.show()
windows.p.clicked.connect(play)
app.exec_()