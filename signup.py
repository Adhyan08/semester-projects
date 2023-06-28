from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    userentry.delete(0,END)
    passwordentry.delete(0,END)
    balance1entry.delete(0,END)
    noentry.delete(0,END)


def check():
    if userentry.get()=='' or passwordentry.get()=='' or password1entry.get()=='' or balance1entry.get()=='' or noentry.get()=='':
        messagebox.showerror('Error','All feilds are required')
    elif passwordentry.get()!=password1entry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif len(passwordentry.get())>10 or len(passwordentry.get())<4:
        messagebox.showerror("Error","The length of password must be less than 10 and greater than 4") 
    elif noentry.get() != int and len(noentry.get())>10 :
        messagebox.showerror('Error','Invalid Input for number')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='workfunction0808')
            cursor=con.cursor()
            #query='create table Customer(id int auto_increment primary key not null,User varchar(100),Password varchar(20),Balance varchar(20),Mobile varchar(15))'
            #cursor.execute(query)
        except:
            messagebox.showerror('Error','Connectivity issue')
            return
        try:
            query='create database dataproject'
            cursor.execute(query)
            query='use dataproject'
            cursor.execute(query)
            query='create table Customer(id int auto_increment primary key not null,User varchar(100),Password varchar(20),Balance varchar(20),Mobile varchar(15))'
            cursor.execute(query)
        except:
            cursor.execute('use dataproject')
        query='select * from Customer where User=%s'
        cursor.execute(query,(userentry.get()))
        row=cursor.fetchone()
        if row!=None:
            messagebox.showerror('Error','Username Already Exists')
        else:
            query='insert into Customer(User,Password,Balance,Mobile) values(%s,%s,%s,%s)'
            cursor.execute(query,(userentry.get(),passwordentry.get(),balance1entry.get(),noentry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration Successful')
            clear()
            sign.destroy()
            import bank
    '''                        
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='workfunction0808')
            cursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Connectivity issue')
            return
        try:
            query='create database data'
            cursor.execute(query)
            query='user data'
            cursor.execute(query)
            query='create table entry(id int_increment primary key not null,username varchar(50),password varchar(20),balance varchar(20),number varchar(15)'
            cursor.execute(query)
        except:
            pass
'''
    
def login_page():
    sign.destroy()
    import bank
    

#gui part
sign=Tk()
sign.title("Signup")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(sign,image=bgimage)
bglabel.grid(row=0,column=0)

frame=Frame(sign).place(x=554,y=100)



heading=Label(frame,text="CREATE AN ACCOUNT",font=("Microsoft Yahei UI Light",15,'bold'),bg='white',fg='firebrick1')
heading.place(x=595,y=120)

userlabel=Label(sign,text="Username:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=180)
userentry=Entry(sign,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
userentry.place(x=575,y=205)
passwordlabel=Label(sign,text="Password:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=230)
passwordentry=Entry(sign,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1',show="*")
passwordentry.place(x=575,y=255)
password1label=Label(sign,text="Confirm Password:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=280)
password1entry=Entry(sign,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1',show="*")
password1entry.place(x=575,y=305)

balancelabel=Label(sign,text="Enter Balance:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=330)
balance1entry=Entry(sign,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
balance1entry.place(x=575,y=355)

nolabel=Label(sign,text="Mobile Number:",font=("Microsoft Yahei UI Light",12,'bold'),fg='firebrick1',bg='white').place(x=572,y=380)
noentry=Entry(sign,width=25,font=("Microsoft Yahei UI Light",10,'bold'),fg='white',bg='firebrick1')
noentry.place(x=575,y=405)

signupbutton=Button(sign,text="Signup",font=('open sans',12,'bold'),fg='white',bg='firebrick1',bd=0,width=10,command=check)
signupbutton.place(x=615,y=445)

c=Button(sign,text="Already have an account?",font=("Microsoft Yahei UI Light",9,'bold'),fg='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2')
c.place(x=580,y=487)
login=Button(sign,text="Login",font=('open sans',9,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page).place(x=750,y=487)


sign.mainloop()