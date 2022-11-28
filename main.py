from tkinter import *
from tkinter import messagebox
from datetime import datetime

root = Tk()

root.title('Age Calculator')
root. geometry ("580x300")
root.configure(bg='orange')
root.resizable(height=False, width=False)


def age():
    if my_entry.get():
        #Get the current year
        current_year = datetime.now().year

        #Calculate age
        your_age = current_year - int(my_entry.get())

        #Show age in message box
        messagebox.showinfo('Your Age', f'Your age is {your_age-1}-{your_age}')
    else:
        #Showw error
        messagebox.showerror('Error', 'You forgot enter your age')

my_label = Label(root, text='Enter your year born', font=('Helvetica', 24), bg='orange', fg='yellow')
my_label.pack(pady=20)

my_entry = Entry(root, font=('Helvetica', 18), bg='darkorange', fg='yellow')
my_entry.pack(pady=10)

my_button = Button(root, text='Calculate Age!', font=('Helvetica', 18), bg='darkorange', fg='yellow', command=age)
my_button.pack(pady=20)

root.mainloop()