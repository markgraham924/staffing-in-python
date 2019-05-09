from tkinter import *
import csv

def submit():
    #functions for changing staff
    def newUser():
        newUserWindow = Tk()
        window.title("New User")
    def viewUser():
        print("view")
    def editUser():
        print("edit")
    def deleteUser():
        print("delete")

    #admin window
    window = Tk()
    username = UsernameInp.get()
    window.title(username + " is logged on!")

    lbl = Label(window, text="Staffing", font=("Arial Bold", 50)).grid(row=0, column=0, sticky=W)
    lbl = Label(window, text="Admin", font=("Arial Bold", 24)).grid(row=1, column=0, sticky=W)
    btn = Button(window, command=newUser, text="New User", font=("Arial Bold", 24))
    btn.grid(row=2, column=0)
    btn = Button(window, command=viewUser, text="View User", font=("Arial Bold", 24))
    btn.grid(row=3, column=0)
    btn = Button(window, command=editUser, text="Edit User", font=("Arial Bold", 24))
    btn.grid(row=4, column=0)
    btn = Button(window, command=deleteUser, text="Delete User", font=("Arial Bold", 24))
    btn.grid(row=5, column=0)


window = Tk()
window.title("Staffing")

lbl = Label(window, text="Staffing", font=("Arial Bold", 50)).grid(row=0, column=0, sticky=W)
lbl = Label(window, text="Login", font=("Arial Bold", 24)).grid(row=1, column=0, sticky=W)
lbl = Label(window, text="Username:", font=("Arial Bold", 20)).grid(row=2, column=0, sticky=W)
UsernameInp = Entry(window,width=10)
UsernameInp.grid(row=2, column=1)
lbl = Label(window, text="Pasword:", font=("Arial Bold", 20)).grid(row=3, column=0, sticky=W)
PaswordInp = Entry(window,width=10)
PaswordInp.grid(row=3, column=1)

btn = Button(window, command=submit, text="Submit", font=("Arial Bold", 20))
btn.grid(row=4, column=1)
window.mainloop()
