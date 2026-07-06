#Created by Pushti Maniyar
#Date 30-09-2022
import tkinter
from tkinter import *
from tkinter import messagebox
import random
top=tkinter.Tk()
l="stone","paper","scissor"
top.geometry("500x430")
top.title("My Game")
top.resizable(False,False)
u=0
n=0
def stone():
    global u
    u="stone"
    txt_1.delete(1.0,2.0)
    txt_1.insert(INSERT,"Stone")
    
def paper():
    global u
    u="paper"
    txt_1.delete(1.0,2.0)
    txt_1.insert(INSERT,"Paper")

def sis():
    global u
    u="scissor"
    txt_1.delete(1.0,2.0)
    txt_1.insert(INSERT,"Scissor")

p=0
q=0

def play():
    global p
    global q
    global u
    global n
    txt_2.delete(1.0,2.0)
    txt_3.delete(1.0,2.0)
    if u!="stone" and u!="paper" and u!="scissor":
        txt_1.delete(1.0,2.0)
        messagebox.showerror("Hello User","Please first enter your choice. to play game")
    else:
        n=random.choice(l)
        txt_2.insert(INSERT,n)
        if(n=="stone" and u=="paper"):
            txt_3.insert(INSERT,"You")
            p=p+1
            q=q+1
        elif(n=="paper" and u=="stone"):
            txt_3.insert(INSERT,"PC")
            p=p+0
            q=q+1
        elif(n=="paper" and u=="scissor"):
            txt_3.insert(INSERT,"You")
            p=p+1
            q=q+1
        elif(n=="scissor" and u=="paper"):
            txt_3.insert(INSERT,"PC")
            p=p+0
            q=q+1
        elif(n=="scissor" and u=="stone"):
            txt_3.insert(INSERT,"You")
            p=p+1
            q=q+1
        elif(n=="stone" and u=="scissor"):
            txt_3.insert(INSERT,"PC")
            p=p+0
            q=q+1
        elif(n=="stone" and u=="stone"):
            txt_3.insert(INSERT,"Game tie")
            p=p+0
            q=q+1
        elif(n=="paper" and u=="paper"):
            txt_3.insert(INSERT,"Game tie")
            p=p+0
            q=q+1
        elif(n=="scissor" and u=="scissor"):
            txt_3.insert(INSERT,"Game tie")
            p=p+0
            q=q+1
    txt_4.delete(1.0,2.0)
    txt_4.insert(INSERT,p)
    txt_5.delete(1.0,2.0)
    txt_5.insert(INSERT,q)
    u=0
        
def clr():
    txt_1.delete(1.0,2.0)
    txt_2.delete(1.0,2.0)
    txt_3.delete(1.0,2.0)

lbl_1=Label(top,text="Your choice",font=("Stencil",14))
lbl_1.pack()
lbl_1.place(x="0",y="10")
txt_1=Text(top,height="2",width="20",font=(15))
txt_1.pack()
txt_1.place(x="130",y="5")
lbl_2=Label(top,text="PC's choice",font=("Stencil",14))
lbl_2.pack()
lbl_2.place(x="0",y="75")
txt_2=Text(top,height="2",width="20",font=(15))
txt_2.pack()
txt_2.place(x="130",y="70")

lbl_5=Label(top,text="Click your choice:",font=("arial",14))
lbl_5.pack()
lbl_5.place(x="0",y="175")
btn_1=Button(top,text="Stone",font=("Lucida Sans",15),bg="chocolate",command=stone)
btn_1.pack()
btn_1.place(x="180",y="170")
btn_2=Button(top,text="Paper",font=("Lucida Sans",15),bg="silver",command=paper)
btn_2.pack()
btn_2.place(x="280",y="170")
btn_3=Button(top,text="Scissor",font=("Lucida Sans",15),bg="lightblue",command=sis)
btn_3.pack()
btn_3.place(x="380",y="170")

btn_4=Button(top,text="Play",font=("Lucida Sans",15),bg="gold",command=play)
btn_4.pack()
btn_4.place(x="210",y="240")

btn_5=Button(top,text="Clear",font=("Lucida Sans",15),bg="lightgreen",command=clr)
btn_5.pack()
btn_5.place(x="310",y="240")

lbl_3=Label(top,text="Winner:",font=("Stencil",14))
lbl_3.pack()
lbl_3.place(x="80",y="320")
txt_3=Text(top,height="2",width="10",font=(15))
txt_3.pack()
txt_3.place(x="190",y="310")

lbl_4=Label(top,text="Total score:",font=("Stencil",12))
lbl_4.pack()
lbl_4.place(x="285",y="390")
txt_4=Text(top,height="1",width="4",font=(15))
txt_4.pack()
txt_4.place(x="410",y="385")
lbl_5=Label(top,text="Total attempt:",font=("Stencil",12))
lbl_5.pack()
lbl_5.place(x="0",y="390")
txt_5=Text(top,height="1",width="4",font=(15))
txt_5.pack()
txt_5.place(x="150",y="385")

top.mainloop()
