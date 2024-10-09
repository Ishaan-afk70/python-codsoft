import tkinter as tk
import string
import random
import pyperclip


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_box.get())

    passwordField.delete(0, tk.END)  # Clear previous password

    if choice.get() == 1:
        password = ''.join(random.sample(small_alphabets, password_length))
    elif choice.get() == 2:
        password = ''.join(random.sample(small_alphabets + capital_alphabets, password_length))
    elif choice.get() == 3:
        password = ''.join(random.sample(all_characters, password_length))
    else:
        password = ''

    passwordField.insert(0, password)


def copy_password():
    pyperclip.copy(passwordField.get())


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x400")
root.config(bg='#2b2b2b')
root.resizable(False, False)

choice = tk.IntVar()

# Styling
font_style = ('Verdana', 12, 'bold')
title_font = ('Verdana', 18, 'bold')

# Title Label
title_label = tk.Label(root, text='Password Generator', font=title_font, bg='#2b2b2b', fg='white')
title_label.pack(pady=20)

# Radio Buttons for Password Strength
radio_frame = tk.Frame(root, bg='#2b2b2b')
radio_frame.pack(pady=10)

weak_radio = tk.Radiobutton(radio_frame, text='Weak', value=1, variable=choice, font=font_style, bg='#2b2b2b', fg='#ffcc00')
weak_radio.grid(row=0, column=0, padx=10)

medium_radio = tk.Radiobutton(radio_frame, text='Medium', value=2, variable=choice, font=font_style, bg='#2b2b2b', fg='#00ccff')
medium_radio.grid(row=0, column=1, padx=10)

strong_radio = tk.Radiobutton(radio_frame, text='Strong', value=3, variable=choice, font=font_style, bg='#2b2b2b', fg='#00ff00')
strong_radio.grid(row=0, column=2, padx=10)

# Password Length Section
length_label = tk.Label(root, text="Password Length:", font=font_style, bg='#2b2b2b', fg='white')
length_label.pack(pady=10)

length_box = tk.Spinbox(root, from_=5, to_=18, width=5, font=font_style, justify='center')
length_box.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text='Generate Password', font=font_style, bg='#1f1f1f', fg='white', width=20, command=generator)
generate_button.pack(pady=20)

# Password Display Entry Field
passwordField = tk.Entry(root, width=25, bd=2, font=font_style, justify='center', fg='black')
passwordField.pack(pady=10)

# Copy Button
copy_button = tk.Button(root, text='Copy Password', font=font_style, bg='#1f1f1f', fg='white', width=20, command=copy_password)
copy_button.pack(pady=20)

root.mainloop()
