from tkinter import *
pro = Tk()
pro.geometry('400x400')
pro.title('somme')
pro.config(background='red')
def function():
    user=e1.get()
    t=0
    for i in range(len(user)):
        if "0"<user[i]<"9":
            t=t+1
    if t==len(user):
        messagebox.showinfo("passable")
    else :
        messagebox.showerror("verifie votre nombe")
            
lab1=Label(text='somme',fg='black',bg='white')
lab1.place(x=10,y=10)
b1=Button(text='validé',fg='black',bg='white', command=function)
b1.place(x=10,y=70)
e1=Entry()
e1.place(x=10,y=48)
pro.mainloop()