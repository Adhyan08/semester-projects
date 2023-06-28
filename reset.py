from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def back():
    root.destroy()
    import bank

def on_enter(event):
    if usernameentry.get()=='Enter New Password':
        usernameentry.delete(0,END)

def on_enter1(event):
    if passwordentry.get()=='Confirm New Password':
         passwordentry.delete(0,END)
def on_enter2(event):
    if user.get()=='Username':
        user.delete(0,END)

def passc():
    if len(usernameentry.get())>10 or len(usernameentry.get())<4:
        messagebox.showerror("Error","The length of password must be less than 10 and greater than 4")
    elif usernameentry.get()!=passwordentry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        con=pymysql.connect(host='localhost',user='root',password='workfunction0808',database='dataproject')
        cursor=con.cursor()
        query='select * from Customer where User=%s'
        cursor.execute(query,user.get())
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Incorrect Username")
        else:
            print(row)
            query='update Customer set Password=%s where User=%s'
            #ab=int(usernameentry.get())-int(123)
            #ab=str(ab)
            cursor.execute(query,(usernameentry.get(),user.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success",("Password Changed",user.get()))
        
#gui part
root=Tk()
root.title("Reset Password")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(root,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(root,text="RESET PASSWORD",font=("Microsoft Yahei UI Light",19,'bold'),bg='white',fg='firebrick1')
heading.place(x=595,y=120)

user=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
user.place(x=580,y=200)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter2)
frame3=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=222)
usernameentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
usernameentry.place(x=580,y=260)
usernameentry.insert(0,'Enter New Password')
usernameentry.bind('<FocusIn>',on_enter)
frame1=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=282)

passwordentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
passwordentry.place(x=580,y=320)
passwordentry.insert(0,'Confirm New Password')
passwordentry.bind('<FocusIn>',on_enter1)
frame2=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=344)



loginbutton=Button(root,text="Change",font=('open sans',15,'bold'),fg='white',bg='firebrick1',bd=0,width=19,command=passc)
loginbutton.place(x=578,y=390)

lbutton=Button(root,text="Go Back",font=('open sans',9,'bold underline'),fg='firebrick1',bg='white',activeforeground='firebrick1',activebackground='white',bd=0,command=back)
lbutton.place(x=760,y=440)
root.mainloop()