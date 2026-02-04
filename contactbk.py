from tkinter import *
from tkinter import messagebox


def add_contact():
    if name_entry.get() == "":
        messagebox.showerror("Error", "Name is required")
        return

    with open("contacts.txt", "a") as f:
        f.write(name_entry.get() + "\n")

    messagebox.showinfo("Success", "Contact Added")
    clear_field()
    view_contacts()


def view_contacts():
    contact_list.delete(0, END)
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                contact_list.insert(END, line.strip())
    except FileNotFoundError:
        pass


def search_contact():
    contact_list.delete(0, END)
    found = False
    with open("contacts.txt", "r") as f:
        for line in f:
            if name_entry.get().lower() in line.lower():
                contact_list.insert(END, line.strip())
                found = True
    if not found:
        messagebox.showinfo("Info", "Contact Not Found")


def delete_contact():
    lines = []
    found = False

    with open("contacts.txt", "r") as f:
        lines = f.readlines()

    with open("contacts.txt", "w") as f:
        for line in lines:
            if line.strip().lower() != name_entry.get().lower():
                f.write(line)
            else:
                found = True

    if found:
        messagebox.showinfo("Deleted", "Contact Deleted")
    else:
        messagebox.showinfo("Info", "Contact Not Found")

    clear_field()
    view_contacts()


def clear_field():
    name_entry.delete(0, END)



root = Tk()
root.title("Contact Book")
root.geometry("500x350")


Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1)


Button(root, text="Add Contact", width=14, command=add_contact).grid(row=0, column=2)
Button(root, text="View Contacts", width=14, command=view_contacts).grid(row=1, column=2)
Button(root, text="Search Contact", width=14, command=search_contact).grid(row=2, column=2)
Button(root, text="Delete Contact", width=14, command=delete_contact).grid(row=3, column=2)
Button(root, text="Clear", width=14, command=clear_field).grid(row=4, column=2)


contact_list = Listbox(root, width=60)
contact_list.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

view_contacts()
root.mainloop()
