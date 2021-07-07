from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime


class Log:
    def __init__(self, login):
        self.login = login
        self.login.title("Login Form")
        self.login.geometry("500x600")
        self.login.config(bg="Grey")
        login.bind("<Control-a>", self.admin)
        frame1 = Frame(self.login, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=300)
        frame1.place(x=25, y=100)
        heading = Label(self.login, text="Register Form", font=("Courier", 26, "italic"), bg="grey")
        heading.place(x=120, y=10)
        self.options = ['Select....', 'Student', 'Lectures', 'Staff', 'Visitors']
        self.variable = StringVar(login)
        self.variable.set(self.options[0])
        self.list = OptionMenu(login, self.variable, *self.options, command=self.sign_in)
        self.list.place(x=50, y=50)
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
        if self.user_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("Error", "field can not be empty")
        try:
            if self.variable.get() == "Select...":
                raise ValueError
            elif self.variable.get() == "Student":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='login', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student where student_name=%s and student_password=%s"
                                  ,(self.user_entry.get()
                                   ,self.password_entry.get()))
                row = my_cursor.fetchone()
                if row == None:
                    log_time = datetime.now().time().strftime("%H:%M:%S")
                    log_date = datetime.now().date().strftime("%Y-%m-%d")
                    my_cursor.execute("INSERT INTO student WHERE sign_in_time=%s and sign_in_date=%s",(log_time, log_date))
                    conn.commit()
                    messagebox.showerror("login Successful", "Enjoy your day")
                else:
                    messagebox.showinfo("Welcome", "login Successful")
            elif self.variable.get() == "Lectures":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='registration', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM lecture where lecturer_name=%s and lecturer_password=%s"
                                  , (self.user_entry.get()
                                     , self.password_entry.get()))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    messagebox.showinfo("login Successful", "Enjoy your day")
        except TypeError:
            pass

    def sign_up(self):
        login.withdraw()
        import register

    def admin(self, event):
        login.withdraw()
        import Admin


if __name__ == "__main__":
    login = Tk()
    app = Log(login)
    login.mainloop()
