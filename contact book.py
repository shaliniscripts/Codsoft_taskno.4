import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append({'Name': name, 'Phone': phone})
        messagebox.showinfo("Success", "Contact added successfully!")
        show_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Missing Info", "Please enter both Name and Phone Number.")

def show_contacts():
    contact_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        contact_listbox.insert(tk.END, f"{i+1}. {contact['Name']} - {contact['Phone']}")

def search_contact():
    search_text = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        if search_text in contact['Name'].lower() or search_text in contact['Phone']:
            contact_listbox.insert(tk.END, f"{i+1}. {contact['Name']} - {contact['Phone']}")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        show_contacts()
        messagebox.showinfo("Deleted", "Contact deleted.")
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")

def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        name = name_entry.get()
        phone = phone_entry.get()
        if name and phone:
            contacts[index] = {'Name': name, 'Phone': phone}
            show_contacts()
            clear_entries()
            messagebox.showinfo("Updated", "Contact updated.")
        else:
            messagebox.showwarning("Missing Info", "Enter both Name and Phone to update.")
    else:
        messagebox.showwarning("No Selection", "Select a contact to update.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")
root.config(bg="lightblue")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Selected Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Selected Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search (by Name or Phone)").pack()
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

contact_listbox = tk.Listbox(root, width=45)
contact_listbox.pack(pady=10)

tk.Button(root, text="Show All Contacts", command=show_contacts).pack(pady=5)

root.mainloop()
