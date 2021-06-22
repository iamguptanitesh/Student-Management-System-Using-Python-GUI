from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="CRIMSON",fg="WHITE")
        title.pack(side=TOP,fill=X)

        #==========All Variables===========
        self.vid_var=StringVar()
        self.name_var=StringVar()
        self.Email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.department_var=StringVar()
        self.password_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



    #manag

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450, height=580)

        m_title=Label(Manage_Frame,text="Manage Faculty Details",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=9)

        lbl_vid=Label(Manage_Frame,text="Faculty ID",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_vid.grid(row=1,column=0,pady=9,padx=20,sticky="W")

        txt_vid=Entry(Manage_Frame,textvariable=self.vid_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_vid.grid(row=1,column=1,pady=9,padx=20,sticky="W")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=9,padx=20,sticky="W")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=9,padx=20,sticky="W")

        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=9,padx=20,sticky="W")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=9,padx=20,sticky="W")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=9,padx=20,sticky="W")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var, font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4, column=1, padx=20,pady=10)

        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=9,padx=20,sticky="W")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=9,padx=20,sticky="W")

        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=9,padx=20,sticky="W")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=9,padx=20,sticky="W")

        lbl_department=Label(Manage_Frame,text="Department",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_department.grid(row=7,column=0,pady=9,padx=20,sticky="W")

        combo_department=ttk.Combobox(Manage_Frame,textvariable=self.department_var, font=("times new roman",13,"bold"),state="readonly")
        combo_department['values']=("COMPS","IT","EXTC")
        combo_department.grid(row=7, column=1, padx=20,pady=10) 

        lbl_password=Label(Manage_Frame, text="Password",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_password.grid(row=8,column=0,pady=9,padx=20,sticky="W")

        txt_password=Entry(Manage_Frame, textvariable=self.password_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_password.grid(row=8,column=1,pady=9,padx=20,sticky="W")

#=========Button Frame========#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=515,width=420)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students,cursor="hand2").grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data,cursor="hand2").grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data,cursor="hand2").grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)




    #manage
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800, height=580)

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="W")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("FID","Name","Contact")
        combo_search.grid(row=0, column=1, padx=20,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20, font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data,cursor="hand2").grid(row=0,column=4,padx=10,pady=10)

        logoutbtn=Button(Detail_Frame,text="Logout",width=7,command=self.exit,pady=5,cursor="hand2").grid(row=0,column=5,padx=5,pady=5)

#=========Table Frame==========
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760, height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("vid","name","Email","gender","contact","dob","department","password"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("vid",text="FID")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("department",text="Department")
        self.Student_table.heading("password",text="Password")

        self.Student_table['show']='headings'
        self.Student_table.column("vid",width=90)
        self.Student_table.column("name",width=100)
        self.Student_table.column("Email",width=150)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("department",width=100)
        self.Student_table.column("password",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.vid_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error!","All Fields are Required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
            cur=con.cursor()
            cur.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.vid_var.get(), self.name_var.get(), self.Email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.department_var.get(),self.password_var.get())
            )
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted Successfully")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("select * from faculty")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.vid_var.set("")
        self.name_var.set("")
        self.Email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.department_var.set("")
        self.password_var.set("")

    def get_cursor(self,event):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.vid_var.set(row[0])
        self.name_var.set(row[1])
        self.Email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.department_var.set(row[6])
        self.password_var.set(row[7])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("update faculty set name = %s,Email = %s,gender = %s,contact = %s,dob = %s,department = %s, password = %s where vid = %s", (self.name_var.get(), self.Email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.department_var.get(),self.password_var.get(),self.vid_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("delete from faculty where vid=%s",self.vid_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        if self.search_txt.get()=="":
            messagebox.showwarning("Error","Invalid Entry!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
            cur=con.cursor()
            cur.execute("select * from faculty where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
            con.close()

    def exit(self):
        messagebox.showinfo("Success","Log Out Successful")
        self.root.destroy()
        import window


    

root=Tk()
obj=Student(root)
root.mainloop()