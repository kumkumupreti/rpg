from tkinter import *
import tkinter as tk
import time
import pyperclip  # Required for copying text to clipboard
import string

def generate_password():
    length = int(length_entry.get())

    # Ensure the password length is between 12 and 32 characters
    if length < 12 or length > 32:
        error_label.config(text="Error: Password length must be between 12 and 32")
        return
    else:
        error_label.config(text="")

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation.replace(" ", "")

    password = ''

    seed = int(time.time())
    random_number = (seed * 9301 + 49297) % 233280
    for _ in range(length - 4):
        random_number = (random_number * 9301 + 49297) % 233280
        char_type = int(random_number / 233280 * 4)  # Choose a character type (0: lowercase, 1: uppercase, 2: number, 3: special character)
        if char_type == 0:
            password += lowercase_letters[int(random_number / 233280 * 26)]
        elif char_type == 1:
            password += uppercase_letters[int(random_number / 233280 * 26)]
        elif char_type == 2:
            password += numbers[int(random_number / 233280 * 10)]
        else:
            password += special_chars[int(random_number / 233280 * len(special_chars))]

    password = lowercase_letters[int(random_number / 233280 * 26)] +numbers[int(random_number / 233280 * 10)]+ password + special_chars[int(random_number / 233280 * len(special_chars))]+ uppercase_letters[int(random_number / 233280 * 26)]

    password_label.config(text="Generated Password: " + password)
    copy_button.config(state=tk.NORMAL)  # Enable the copy button after generating the password

def copy_password():
    generated_password = password_label.cget("text").split(": ")[1]  # Extract the generated password from the label
    pyperclip.copy(generated_password)  # Copy the password to clipboard

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("640x420")  # Set window size to 720x720

# Create a Canvas widget
canvas = Canvas(window, width=720, height=720)
canvas.pack()

# Load and set the background image
bgimg = tk.PhotoImage(file="password.png")
canvas.create_image(0, 0, image=bgimg, anchor="nw")

# Create a rounded rectangle shape
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

rounded_rectangle = create_rounded_rectangle(canvas, 160, 300, 480, 340, 20, fill="#5D9CEC")  # Adjust the coordinates and radius as needed

# Create the widgets
length_label = tk.Label(window, text="ENTER PASSWORD LENGTH BETWEEN(12-32):", font=("Helvetica", 14, "bold"), bg="#5D9CEC", fg="white")
length_label.place(x=140, y=50, width=330, height=30)  # Use place() method to specify the coordinates

length_entry = tk.Entry(window)
length_entry.place(x=260, y=96, width=90, height=35)  # Use place() method to specify the coordinates

generate_button = tk.Button(window, text="Generate", command=generate_password, bg="#FFC0CB", fg="black", font=("Helvetica", 12, "bold"), relief="flat", width=120, height=50)
generate_button.place(x=240, y=235, width=120, height=50)  # Use place() method to specify the coordinates and size

password_label = tk.Label(canvas, text="Generated Password: ", font=("Helvetica", 14, "bold"), bg="#5D9CEC", fg="white")
canvas.create_window(310, 317, window=password_label)  # Use create_window to place the label inside the rounded rectangle

copy_button = tk.Button(window, text="Copy Password", command=copy_password, state=tk.DISABLED)  # Initially disable the copy button
copy_button.place(x=240, y=360)  # Use place() method to specify the coordinates

error_label = tk.Label(window, text="", fg="red")
error_label.place(x=180, y=150)

# Run the main loop
window.mainloop()
