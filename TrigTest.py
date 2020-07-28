from tkinter import *
from math import *

# Tkinter Things
window = Tk()
canvas = Canvas(window, width=1000, height=900)
img = PhotoImage(file="triangle.gif")
canvas.create_image(0, -150, anchor=NW, image=img)  # Creates tirangle Graphic
Hyp = Entry(fg="Black", bg="#FFFFFF", width="20")
Hyp.pack()
Hyp.place(x=500, y=400)
canvas.pack()
canvas.configure(bg="#FFFFFF")
window.mainloop()

# main Program
Deg = int(input("Input angle: "))
H = int(input("Input Length: "))
Rad = radians(Deg)
O = H * sin(Rad)
print(O)
