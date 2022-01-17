from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

#Constants
PINK = "#e2979c"
RED = "#e74c3c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# Timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(countdown_label, text="00:00")
    title_label.config(text="Pomodoro Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    
# Timer mechanism
def start_timer():
    global reps
    reps = reps + 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work")

# Countdown mechanism
def count_down(count):
    
    count_min = math.floor(count/60)
    count_second = count % 60
    if count_min == 0:
        count_min = "00"
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(countdown_label, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        

# UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Title Label

title_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 60), text="Pomodoro Timer")
title_label.grid(row=0, column=1)

# canvas

canvas = Canvas(width=800, height=600, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro-tomato.png")
canvas.create_image(400, 300, image=tomato_image)
countdown_label = canvas.create_text(400, 300, text="00:00", font=(FONT_NAME, 100), fill="white")
canvas.grid(row=1, column=1)

# Start button
start_button = Button(
    text="Start", 
    bg=RED, 
    fg="black", 
    font=(FONT_NAME, 30), 
    highlightthickness=0, 
    command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(
    text="Reset", 
    bg=RED, 
    fg="black", 
    font=(FONT_NAME, 30), 
    highlightthickness=0,
    command=reset_timer)
reset_button.grid(row=2, column=2)

# check marks
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
check_marks.grid(row=3, column=1)

window.mainloop()