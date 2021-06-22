from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Admin:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("650x450+0+0")

        lbl=Label( text="Welcome to Python Project", font=("times new roman", 25, "bold"), fg="black",bg="Red").pack(side=TOP,fill=X)
        
        Admin_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Aquamarine")
        Admin_Frame.place(x=5,y=50,width=635, height=395)
        title=Label(Admin_Frame,text="Admin Login",bg="Navy blue",fg="white",font=("times new roman",30,"bold"))
        title.pack(fill=X)


        l1 = Label(Admin_Frame, text="Username", font=("Goudy old style", 25, "bold"), fg="black", bg="Aquamarine").place(x=100, y=120, width=145, height=40)
        self.Email = StringVar()
        self.Email_txt = Entry(Admin_Frame,font=("Goudy old style", 20), bg="white", textvariable = self.Email).place(x=270,y=120,width=240,height=40)


        l2 = Label(Admin_Frame, text="Password", font=("Goudy old style", 25, "bold"), fg="black", bg="Aquamarine").place(x=100, y=180, width=145, height=40)
        self.password = StringVar()
        self.password_txt = Entry(Admin_Frame,font=("Goudy old style", 20),show="*", bg="white", textvariable = self.password).place(x=270,y=180,width=240,height=40)


        btn_login = Button(Admin_Frame,text="Login",font=("times new roman", 19, "bold"),command=self.admin_list, bg="white", cursor="hand2").place(x=180, y=280,width=160, height=40)
        btn=Button(Admin_Frame,text="Back",command=self.page_window,font=("times new roman", 10, "bold"), bg="white", cursor="hand2")
        btn.place(x=450, y=330, width=80, height=40)


    def page_window(self):
        self.root.destroy()
        import window    


    def admin_list(self):
        if self.Email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
                cur=con.cursor()
                cur.execute("select * from admin where email=%s and ps=%s",(self.Email.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invailed Username Or Password",parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome to SMS Admin Panel", parent=self.root)
                    self.root.destroy()
                    import admin_window
                    con.close()
                
            except Exception as es:
                messagebox.showerror("Error","Unable to Login!")

root = Tk()
obj = Admin(root)
root.mainloop()
