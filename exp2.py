import tkinter as tk
from tkinter import messagebox, simpledialog, StringVar


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")
        self.root.geometry("400x650+400+100")
        self.root.resizable(False, False)

        self.task_list = []

        # Top bar heading
        self.heading = tk.Label(root, text="ALL TASKS", font="arial 20 bold", fg="white", bg="#32405b")
        self.heading.pack(pady=10)

        # Entry frame for new task
        self.frame = tk.Frame(root, width=400, height=50, bg="white")
        self.frame.pack(pady=(10, 0))

        self.task_var = StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25, font="arial 20", bd=0)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_entry.focus()

        # Listbox frame
        self.frame1 = tk.Frame(root, bd=3, width=400, height=280, bg="#32405b")
        self.frame1.pack(pady=(10, 0))

        self.listbox = tk.Listbox(self.frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white",
                                  cursor="hand2", selectbackground="#5a95ff")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

        self.scrollbar = tk.Scrollbar(self.frame1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Add button (moved above the update button)
        self.add_button = tk.Button(root, text="ADD", font="arial 20 bold", width=10, bg="#5a95ff", fg="#fff",
                                    bd=0, command=self.add_task)
        self.add_button.pack(pady=10)

        # Update and Delete buttons
        self.update_button = tk.Button(root, text="UPDATE", font="arial 15", bg="#ffbb33", command=self.update_task)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(root, text="DELETE", font="arial 15", bg="salmon", command=self.delete_task)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_var.get()
        if task != "":
            self.task_list.append(task)
            self.update_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            current_task = self.task_list[selected_index]
            new_task = simpledialog.askstring("Update Task", "Edit your task:", initialvalue=current_task)
            if new_task:
                self.task_list[selected_index] = new_task
                self.update_listbox()
        except IndexError:
            messagebox.showwarning("Update Task", "Select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.task_list.pop(selected_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.task_list:
            self.listbox.insert(tk.END, task)  # Add tasks to the listbox


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
