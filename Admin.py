from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


administrator = Tk()
administrator.title("Admin Account")
administrator.config(bg="grey")
administrator.geometry("680x500")

# declaring text variables
name = StringVar()
person_id = IntVar()
surname = StringVar()
password = IntVar()
phone = IntVar()


def add_data(table):
    frame = Frame(administrator, width=400, height=320, bg="black")
    frame.place(x=100, y=150)
    l1 = Label(frame, text="name", width=8)
    e1 = Entry(frame, textvariable=name, width=25)
    l1.place(x=50, y=30)
    e1.place(x=170, y=30)

    l2 = Label(frame, text="ID number", width=8)
    e2 = Entry(frame, textvariable=person_id, width=25)
    l2.place(x=50, y=70)
    e2.place(x=170, y=70)

    l3 = Label(frame, text="Surname", width=8)
    l3.place(x=50, y=110)
    e3 = Entry(frame, textvariable=surname, width=25)
    e3.place(x=170, y=110)

    l5 = Label(frame, text="Phone number", width=11)
    l5.place(x=50, y=150)
    e5 = Entry(frame, textvariable=phone, width=25)
    e5.place(x=170, y=150)
    e5.delete(0, END)

    l5 = Label(frame, text="Password", width=8)
    l5.place(x=50, y=190)
    e5 = Entry(frame, textvariable=password, width=25)
    e5.place(x=170, y=190)

    def insert_data():
        pass

    def destroy():
        pass

    submit_btn = Button(frame, text="submit", command=insert_data)
    submit_btn.configure(bg='white', fg='black')
    submit_btn.place(x=100, y=280)
    cancel_btn = Button(frame, text="cancel", command=destroy)
    cancel_btn.configure(bg='white', fg='black')
    cancel_btn.place(x=240, y=280)

heading = Label(administrator, text="Administrator", font=("Courier", 26, "italic"), bg="grey")
heading.place(x=210, y=10)

user_lbl = Label(administrator, text="Please enter username: ", bg="grey")
user_lbl.place(x=50, y=80)
user_entry = Entry(administrator)
user_entry.place(x=450, y=80)

frame1 = Frame(administrator, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=300)
frame1.place(x=25, y=190)

table = ttk.Treeview(frame1, columns=(1, 2, 3), show="headings")
table.pack()

table.heading(1, text="ID")
table.heading(2, text="Username")
table.heading(3, text="Surname")

conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='registration', auth_plugin='mysql_native_password')
cursor = conn.cursor()

sql = "SELECT id, student_name, student_surname FROM student"
cursor.execute(sql)

rows = cursor.fetchall()
total = cursor.rowcount

for i in rows:
    table.insert("", 'end', values=i)


def delete():
    pass


def insert():
    pass


delete_entries = Button(administrator, text="delete", bg="white", fg="black", command=delete)
delete_entries.place(x=50, y=450)
insert_entries = Button(administrator,text="insert", bg="white", fg="black", command=lambda: add_data(table))
insert_entries.place(x=150, y=450)
administrator.mainloop()
