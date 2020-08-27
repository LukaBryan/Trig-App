from tkinter import *
from math import *

DegEntry = 0
HypEntry = 0
ObEntry = 0
AjEntry = 0


# Functions
def trig():
    Answer = "bruh"
    DegEntry = 0
    HypEntry = 0
    ObEntry = 0
    AjEntry = 0
    if not Deg.get():
        print("Deg has no value")
    else:
        DegEntry = 1
        print(Deg.get())
        Deg1 = int(Deg.get())
        if Deg1 < 1.5708:
            print("you cant do that")
            Deg.delete(0, END)
    if not Hyp.get():
        print("Hyp has no value")
    else:
        HypEntry = 1
        Hyp1 = int(Hyp.get())
        print(Hyp.get())
    if not Ob.get():
        print("Ob has no value")
    else:
        ObEntry = 1
        Ob1 = int(Ob.get())
        print(Ob.get())
    if not Aj.get():
        print("Ad has no value")
    else:
        AjEntry = 1
        print(Aj.get())
        Aj1 = int(Aj.get())
    if DegEntry == 1 and HypEntry == 1 or ObEntry == 1 and DegEntry == 1:
        print("sin")
        if DegEntry == 1 and HypEntry:
            Answer = Hyp1 / sin(Deg1)
        if DegEntry == 1 and ObEntry == 1:
            Answer = Ob1 * sin(Deg1)
        print(Answer)
    if DegEntry == 1 and HypEntry == 1 or AjEntry == 1 and DegEntry == 1:
        print("cos")
        if DegEntry == 1 and HypEntry:
            Answer = Hyp1 / cos(Deg1)
        if DegEntry == 1 and ObEntry == 1:
            Answer = Aj1 * cos(Deg1)
        print(Answer)
    if DegEntry == 1 and ObEntry == 1 or AjEntry == 1 and DegEntry == 1:
        print("tan")
        if DegEntry == 1 and HypEntry:
            Answer = Aj1 / cos(Deg1)
        if DegEntry == 1 and ObEntry == 1:
            Answer = Ob1 * cos(Deg1)
        print(Answer)
    if ObEntry == 1 and HypEntry == 1 or ObEntry == 1 and AjEntry == 1 or HypEntry == 1 and AjEntry == 1:
        print("py")
        if ObEntry == 1 and HypEntry == 1:
            Answer = int(sqrt(Ob1 ** 2 - Hyp1 ** 2))
            print(Answer)
        if AjEntry == 1 and HypEntry == 1:
            Answer = int(sqrt(Aj1 ** 2 - Hyp1 ** 2))
            print(Answer)
        if ObEntry == 1 and AjEntry == 1:
            Answer = int(sqrt(Ob1 ** 2 + Aj1 ** 2))
            print(Answer)
    Ans = Label(text=str(Answer))
    Ans.pack()


# Tkinter Things
window = Tk()
canvas = Canvas(window, width=1000, height=900)
img = PhotoImage(file="triangle.gif")
canvas.create_image(0, -150, anchor=NW, image=img)  # Creates triangle Graphic
Hyp = Entry(window, fg="Black", bg="#FFFFFF", width="20")
Hyp.pack()
Hyp.place(x=500, y=400)
Deg = Entry(fg="Black", bg="#FFFFFF", width="20")
Deg.pack()
Deg.place(x=590, y=700)
Aj = Entry(fg="Black", bg="#FFFFFF", width="20")
Aj.pack()
Aj.place(x=400, y=800)
Ob = Entry(fg="Black", bg="#FFFFFF", width="20")
Ob.pack()
Ob.place(x=10, y=400)
Adv = Button(fg="black", bg="#FFFFFF", width="20", text="Continue", command=trig)
Adv.pack()
Adv.place(x=20, y=20)
canvas.pack()
canvas.configure(bg="#F98E1D")
window.resizable(False, False)
window.title("Trig App")
window.mainloop()
