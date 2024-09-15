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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfigure(canvas_text, text="00:00")
    reps = 0
    label.config(text="Timer")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps,checkmarks
    reps += 1

    WORK_SECS = WORK_MIN * 60
    SHORT_BREAK_SECS = SHORT_BREAK_MIN * 60
    LONG_BREAK_SECS = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(LONG_BREAK_SECS)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SECS)
        label.config(text="Break", fg=PINK)

    else:
        count_down(WORK_SECS)
        label.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if  count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        num_marks = math.floor(reps/2)
        for _ in range(num_marks):
            marks += "✅"
        check_mark.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#making a canvas
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

#ext="✅"

#challenge part
#making a label
label = Label()
label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"),bg=YELLOW)
label.grid(row=0, column=1)

#creating the checkmark
check_mark = Label()
check_mark.config(bg=YELLOW, pady=10)
check_mark.grid(row=3, column=1)

#creating buttons
start_button = Button()
start_button.config(text="Start",bg=YELLOW, font=(FONT_NAME,15,"normal"), highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button()
reset_button.config(text="Reset",bg=YELLOW, font=(FONT_NAME,15,"normal"), highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2,column=2)


window.mainloop()