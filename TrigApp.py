from tkinter import *
from math import *

DegEntry = 0
HypEntry = 0
ObEntry = 0
AjEntry = 0

# Functions


# Tkinter Set up
window = Tk()
canvas = Canvas(window, width=1000, height=1000)  # Defines how big the window can be
img = PhotoImage(file="Updatedgraphic.gif")  # Import image
canvas.create_image(500, 500, image=img)  # Creates triangle Graphic
window.resizable(False, False)  # Stop the ability for the window to be resized
Hyp = Entry(window, fg="Black", bg="#FFFFFF", width="25")  # Entry box for the H leng on triangle
Hyp.pack()
Hyp.place(x=775, y=50)
window.title("Trig App")  # Sets window name
canvas.pack()
window.mainloop()
