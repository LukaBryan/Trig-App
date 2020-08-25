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
img = PhotoImage(file="kinghom.gif")  # Import image
canvas.create_image(500, 500, image=img)  # Creates triangle Graphic
window.resizable(False, False)  # Stop the ability for the window to be resized


Hyp = Entry(window, fg="Black", bg="#FFFFFF", width="10", font=("arial", 20))  # Entry box for the H length on triangle
HypLabel = Label(window, text="H = ", bg="white", font=("arial", 24))
Hyp.place(relx=0.8, rely=0.08, anchor=CENTER)
HypLabel.place(relx=0.6, rely=0.08, anchor=CENTER)

Opp = Entry(window, fg="Black", bg="#FFFFFF", width="10", font=("arial", 20))

Adj = Entry(window, fg="Black", bg="#FFFFFF", width="10", font=("arial", 20))

window.title("Trig App")  # Sets window name
###canvas.configure(bg="grey50")
canvas.pack()
window.mainloop()
