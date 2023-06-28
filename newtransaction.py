from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def withdra():
    def withdrawal():
        con=pymysql.connect(host='localhost',user='root',password='jagjit',database='dataproject')
        cursor=con.cursor()
        query='select * from Customer where User=%s and Password=%s'
        cursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=cursor.fetchone()
        #balance=row[3]
        #print(balance)
        if row==None:
            messagebox.showerror("Error","Incorrect Credentials")
        else:
            balance=row[3]
            query='update Customer set Balance=%s where User=%s'
            new=int(balance)-int(amountentry.get())
            new=str(new)
            cursor.execute(query,(new,usernameentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Transaction Successful")
            drawal.destroy()
    tra.destroy()
    def on_enter(event):
              if usernameentry.get()=='Username':
                 usernameentry.delete(0,END)

    def on_enter1(event):
              if passwordentry.get()=='Password':
                 passwordentry.delete(0,END)
    def on_enter2(event):
        if amountentry.get()=='Enter Amount':
                 amountentry.delete(0,END)
    drawal=Tk()
   
    drawal.title("WITHDRAWAL")
    bgimage=ImageTk.PhotoImage(file='bg.jpg')
    heading=Label(drawal,text="USER LOGIN",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
    heading.place(x=605,y=120)
    bglabel=Label(drawal ,image=bgimage)
    bglabel.grid(row=0,column=0)
    heading=Label(drawal,text="WITHDRAWAL",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
    heading.place(x=605,y=120)
    usernameentry=Entry(drawal,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    usernameentry.place(x=580,y=200)
    usernameentry.insert(0,'Username')
    usernameentry.bind('<FocusIn>',on_enter)
    frame1=Frame(drawal,width=250,height=2,bg='firebrick1').place(x=580,y=222)


    passwordentry=Entry(drawal,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    passwordentry.place(x=580,y=260)
    passwordentry.insert(0,'Password')
    passwordentry.bind('<FocusIn>',on_enter1)
    frame2=Frame(drawal,width=250,height=2,bg='firebrick1').place(x=580,y=282)

    amountentry=Entry(drawal,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    amountentry.place(x=580,y=320)
    amountentry.insert(0,'Enter Amount')
    amountentry.bind('<FocusIn>',on_enter2)
    frame3=Frame(drawal,width=250,height=2,bg='firebrick1').place(x=580,y=342)
    loginbutton=Button(drawal,text="Proceed",font=('open sans',15,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=withdrawal)
    loginbutton.place(x=578,y=360)
    drawal.mainloop()

def deposit():
    def depo():
        con=pymysql.connect(host='localhost',user='root',password='jagjit',database='dataproject')
        cursor=con.cursor()
        query='select * from Customer where User=%s and Password=%s'
        cursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=cursor.fetchone()
        #balance=row[3]
        if row==None:
            messagebox.showerror("Error","Incorrect Credentials")
        else:
            balance=row[3]
            query='update Customer set Balance=%s where User=%s'
            new=int(balance)+int(amountentry.get())
            new=str(new)
            cursor.execute(query,(new,usernameentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Transaction Successful")
            dep.destroy()
    tra.destroy()
    def on_enter(event):
            if usernameentry.get()=='Username':
             usernameentry.delete(0,END)

    def on_enter1(event):
        if passwordentry.get()=='Password':
            passwordentry.delete(0,END)
    def on_enter2(event):
        if amountentry.get()=='Enter Amount':
            amountentry.delete(0,END)
    dep=Tk()
   
    dep.title("WITHDRAWAL")
    bgimage=ImageTk.PhotoImage(file='bg.jpg')
    
    bglabel=Label(dep ,image=bgimage)
    bglabel.grid(row=0,column=0)
    heading=Label(dep,text="DEPOSIT",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
    heading.place(x=605,y=120)
    usernameentry=Entry(dep,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    usernameentry.place(x=580,y=200)
    usernameentry.insert(0,'Username')
    usernameentry.bind('<FocusIn>',on_enter)
    frame1=Frame(dep,width=250,height=2,bg='firebrick1').place(x=580,y=222)


    passwordentry=Entry(dep,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    passwordentry.place(x=580,y=260)
    passwordentry.insert(0,'Password')
    passwordentry.bind('<FocusIn>',on_enter1)
    frame2=Frame(dep,width=250,height=2,bg='firebrick1').place(x=580,y=282)

    amountentry=Entry(dep,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
    amountentry.place(x=580,y=320)
    amountentry.insert(0,'Enter Amount')
    amountentry.bind('<FocusIn>',on_enter2)
    frame3=Frame(dep,width=250,height=2,bg='firebrick1').place(x=580,y=342)
    loginbutton=Button(dep,text="Proceed",font=('open sans',15,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=depo)
    loginbutton.place(x=578,y=360)

    dep.mainloop()    

#guipart
tra=Tk()
tra.title("New Transaction")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(tra,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(tra,text="TRANSACTION",font=("Microsoft Yahei UI Light",20,'bold'),bg='white',fg='firebrick1')
heading.place(x=595,y=120)

button1=Button(tra,width=19,text="WITHDRAWAL",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=withdra).place(x=605,y=220)
button2=Button(tra,width=19,text="DEPOSIT",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=deposit).place(x=605,y=300)

tra.mainloop()