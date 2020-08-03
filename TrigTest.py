from tkinter import *
from math import *

#Functions
def trig():
    Deg1.insert(0,"")
    Deg=int(Deg1.get())
    if not Deg:
        print("Please Enter a Angle for the program to continue")
    HY=int(Hyp.get())
    OB=int(Ob.get())
    AD=int(Ad.get())
    print(HY)
    print(OB)
    print(AD)
    print(Deg)
    Rad = radians(Deg)
    if HY>1:
        print(HY*sin(Deg))
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
Ad = Entry(fg="Black", bg="#FFFFFF", width="20")
Ad.pack()
Ad.place(x=400, y=800)
Ob = Entry(fg="Black", bg="#FFFFFF", width="20")
Ob.pack()
Ob.place(x=10, y=400)
Adv = Button(fg="black", bg="#FFFFFF", width="20", text="Continue", command=trig)
Adv.pack()
Adv.place(x=20,y=20)
canvas.pack()
canvas.configure(bg="#F98E1D")
window.resizable(False, False)
window.mainloop()
