from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#89CC9A"
YELLOW = "#f7f5dd"

# Font
FONT_NAME = "Courier"

# Pomodoro periods
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

iteration = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global iteration
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    iteration = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global iteration
    global sessions_completed

    iteration += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if iteration % 2 != 0:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_seconds)
    elif iteration == 8:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_seconds)
    else:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds == 0:
        seconds = '00'
    elif seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text='✔' * int(iteration / 2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
title_label = Label(text='Timer')
title_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, 'bold'))
title_label.grid(row=0, column=1)

# Add image to the background
canvas = Canvas(width=256, height=256, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(128, 128, image=image)
timer_text = canvas.create_text(128, 160, text="00:00", fill="white", font=(FONT_NAME, 38, 'bold'))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text='Start', command=start_timer, font=(FONT_NAME, 15, 'bold'))
start_button.grid(row=2, column=0)

# Reset button
start_button = Button(text='Reset', command=reset_timer, font=(FONT_NAME, 15, 'bold'))
start_button.grid(row=2, column=2)

# Check marks
check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)


window.mainloop()
