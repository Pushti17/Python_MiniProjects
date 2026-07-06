import tkinter
from tkinter import *
from tkinter import messagebox
import math
a=0
b=0
l=[]
def A():
    txt_1.insert(INSERT,1)
    l.append(1)
def b():
    txt_1.insert(INSERT,2)
    l.append(2)
def c():
    txt_1.insert(INSERT,3)
    l.append(3)
def d():
    txt_1.insert(INSERT,4)
    l.append(4)
def e():
    txt_1.insert(INSERT,5)
    l.append(5)
def f():
    txt_1.insert(INSERT,6)
    l.append(6)
def g():
    txt_1.insert(INSERT,7)
    l.append(7)
def h():
    txt_1.insert(INSERT,8)
    l.append(8)
def i():
    txt_1.insert(INSERT,9)
    l.append(9)
def j():
    txt_1.insert(INSERT,0)
    l.append(0)
def point():
    txt_1.insert(INSERT,".")
    l.append(".")
def pm():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        z=int("".join(s))
        a=z*-1
        txt_1.delete(1.0,2.0)
        l.clear()
        txt_1.insert(INSERT,a)
def plus():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
    global m
    m="add"
def mins():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
    global m
    m="minus"
def mult():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
    global m
    m="multiply"
def div():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
    global m
    m="divide"
def prn():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
    global m
    m="prn"
def ce():
    txt_1.delete(1.0,2.0)
def Del():
    txt_1.delete(1.0,2.0)
def sq():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
        txt_1.insert(INSERT,a*a)
def cub():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
        txt_1.insert(INSERT,a**3)
def sqt():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
        SQ=math.sqrt(a)
        txt_1.insert(INSERT,SQ)
def Mode():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
        M=a*-1
        txt_1.insert(INSERT,M)
    else:
        s=[str(i)for i in l]
        global q
        q=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
        txt_1.insert(INSERT,q)
def op():
    global a
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s=[str(i)for i in l]
        a=int("".join(s))
        txt_1.delete(1.0,2.0)
        l.clear()
        O=1/a
        O=float(O)
        txt_1.insert(INSERT,O)
def eq():
    global b
    c=len(l)
    if c==0:
        txt_1.delete(1.0,2.0)
    else:
        s2=[str(i)for i in l]
        b=int("".join(s2))
        txt_1.delete(1.0,2.0)
        l.clear()
        if m=="add":
            A=a+b
            txt_1.insert(INSERT,A)
        elif m=="minus":
            txt_1.insert(INSERT,a-b)
        elif m=="multiply":
            txt_1.insert(INSERT,a*b)
        elif m=="prn":
            txt_1.insert(INSERT,a%b) 
        elif m=="divide":
            B=a/b
            B=float(B)
            txt_1.insert(INSERT,B)
top=tkinter.Tk()
top.geometry("250x350")
top.resizable(False,False)#or 0,0
top.title("Calculator")
txt_1=Text(top,height=3,width=21,font=("arial",16))
txt_1.pack()
txt_1.place(x=0,y=0)

btn_cube=Button(top,text="x3",width="4",font=("arial",12,"bold"),bg="lightblue",command=cub)
btn_cube.pack()
btn_cube.place(x=0,y=100)
btn_mo=Button(top,text="| |",width="4",font=("arial",12,"bold"),bg="lightblue",command=Mode)
btn_mo.pack()
btn_mo.place(x=60,y=100)
btn_cl=Button(top,text="C",width="4",font=("arial",12,"bold"),bg="lightgreen",command=Del)
btn_cl.pack()
btn_cl.place(x=120,y=100)
btn_ac=Button(top,text="AC",width="4",font=("arial",12,"bold"),bg="lightgreen",command=ce)
btn_ac.pack()
btn_ac.place(x=180,y=100)
btn_ro=Button(top,text="√x",width="4",font=("arial",12,"bold"),bg="lightblue",command=sqt)
btn_ro.pack()
btn_ro.place(x=0,y=140)
btn_ur=Button(top,text="x²",width="4",font=("arial",12,"bold"),bg="lightblue",command=sq)
btn_ur.pack()
btn_ur.place(x=60,y=140)
btn_inv=Button(top,text="1/x",width="4",font=("arial",12,"bold"),bg="lightblue",command=op)
btn_inv.pack()
btn_inv.place(x=120,y=140)
btn_eto=Button(top,text="=",width="4",font=("arial",12,"bold"),bg="blue",command=eq)
btn_eto.pack()
btn_eto.place(x=180,y=140)

btn_1=Button(top,text="1",width="4",command=A,font=("arial",12,"bold"),bg="lightpink")
btn_1.pack()
btn_1.place(x=0,y=180)
btn_2=Button(top,text="2",width="4",command=b,font=("arial",12,"bold"),bg="lightpink")
btn_2.pack()
btn_2.place(x=60,y=180)
btn_3=Button(top,text="3",width="4",command=c,font=("arial",12,"bold"),bg="lightpink")
btn_3.pack()
btn_3.place(x=120,y=180)
btn_4=Button(top,text="4",width="4",command=d,font=("arial",12,"bold"),bg="lightpink")
btn_4.pack()
btn_4.place(x=0,y=220)
btn_5=Button(top,text="5",width="4",command=e,font=("arial",12,"bold"),bg="lightpink")
btn_5.pack()
btn_5.place(x=60,y=220)
btn_6=Button(top,text="6",width="4",command=f,font=("arial",12,"bold"),bg="lightpink")
btn_6.pack()
btn_6.place(x=120,y=220)
btn_7=Button(top,text="7",width="4",command=g,font=("arial",12,"bold"),bg="lightpink")
btn_7.pack()
btn_7.place(x=0,y=260)
btn_8=Button(top,text="8",width="4",command=h,font=("arial",12,"bold"),bg="lightpink")
btn_8.pack()
btn_8.place(x=60,y=260)
btn_9=Button(top,text="9",width="4",command=i,font=("arial",12,"bold"),bg="lightpink")
btn_9.pack()
btn_9.place(x=120,y=260)
btn_ps=Button(top,text="+/-",width="4",command=pm,font=("arial",12,"bold"),bg="lightblue")
btn_ps.pack()
btn_ps.place(x=0,y=300)
btn_0=Button(top,text="0",width="4",command=j,font=("arial",12,"bold"),bg="lightpink")
btn_0.pack()
btn_0.place(x=60,y=300)
btn_prn=Button(top,text="%",width="4",font=("arial",12,"bold"),command=prn)
btn_prn.pack()
btn_prn.place(x=120,y=300)

btn_pl=Button(top,text="+",width="4",command=plus,font=("arial",12,"bold"))
btn_pl.pack()
btn_pl.place(x=180,y=180)
btn_m=Button(top,text="-",width="4",command=mins,font=("arial",12,"bold"))
btn_m.pack()
btn_m.place(x=180,y=220)
btn_ml=Button(top,text="x",width="4",command=mult,font=("arial",12,"bold"))
btn_ml.pack()
btn_ml.place(x=180,y=260)
btn_d=Button(top,text="/",width="4",command=div,font=("arial",12,"bold"))
btn_d.pack()
btn_d.place(x=180,y=300)

top.mainloop()
