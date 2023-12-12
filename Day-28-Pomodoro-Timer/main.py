from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_ticker.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    if reps > 8:
        return 0

    if reps % 8 == 0:
        count_down(10)
        label_timer.config(text="Break", fg=RED)
        label_ticker.config(text="✔" * int(reps / 2))

    elif reps % 2 == 0:
        count_down(5)
        label_timer.config(text="Break", fg=PINK)
        label_ticker.config(text="✔" * int(reps / 2))

    else:
        count_down(10)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    seconds = int(count % 60)
    minutes = int(count / 60)
    global timer

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    time = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()


# --------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)  # will create space around image

# Label Timer
label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label_timer.grid(column=1, row=0)

# Label thick
label_ticker = Label(text=" ", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_ticker.grid(column=1, row=3)

# Button Reset
button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

# canvas layout
canvas = Canvas(width=200, height=224, bg=YELLOW)  # size of canvas according to size of img
tomato_img = PhotoImage(file="tomato.png")  # PhotoImage is tkinter widget used to read images and put it as a variable
# proces of creating image with source and x,y position of image's middle
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Button Start
button_start = Button(text="Start", command=start_count, highlightthickness=0)
button_start.grid(column=0, row=2)

window.mainloop()
