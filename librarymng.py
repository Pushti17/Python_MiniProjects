import mysql.connector as sql
db=sql.connect(host="localhost",user="root",password="pu13413",database="pushti")




import tkinter
from tkinter import *
from tkinter import messagebox

#@@@@@@@@@@@@@@@@@@@@@@@@@@ show books @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def showbooks():
    book1=tkinter.Tk()
    book1.geometry("400x400")
    book1.title("Books")
    book1.resizable(False,False)
    lb=Label(book1,font=("stencil",25),text="Books")
    lb.pack()
    lb.place(x="150")
    listbox=Listbox(book1,height=10,width=30,bg="lightblue",font=("stencil"))
    mycursor=db.cursor()
    mycursor.execute("SELECT * from books")
    result=mycursor.fetchall()
    for i in result:
        listbox.insert(i[0],i[1])
    listbox.pack()
    listbox.place(x="40",y="70")
    book1.mainloop()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ add book  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def addbook():
    book2=tkinter.Tk()
    book2.config(bg="lightpink")
    book2.title("Add books...")
    book2.resizable(False,False)
    book2.geometry("500x500")
    albl=Label(book2,font=("stencil",25),text="Add Books")
    albl.pack()
    albl.place(x="160")
    alb2=Label(book2,font=("stencil",18),text="Bookid:")
    alb2.pack()
    alb2.place(x="20",y="100")
    alb3=Label(book2,font=("stencil",18),text="Book name:")
    alb3.pack()
    alb3.place(x="20",y="170")
    alb4=Label(book2,font=("stencil",18),text="Author:")
    alb4.pack()
    alb4.place(x="20",y="240")
    alb5=Label(book2,font=("stencil",18),text="Price:")
    alb5.pack()
    alb5.place(x="20",y="310")
    alb6=Label(book2,font=("stencil",18),text="Rent per day:")
    alb6.pack()
    alb6.place(x="20",y="380")
    global atx1
    atx1=Text(book2,font=(17),height="2",width="17")
    atx1.pack()
    atx1.place(x="200",y="100")
    global atx2
    atx2=Text(book2,font=(17),height="2",width="17")
    atx2.pack()
    atx2.place(x="200",y="170")
    global atx3
    atx3=Text(book2,font=(17),height="2",width="17")
    atx3.pack()
    atx3.place(x="200",y="240")
    global atx4
    atx4=Text(book2,font=(17),height="2",width="17")
    atx4.pack()
    atx4.place(x="200",y="310")
    global atx5
    atx5=Text(book2,font=(17),height="2",width="17")
    atx5.pack()
    atx5.place(x="200",y="380")
    abt1=Button(book2,font=("stencil",17),text="Insert data",bg="blue",fg="white",command=bookinsert)
    abt1.pack()
    abt1.place(x="190",y="450")

def bookinsert():
    global atx1
    global atx2
    global atx3
    global atx4
    global atx5
    try:
        a = int(atx1.get(1.0, "end-1c").strip())
        b = atx2.get(1.0, "end-1c").strip()
        c = atx3.get(1.0, "end-1c").strip()
        d = int(atx4.get(1.0, "end-1c").strip())
        e = int(atx5.get(1.0, "end-1c").strip())

        mycursor = db.cursor()

        sql = """
            INSERT INTO books
            (bookid, bookname, author, price, rentperday)
            VALUES (%s, %s, %s, %s, %s)
        """

        mycursor.execute(sql, (a, b, c, d, e))
        db.commit()

    except Exception as e:
        #messagebox.showerror("Hello user","Please enter valid values...")
        messagebox.showerror("Hello user",e)
    finally:
        atx1.delete(1.0,2.0)
        atx2.delete(1.0,2.0)
        atx3.delete(1.0,2.0)
        atx4.delete(1.0,2.0)
        atx5.delete(1.0,2.0)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ issue book @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def issuebook():
    st=tkinter.Tk()
    st.geometry("600x650")
    st.title("Issue book")
    st.resizable(False,False)
    st.config(bg="lightyellow")
    ilbl=Label(st,font=("stencil",25),text="Enter Student Details:",bg="brown",fg="white")
    ilbl.pack()
    ilbl.place(x="120")
    ilb2=Label(st,font=("stencil",18),text="Enr No. :")
    ilb2.pack()
    ilb2.place(x="20",y="100")
    ilb3=Label(st,font=("stencil",18),text="Name:")
    ilb3.pack()
    ilb3.place(x="20",y="170")
    ilb4=Label(st,font=("stencil",18),text="Branch:")
    ilb4.pack()
    ilb4.place(x="20",y="240")
    ilb5=Label(st,font=("stencil",18),text="Semester:")
    ilb5.pack()
    ilb5.place(x="20",y="310")
    ilb6=Label(st,font=("stencil",18),text="Book name:")
    ilb6.pack()
    ilb6.place(x="20",y="380")
    ilb7=Label(st,font=("stencil",18),text="Date of issue:")
    ilb7.pack()
    ilb7.place(x="20",y="450")
    ilb9=Label(st,font=("stencil",13),text="(yyyy-mm-dd)")
    ilb9.pack()
    ilb9.place(x="25",y="490")
    global itx1
    itx1=Text(st,font=(17),height="2",width="17")
    itx1.pack()
    itx1.place(x="200",y="100")
    global itx2
    itx2=Text(st,font=(17),height="2",width="17")
    itx2.pack()
    itx2.place(x="200",y="170")
    global itx3
    itx3=Text(st,font=(17),height="2",width="17")
    itx3.pack()
    itx3.place(x="200",y="240")
    global itx4
    itx4=Text(st,font=(17),height="2",width="17")
    itx4.pack()
    itx4.place(x="200",y="310")
    global itx5
    itx5=Text(st,font=(17),height="2",width="17")
    itx5.pack()
    itx5.place(x="200",y="380")
    global itx7
    itx7=Text(st,font=(17),height="2",width="17")
    itx7.pack()
    itx7.place(x="200",y="450")
    ibt1=Button(st,font=("stencil",17),text="Insert data",bg="brown",fg="white",command=ins)
    ibt1.pack()
    ibt1.place(x="190",y="520")

def ins():
    global itx1
    global itx2
    global itx3
    global itx4
    global itx5
    global itx7
    try:
        a=itx1.get(1.0,"end-1c")
        a=int(a)
        b=itx2.get(1.0,"end-1c")
        b=str(b)
        c=itx3.get(1.0,"end-1c")
        c=str(c)
        d=itx4.get(1.0,"end-1c")
        d=int(d)
        e=itx5.get(1.0,"end-1c")
        e=str(e)
        g=itx7.get(1.0,"end-1c")
        g=str(g)
        mycursor=db.cursor()
        val=(a,b,c,d,e,g)
        sql="""INSERT INTO stud(ano,name,branch,sem,book,issue_date) VALUES(%s,%s,%s,%s,%s,%s)"""
        mycursor.execute(sql,val)
        db.commit()
    except:
        messagebox.showerror("Hello user","Please enter valid values...")
    finally:
        itx1.delete(1.0,2.0)
        itx2.delete(1.0,2.0)
        itx3.delete(1.0,2.0)
        itx4.delete(1.0,2.0)
        itx5.delete(1.0,2.0)
        itx7.delete(1.0,2.0)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ studnt info @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def student():
    st2=tkinter.Tk()
    st2.title("Student Information")
    st2.geometry("550x400")
    st2.resizable(False,False)
    st2.config(bg="lightgreen")
    lb1=Label(st2,text="Student Information",bg="green",font=("stencil",25))
    lb1.pack()
    lb1.place(x="70")
    lb2=Label(st2,text="Enter Enn No. :",font=("stencil",18),bg="lightgreen")
    lb2.pack()
    lb2.place(x="20",y="110")
    global itx
    itx=Text(st2,font=(17),height="2",width="6")
    itx.pack()
    itx.place(x="220",y="100")
    global itx2
    itx2=Text(st2,font=(20),height="8",width="35")
    itx2.pack()
    itx2.place(x="50",y="200")
    b=Button(st2,font=("stencil",15),text="Show info",bg="blue",fg="white",command=btn)
    b.pack()
    b.place(x="390",y="100")


def btn():
    global itx
    global itx2
    t=itx.get(1.0,"end-1c")
    try:
        itx2.delete(1.0,END)
        t=int(t)
        mycursor=db.cursor()
        qr="SELECT * from stud where ano=%d"%t
        mycursor.execute(qr)
        result=mycursor.fetchall()
        print(result)
        for i in result:
            val=(i[0],i[1],i[2],i[3],i[4],i[5])
            qry="Eno: %d\n name: %s\n Branch: %s\n Sem: %d\n Book: %s\n Date of issueing: %s\n"%val
            itx2.insert(INSERT,qry)
            val2=i[5]
            qry2="SELECT ADDDATE(issue_date,INTERVAL 15 day) from stud where ano=%d"%t
            mycursor.execute(qry2)
            result2=mycursor.fetchall()
            itx2.insert(INSERT,"Date of Return: ")
            itx2.insert(INSERT,result2)
    except:
        messagebox.showerror("Hello user","The student does not present in libreary records")
        itx.delete(1.0,2.0)
    finally:
        itx.delete(1.0,2.0)
        


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Home page @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def lgn():
    name=mtx1.get(1.0,"end-1c")
    pswd=mtx2.get(1.0,"end-1c")
    if name=="Pushti" and pswd=="123":
        top2=tkinter.Toplevel()
        top2.config(bg="lightgrey")
        top2.title("Library management system")
        top2.geometry("800x550")
        top2.resizable(False,False)
        tlb1=Label(top2,text="WELCOME TO RISEUP LIBRARY",font=("Stencil",35),padx=5,bg="powderblue")
        tlb1.pack()
        photo=PhotoImage(file='library4.png')
        Label(top2,image=photo,bg="lightgrey").place(x="260",y="80")
        tbn1=Button(top2,text="Show Books",font=("Stencil",20),bg="black",foreground="white",command=showbooks)
        tbn1.pack()
        tbn1.place(x="20",y="100")
        tbn2=Button(top2,text="add Books",font=("Stencil",20),bg="black",foreground="white",command=addbook)
        tbn2.pack()
        tbn2.place(x="20",y="200")
        tbn3=Button(top2,text="Issue Book",font=("Stencil",20),bg="black",foreground="white",command=issuebook)
        tbn3.pack()
        tbn3.place(x="20",y="300")
        tbn4=Button(top2,text="Student Info",font=("Stencil",20),bg="black",foreground="white",command=student)
        tbn4.pack()
        tbn4.place(x="20",y="400")
        top2.mainloop()
    else:
        messagebox.showerror("Hello user","Please enter valid id & password")
def clr():
    mtx1.delete(1.0,2.0)
    mtx2.delete(1.0,2.0)
        
#@@@@@@@@@@@@@@@@@@@@@@@ login page @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

top=tkinter.Tk()
top.geometry("400x300")
top.title("Library Login")
top.resizable(False,False)
title=Label(top,text="Login",font=("Stencil",28),padx=5)
title.pack()
mlb1=Label(top,text="User ID:",font=("Stencil",18))
mlb1.pack()
mlb1.place(x="10",y="70")
mlb2=Label(top,text="Password:",font=("Stencil",18))
mlb2.pack()
mlb2.place(x="10",y="150")
mtx1=Text(top,height="2",width="17",font=(16))
mtx1.pack()
mtx1.place(x="160",y="65")
mtx2=Text(top,height="2",width="17",font=(16))
mtx2.pack()
mtx2.place(x="160",y="145")

mbt1=Button(top,text="Login",font=("Lucida Sans",15),bg="lightblue",command=lgn)
mbt1.pack()
mbt1.place(x="70",y="230")
mbt2=Button(top,text="Reset",font=("Lucida Sans",15),bg="lightyellow",command=clr)
mbt2.pack()
mbt2.place(x="200",y="230")

