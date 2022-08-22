from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_clicked():
    global REPS
    window.after_cancel(TIMER)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    REPS = 0
    set_count_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global REPS
    REPS += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if REPS == 8:
        count_down(long_break_time)
        timer_label.config(text="Long Break", fg=RED)
        REPS = 0
    elif REPS%2 == 0:
        count_down(short_break_time)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_time)
        timer_label.config(text="Work Time", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER

    count_min = math.floor(count/60)
    count_sec = (count%60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1, count_down, count - 1)
    else:
        start_clicked()
        mark = ""
        for x in range(math.floor(REPS/2)):
            mark += "✔"
        set_count_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
timer_label.grid(row=0, column = 1)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="start", command=start_clicked, highlightbackground=YELLOW, highlightthickness=0)
start_button.grid(row=3,column=0)

reset_button = Button(text="reset", command=reset_clicked, highlightbackground=YELLOW, highlightthickness=0)
reset_button.grid(row=3,column=3)

set_count_label = Label(bg=YELLOW, fg=GREEN)
set_count_label.grid(row=4,column=1)

window.mainloop()