import tkinter as tk
from tkinter import ttk, messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []
 
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self.master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self.master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(self.master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(self.master)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(self.master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.contacts_tree = ttk.Treeview(self.master, columns=("Name", "Phone"))
        self.contacts_tree.heading("#0", text="ID")
        self.contacts_tree.heading("Name", text="Name")
        self.contacts_tree.heading("Phone", text="Phone")
        self.contacts_tree.grid(row=8, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=1, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        self.contacts_tree.delete(*self.contacts_tree.get_children())
        for idx, contact in enumerate(self.contacts, start=1):
            self.contacts_tree.insert("", "end", iid=idx, values=(contact["Name"], contact["Phone"]))

    def search_contact(self):
        query = self.search_entry.get().lower()
        found_contacts = [contact for contact in self.contacts if query in contact["Name"].lower() or query in contact["Phone"].lower()]

        self.contacts_tree.delete(*self.contacts_tree.get_children())
        for idx, contact in enumerate(found_contacts, start=1):
            self.contacts_tree.insert("", "end", iid=idx, values=(contact["Name"], contact["Phone"]))

    def update_contact(self):
        selected_contact_id = self.contacts_tree.selection()
        if selected_contact_id:
            selected_contact_id = int(selected_contact_id[0])
            selected_contact = self.contacts[selected_contact_id - 1]

            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone:
                selected_contact["Name"] = name
                selected_contact["Phone"] = phone
                selected_contact["Email"] = email
                selected_contact["Address"] = address
                self.clear_entries()
                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Error", "Name and Phone are required fields.")
        else:
            messagebox.showwarning("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_contact_id = self.contacts_tree.selection()
        if selected_contact_id:
            selected_contact_id = int(selected_contact_id[0])
            del self.contacts[selected_contact_id - 1]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Error", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
