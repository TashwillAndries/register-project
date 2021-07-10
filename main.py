from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
login = Tk()
login.title("Login Form")
login.geometry("500x600")
login.config(bg="#FF5733")

canvas = Canvas(login, width=200, height=200)
image = PhotoImage(file="index.png")
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.place(x=150, y=350)


class Log:
    def __init__(self, login):
        self.login = login
        self.login.bind("<Control-a>", self.admin)
        self.frame1 = Frame(self.login, bg="#FF5733", highlightbackground="white", highlightthickness=5, width=450, height=200)
        self.frame1.place(x=25, y=100)
        self.heading = Label(self.login, text="Login Form", font=("Courier", 26, "italic"), bg="#FF5733")
        self.heading.place(x=150, y=10)
        self.options = ['Select....', 'Student', 'Lectures', 'Staff', 'Visitors']
        self.variable = StringVar(login)
        self.variable.set(self.options[0])
        self.list = OptionMenu(login, self.variable, *self.options)
        self.list.place(x=50, y=50)
        self.user_name = Label(self.frame1, text="Please Enter User Name: ", bg="#FF5733")
        self.user_name.place(x=20, y=15)
        self.user_entry = Entry(self.frame1)
        self.user_entry.place(x=250, y=15)
        self.password_lbl = Label(self.frame1, text="Please Enter Password: ", bg="#FF5733")
        self.password_lbl.place(x=20, y=60)
        self.password_entry = Entry(self.frame1)
        self.password_entry.place(x=250, y=60)
        self.login_btn = Button(self.frame1, text="Login", bg="#F33A6A", fg="Black", command=self.sign_in, borderwidth=5, padx=2, pady=2)
        self.login_btn.place(x=20, y=150)
        self.register_btn = Button(self.frame1, text="Register", bg="#F33A6A", fg="black", command=self.sign_up, borderwidth=5, padx=2, pady=2)
        self.register_btn.place(x=150, y=150)
        self.ministrator = Button(self.frame1, text="Administrator", bg="#F33A6A", fg="black", command=self.binded, borderwidth=5, padx=2, pady=2)
        self.ministrator.place(x=300, y=150)

    # letting users know that admin can only be accessed with control + A
    def binded(self):
        messagebox.showerror("ERROR", "Administrator can only be accessed by pressing control plus A")

    # sign out for students
    def signing_out(self):
        log_out = datetime.now().time().strftime("%H:%M:%S")
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE log_times SET sign_out_time=%s WHERE id_number=%s", (log_out, id_no))
        conn.commit()
        popup_one.destroy()

    # sign out for lectures
    def signing_out_lect(self):
        log_out = datetime.now().time().strftime("%H:%M:%S")
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE log_times SET sign_out_time=%s WHERE id_number=%s", (log_out, id_no_lect))
        conn.commit()
        popup_two.destroy()

    # sign out for staff members
    def signing_out_staff(self):
        log_out = datetime.now().time().strftime("%H:%M:%S")
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE log_times SET sign_out_time=%s WHERE id_number=%s", (log_out, id_no_staff))
        conn.commit()
        popup_three.destroy()

    # sign out for visitors
    def signing_out_visit(self):
        log_out = datetime.now().time().strftime("%H:%M:%S")
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE log_times SET sign_out_time=%s WHERE id_number=%s", (log_out, visit_id))
        conn.commit()
        popup_four.destroy()

    def sign_in(self):

        if self.user_entry.get() == "" and self.password_entry.get() == "":
            messagebox.showerror("Error", "field can not be empty")
        try:
            if self.variable.get() == [0]:
                messagebox.showerror("Error", "no valid user selected")
            elif self.variable.get() == "Student":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='lifechoices_login', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                vals = (self.user_entry.get(), self.password_entry.get(), 'Student')
                my_cursor.execute("SELECT * FROM users where username=%s AND password=%s AND privilege= %s", vals)
                row = my_cursor.fetchall()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    # window to sign out
                    global popup_one
                    global id_no
                    popup_one = Toplevel(login)
                    popup_one.title("welcome")
                    popup_one.geometry("250x150")
                    popup_one.config(bg="white")
                    welcome = Label(popup_one, text="Enjoy Your day")
                    welcome.pack()
                    frame = Frame(popup_one, bg="grey")
                    frame.pack()
                    sign_out = Button(frame, text="Sign out", command=self.signing_out, bg="white", fg="black")
                    sign_out.pack()
                    id_no = row[0][0]
                    log_time = datetime.now().time().strftime("%H:%M:%S")
                    log_date = datetime.now().date().strftime("%y-%m-%d")
                    query_1 = "INSERT INTO log_times(id_number, sign_in_time, sign_in_date) VALUES(%s,%s,%s)"
                    values = (id_no, log_time, log_date)
                    my_cursor.execute(query_1, values)
                    conn.commit()
            elif self.variable.get() == "Lectures":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                   database='lifechoices_login', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                vals = (self.user_entry.get(), self.password_entry.get(), 'Lecturer')
                my_cursor.execute("SELECT * FROM users where username=%s AND password=%s AND privilege= %s", vals)
                row = my_cursor.fetchall()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    global popup_two
                    global id_no_lect
                    popup_two = Toplevel(login)
                    popup_two.title("welcome")
                    popup_two.geometry("250x150")
                    popup_two.config(bg="white")
                    welcome = Label(popup_two, text="Enjoy Your day")
                    welcome.pack()
                    frame = Frame(popup_two, bg="grey")
                    frame.pack()
                    sign_out = Button(frame, text="Sign out", command=self.signing_out_lect, bg="white", fg="black")
                    sign_out.pack()
                    id_no_lect = row[0][0]
                    log_time = datetime.now().time().strftime("%H:%M:%S")
                    log_date = datetime.now().date().strftime("%y-%m-%d")
                    query_1 = "INSERT INTO log_times(id_number, sign_in_time, sign_in_date) VALUES(%s,%s,%s)"
                    values = (id_no_lect, log_time, log_date)
                    my_cursor.execute(query_1, values)
                    conn.commit()
            elif self.variable.get() == "Staff":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                   database='lifechoices_login', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                vals = (self.user_entry.get(), self.password_entry.get(), 'Staff')
                my_cursor.execute("SELECT * FROM users where username=%s AND password=%s AND privilege= %s", vals)
                row = my_cursor.fetchall()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    # separate window to sign ou
                    global popup_three
                    global id_no_staff
                    popup_three = Toplevel(login)
                    popup_three.title("welcome")
                    popup_three.geometry("250x150")
                    popup_three.config(bg="white")
                    welcome = Label(popup_three, text="Enjoy Your day")
                    welcome.pack()
                    frame = Frame(popup_three, bg="grey")
                    frame.pack()
                    sign_out = Button(frame, text="Sign out", command=self.signing_out_staff, bg="white", fg="black")
                    sign_out.pack()
                    id_no_staff = row[0][0]
                    log_time = datetime.now().time().strftime("%H:%M:%S")
                    log_date = datetime.now().date().strftime("%y-%m-%d")
                    query_1 = "INSERT INTO log_times(id_number, sign_in_time, sign_in_date) VALUES(%s,%s,%s)"
                    values = (id_no_staff, log_time, log_date)
                    my_cursor.execute(query_1, values)
                    conn.commit()
            elif self.variable.get() == "Visitors":
                conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='lifechoices_login', auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                vals = (self.user_entry.get(), self.password_entry.get(), 'Visitor')
                my_cursor.execute("SELECT * FROM users where username=%s AND password=%s AND privilege= %s", vals)
                row = my_cursor.fetchall()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password")
                else:
                    # separate window to sign ou
                    global popup_four
                    global visit_id
                    popup_four = Toplevel(login)
                    popup_four.title("welcome")
                    popup_four.geometry("250x150")
                    popup_four.config(bg="white")
                    welcome = Label(popup_four, text="Enjoy Your day")
                    welcome.pack()
                    frame = Frame(popup_four, bg="grey")
                    frame.pack()
                    sign_out = Button(frame, text="Sign out", command=self.signing_out_visit, bg="white", fg="black")
                    sign_out.pack()
                    visit_id = row[0][0]
                    log_time = datetime.now().time().strftime("%H:%M:%S")
                    log_date = datetime.now().date().strftime("%y-%m-%d")
                    query_1 = "INSERT INTO log_times(id_number, sign_in_time, sign_in_date) VALUES(%s,%s,%s)"
                    values = (visit_id, log_time, log_date)
                    my_cursor.execute(query_1, values)
                    conn.commit()
        except ValueError:
            messagebox.showinfo("Error", "No matches found register user")
        except IndexError:
            messagebox.showerror("Error", "Wrong privilege chosen")


    def sign_up(self):
        login.withdraw()
        import register

    def admin(self, event):
        login.withdraw()
        import Admin


app = Log(login)
login.mainloop()
