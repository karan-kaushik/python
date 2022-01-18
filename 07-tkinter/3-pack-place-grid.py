from tkinter import Tk, Label, Button, Entry

window = Tk()

window.title("Hello World")
window.minsize(width=800, height=600)

# label
label = Label(text="Hello World", font=("Roboto", 24, "bold"))
# label.pack()
# label.place(x=100, y=100)
label.grid(row=0, column=0)

# Button
def button_clicked():
    new_text = input.get()
    label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

# Entry
input = Entry(text="Type here")
# input.pack()
input.grid(row=2, column=2)

window.mainloop()