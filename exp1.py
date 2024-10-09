import tkinter as tk
from tkinter import messagebox


# Function for numeric operations
def perform_numeric():
    def calculate_numeric():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            operation = numeric_var.get()

            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
            elif operation == "Modulo":
                result = num1 % num2
            elif operation == "Power":
                result = num1 ** num2

            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    numeric_window = tk.Toplevel()
    numeric_window.title("Numeric Calculator")
    numeric_window.configure(bg="#f0f0f0")

    tk.Label(numeric_window, text="Enter first number:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_num1 = tk.Entry(numeric_window, font=("Arial", 14), width=10)
    entry_num1.pack(pady=5)

    tk.Label(numeric_window, text="Enter second number:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_num2 = tk.Entry(numeric_window, font=("Arial", 14), width=10)
    entry_num2.pack(pady=5)

    numeric_var = tk.StringVar(numeric_window)
    numeric_var.set("Addition")

    operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo", "Power"]
    tk.OptionMenu(numeric_window, numeric_var, *operations).pack(pady=10)

    tk.Button(numeric_window, text="Calculate", font=("Arial", 14), command=calculate_numeric, bg="#1e90ff",
              fg="white").pack(pady=10)

    result_label = tk.Label(numeric_window, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
    result_label.pack(pady=10)


# Function for logical operations
def perform_logical():
    def calculate_logical():
        a = entry_a.get()
        b = entry_b.get()
        operation = logical_var.get()

        if operation == "AND":
            result = "1" if a == '1' and b == '1' else "0"
        elif operation == "OR":
            result = "1" if a == '1' or b == '1' else "0"

        result_label.config(text=f"Result: {result}")

    logical_window = tk.Toplevel()
    logical_window.title("Logical Calculator")
    logical_window.configure(bg="#f0f0f0")

    tk.Label(logical_window, text="Enter 1st statement value (0/1):", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_a = tk.Entry(logical_window, font=("Arial", 14), width=10)
    entry_a.pack(pady=5)

    tk.Label(logical_window, text="Enter 2nd statement value (0/1):", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_b = tk.Entry(logical_window, font=("Arial", 14), width=10)
    entry_b.pack(pady=5)

    logical_var = tk.StringVar(logical_window)
    logical_var.set("AND")

    operations = ["AND", "OR"]
    tk.OptionMenu(logical_window, logical_var, *operations).pack(pady=10)

    tk.Button(logical_window, text="Calculate", font=("Arial", 14), command=calculate_logical, bg="#1e90ff",
              fg="white").pack(pady=10)

    result_label = tk.Label(logical_window, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
    result_label.pack(pady=10)


# Function for bitwise operations
def perform_bitwise():
    def calculate_bitwise():
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            operation = bitwise_var.get()

            if operation == "&":
                result = a & b
            elif operation == "|":
                result = a | b
            elif operation == "^":
                result = a ^ b
            elif operation == "~":
                result = ~a
            elif operation == "<<":
                result = a << b
            elif operation == ">>":
                result = a >> b

            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    bitwise_window = tk.Toplevel()
    bitwise_window.title("Bitwise Calculator")
    bitwise_window.configure(bg="#f0f0f0")

    tk.Label(bitwise_window, text="Enter first number:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_a = tk.Entry(bitwise_window, font=("Arial", 14), width=10)
    entry_a.pack(pady=5)

    tk.Label(bitwise_window, text="Enter second number:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    entry_b = tk.Entry(bitwise_window, font=("Arial", 14), width=10)
    entry_b.pack(pady=5)

    bitwise_var = tk.StringVar(bitwise_window)
    bitwise_var.set("&")

    operations = ["&", "|", "^", "~", "<<", ">>"]
    tk.OptionMenu(bitwise_window, bitwise_var, *operations).pack(pady=10)

    tk.Button(bitwise_window, text="Calculate", font=("Arial", 14), command=calculate_bitwise, bg="#1e90ff",
              fg="white").pack(pady=10)

    result_label = tk.Label(bitwise_window, text="Result: ", font=("Arial", 14), bg="#f0f0f0")
    result_label.pack(pady=10)


# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#f5f5f5")

# Welcome label
tk.Label(root, text="Welcome to the Calculator!", font=("Arial", 16), bg="#f5f5f5").pack(pady=20)

# Buttons for choices
tk.Button(root, text="Numeric Operations", font=("Arial", 14), command=perform_numeric, bg="#1e90ff", fg="white").pack(
    pady=10)
tk.Button(root, text="Logical Operations", font=("Arial", 14), command=perform_logical, bg="#32cd32", fg="white").pack(
    pady=10)
tk.Button(root, text="Bitwise Operations", font=("Arial", 14), command=perform_bitwise, bg="#ffa500", fg="white").pack(
    pady=10)
tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit, bg="#ff6347", fg="white").pack(pady=10)

# Start the GUI
root.mainloop()
