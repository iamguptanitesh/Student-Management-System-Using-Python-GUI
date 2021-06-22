from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox

class Signup:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("700x500+0+0")

        Signup_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="CYAN")
        Signup_Frame.place(x=5,y=5,width=685, height=488)

        lbl=Label(Signup_Frame,text="Create a new account",bd=10,relief=GROOVE, font=("times new roman", 25, "bold"), fg="#6162FF",bg="white")
        lbl.pack(side=TOP,fill=X)


        l1 = Label(Signup_Frame,text="Name : ",font=("times new roman",15,"bold"), fg="black", bg="white")
        l1.place(x=130, y=80, width=110)
        self.name = StringVar()
        self.name_txt = Entry(Signup_Frame, width = 30, font=("times new roman",13,"bold"),textvariable = self.name)
        self.name_txt.place(x=245, y=80, height=29)

        l2 = Label(Signup_Frame,text="Email ID : ", font=("times new roman",15,"bold"), fg="black", bg="white")
        l2.place(x=130, y=115, width=110)
        self.email = StringVar()
        self.email_txt = Entry(Signup_Frame, width = 30, font=("times new roman",13,"bold"),textvariable = self.email)
        self.email_txt.place(x=245, y=115, height=29)

        l3 = Label( Signup_Frame,text="Phone No : ", font=("times new roman",15,"bold"), fg="black", bg="white")
        l3.place(x=130, y=150, width=110)
        self.phn = StringVar()
        self.phn_txt = Entry(Signup_Frame, width = 30,font=("times new roman",13,"bold"), textvariable = self.phn)
        self.phn_txt.place(x=245, y=150, height=29)

        l4 = Label(Signup_Frame,text="FID No : ", font=("times new roman",15,"bold"), fg="black", bg="white")
        l4.place(x=130, y=185, width=110)
        self.vid = StringVar()
        self.vid_txt = Entry(Signup_Frame, width = 30,font=("times new roman",13,"bold"), textvariable =self.vid)
        self.vid_txt.place(x=245, y=185, height=29)

        lbl = Label(Signup_Frame,text="D.O.B", font=("times new roman",15,"bold"), fg="black", bg="white")
        lbl.place(x=130, y=220, width=110)
        self.dob = StringVar()
        self.dob_txt = Entry(Signup_Frame, width = 30,font=("times new roman",13,"bold"), textvariable =self.dob)
        self.dob_txt.place(x=245, y=220, height=29, width=185)

        lbl_gender=Label(Signup_Frame,text="Gender",bg="white",fg="black",font=("times new roman",15,"bold"))
        lbl_gender.place(x=130, y=255, width=110)
        self.gender_var=StringVar()
        combo_gender=ttk.Combobox(Signup_Frame,textvariable=self.gender_var, font=("times new roman",15,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.place(x=245, y=255, height=29, width=185)

        lbl_department=Label(Signup_Frame,text="Department",bg="white",fg="black",font=("times new roman",15,"bold"))
        lbl_department.place(x=130, y=290, width=110)
        self.department_var=StringVar()
        combo_department=ttk.Combobox(Signup_Frame,textvariable=self.department_var, font=("times new roman",15,"bold"),state="readonly")
        combo_department['values']=("Comps","IT","EXTC")
        combo_department.place(x=245, y=290,height=29)

        l4 = Label(Signup_Frame,text="Password : ", font=("times new roman",15,"bold"), fg="black", bg="white")
        l4.place(x=130, y=330,height=29, width=110)
        self.ps = StringVar()
        self.ps_txt = Entry(Signup_Frame,width = 30 ,font=("times new roman",13,"bold"),textvariable = self.ps)
        self.ps_txt.place(x=245, y=330,height=29)

        btn=Button(Signup_Frame, text="Submit",command=self.registration,font=("times new roman", 19, "bold"), bg="white", cursor="hand2")
        btn.place(x=200, y=380, width=160, height=40)

        btn=Button(Signup_Frame,  text="Already Registered/Login",command=self.page_window,font=("times new roman", 15, "bold"), bg="white", cursor="hand2")
        btn.place(x=160, y=430, width=250, height=40)        

    def registration(self):
        if self.vid.get()=="" or self.name.get()=="" or self.phn.get()=="" or self.email.get()=="" or self.name.get()=="" or self.ps.get()=="":
            messagebox.showerror("Error!","All Fields are Required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
            cur=con.cursor()
            cur.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.vid.get(),self.name.get(),self.email.get(), self.gender_var.get(),self.phn.get(), self.dob.get(),self.department_var.get,self.ps.get())
            )
            con.commit()
            
            con.close()
            messagebox.showinfo("Success","Registration Successful, Redirecting to Login Page...")
            self.root.destroy()
            import Login

    
    def page_window(self):
        self.root.destroy()
        import Login

root = Tk()
obj = Signup(root)
root.mainloop()