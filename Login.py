from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("650x450+0+0")

        Login_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="orchid")
        Login_Frame.place(x=5,y=5,width=635, height=438)

        title = Label(Login_Frame, text="LOGIN HERE",bd=10,relief=GROOVE, font=("times new roman", 35, "bold"), fg="#6162FF",bg="Aquamarine")
        title.pack(side=TOP,fill=X)

        l1 = Label(Login_Frame, text="Username", font=("Goudy old style", 25, "bold"), fg="black", bg="orchid").place(x=100, y=120, width=145, height=40)
        self.Email = StringVar()
        self.Email_txt = Entry(Login_Frame,font=("Goudy old style", 20), bg="white", textvariable = self.Email).place(x=270,y=120,width=240,height=40)


        l2 = Label(Login_Frame, text="Password", font=("Goudy old style", 25, "bold"), fg="black", bg="orchid").place(x=100, y=180, width=145, height=40)
        self.password = StringVar()
        self.password_txt = Entry(Login_Frame,font=("Goudy old style", 20),show="*", bg="white", textvariable = self.password).place(x=270,y=180,width=240,height=40)


        btn_login = Button(Login_Frame,text="Login",command=self.new_page,font=("times new roman", 19, "bold"), bg="white", cursor="hand2").place(x=180, y=280,width=160, height=40)

        btn=Button( text="Back",command=self.page_window,font=("times new roman", 10, "bold"), bg="white", cursor="hand2")
        btn.place(x=450, y=330, width=80, height=40)        

    def page_window(self):
        self.root.destroy()
        import window

    def new_page(self):
        if self.Email.get()=="" or self.password.get()=="1234":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("select * from faculty where Email=%s and password=%s",(self.Email.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invailed Username Or Password",parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome to Student Management System", parent=self.root)
                    self.root.destroy()
                    import Student
                    con.close()



            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()