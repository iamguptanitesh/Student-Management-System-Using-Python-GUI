from tkinter import *

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("MiniProject")
        self.root.geometry("650x450+0+0")

        window_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        window_Frame.place(x=5,y=5,width=635, height=438)


        lbl=Label(window_Frame, text="Welcome to Python Project", font=("times new roman", 25, "bold"), fg="black",bg="Red").pack(side=TOP,fill=X)
    
        btn=Button(window_Frame,text="Faculty Login",command=self.login_window,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=190, width=190, height=40)
        btn=Button(window_Frame,text="Register",command=self.signup_window,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=260, width=190, height=40)
        btn=Button(window_Frame,text="Exit",font=("times new roman", 19, "bold"),command=self.terminate, bg="yellow", cursor="hand2").place(x=200, y=330, width=190, height=40)
        btn=Button(window_Frame,text="Admin Login",command=self.admin_window,font=("times new roman", 19, "bold"), bg="yellow", cursor="hand2").place(x=200, y=120, width=190, height=40)

    def login_window(self):
        self.root.destroy()
        import Login

    def signup_window(self):
        self.root.destroy()
        import Signup
    
    def admin_window(self):
        self.root.destroy()
        import Admin
    
    def terminate(self):
        self.root.destroy()

root = Tk()
obj = Login(root)
root.mainloop()