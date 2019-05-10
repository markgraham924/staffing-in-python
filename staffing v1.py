from tkinter import *
import csv

def submit():
    #functions for changing staff
    def newUser():
        def submitUser():
            #fecthing the varaibles from tkinter
            forename = ForenameInp.get()
            surname = SurnameInp.get()
            dob = DOBInp.get()
            gender = GenderInp.get()
            emp = EmpInp.get()
            with open('emps.csv', mode='a') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow([forename, surname, dob, gender, emp])

        newUserWindow = Tk()
        newUserWindow.title("New User")
        lbl = Label(newUserWindow, text="Staffing", font=("Arial Bold", 50)).grid(row=0, column=0, sticky=W)
        lbl = Label(newUserWindow, text="New User", font=("Arial Bold", 24)).grid(row=1, column=0, sticky=W)
        lbl = Label(newUserWindow, text="Forename:", font=("Arial Bold", 20)).grid(row=2, column=0, sticky=W)
        ForenameInp = Entry(newUserWindow,width=10)
        ForenameInp.grid(row=2, column=1)
        lbl = Label(newUserWindow, text="Surname:", font=("Arial Bold", 20)).grid(row=3, column=0, sticky=W)
        SurnameInp = Entry(newUserWindow,width=10)
        SurnameInp.grid(row=3, column=1)
        lbl = Label(newUserWindow, text="DOB:", font=("Arial Bold", 20)).grid(row=4, column=0, sticky=W)
        DOBInp = Entry(newUserWindow,width=10)
        DOBInp.grid(row=4, column=1)
        lbl = Label(newUserWindow, text="Gender (m/f):", font=("Arial Bold", 20)).grid(row=5, column=0, sticky=W)
        GenderInp = Entry(newUserWindow,width=10)
        GenderInp.grid(row=5, column=1)
        lbl = Label(newUserWindow, text="Emp No.:", font=("Arial Bold", 20)).grid(row=6, column=0, sticky=W)
        EmpInp = Entry(newUserWindow,width=10)
        EmpInp.grid(row=6, column=1)
        btn = Button(newUserWindow, command=submitUser, text="Submit", font=("Arial", 18))
        btn.grid(row=7, column=1)

        
    def viewUser():
        viewUserWindow = Tk()
        viewUserWindow.title("View User")
        lbl = Label(viewUserWindow, text="Staffing", font=("Arial Bold", 50)).grid(row=0, column=0, sticky=W)
        lbl = Label(viewUserWindow, text="View User", font=("Arial Bold", 24)).grid(row=1, column=0, sticky=W)

        
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
