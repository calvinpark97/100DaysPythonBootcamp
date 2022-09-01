from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_password():
    rand_password = []
    nr_letters=random.randint(7,10)
    nr_numbers=random.randint(3,5)
    nr_symbols=random.randint(3,4)
    for letter in range(nr_letters):
        rand_password += random.choice(letters)
    for number in range(nr_numbers):
        rand_password += random.choice(numbers)
    for symbol in range(nr_symbols):
        rand_password += random.choice(symbols)

    random.shuffle(rand_password)
    rand_password = "".join(rand_password)
    password_text.insert(0, string=rand_password)
    pyperclip.copy(rand_password)

def search_info():
    website = website_text.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="ERROR", message=f"No details for {website} exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_text.get()
    username = username_text.get()
    password = password_text.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Blank fields found")
    else:
        try:
            with open("passwords.json", 'r') as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_text.delete(0,END)
            username_text.delete(0,END)
            password_text.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0, column=1)

#website_label
website_label = Label(text="website: ")
website_label.grid(row=1, column=0)
#website text box
website_text = Entry(width=20)
website_text.grid(row=1, column=1)
website_text.focus()
#Website search button
search_button = Button(text="Search", command=search_info, width=14)
search_button.grid(row=1, column=2)
#email/username label
username_label = Label(text="email/username: ")
username_label.grid(row=2, column=0)
#email/username textbox
username_text = Entry(width=35)
username_text.grid(row=2, column=1, columnspan=2, sticky="EW")
#password label
password_label = Label(text="password: ")
password_label.grid(row=3, column=0)
#password textbox
password_text = Entry(width=21)
password_text.grid(row=3, column=1, sticky="W")
#generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
#add to text file button
add_button = Button(text="Add", width=36, command=add_to_file)
add_button.grid(row=4,column=1, columnspan=2, sticky="EW")


window.mainloop()