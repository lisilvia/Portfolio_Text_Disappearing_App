from tkinter import *

FONT_NAME = "Montserrat"
timer = 5
not_typing = False


def countdown():
    global not_typing
    if not_typing:
        global timer
        timer -= 1
    if timer <= 4:
        text_area.config(fg="#303030")
    if timer <= 3:
        text_area.config(fg="#494B50")
    if timer <= 2:
        text_area.config(fg="#5F6971")
    if timer <= 1:
        text_area.config(fg="#C6C6C6")
    if timer <= 0:
        delete_text()
        not_typing = False
    window.after(1000, countdown)


def reset_timer():
    global timer
    timer = 5


def action(event=None):
    global not_typing
    if not_typing:
        reset_timer()
    else:
        not_typing = True
        countdown()


def delete_text():
    text_area.delete('1.0', END)
    reset_timer()


window = Tk()
window.title("Disappearing Text Writing App")
window.minsize(100, 30)


text_area = Text(window, width=100, height=30, font=(FONT_NAME, 16), fg="#303030", highlightthickness=0, padx=40, pady=40)
text_area.config(spacing2=8)
text_area.insert(END, "Start typing here...")
text_area.bind("<FocusIn>", lambda args: text_area.delete('1.0', END))
text_area.bind("<Key>", action)
text_area.pack()

window.mainloop()
