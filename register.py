from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber

register = Tk()


# unlocks the window for users to type
def unlock():
    frame1.config(bg="#FF5733")
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
        id_number = rsaidnumber.parse(id_number_entry.get())
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login', auth_plugin='mysql_native_password') # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Student')"
        val = (str(id_number), user_entry.get(), surname_entry.get(),phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except ValueError:
        messagebox.showerror("Error", "ID number not valid")

# register for lecturers
def lecturer():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        id_number = rsaidnumber.parse(id_number_entry.get())
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Lecturer')"
        val = (
            str(id_number), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except ValueError:
        messagebox.showerror("Error", "ID number not valid")

# register for staff
def staff():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        id_number = rsaidnumber.parse(id_number_entry.get())
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege)" \
               " VALUES (%s, %s, %s, %s, %s,'Staff')"
        val = (
               str(id_number), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        messagebox.showinfo("Success", "Register Successful")
    except ValueError:
        messagebox.showerror("Error", "ID number not valid")

# register of visitors
def visitors():
    if user_entry.get() == "" or id_number_entry.get() == "":
        messagebox.showerror("Error", "Information cant be blank")
    try:
        id_number = rsaidnumber.parse(id_number_entry.get())
        conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='lifechoices_login',
                                       auth_plugin='mysql_native_password')  # linking python to the mysql database
        my_cursor = conn.cursor()
        data = "INSERT INTO users (id_number,username,surname,phone,password,privilege) VALUES (%s, %s, %s, %s, %s,'Visitor')"
        val = (
               str(id_number), user_entry.get(), surname_entry.get(), phone_number_entry.get(), password_entry.get())
        my_cursor.execute(data, val)
        conn.commit()
        frame = Frame(register, width=400, height=320, bg="#F33A6A")
        frame.place(x=50, y=150)
        kin_details = Label(frame, text="Next Of Kin Details", bg="#F33A6A")
        kin_details.place(x=60, y=18)
        username = Label(frame, text="username", width=8, bg="#F33A6A")
        username_entry = Entry(frame, width=25)
        username.place(x=50, y=70)
        username_entry.place(x=170, y=70)

        kin_no = Label(frame, text="Phone_number", width=11, bg="#F33A6A")
        kin_no_entry = Entry(frame, width=25)
        kin_no.place(x=50, y=110)
        kin_no_entry.place(x=170, y=110)

        def submit():
            data = "INSERT INTO kin(username,kin_name,phone_number) VALUES(%s, %s, %s)"
            values = (id_number_entry.get(), username_entry.get(), kin_no_entry.get())
            my_cursor.execute(data, values)
            conn.commit()
            messagebox.showinfo("Success", "Register Successful")

        submit_btn = Button(frame, text="submit", command=submit, borderwidth=5, padx=2, pady=2)
        submit_btn.configure(bg="#F33A6A", fg='black')
        submit_btn.place(x=100, y=280)
        cancel_btn = Button(frame, text="cancel", command=frame.destroy, borderwidth=5, padx=2, pady=2)
        cancel_btn.configure(bg="#F33A6A", fg='black')
        cancel_btn.place(x=240, y=280)

    except ValueError:
        messagebox.showerror("Error", "ID number not valid")


register.title("Register Form")
register.geometry("500x500")
register.config(bg="#FF5733")
heading = Label(register, text="Register Form", font=("Courier", 26, "italic"), bg="#FF5733")
heading.place(x=120, y=10)
student_btn = Button(register, text="Unlock Window", bg="white", fg="black", command=unlock)
student_btn.place(x=50, y=60)
frame1 = Frame(register, bg="#F33A6A", highlightbackground="white", highlightthickness=5, width=450, height=300)
frame1.place(x=25, y=100)

user_name = Label(frame1, text="First Name", bg="#FF5733")
user_name.place(x=60, y=20)
user_entry = Entry(frame1, state="disabled")
user_entry.place(x=20, y=50)

surname_lbl = Label(frame1, text="Surname", bg="#FF5733")
surname_lbl.place(x=330, y=20)
surname_entry = Entry(frame1, state="disabled")
surname_entry.place(x=270, y=50)

id_number = Label(frame1, text="ID Number", bg="#FF5733")
id_number.place(x=60, y=90)
id_number_entry = Entry(frame1, state="disabled")
id_number_entry.place(x=20, y=120)

phone_number = Label(frame1, text="Phone Number", bg="#FF5733")
phone_number.place(x=315, y=90)
phone_number_entry = Entry(frame1, state="disabled")
phone_number_entry.place(x=270, y=120)

password_lbl = Label(frame1, text="Password", bg="#FF5733")
password_lbl.place(x=60, y=160)
password_entry = Entry(frame1, state="disabled")
password_entry.place(x=20, y=190)

reg_btn = Button(frame1, text="Student", bg="#F33A6A", fg="black", command=student, borderwidth=5, padx=2, pady=2)
reg_btn.place(x=50, y=250)
lecturer_btn = Button(frame1, text="Lecturer", bg="#F33A6A", fg="black", command=lecturer, borderwidth=5, padx=2, pady=2)
lecturer_btn.place(x=150, y=250)
lecturer_btn = Button(frame1, text="Staff", bg="#F33A6A", fg="black", command=staff, borderwidth=5, padx=2, pady=2)
lecturer_btn.place(x=250, y=250)
lecturer_btn = Button(frame1, text="Visitor", bg="#F33A6A", fg="black", command=visitors, borderwidth=5, padx=2, pady=2)
lecturer_btn.place(x=350, y=250)

register.mainloop()
