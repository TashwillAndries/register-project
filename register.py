from tkinter import *
from tkinter import messagebox

register =Tk()


def student():
    frame1.config(bg="grey")
    password_entry.config(state="normal")
    id_number_entry.config(state="normal")
    phone_number_entry.config(state="normal")
    surname_entry.config(state="normal")
    user_entry.config(state="normal")


register.title("Register Form")
register.geometry("500x500")
register.config(bg="grey")
heading = Label(register, text="Register Form", font=("Courier", 26, "italic"), bg="grey")
heading.place(x=120, y=10)
student_btn = Button(register, text="Student", bg="white", fg="black", command=student)
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

sign_up = Button(frame1, text="Register", bg="white", fg="black")
sign_up.place(x=200, y=250)

register.mainloop()
