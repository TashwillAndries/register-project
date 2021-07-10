from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


administrator = Tk()
administrator.title("Admin Account")
administrator.config(bg="#FF5733")
administrator.geometry("1250x900")


heading = Label(administrator, text="Administrator", font=("Courier", 26, "italic"), bg="#FF5733")
heading.place(x=520, y=10)
in_count = Label(administrator, text="Number of users logged in:", bg="#FF5733")
in_count.place(x=650, y=70)
in_number = Label(administrator, bg="white", width=10)
in_number.place(x=850, y=70)
out_count = Label(administrator, text="Number of users logged out:", bg="#FF5733")
out_count.place(x=650, y=100)
out_number = Label(administrator, bg="white", width=10)
out_number.place(x=850, y=100)



# declaring text variables
name = StringVar()
person_id = StringVar()
surname = StringVar()
password = StringVar()
privilege = StringVar()
phone = StringVar()
k_name = StringVar()
kin_phone = StringVar()


# outer functions for the inserting
def add_data(table):
    frame = Frame(administrator, width=400, height=420, bg="#C70039")
    frame.place(x=100, y=150)
    user_label = Label(frame, text="username", width=8, bg="#C70039")
    user_entry = Entry(frame, textvariable=name, width=25)
    user_label.place(x=50, y=30)
    user_entry.place(x=170, y=30)

    id_label = Label(frame, text="ID number", width=8, bg="#C70039")
    id_entry = Entry(frame, textvariable=person_id, width=25)
    id_label.place(x=50, y=70)
    id_entry.place(x=170, y=70)

    surname_label = Label(frame, text="Surname", width=8, bg="#C70039")
    surname_label.place(x=50, y=110)
    surname_entry = Entry(frame, textvariable=surname, width=25)
    surname_entry.place(x=170, y=110)

    phone_label = Label(frame, text="Phone", width=11, bg="#C70039")
    phone_label.place(x=50, y=150)
    phone_entry = Entry(frame, textvariable=phone, width=25)
    phone_entry.place(x=170, y=150)

    password_label = Label(frame, text="Password", width=8, bg="#C70039")
    password_label.place(x=50, y=190)
    password_entry = Entry(frame, textvariable=password, width=25)
    password_entry.place(x=170, y=190)

    # inserting data into the database from mysql
    def insert_data():
        try:
            nonlocal user_entry, id_entry, surname_entry, phone_entry, password_entry
            if variable.get() == "Student" and len(phone_entry.get()) == 11:
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                cursor.execute("INSERT INTO users(id_number, username, surname, phone, password, privilege) VALUES(%s, %s, %s, %s,%s, 'Student')", (id_number, username, s_name, number, p_word))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Student"))
                messagebox.showinfo("Success", "Student Registered")
                user_entry.delete(0, END)
                id_entry.delete(0, END)
                surname_entry.delete(0, END)
                phone_entry.delete(0, END)
                password_entry.delete(0, END)
                frame.destroy()
            else:
                messagebox.showerror("Error", "Too little digits in phone")

            if variable.get() == "Lectures" and len(phone_entry.get()) == 11:
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
                user_entry.delete(0, END)
                id_entry.delete(0, END)
                surname_entry.delete(0, END)
                phone_entry.delete(0, END)
                password_entry.delete(0, END)
                frame.destroy()
            else:
                messagebox.showerror("Error", "Too little digits in phone")

            if variable.get() == "Staff" and len(phone_entry.get()) == 11:
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
                user_entry.delete(0, END)
                id_entry.delete(0, END)
                surname_entry.delete(0, END)
                phone_entry.delete(0, END)
                password_entry.delete(0, END)
                frame.destroy()
                messagebox.showinfo("Success", "Staff member Registered")
            else:
                messagebox.showerror("Error", "Too little digits in phone")
        except ValueError:
            pass

    submit_btn = Button(frame, text="submit", command=insert_data, borderwidth=5, padx=2, pady=2)
    submit_btn.configure(bg="#F33A6A", fg='black')
    submit_btn.place(x=100, y=380)
    cancel_btn = Button(frame, text="cancel", command=frame.destroy, borderwidth=5, padx=2, pady=2)
    cancel_btn.configure(bg="#F33A6A", fg='black')
    cancel_btn.place(x=240, y=380)

# function to delete entries with visitor privilege
def insert_visitors(table):
    frame = Frame(administrator, width=400, height=420, bg="#C70039")
    frame.place(x=100, y=150)
    user_label = Label(frame, text="username", width=8, bg="#C70039")
    user_entry = Entry(frame, textvariable=name, width=25)
    user_label.place(x=50, y=30)
    user_entry.place(x=170, y=30)

    id_label = Label(frame, text="ID number", width=8, bg="#C70039")
    id_entry = Entry(frame, textvariable=person_id, width=25)
    id_label.place(x=50, y=70)
    id_entry.place(x=170, y=70)

    surname_label = Label(frame, text="Surname", width=8, bg="#C70039")
    surname_label.place(x=50, y=110)
    surname_entry = Entry(frame, textvariable=surname, width=25)
    surname_entry.place(x=170, y=110)

    phone_label = Label(frame, text="Phone", width=11, bg="#C70039")
    phone_label.place(x=50, y=150)
    phone_entry = Entry(frame, textvariable=phone, width=25)
    phone_entry.place(x=170, y=150)

    password_label = Label(frame, text="Password", width=8, bg="#C70039")
    password_label.place(x=50, y=190)
    password_entry = Entry(frame, textvariable=password, width=25)
    password_entry.place(x=170, y=190)

    kin_name = Label(frame, text="Next of kin name", width=15, bg="#C70039")
    kin_name.place(x=40, y=230)
    kin_entry = Entry(frame, textvariable=k_name, width=25)
    kin_entry.place(x=170, y=230)

    kin_number = Label(frame, text="Next of kin number", width=16, bg="#C70039")
    kin_number.place(x=35, y=270)
    number_entry = Entry(frame, textvariable=kin_phone, width=25)
    number_entry.place(x=170, y=270)

    def submit():
        try:
            nonlocal user_entry, id_entry, surname_entry, phone_entry, password_entry, kin_entry, number_entry
            if variable.get() == "Visitors":
                username = name.get()
                id_number = person_id.get()
                p_word = password.get()
                s_name = surname.get()
                number = phone.get()
                kin_name = k_name.get()
                kin_no = kin_phone.get()
                cursor.execute(
                        "INSERT INTO users(id_number, username, surname, phone, password,"
                        " privilege) VALUES(%s, %s, %s, %s,%s, 'Visitor')",
                        (id_number, username, s_name, number, p_word))
                cursor.execute("INSERT INTO kin(username,kin_name,phone_number) VALUE(%s, %s, %s)", (id_number, kin_name,
                                                                                                     kin_no))
                conn.commit()
                table.insert('', 'end', text='', values=(id_number, username, s_name, number, p_word, "Visitor"))
                messagebox.showinfo("Success", "Visitor Registered")
                user_entry.delete(0, END)
                id_entry.delete(0, END)
                surname_entry.delete(0, END)
                phone_entry.delete(0, END)
                password_entry.delete(0, END)
                kin_entry.delete(0, END)
                number_entry.delete(0, END)
                frame.destroy()
            else:
                messagebox.showerror("Error", "Please Select Visitor Privilege")
        finally:
            pass

    def cancel():
        user_entry.delete(0, END)
        id_entry.delete(0, END)
        surname_entry.delete(0, END)
        phone_entry.delete(0, END)
        password_entry.delete(0, END)
        kin_entry.delete(0, END)
        number_entry.delete(0, END)
        frame.destroy()

    submit_btn = Button(frame, text="submit", command=submit, borderwidth=5, padx=2, pady=2)
    submit_btn.configure(bg="#F33A6A", fg='black')
    submit_btn.place(x=100, y=380)
    cancel_btn = Button(frame, text="cancel", command=cancel, borderwidth=5, padx=2, pady=2)
    cancel_btn.configure(bg="#F33A6A", fg='black')
    cancel_btn.place(x=240, y=380)


# deleting selected data from the Treeview and the database
def destroy(table):
    selected_item = table.selection()[0]
    uid = table.item(selected_item)['values'][0]
    remove_log = "DELETE FROM log_times WHERE id_number = %s"
    remove = "DELETE FROM users WHERE id_number = %s"
    selected_data = (uid,)
    cursor.execute(remove_log, selected_data)
    cursor.execute(remove, selected_data)
    conn.commit()
    table.delete(selected_item)
    messagebox.showinfo("Success", "User Data Removed")

# deletes data from visitors and next of kin
def delete_visitor(table):
    selected_item = table.selection()[0]
    selection = table.item(selected_item)['values'][0]
    remove_log = "DELETE FROM log_times Where id_number = %s"
    remove_kin = "DELETE FROM kin WHERE username = %s"
    remove = "DELETE FROM users WHERE id_number = %s"
    selected_data = (selection,)
    cursor.execute(remove_log, selected_data)
    cursor.execute(remove_kin, selected_data)
    cursor.execute(remove, selected_data)
    conn.commit()
    table.delete(selected_item)
    messagebox.showinfo("Success", "User Data Removed")


# shows how many users logged in
def show_in():
    conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='lifechoices_login', auth_plugin='mysql_native_password')
    my_cursor = conn.cursor()
    my_cursor.execute("select sum(case when sign_in_time IS NOT NULL and sign_out_time IS NULL then 1 else 0 end) FROM log_times")
    amount = my_cursor.fetchone()[0]
    in_number.config(text=amount)

# shows How many users signed out
def show_out():
    conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='lifechoices_login', auth_plugin='mysql_native_password')
    my_cursor = conn.cursor()
    my_cursor.execute("select sum(case when sign_out_time IS NOT NULL then 1 else 0 end) FROM log_times")
    amount = my_cursor.fetchone()[0]
    out_number.config(text=amount)


options = ['Select....', 'Student', 'Lectures', 'Staff', 'Visitors']
variable = StringVar(administrator)
variable.set(options[0])
privilege_list = OptionMenu(administrator, variable, *options)
privilege_list.place(x=450, y=80)
privilege_label = Label(administrator, text="Please Select Privilege to change: ", bg='#FF5733')
privilege_label.place(x=150, y=90)

frame1 = Frame(administrator, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=300)
frame1.place(x=25, y=150)

table = ttk.Treeview(frame1, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.pack()

# table on headings
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

# loop that inserts the data from mysql table into treeview
for i in rows:
    table.insert("", 'end', values=i)

# creating second Treeview
frame2 = Frame(administrator, bg="grey", highlightbackground="white", highlightthickness=5, width=450, height=150)
frame2.place(x=25, y=390)
table_two = ttk.Treeview(frame2, columns=(1, 2, 3, 4, 5), show="headings")
table_two.pack()

# headings for the the send table
table_two.heading(1, text="Position")
table_two.heading(2, text="ID Number")
table_two.heading(3, text="Sign-in Time")
table_two.heading(4, text="Sign-in Date")
table_two.heading(5, text="Sign-out Time")

conn = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='lifechoices_login', auth_plugin='mysql_native_password')
cursor = conn.cursor()
sql = "SELECT id, id_number, sign_in_time, sign_in_date, sign_out_time FROM log_times"
cursor.execute(sql)

rows = cursor.fetchall()
total = cursor.rowcount


# loops over database and insert into the Treeview
for i in rows:
    table_two.insert("", 'end', values=i)


def selected_data(table):
    cur_item = table.focus()
    value = table.item(cur_item, "values")
    frame = Frame(administrator, width=400, height=320, bg="#C70039")
    frame.place(x=100, y=150)
    username_label = Label(frame, text="username", width=8, bg="#C70039")
    username_entry = Entry(frame, textvariable=name, width=25)
    username_label.place(x=50, y=30)
    username_entry.place(x=170, y=30)

    surname_label = Label(frame, text="Surname", width=8, bg="#C70039")
    surname_label.place(x=50, y=70)
    surname_entry = Entry(frame, textvariable=surname, width=25)
    surname_entry.place(x=170, y=70)

    phone_no = Label(frame, text="Phone", width=11, bg="#C70039")
    phone_no.place(x=50, y=110)
    phone_entry = Entry(frame, textvariable=phone, width=25)
    phone_entry.place(x=170, y=110)

    password_label = Label(frame, text="Password", width=8, bg="#C70039")
    password_label.place(x=50, y=150)
    password_entry = Entry(frame, textvariable=password, width=25)
    password_entry.place(x=170, y=150)

    privilege_lbl = Label(frame, text="Privilege", width=8, bg="#C70039")
    privilege_lbl.place(x=50, y=190)
    privilege_entry = Entry(frame, textvariable=privilege, width=25)
    privilege_entry.place(x=170, y=190)

    username_entry.insert(0, value[1])
    surname_entry.insert(0, value[2])
    phone_entry.insert(0, value[3])
    password_entry.insert(0, value[4])
    privilege_entry.insert(0, value[5])

    def update_data():
        nonlocal username_entry, surname_entry, phone_entry, password_entry, privilege_entry, cur_item, value
        username = name.get()
        p_word = password.get()
        s_name = surname.get()
        number = phone.get()
        role = privilege.get()
        table.item(cur_item, value=(value[0], username, s_name, number, p_word, role))
        cursor.execute("UPDATE users SET username=%s, surname=%s,phone=%s,password=%s, privilege=%s WHERE id_number=%s",
                       (username, s_name, number, p_word, role, value[0]))

        conn.commit()
        messagebox.showinfo("Success", "User Updated")
        username_entry.delete(0, END)
        surname_entry.delete(0, END)
        phone_entry.delete(0, END)
        password_entry.delete(0, END)
        privilege_entry.delete(0, END)
        frame.destroy()

    def cancel():
        username_entry.delete(0, END)
        surname_entry.delete(0, END)
        phone_entry.delete(0, END)
        password_entry.delete(0, END)
        privilege_entry.delete(0, END)
        frame.destroy()

    submit_btn = Button(frame, text="submit", command=update_data, borderwidth=5, padx=2, pady=2)
    submit_btn.configure(bg="#F33A6A", fg='black')
    submit_btn.place(x=100, y=280)
    cancel_btn = Button(frame, text="cancel",command=cancel, borderwidth=5, padx=2, pady=2)
    cancel_btn.configure(bg="#F33A6A", fg='black')
    cancel_btn.place(x=240, y=280)


def log_out():
    administrator.destroy()
    import main


delete_entries = Button(administrator, text="delete", bg="#F33A6A", fg="black", command=lambda: destroy(table), borderwidth=5, padx=2, pady=2)
delete_entries.place(x=50, y=650)
insert_entries = Button(administrator, text="insert", bg="#F33A6A", fg="black", command=lambda: add_data(table), borderwidth=5, padx=2, pady=2)
insert_entries.place(x=150, y=650)
update_entries = Button(administrator, text="Update", bg="#F33A6A", fg="black", command=lambda: selected_data(table), borderwidth=5, padx=2, pady=2)
update_entries.place(x=250, y=650)
users_in = Button(administrator, text="Sign-in Count", bg="#F33A6A", fg="black", command=show_in, borderwidth=5, padx=2, pady=2)
users_in.place(x=350, y=650)
users_out = Button(administrator, text="Sign-out Count", bg="#F33A6A", fg="black", command=show_out, borderwidth=5, padx=2, pady=2)
users_out.place(x=490, y=650)
log_out = Button(administrator, text="Log-out", bg="#F33A6A", fg="black", command=log_out, borderwidth=5, padx=2, pady=2)
log_out.place(x=940, y=650)
delete_visitors = Button(administrator, text="Delete Visitors", bg="#F33A6A", fg="black", command=lambda: delete_visitor(table), borderwidth=5, padx=2, pady=2)
delete_visitors.place(x=640, y=650)
insert_visitor = Button(administrator, text="Insert Visitors", bg="#F33A6A", fg="black", command=lambda: insert_visitors(table), borderwidth=5, padx=2, pady=2)
insert_visitor.place(x=790, y=650)
administrator.mainloop()
