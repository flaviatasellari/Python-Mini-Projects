from tkinter import *

root = Tk()
root.geometry ('550x550')
root.config (bg = 'Salmon')
root.title ('Contact Book')
root.resizable (0,0)

contacts = [
    ['Madison White', '0876633501'],
    ['Jessica Smith', '2064778321'],
    ['Aaron Williams', '3557905042'],
    ['Joana Miller', '9067342299'],
    ['Betty Johnson', '5660312510'],
    ['David Allen' , '2398703011'],
    ['Carl Bell' , '7488763493'],
    ]

person_name = StringVar()
person_phone = StringVar()

frame = Frame(root)
frame.pack (padx = 40, side = LEFT)
scroll = Scrollbar (frame, orient = VERTICAL)
select = Listbox (frame, yscrollcommand=scroll.set, height = 15)
scroll.config (command = select.yview)
scroll.pack (side = RIGHT, fill = Y)
select.pack (side = LEFT, fill = BOTH, expand = 1)


# FUNCTIONS TO PERFORM DIFFERENT OPERATIONS

def Selected():
    return int (select.curselection()[0])

# Function to view the selected contact
def view_contact():
    name, phone = contacts[Selected()]
    person_name.set(name)
    person_phone.set(phone)

# Function to edit the selected contact
def edit_contact():
    contacts[Selected()] = [person_name.get(), person_phone.get()]
    Select_set()

# Function to add a new contact
def add_contact():
    contacts.append ([person_name.get(), person_phone.get()])
    Select_set()

# Function to delete the selected contact
def delete_contact():
    del contacts[Selected()]
    Select_set()

# Function to reset 
def to_reset():
    person_name.set('')
    person_phone.set('')

# Function to leave the program  
def to_exit():
    root.destroy()


def Select_set() :
    contacts.sort()
    select.delete (0, END)

    for name, phone in contacts :
        select.insert (END, name)
Select_set()


# Create buttons
Label (root, text = 'Name', font = 'arial 13 bold', bg = 'PeachPuff').place(x = 70,  y= 40)
Entry (root, textvariable = person_name).place(x = 150, y = 40)
Label (root, text = 'Phone number', font ='arial 13 bold', bg = 'PeachPuff').place(x = 70, y = 90)
Entry (root, textvariable = person_phone).place(x = 210, y = 90)

Button (root, text = "VIEW", font = '"times new roman" 13 bold', bg = 'brown', command = view_contact).place(x = 380, y = 150)
Button (root, text = "EDIT", font = '"times new roman" 13 bold', bg = 'brown', command = edit_contact).place(x = 380, y = 210)
Button (root, text = "ADD", font = '"times new roman" 13 bold', bg = 'brown', command = add_contact).place(x = 380, y = 270)
Button (root, text = "DELETE", font = '"times new roman" 13 bold', bg = 'brown', command = delete_contact).place(x = 380, y = 330)
Button (root,text = "RESET", font = '"times new roman" 13 bold', bg = 'brown', command = to_reset).place(x = 380, y = 390)
Button (root,text = "EXIT", font = '"times new roman" 13 bold', bg = 'red', command = to_exit).place(x = 250, y = 470)

root.mainloop()
  
