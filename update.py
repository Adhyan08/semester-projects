from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def updatedata():
    try:
        con=pymysql.connect(host='localhost',user='root',password='workfunction0808')
        cursor=con.cursor()
    except:
        messagebox.showerror("Error","Connection is not established try again")
        return
    query='use dataproject'
    cursor.execute(query)
    query='select * from Customer where User=%s and Password=%s'
    cursor.execute(query,(userentry.get(),balance1entry.get(),noentry.get()))
    row=cursor.fetchone()
    if row==None:
        messagebox.showerror("Error","Invalid Username or Password")
    else:
        messagebox.showinfo("Welcome","Login is Successful")
up=Tk()
up.title("Update Record")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(up,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(up,text="UPDATE",font=("Microsoft Yahei UI Light",20,'bold'),bg='white',fg='firebrick1')
heading.place(x=635,y=120)
username=Label(up,text="Update Username:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=180)
userentry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
userentry.place(x=575,y=205)


balancelabel=Label(up,text="Update Balance:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=230)
balance1entry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
balance1entry.place(x=575,y=255)

nolabel=Label(up,text="Update Mobile Number:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=280)
noentry=Entry(up,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
noentry.place(x=575,y=305)

loginbutton=Button(up,text="Update",font=('open sans',15,'bold'),fg='white',bg='firebrick1',activebackground='firebrick1',activeforeground='white',bd=0,command=updatedata)
loginbutton.place(x=630,y=360)






up.mainloop()