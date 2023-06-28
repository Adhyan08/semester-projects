from tkinter import*
from PIL import ImageTk

def logout():
    main.destroy()
    import bank 
def new():
    main.destroy()
    import newtransaction
def view():
    main.destroy()
    import view

#gui part
main=Tk()
main.title("Main Menu")
bgimage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(main,image=bgimage)
bglabel.grid(row=0,column=0)
heading=Label(main,text="MAIN MENU",font=("Microsoft Yahei UI Light",23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
button1=Button(main,width=19,text="New Transaction",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=new).place(x=605,y=200)
button2=Button(main,width=19,text="View Balance",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",activeforeground="white",activebackground="firebrick1",command=view).place(x=605,y=260)

logout=Button(main,text="Logout",font=("Microsoft Yahei UI Light",11,'bold'),fg="white",bg="firebrick1",command=logout).place(x=670,y=320)
main.mainloop()