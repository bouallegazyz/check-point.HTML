def saisir():
    n=int(input("donner un entier n telque 3=<n<=20"))
    while not 3<n<20 :
        n=int(input("donner un entier n telque 3=<n<=20"))
#remplissage de tableau
def remplir(t,n):
    for i in range (n):
        t[i]=input("donner un nom")
        while not(len(t[i])==10 and verif(t[i])==True):
            t[i]=input("donner un nom")
#fonction vérif
def verif(ch):
    test=True
    s=0
    for i in range(len(ch)):
        if "A"<ch[i]<"Z":
            s=s+1
    if s==len(ch):
        test=True
    else :
        test=False
    return test
#saisir p
def saisir2():
    p=int(input("donner un entier"))
    while not(p<10):
        p=int(input("donner un entier"))
def former(t,p,n):
    ch=''
    for i in range(n):
        ch=ch+t[i][p]
    return ch

#programme principale
from numpy import *
saisir()
saisir2()
t=array([str]*4)
remplir(t)
ch=former(t)
print(ch)

        

        
            
            
            
        