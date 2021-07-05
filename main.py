from tkinter import *
from tkinter import messagebox


class Log:
    def __init__(self, login):
        self.login = login
        self.login.title("Login Form")
        self.login.geometry("500x600")
        self.login.config(bg="Grey")
        frame1 = Frame(self.login, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=300)
        frame1.place(x=25, y=100)
        heading = Label(self.login, text="Register Form", font=("Courier", 26, "italic"), bg="grey")
        heading.place(x=120, y=10)
        user_name = Label(frame1, text="Please Enter User Name: ", bg="grey")
        user_name.place(x=20, y=15)
        self.user_entry = Entry(frame1)
        self.user_entry.place(x=250, y=15)
        password_lbl = Label(frame1, text="Please Enter Password: ", bg="grey")
        password_lbl.place(x=20, y=60)
        self.password_entry = Entry(frame1)
        self.password_entry.place(x=250, y=60)
        login_btn = Button(frame1, text="Login", bg="white", fg="Black", command=self.sign_in)
        login_btn.place(x=20, y=150)
        register_btn = Button(frame1, text="Register", bg="white", fg="black", command=self.sign_up)
        register_btn.place(x=150, y=150)
        admin_btn = Button(frame1, text="Administrator", bg="white", fg="black")
        admin_btn.place(x=300, y=150)

    def sign_in(self):
        try:
            if self.user_entry.get() == "" or self.password_entry.get() == "":
                messagebox.showerror("Error", "All fields required", parent=self.login)
        finally:
            pass

    def sign_up(self):
        login.destroy()
        import register


if __name__ == "__main__":
    login = Tk()
    app = Log(login)
    login.mainloop()
