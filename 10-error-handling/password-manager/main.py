from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# func to generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# func to save password to text file data.txt
def save_password():
    
    # get entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { 
        website: {
            "email": email,
            "password": password
        }
    }
    # data = f"{website} | {email} | {password}\n"
    
    # validate if fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            # add to file
            with open("data.json", "r") as file:
                data = json.load(file) 
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:  
            # clear entries
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")
    
    

# Creating a new window and configurations
window = Tk()
window.title("Password Manager/Generator")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=400, height=300, highlightthickness=0)
mypass_img = PhotoImage(file="mypass.png")
canvas.create_image(200, 150, image=mypass_img)
canvas.grid(row=0, column=0, columnspan=3)

# Website Label and Entry
webiste_label = Label(text="Website: ", font=("Roboto", 24, "bold"), fg="white")
webiste_label.grid(row=1, column=0)

website_entry = Entry(width=40, font=("Roboto", 24), fg="white")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email label and entry
email_label = Label(text="Email: ", fg="white", font=("Roboto", 24, "bold"))
email_label.grid(row=2, column=0)

email_entry = Entry(width=40, font=("Roboto", 24), fg="white")
# email_entry.insert(0, "test@example.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password label and entry
password_label = Label(text="Password: ", fg="white", font=("Roboto", 24, "bold"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=40, font=("Roboto", 24), fg="white")
password_entry.grid(row=3, column=1, columnspan=2)

# generate button
generate_button = Button(text="Generate", font=("Roboto", 24, "bold"), width=40, command=generate_password)
generate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# add to file button
add_button = Button(text="Add to file", font=("Roboto", 24, "bold"), width=40, command=save_password)
add_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)


window.mainloop()
