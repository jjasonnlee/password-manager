from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_pw.delete(0, END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_pw.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_web.get()
    password = entry_pw.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Is this correct?\nWebsite: {website}\nEmail: {email}\n"
                                                          f"Password: {password}")
        with open("data.txt", "a") as f:
            format = f"{website} | {email} | {password}\n"
            f.write(format)
            entry_web.delete(0, END)
            entry_pw.delete(0, END)
            entry_web.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_png)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "jjasonnlee2411@gmail.com")

entry_pw = Entry(width=18)
entry_pw.grid(column=1, row=3)

button_password = Button(text="Generate password", command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=33, command=save)
button_add.grid(column=1, row=4, columnspan=2)











window.mainloop()