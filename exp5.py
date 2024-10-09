import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        self.contacts = {}
        self.deleted_contacts = {}

        # Title Label
        self.title_label = tk.Label(self.root, text="Contact Book", font=('Helvetica', 20, 'bold'))
        self.title_label.pack(pady=10)

        # Contact List
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10, font=('Helvetica', 12))
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind('<Double-1>', self.view_contact)

        # Buttons
        self.add_contact_button = tk.Button(self.root, text="Add Contact", font=('Helvetica', 12),
                                            command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.update_contact_button = tk.Button(self.root, text="Update Contact", font=('Helvetica', 12),
                                               command=self.update_contact)
        self.update_contact_button.pack(side=tk.LEFT, padx=10)

        self.delete_contact_button = tk.Button(self.root, text="Delete Contact", font=('Helvetica', 12),
                                               command=self.delete_contact)
        self.delete_contact_button.pack(side=tk.LEFT, padx=10)

        self.search_contact_button = tk.Button(self.root, text="Search Contact", font=('Helvetica', 12),
                                               command=self.search_contact)
        self.search_contact_button.pack(side=tk.LEFT, padx=10)

        self.view_history_button = tk.Button(self.root, text="View History", font=('Helvetica', 12),
                                             command=self.view_history)
        self.view_history_button.pack(pady=10)

        self.refresh_contact_list()

    def refresh_contact_list(self):
        """ Refresh the contact listbox with updated contacts """
        self.contact_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name} - {details['phone']}")

    def add_contact(self):
        """ Add a new contact """
        name = simpledialog.askstring("Input", "Enter Name:")
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
            return

        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        if name and phone:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            self.refresh_contact_list()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contact(self, event):
        """ View the details of the selected contact """
        selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
        name = selected_contact.split(" - ")[0]
        details = self.contacts.get(name)

        messagebox.showinfo("Contact Details",
                            f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")

    def search_contact(self):
        """ Search for a contact by name or phone number """
        search_term = simpledialog.askstring("Search", "Enter Name or Phone Number:")
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                messagebox.showinfo("Search Result",
                                    f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        """ Update the selected contact """
        try:
            selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
            name = selected_contact.split(" - ")[0]

            new_phone = simpledialog.askstring("Update", "Enter New Phone Number:",
                                               initialvalue=self.contacts[name]['phone'])
            new_email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=self.contacts[name]['email'])
            new_address = simpledialog.askstring("Update", "Enter New Address:",
                                                 initialvalue=self.contacts[name]['address'])

            if new_phone:
                self.contacts[name]['phone'] = new_phone
            if new_email:
                self.contacts[name]['email'] = new_email
            if new_address:
                self.contacts[name]['address'] = new_address

            self.refresh_contact_list()
        except IndexError:
            messagebox.showwarning("Update", "Select a contact to update.")

    def delete_contact(self):
        """ Delete the selected contact and add to history """
        try:
            selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
            name = selected_contact.split(" - ")[0]
            delete_date = datetime.now()

            # Add the deleted contact to the history with timestamp
            self.deleted_contacts[name] = {
                'details': self.contacts[name],
                'delete_date': delete_date
            }
            del self.contacts[name]
            self.refresh_contact_list()
        except IndexError:
            messagebox.showwarning("Delete", "Select a contact to delete.")

    def view_history(self):
        """ View deleted contacts and provide an option to restore them within 10 days """
        history_window = tk.Toplevel(self.root)
        history_window.title("Deleted Contacts History")
        history_window.geometry("400x300")

        history_listbox = tk.Listbox(history_window, width=50, height=10, font=('Helvetica', 12))
        history_listbox.pack(pady=10)

        restore_button = tk.Button(history_window, text="Restore Contact", font=('Helvetica', 12),
                                   command=lambda: self.restore_contact(history_listbox))
        restore_button.pack(pady=10)

        for name, info in self.deleted_contacts.items():
            if datetime.now() - info['delete_date'] <= timedelta(days=10):
                history_listbox.insert(tk.END, f"{name} - {info['details']['phone']}")

    def restore_contact(self, listbox):
        """ Restore a deleted contact if within 10 days """
        try:
            selected_contact = listbox.get(listbox.curselection())
            name = selected_contact.split(" - ")[0]

            # Restore the contact from deleted contacts
            if name in self.deleted_contacts and datetime.now() - self.deleted_contacts[name]['delete_date'] <= timedelta(days=10):
                self.contacts[name] = self.deleted_contacts[name]['details']
                del self.deleted_contacts[name]
                self.refresh_contact_list()
                messagebox.showinfo("Restored", f"{name}'s contact has been restored.")
            else:
                messagebox.showerror("Error", "Cannot restore this contact.")
        except IndexError:
            messagebox.showwarning("Restore", "Select a contact to restore.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
