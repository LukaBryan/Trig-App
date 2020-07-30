from tkinter import *
from math import *

#Functions
def trig():
    Deg=int(Deg1.get())
    H=int(Hyp.get())
    Rad = radians(Deg)
    O = H * sin(Rad)
    print(O)
    Deg1.delete(0, 'end')
    Hyp.delete(0, 'end')

# Tkinter Things
window = Tk()
canvas = Canvas(window, width=1000, height=900)
img = PhotoImage(file="triangle.gif")
canvas.create_image(0, -150, anchor=NW, image=img)  # Creates triangle Graphic
Hyp = Entry(fg="Black", bg="#FFFFFF", width="20")
Hyp.pack()
Hyp.place(x=500, y=400)
Deg1 = Entry(fg="Black", bg="#FFFFFF", width="20")
Deg1.pack()
Deg1.place(x=590, y=700)
Adv = Button(fg="black", bg="#FFFFFF", width="20", text="Continue", command=trig)
Adv.pack()
Adv.place(x=20,y=20)
canvas.pack()
canvas.configure(bg="#FFFFFF")
window.resizable(False, False)
window.mainloop()
