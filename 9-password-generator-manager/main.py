from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button


# Creating a new window and configurations
window = Tk()
window.title("Password Manager/Generator")
window.config(padx=20, pady=20)

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
email_entry.grid(row=2, column=1, columnspan=2)

# Password label and entry
password_label = Label(text="Password: ", fg="white", font=("Roboto", 24, "bold"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=40, font=("Roboto", 24), fg="white")
password_entry.grid(row=3, column=1, columnspan=2)

# generate button
generate_button = Button(text="Generate", font=("Roboto", 24, "bold"), width=40)
generate_button.grid(row=4, column=0, columnspan=3)

# add to file button
add_button = Button(text="Add to file", font=("Roboto", 24, "bold"), width=40)
add_button.grid(row=5, column=0, columnspan=3)

window.mainloop()