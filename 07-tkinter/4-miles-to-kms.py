from tkinter import Tk, Label, Button, Entry

def miles_to_kms():
    km_value = float(mile_input.get()) * 1.609
    km_output.config(text=round(km_value, 2))

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)
# window.minsize(width=400, height=300)

mile_input = Entry(width=10, text="Enter miles here")
mile_input.grid(row=1, column=0)

mile_label = Label(text="Miles")
mile_label.grid(row=1, column=1)

center_label = Label(text="is equal to")
center_label.grid(row=2, column=0)

km_output = Label(text="")
km_output.grid(row=3, column=0)

km_label = Label(text="KMs")
km_label.grid(row=3, column=1)

calculate_button = Button(text="Calculate", command=miles_to_kms)
calculate_button.grid(row=4, column=0)


window.mainloop()