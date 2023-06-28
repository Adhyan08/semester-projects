from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql



def forgot():
    root.destroy()
    import reset
def signup():
    root.destroy()
    import signup
def hide():
    eyeimg.config(file='closeye.png')
    passwordentry.config(show='*')
    eyebutton.config(command=show)

def show():
     eyeimg.config(file='openeye.png')
     passwordentry.config(show='')
     eyebutton.config(command=hide)


def on_enter(event):
    if usernameentry.get()=='Username':
        usernameentry.delete(0,END)

def on_enter1(event):
    if passwordentry.get()=='Password':
         passwordentry.delete(0,END)

def loginuser():
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='workfunction0808')
            cursor=con.cursor()
        except:
            messagebox.showerror("Error","Connection is not established try again")
            return
        query='use dataproject'
        cursor.execute(query)
        query='select * from Customer where User=%s and Password=%s'
        cursor.execute(query,(usernameentry.get(),passwordentry.get()))
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid Username or Password")
        else:
            messagebox.showinfo("Welcome","Login is Successful")
            root.destroy()
            import mainmenu


#gui part
root=Tk()
root.title("Login Menu")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(root,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(root,text="USER LOGIN",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
usernameentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
usernameentry.place(x=580,y=200)
usernameentry.insert(0,'Username')
usernameentry.bind('<FocusIn>',on_enter)
frame1=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=222)

passwordentry=Entry(root,width=25,font=("Microsoft Yahei UI Light",11,'bold'),bd=0,fg='firebrick1')
passwordentry.place(x=580,y=260)
passwordentry.insert(0,'Password')
passwordentry.bind('<FocusIn>',on_enter1)
frame2=Frame(root,width=250,height=2,bg='firebrick1').place(x=580,y=282)
eyeimg=PhotoImage(file="openeye.png")
eyebutton=Button(root,image=eyeimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=800,y=255)


forgetbutton=Button(root,text="Forgot password ?",font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2',command=forgot)
forgetbutton.place(x=715,y=285)

loginbutton=Button(root,text="Login",font=('open sans',15,'bold'),fg='white',bg='firebrick1',activeforeground='firebrick1',bd=0,width=19,command=loginuser)
loginbutton.place(x=578,y=320)


newbutton=Button(root,text="Don't have an account?",font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2')
newbutton.place(x=615,y=370)
Signup=Button(root,text="Signup",font=('open sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=signup).place(x=773,y=370)








root.mainloop()