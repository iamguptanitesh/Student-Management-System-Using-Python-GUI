from tkinter import *
import pymysql
from tkinter import messagebox

class Signup:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("550x380+0+0")
        lbl=Label(text="Create a new account",bd=10,relief=GROOVE, font=("times new roman", 25, "bold"), fg="#6162FF",bg="white")
        lbl.pack(side=TOP,fill=X)


        l1 = Label(text="Name : ", font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        l1.place(x=80, y=100)
        self.name = StringVar()
        self.name_txt = Entry(width = 30, textvariable = self.name)
        self.name_txt.place(x=180, y=100)

        l2 = Label(text="Email ID : ", font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        l2.place(x=80, y=135)
        self.email = StringVar()
        self.email_txt = Entry( width = 30, textvariable = self.email)
        self.email_txt.place(x=180, y=135)

        l3 = Label( text="Phone No : ", font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        l3.place(x=80, y=170)
        self.phn = StringVar()
        self.phn_txt = Entry( width = 30, textvariable = self.phn)
        self.phn_txt.place(x=180, y=170)

        l4 = Label(text="VID No : ", font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        l4.place(x=80, y=205)
        self.vid = StringVar()
        self.vid_txt = Entry( width = 30, textvariable =self.vid)
        self.vid_txt.place(x=180, y=205)

        l4 = Label(text="Password : ", font=("Goudy old style", 15, "bold"), fg="black", bg="white")
        l4.place(x=80, y=240)
        self.ps = StringVar()
        self.ps_txt = Entry(width = 30, textvariable = self.ps)
        self.ps_txt.place(x=180, y=240)

        btn=Button( text="Submit",command=self.registration,font=("times new roman", 19, "bold"), bg="blue", cursor="hand2")
        btn.place(x=180, y=270, width=160, height=40)

        btn=Button( text="Already Registered/Login",command=self.page_window,font=("times new roman", 15, "bold"), bg="blue", cursor="hand2")
        btn.place(x=140, y=320, width=250, height=40)        

    def registration(self):
        if self.vid.get()=="" or self.name.get()=="" or self.phn.get()=="" or self.email.get()=="" or self.name.get()=="" or self.ps.get()=="":
            messagebox.showerror("Error!","All Fields are Required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into users values(%s,%s,%s,%s,%s)",(self.name.get(),self.email.get(),self.phn.get(),self.vid.get(),self.ps.get())
            )
            con.commit()
            
            con.close()
            messagebox.showinfo("Success","Registration Successful, Go back to Login Page...")
    
    def page_window(self):
        self.root.destroy()
        import Login

root = Tk()
obj = Signup(root)
root.mainloop()
