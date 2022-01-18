from tkinter import Tk, Label, Button, Entry

window = Tk()

window.title("Hello World")
window.minsize(width=800, height=600)

# label
label = Label(text="Hello World", font=("Roboto", 24, "bold"))
label.pack()

# Button
def button_clicked():
    new_text = input.get()
    label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry()
input.pack()

window.mainloop()