import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gener_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbol + password_letter
    random.shuffle(password_list)

    password = "".join(password_list) # will join each item in list with symbol "" will return string

    entry_pass.delete(0, tk.END)  # delete if something is in pass entry box
    entry_pass.insert(0, password)
    pyperclip.copy(password) # will copy password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def print_data():
    web_text = entry_web.get()
    email_text = entry_email.get()
    pass_text = entry_pass.get()

    new_data = {
        web_text: {
            "email": email_text,
            "password": pass_text,
        }
    }

    if len(web_text) == 0 or len(email_text) == 0 or len(pass_text) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web_text, message=f"These are the details entered: \nEmail: {email_text} "
                                                               f"\nPassword: {pass_text} \n Is it ok to save?")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as data_file:   #open json file
                    data = json.load(data_file)  #load data from file
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:  # open file again in write mode
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)   # update data with new data
                with open(file="data.json", mode="w") as data_file:   #open file again in write mode
                    json.dump(data, data_file, indent=4)   #overwrite old data with updated data
            finally:
                entry_web.delete(0, tk.END)
                entry_pass.delete(0, tk.END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web_text = entry_web.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(web_text, "No Data File Found.")
    else:
        if web_text in data:
            email = data[web_text]["email"]
            password = data[web_text]["password"]
            messagebox.showinfo(web_text, f"Email: {email}\nPassword: {password}")
            # info = data[web_text]
            # messagebox.showinfo(web_text, f"Email: {info['email']}\nPassword: {info['password']}")
            entry_web.delete(0, tk.END)
        else:
            messagebox.showinfo(web_text, "No details for the website exists.")



# ---------------------------- UI SETUP ------------------------------- #
# setting new window
window = tk.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# canvas set up to show logo image
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label website
label_web = tk.Label(text="Website:")
label_web.grid(row=1, column=0)


#Label email/username
label_email = tk.Label(text="Email/Username:")
label_email.grid(row=2, column=0)

#Label password
label_pass = tk.Label(text="Password:")
label_pass.grid(row=3, column=0)

#Entry web
entry_web = tk.Entry(width=32)
entry_web.focus()   # cursor will be placed to this box
entry_web.grid(row=1, column=1)

#Entry email/username
entry_email = tk.Entry(width=50)
#print(entry_email.get())
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "your.email@gmail.com")

#Entry password
entry_pass = tk.Entry(width=32)
entry_pass.grid(row=3, column=1)

#Button Password
button_pass = tk.Button(text="Generate Password", command=gener_pass)
button_pass.grid(row=3, column=2)

#Button Add
button_add = tk.Button(text="Add")
button_add.config(width=40, command=print_data)
button_add.grid(row=4, column=1, columnspan=2)

#Button Search
button_search = tk.Button(text="Search", width=14, command=find_password)
button_search.grid(row=1, column=2)

window.mainloop()
