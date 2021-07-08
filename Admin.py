from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


administrator = Tk()
administrator.title("Admin Account")
administrator.config(bg="grey")
administrator.geometry("1250x500")

# declaring text variables
name = StringVar()
person_id = StringVar()
surname = StringVar()
password = StringVar()
privilege = StringVar()
phone = StringVar()


def add_data(table):
    frame = Frame(administrator, width=400, height=320, bg="black")
    frame.place(x=100, y=150)
    l1 = Label(frame, text="username", width=8)
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

    l4 = Label(frame, text="Phone", width=11)
    l4.place(x=50, y=150)
    e4 = Entry(frame, textvariable=phone, width=25)
    e4.place(x=170, y=150)

    l5 = Label(frame, text="Password", width=8)
    l5.place(x=50, y=190)
    e5 = Entry(frame, textvariable=password, width=25)
    e5.place(x=170, y=190)

    def insert_data():
        try:
            nonlocal e1, e2, e3, e4, e5
            if variable.get() == "Student":
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                cursor.execute("INSERT INTO users(id_number, username, surname, phone, password, privilege) VALUES(%s, %s, %s, %s,%s, 'Student')", (id_number, username, s_name, number, p_word))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Student"))
                messagebox.showinfo("Success", "Student Registered")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                frame.destroy()
            elif variable.get() == "Lectures":
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                cursor.execute(
                    "INSERT INTO users(id_number, username, surname, phone, password, privilege) VALUES(%s, %s, %s, %s,%s, 'Lecturer')",
                    (id_number, username, s_name, number, p_word))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Lecturer"))
                messagebox.showinfo("Success", "Lecturer Registered")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                frame.destroy()
            elif variable.get() == "Staff":
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                cursor.execute(
                    "INSERT INTO users(id_number, username, surname, phone, password, privilege) VALUES(%s, %s, %s, %s,%s, 'Staff')",
                    (id_number, username, s_name, number, p_word))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Staff"))
                messagebox.showinfo("Success", "Staff member Registered")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                frame.destroy()
            elif variable.get() == "Visitors":
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                cursor.execute(
                    "INSERT INTO users(id_number, username, surname, phone, password, privilege) VALUES(%s, %s, %s, %s,%s, 'Visitor')",
                    (id_number, username, s_name, number, p_word))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Visitor"))
                messagebox.showinfo("Success", "Visitor Registered")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                frame.destroy()
        finally:
            pass

    submit_btn = Button(frame, text="submit", command=insert_data)
    submit_btn.configure(bg='white', fg='black')
    submit_btn.place(x=100, y=280)
    cancel_btn = Button(frame, text="cancel", command=frame.destroy)
    cancel_btn.configure(bg='white', fg='black')
    cancel_btn.place(x=240, y=280)


def destroy(table):
    selected_item = table.selection()[0]
    uid = table.item(selected_item)['values'][0]
    remove = "DELETE FROM users WHERE id_number = %s"
    selected_data = (uid,)
    cursor.execute(remove, selected_data)
    conn.commit()
    table.delete(selected_item)
    messagebox.showinfo("Success", "User Data Removed")


heading = Label(administrator, text="Administrator", font=("Courier", 26, "italic"), bg="grey")
heading.place(x=210, y=10)

options = ['Select....', 'Student', 'Lectures', 'Staff', 'Visitors']
variable = StringVar(administrator)
variable.set(options[0])
privilege_list = OptionMenu(administrator, variable, *options)
privilege_list.place(x=450, y=80)
privilege_label = Label(administrator, text="Please Select Privilege to change: ", bg='grey')
privilege_label.place(x=150, y=90)

frame1 = Frame(administrator, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=300)
frame1.place(x=25, y=190)

table = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.pack()


table.heading(1, text="ID Number")
table.heading(2, text="Username")
table.heading(3, text="Surname")
table.heading(4, text="Phone Number")
table.heading(5, text="Password")
table.heading(6, text="privilege")

conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='lifechoices_login', auth_plugin='mysql_native_password')
cursor = conn.cursor()
sql = "SELECT id_number, username,surname,phone ,password, privilege FROM users"
cursor.execute(sql)

rows = cursor.fetchall()
total = cursor.rowcount

for i in rows:
    table.insert("", 'end', values=i)


def selected_data(table):
    cur_item = table.focus()
    value = table.item(cur_item, "values")
    frame = Frame(administrator, width=400, height=320, bg="black")
    frame.place(x=100, y=150)
    l1 = Label(frame, text="username", width=8)
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

    l4 = Label(frame, text="Phone", width=11)
    l4.place(x=50, y=150)
    e4 = Entry(frame, textvariable=phone, width=25)
    e4.place(x=170, y=150)

    l5 = Label(frame, text="Password", width=8)
    l5.place(x=50, y=190)
    e5 = Entry(frame, textvariable=password, width=25)
    e5.place(x=170, y=190)

    e6 = Label(frame, text="Privilege", width=8)
    e6.place(x=50, y=230)
    e6 = Entry(frame, textvariable=privilege, width=25)
    e6.place(x=170, y=230)

    e1.insert(0, value[1])# username
    e2.insert(0, value[0])# id number
    e3.insert(0, value[2])#  surname
    e4.insert(0, value[3])# phone
    e5.insert(0, value[4])# password
    e6.insert(0, value[5])# prilivege


    def update_data():
        nonlocal e1, e2, e3, e4, e5, e6, cur_item, value
        username = name.get()
        id_number = person_id.get()
        p_word = password.get()
        s_name = surname.get()
        number = phone.get()
        role = privilege.get()
        table.item(cur_item, value=(id_number, username, s_name, number, p_word, role))
        cursor.execute('UPDATE users SET WHERE id_number=%s, username=%s, surname=%s, privilege=%s) ', (id_number,
                                                                                                       username, p_word, number, role))

        conn.commit()
        messagebox.showinfo("Success", "Students Updated")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        frame.destroy()

    submit_btn = Button(frame, text="submit", command=update_data)
    submit_btn.configure(bg='white', fg='black')
    submit_btn.place(x=100, y=280)
    cancel_btn = Button(frame, text="cancel", command=frame.destroy)
    cancel_btn.configure(bg='white', fg='black')
    cancel_btn.place(x=240, y=280)


delete_entries = Button(administrator, text="delete", bg="white", fg="black", command=lambda: destroy(table))
delete_entries.place(x=50, y=450)
insert_entries = Button(administrator, text="insert", bg="white", fg="black", command=lambda: add_data(table))
insert_entries.place(x=150, y=450)
update_entries = Button(administrator, text="Update", bg="white", fg="black", command=lambda: selected_data(table))
update_entries.place(x=250, y=450)
administrator.mainloop()
