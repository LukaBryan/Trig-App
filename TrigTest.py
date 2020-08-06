from tkinter import *
from math import *
DegEntry=0
HypEntry=0
ObEntry=0
AdEntry=0

#Functions
def trig():
    func=0
    DegEntry=0
    HypEntry=0
    ObEntry=0
    AdEntry=0
    if not Deg1.get():
        print("Deg has no value")
    else:
        DegEntry=1
        print(Deg1.get())
    if not Hyp.get():
        print("Hyp has no value")
    else:
        HypEntry=1
        print(Hyp.get())
    if not Ob.get():
        print("Ob has no value")
    else:
        ObEntry=1
        print(Ob.get())
    if not Ad.get():
        print("Ad has no value")
    else:
        AdEntry=1
        print(Ad.get())
    if DegEntry==1 and HypEntry==1 or ObEntry==1 and DegEntry==1:
        print("sin")
    if DegEntry==1 and HypEntry==1 or AdEntry==1 and DegEntry==1:
        print("cos")
    if DegEntry==1 and ObEntry==1 or ObEntry==1 and DegEntry==1:
        print("tan")
    if  ObEntry==1 and HypEntry==1 or ObEntry==1 and AdEntry==1 or HypEntry==1 and AdEntry==1:
        print("py")
        if ObEntry==1 and HypEntry==1:
            print(sqrt(int(Ob.get())**2 * int(Hyp.get())**2))
# Tkinter Things
window = Tk()
canvas = Canvas(window, width=1000, height=900)
img = PhotoImage(file="triangle.gif")
canvas.create_image(0, -150, anchor=NW, image=img)  # Creates triangle Graphic
Hyp = Entry(window, fg="Black", bg="#FFFFFF", width="20")
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

