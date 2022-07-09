from tkinter import *
from tkinter import messagebox
import random

import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def create_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pass_entry.insert(0, password)


def search_website():
    website_name = web_entry.get()
    try:
        with open("data.json") as n_data:
            data = json.load(n_data)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="file not found")
    else:
        if website in data:
            email_name = data[website_name]["email"]
            password_name = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"email: {email_name}\n password: {password_name}")
        else:
            messagebox.showinfo(title="error", message="website not found")

        # if len(website_name) == 0:
        #     messagebox.showinfo(title="oops", message="you have to insert a website")
        # else:
        #     try:
        #
        #     except KeyError:
        #         messagebox.showinfo(title="ooops", message="name not found!")


def save():
    password_char = pass_entry.get()
    user_email = user_entry.get()
    website_name = web_entry.get()

    new_data = {
        website_name: {
            "email": user_email,
            "password": password_char,
        }
    }

    if len(password_char) == 0 or len(website_name) == 0:
        messagebox.showinfo(title="oops", message="you should not leave any field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            pass_entry.delete(0, END)
            web_entry.delete(0, END)

window = Tk()
window.title("password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=2, row=1)

website = Label(text="website:", font=("arial", 14))
website.grid(column=1, row=2)


username = Label(text="E-mail/ username:", font=("arial", 14))
username.grid(column=1, row=3)

password = Label(text="password:", font=("arial", 14))
password.grid(column=1, row=4)

gen_password = Button(text="generate password", command=create_password)
gen_password.grid(column=3, row=4)

add_password = Button(text="add", command=save)
add_password.config(width=43)
add_password.grid(column=2, row=5, columnspan=2)

web_entry = Entry()
web_entry.config(width=30)
web_entry.focus()
web_entry.grid(column=2, row=2)

search = Button(text="search", command=search_website)
search.config(width=13)
search.grid(column=3, row=2)

user_entry = Entry()
user_entry.config(width=50)
user_entry.insert(0, "gadson@gmail.com")
user_entry.grid(column=2, row=3, columnspan=2)


pass_entry = Entry()
pass_entry.config(width=32)
pass_entry.grid(column=2, row=4)







window.mainloop()