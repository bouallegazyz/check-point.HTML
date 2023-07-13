from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def lettre(x):
    t=False
    for i in range(len(ch)):
        if "a"<=x[i]<="z" or "a"<=x[i]<="z":
            t=True
    return t
def vérif(ch,ch1):
    if not(lettre(ch)==True):
        msg="mots 1 doit conventir que des lettres"
    if not(lettre(ch1)==True):
        msg="mots 2 doit conventir que des lettres"
    else :
        msg=ch1,"non cyclique ",ch
        if not len(ch)==len(ch1):
           msg=ch1,"non cyclique ",ch
        else:
            test=True
            for i in range(len(ch)):
                nb=0
                for j in range(len(ch)):
                    if ch[i]==ch1[J]:
                        nb=nb+1
                if nb==1:
                    test==True
                else :
                    test==False
            if test==True :
                msg=ch1,"cyclique",ch
    return msg
                
            

def play():
    a=windows.t1.text()
    b=windows.t2.text()
    windows.label_4.setText(vérif(a,b))
    

app=QApplication([])
windows=loadUi("aziz.ui")
windows.show()
windows.p.clicked.connect(play)
app.exec_()