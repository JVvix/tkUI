from tkinter import *
from os import *

root = Tk()
root.geometry = "200x100"
root.title("Faye's User Interface")

def run_timer():
    system("python3 C:\\Users\\fly\\src\\timerpy\\timer.py")

def run_to_do():
    system("python3 C:\\Users\\fly\\src\\tkToDo\\tkToDo.py")

introdution = Label(root, text="This is Faye's Program Launchers").grid(row=0)
instructions = Label(root, text="Please press the buttons below to run the programs.").grid(row=3)
timer_button = Button(root, text="TIMER.PY", command=run_timer).grid(row=5)
to_do_button = Button(root, text="TO_DO_LIST.PY", command=run_to_do).grid(row=7)

root.mainloop()
