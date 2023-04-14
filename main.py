from tkinter import *

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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer/ label
timer_label = Label(text='Timer')
timer_label.config(bg=YELLOW, fg=GREEN, font=('Times new roman', 50, 'bold'))
timer_label.grid(row=0, column=1)

# Add image to the background
canvas = Canvas(width=256, height=256, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(128, 128, image=image)
canvas.create_text(128, 150, text="00:00", fill="white", font=(FONT_NAME, 38, 'bold'))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text='Start')
start_button.grid(row=2, column=0)

# Reset button
start_button = Button(text='Reset')
start_button.grid(row=2, column=2)

# Check marks
check_marks = Label(text='✔', bg=YELLOW)
check_marks.grid(row=3, column=1)


window.mainloop()
