from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

register = Tk()


# unlocks the window for users to type
def unlock():
    frame1.config(bg="grey")
    password_entry.config(state="normal")
    id_number_entry.config(state="normal")
    phone_number_entry.config(state="normal")
    surname_entry.config(state="normal")
    user_entry.config(state="normal")


# function to add information to the database
def student():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password') # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Student')"
        val = (id_number_entry.get(), user_entry.get(), surname_entry.get(),phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "ID and number must be in digits" + (format(err)))

def lecturer():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Lecturer')"
        val = (
        id_number_entry.get(), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "ID and number must be in digits" + (format(err)))

def staff():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Staff')"
        val = (
        id_number_entry.get(), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "ID and number must be in digits" + (format(err)))

def visitors():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Visitors')"
        val = (
        id_number_entry.get(), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", "ID and number must be in digits" + (format(err)))

register.title("Register Form")
register.geometry("500x500")
register.config(bg="grey")
heading = Label(register, text="Register Form", font=("Courier", 26, "italic"), bg="grey")
heading.place(x=120, y=10)
student_btn = Button(register, text="Unlock Window", bg="white", fg="black", command=unlock)
student_btn.place(x=50, y=60)
frame1 = Frame(register, bg="black", highlightbackground="white", highlightthickness=5, width=450, height=300)
frame1.place(x=25, y=100)

user_name = Label(frame1, text="First Name", bg="grey")
user_name.place(x=60, y=20)
user_entry = Entry(frame1, state="disabled")
user_entry.place(x=20, y=50)

surname_lbl = Label(frame1, text="Surname", bg="grey")
surname_lbl.place(x=330, y=20)
surname_entry = Entry(frame1, state="disabled")
surname_entry.place(x=270, y=50)

id_number = Label(frame1, text="ID Number", bg="grey")
id_number.place(x=60, y=90)
id_number_entry = Entry(frame1, state="disabled")
id_number_entry.place(x=20, y=120)

phone_number = Label(frame1, text="Phone Number", bg="grey")
phone_number.place(x=315, y=90)
phone_number_entry = Entry(frame1, state="disabled")
phone_number_entry.place(x=270, y=120)

password_lbl = Label(frame1, text="Password", bg="grey")
password_lbl.place(x=60, y=160)
password_entry = Entry(frame1, state="disabled")
password_entry.place(x=20, y=190)

reg_btn = Button(frame1, text="Student", bg="white", fg="black", command=student)
reg_btn.place(x=50, y=250)
lecturer_btn = Button(frame1, text="Lecturer", bg="White", fg="black", command=lecturer)
lecturer_btn.place(x=150, y=250)
lecturer_btn = Button(frame1, text="Staff", bg="White", fg="black", command=staff)
lecturer_btn.place(x=250, y=250)
lecturer_btn = Button(frame1, text="Visitor", bg="White", fg="black", command=visitors)
lecturer_btn.place(x=350, y=250)

register.mainloop()
