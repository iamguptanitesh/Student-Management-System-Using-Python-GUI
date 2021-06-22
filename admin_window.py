from tkinter import *
from tkinter import messagebox

class Admin_window:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("650x450+0+0")

        window_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Aquamarine")
        window_Frame.place(x=5,y=5,width=635, height=438)


        lbl=Label(window_Frame, text="Welcome to Python Project", font=("times new roman", 25, "bold"), fg="black",bg="Khaki").pack(side=TOP,fill=X)

        btn=Button(window_Frame,text="Manage Faculty",command=self.user,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=120, width=190, height=40)
        btn=Button(window_Frame,text="Manage Students",command=self.students,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=190, width=190, height=40)
        btn=Button(window_Frame,text="Exit",font=("times new roman", 19, "bold"),command=self.terminate, bg="yellow", cursor="hand2").place(x=200, y=330, width=190, height=40)
        btn=Button(window_Frame,text="Logout",command=self.logout,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=260, width=190, height=40)

    def user(self):
        self.root.destroy()
        import user

    def students(self):
        self.root.destroy()
        import Student

    def terminate(self):
        self.root.destroy()

    def logout(self):
        messagebox.showinfo("Success","Log Out Successful")
        self.root.destroy()
        import window

root = Tk()
obj = Admin_window(root)
root.mainloop()