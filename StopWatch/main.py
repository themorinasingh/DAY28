from tkinter import *
import math

#COLORS
BLACK = "#181C14"
WHITE = "#FCFAEE"


current_secs = 0
timer = None

#TODO to create functionality for start, stop and reset
def start_function():
    global current_secs, timer
    current_secs += 1
    minutes = math.floor(current_secs / 60)
    if minutes < 10:
        minutes = f"0{minutes}"

    secs = current_secs % 60

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfigure(canvas_text, text=f"{minutes}:{secs}")
    timer = window.after(1000, start_function)

def stop_function():
    global current_secs
    window.after_cancel(timer)
    minutes = math.floor(current_secs / 60)

    if minutes < 10:
        minutes = f"0{minutes}"

    secs = current_secs % 60

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfigure(canvas_text, text=f"{minutes}:{secs}")

def reset_function():
    window.after_cancel(timer)
    global current_secs
    current_secs = 0
    canvas.itemconfigure(canvas_text, text=f"00:00")

#ToDo GUI Setup
window = Tk()
window.config(padx=100,pady=50, bg=BLACK)
window.title("StopWatch")

#todo create a label
label = Label()
label.config(text="Stopwatch",fg=WHITE,bg=BLACK, font=("Courier", 40, "italic") )
label.grid(row=0 , column=1 )

#TODO setup the canvas
canvas = Canvas( highlightthickness=0)
watch_image = PhotoImage(file="watch.png")
canvas.create_image(140, 100, image=watch_image)
canvas_text = canvas.create_text(140, 100, text="00:00", fill=BLACK ,font=("Courier", 30, "bold"))
canvas.grid(row=1 , column= 1, pady = 20)

#TODO create 3 buttons, start, stop, reset
start_button = Button()
start_button.config(text="Start", highlightbackground=BLACK, bg=WHITE, font=("Courier", 15, "normal"))
start_button.config(command=start_function)
start_button.grid(row=2 , column=0 )

stop_button = Button()
stop_button.config(text="Stop", highlightbackground=BLACK, bg=WHITE, font=("Courier", 15, "normal"))
stop_button.config(command=stop_function)
stop_button.grid(row= 2, column= 1)

reset_button = Button()
reset_button.config(text="Reset", highlightbackground=BLACK, bg=WHITE, font=("Courier", 15, "normal"))
reset_button.config(command=reset_function)
reset_button.grid(row= 2, column= 2 )


window.mainloop()