import tkinter

reps = 0
time = None


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(1200)
        label.config(text="Break", fg="#DF0C36")
    elif reps % 2 == 0:
        countdown(300)
        label.config(text="Break", fg="#DC8899")
    else:
        countdown(1500)
        label.config(text="Work", fg="#9bdeac")

    checkmark["text"] = int(reps / 2) * "✔"


def countdown(count):
    # To change an attribute of a something inside the canvas, we need to use canvas.itemconfig() and pass in the
    # variable inside of canvas we want to change, then state the attribute of that variable that should be changed
    minutes = int(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    # window.after() sets a cool down of the time specified (in this case 1000ms meaning 1 second)
    # Its similar to import time but its directly built-in inside tkinter
    if count >= 0:
        global time
        time = window.after(1000, countdown, count - 1)
    else:
        start_timer()


def reset_timer():
    global reps
    reps = 0
    checkmark["text"] = ""
    label.config(text="Timer", fg="#9bdeac")
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")


window = tkinter.Tk()
window.title("Pomodoro")
# In window.config we can change the color of the background of our window by saying bg="#some hex code"
window.config(padx=100, pady=50, bg="#f7f5dd")

# To set the colour of our text, we need to use fg (foreground) rather than using bg (background)
label = tkinter.Label(text="Timer", bg="#f7f5dd", fg="#9bdeac", font=("Courier", 35))
label.grid(column=1, row=0)

start = tkinter.Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

checkmark = tkinter.Label(text="", fg="#9bdeac", bg="#f7f5dd")
checkmark.grid(column=1, row=3)

# To set the background to be a tomato image, we need to create a Canvas and provide it the width and height we want
# Normally the width and height of the canvas is the same as the image we want
# Similar to setting the background in window.config, we can also set the bg color for our canvas
# After we change the bg of our canvas, we can still see a thin white border across the canvas, to remove it we use the
# highlightthickness attribute
canvas = tkinter.Canvas(width=200, height=223, bg="#f7f5dd", highlightthickness=0)
# After creating the canvas we need to save the image in a variable by using PhotoImage()
tomato_image = tkinter.PhotoImage(file="tomato.png")
# Now we can create_image on the canvas we have created by providing the x, y coordinates and the image name
canvas.create_image(100, 111, image=tomato_image)
# We can make labels in canvas using create_text and provide it the x, y coordinates and the text
# Furthermore, we could also provide the font type, fill (color)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 30, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
