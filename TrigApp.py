from tkinter import *
from math import *


# Functions
def EntryValue():
    global HypInt
    global OppInt
    global AdjInt
    global Deg1Int
    global Deg2Int

    # Checks for values in each entry
    while True:
        try:
            HypInt = float(Hyp.get())
            break
        except ValueError or AttributeError:
            HypInt = float()
            print("Hyp not given, set to 0")
            break
    while True:
        try:
            OppInt = float(Opp.get())
            break
        except ValueError:
            OppInt = float()
            print("Opp not given, set to 0")
            break
    while True:
        try:
            AdjInt = float(Adj.get())
            break
        except ValueError or AttributeError:
            AdjInt = float()
            print("Adj not given, set to 0")
            break
    while True:
        try:
            Deg1Int = float(Angle1.get())
            Deg1int=radians(Deg1Int)
            break
        except ValueError or AttributeError:
            Deg1Int = float()
            print("Deg1 not given, set to 0")
            break
    while True:
        try:
            Deg2Int = float(Angle2.get())
            Deg2int=radians(Deg2Int)
            break
        except ValueError or AttributeError:
            Deg2Int = float()
            print("Deg2 not given, set to 0")
            break
    print(HypInt)
    print(OppInt)
    print(AdjInt)
    print(Deg1Int)
    print(Deg2Int)

def TrigFunc():
    # Working out what trig scenario to use
    if (Deg1Int or Deg2Int) and HypInt >0: # Sin Hyp and Deg1 or Deg2
        print("Sin 1")
        if Deg1Int >0:
            AnswerTrig=float(sin(Deg1Int)*HypInt)
        elif Deg2Int >0:
            AnswerTrig=float(sin(Deg2Int)*HypInt)
        print("{:.2f}".format(AnswerTrig))

    elif (Deg1Int or Deg2Int) and OppInt >0: # Sin Opp and Deg1 or Deg2
        print("Sin 2")

    elif (Deg1Int or Deg2Int) and HypInt >0: # Cos Hyp and Deg1 or Deg2
        print("Cos 1")

    elif (Deg1Int or Deg2Int) and AdjInt >0: # Cos Adj and Deg1 or Deg2
        print("Cos 2")

    elif (Deg1Int or Deg2Int) and AdjInt >0: # Cos Adj and Deg1 or Deg2
        print("Trig 1")

    elif (Deg1Int or Deg2Int) and OppInt >0: # Cos Adj and Deg1 or Deg2
        print("Trig 2")

def AngleCal():
    if Deg1Int >0: # Checking angle 1 value
        if Deg1Int < 90: # Checks if value is valid
            AnswerDeg=int(90-Deg1Int)
            print("Angle 1 is {} Degrees".format(AnswerDeg))
        else:
            print("{} is an invalid input".format(Deg1Int))

    elif Deg2Int >0: # Checking angle 2 value
        if Deg2Int < 90: # Checks if value is valid
            AnswerDeg=int(90-Deg2Int)
            print("Angle 2 is {} Degrees".format(AnswerDeg))
        else:
            print("{} is an invalid input".format(Deg2Int))

def Pythag():
    if OppInt and HypInt >0: # Checking what Py scenario to use
        print("Py 1")
        AnswerPy=float(sqrt(HypInt**2-OppInt**2))
        print("Adj is {:.2f}".format(AnswerPy))

    elif AdjInt and HypInt >0: # Checking what Py scenario to use
        print("Py 2")
        AnswerPy=float(sqrt(HypInt**2-AdjInt**2))
        print("Opp is {:.2f}".format(AnswerPy))

    elif AdjInt and OppInt >0: # Checking what Py scenario to use
        print("Py 3")
        AnswerPy=float(sqrt(AdjInt**2+OppInt**2))
        print("Hyp is {:.2f}".format(AnswerPy))

def MainProgram():
    EntryValue()
    TrigFunc()

### Tkinter Set up
window = Tk()
canvas = Canvas(window, width=1000, height=1000)  # Defines how big the window can be
img = PhotoImage(file="kinghom.gif")  # Import image
canvas.create_image(500, 500, image=img)  # Creates triangle Graphic
window.resizable(False, False)  # Stop the ability for the window to be resized

LabelRelXFloat = 0.58
EntryRelXFloat = 0.8
Height = 0.08
HeightInc = 0.06

### USER INTERFACE FEATURES
# Title
TitleLabel = Label(window, text="Trig Calculator", font=("arial", 48))
TitleLabel.place(x=20, y=16, anchor=NW)

# Entries and entry labels
Hyp = Entry(window, fg="Black", width="10", font=("arial", 28))  # Entry box for the H length on triangle
HypLabel = Label(window, text="H = ", bg="white", font=("arial", 32))
Hyp.place(relx=EntryRelXFloat, rely=Height, anchor=CENTER)
HypLabel.place(relx=LabelRelXFloat, rely=Height, anchor=CENTER)

Opp = Entry(window, fg="Black", width="10", font=("arial", 28))
OppLabel = Label(window, text="O = ", bg="white", font=("arial", 32))
Opp.place(relx=EntryRelXFloat, rely=Height + HeightInc, anchor=CENTER)
OppLabel.place(relx=LabelRelXFloat, rely=Height + HeightInc, anchor=CENTER)

Adj = Entry(window, fg="Black", width="10", font=("arial", 28))
AdjLabel = Label(window, text="A = ", bg="white", font=("arial", 32))
Adj.place(relx=EntryRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)
AdjLabel.place(relx=LabelRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)

Angle1 = Entry(window, fg="Black", width="10", font=("arial", 28))
Angle1Label = Label(window, text="∠1 = ", bg="white", font=("arial", 32))
Angle1.place(relx=EntryRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)
Angle1Label.place(relx=LabelRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)

Angle2 = Entry(window, fg="Black", bg="#FFFFFF", width="10", font=("arial", 28))
Angle2Label = Label(window, text="∠2 = ", bg="white", font=("arial", 32))
Angle2.place(relx=EntryRelXFloat, rely=Height + 4 * HeightInc, anchor=CENTER)
Angle2Label.place(relx=LabelRelXFloat, rely=Height + 4 * HeightInc, anchor=CENTER)

# Triangle labels
HLabel = Label(window, text="H", bg="white", font=("arial", 32))
HLabel.place(x=450, y=560, anchor=CENTER)

OLabel = Label(window, text="O", bg="white", font=("arial", 32))
OLabel.place(x=40, y=620, anchor=CENTER)

ALabel = Label(window, text="A", bg="white", font=("arial", 32))
ALabel.place(x=360, y=950, anchor=CENTER)

OneLabel = Label(window, text="1", bg="white", font=("arial", 32))
OneLabel.place(x=595, y=845, anchor=CENTER)

TwoLabel = Label(window, text="2", bg="white", font=("arial", 32))
TwoLabel.place(x=150, y=450, anchor=CENTER)

# Buttons
Buttonimg = PhotoImage(file="ButtonImage.gif")
Submit = Button(window, image=Buttonimg, font=("arial", 32), text="Submit", border=0, command=MainProgram)
Submit.place(relx=0.734, rely=Height + 5.3 * HeightInc, anchor=CENTER)

window.title("Trig Calculator")  # Sets window name
###canvas.configure(bg="grey50")
window.iconbitmap(bitmap="icon.ico")
canvas.pack()
window.mainloop()
