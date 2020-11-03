from tkinter import *
from math import *

ToggleEntry = True
HypVar = 0
OppVar = 0
AdjVar = 0
Deg1Var = 0
Deg2Var = 0


# Functions
def EntryValue():
    global Exit, HypVar, OppVar, AdjVar, Deg1Var, Deg2Var
    Exit = 0

    # Checks for values in each entry
    while True:
        try:
            HypVar = float(Hyp.get())
            break
        except ValueError or AttributeError:
            HypVar = float()
            print("Hyp not given, set to 0")
            break
    while True:
        try:
            OppVar = float(Opp.get())
            break
        except ValueError:
            OppVar = float()
            print("Opp not given, set to 0")
            break
    while True:
        try:
            AdjVar = float(Adj.get())
            break
        except ValueError or AttributeError:
            AdjVar = float()
            print("Adj not given, set to 0")
            break
    while True:
        try:
            Deg1Var = float(Angle1.get())
            break
        except ValueError or AttributeError:
            Deg1Var = float()
            print("Deg1 not given, set to 0")
            break
    while True:
        try:
            Deg2Var = float(Angle2.get())
            break
        except ValueError or AttributeError:
            Deg2Var = float()
            print("Deg2 not given, set to 0")
            break
    print(HypVar)
    print(OppVar)
    print(AdjVar)
    print(Deg1Var)
    print(Deg2Var)
    if HypVar != 0:
        if OppVar or AdjVar > HypVar:
            print("Math error Hyp cant be smaller than opp and adj")
            Hyp.delete(0, END)
            Opp.delete(0, END)
            Adj.delete(0, END)
            Hyp.insert(0, "Math Error")
            Exit = 1


def TrigFunc():
    global HypVar, AnswerTrig, OppVar, AdjVar

    # Working out what trig scenario to use
    if (Deg1Var or Deg2Var) and HypVar > 0:  # Sin Hyp and Deg1 or Deg2
        print("Sin 1")
        if Deg1Var > 0:
            AnswerTrig = float(sin(Deg1Var) * HypVar)
        elif Deg2Var > 0:
            AnswerTrig = float(sin(Deg2Var) * HypVar)
        print(f"Opp = {AnswerTrig:.2f}")
        OppVar = AnswerTrig

    elif (Deg1Var or Deg2Var) and OppVar > 0:  # Sin Opp and Deg1 or Deg2
        print("Sin 2")
        if Deg1Var > 0:
            AnswerTrig = float(OppVar / sin(Deg1Var))
        elif Deg2Var > 0:
            AnswerTrig = float(OppVar / sin(Deg2Var))
        print("Hyp = {:.2f}".format(AnswerTrig))
        HypVar = AnswerTrig

    elif (Deg1Var or Deg2Var) and HypVar > 0:  # Cos Hyp and Deg1 or Deg2
        print("Cos 1")
        if Deg1Var > 0:
            AnswerTrig = float(HypVar * cos(Deg1Var))
        elif Deg2Var > 0:
            AnswerTrig = float(HypVar * sin(Deg2Var))
        print("Hyp = {:.2f}".format(AnswerTrig))
        AdjVar = AnswerTrig

    elif (Deg1Var or Deg2Var) and AdjVar > 0:  # Cos Adj and Deg1 or Deg2
        print("Cos 2")
        if Deg1Var > 0:
            AnswerTrig = float(OppVar / sin(Deg1Var))
        elif Deg2Var > 0:
            AnswerTrig = float(OppVar / sin(Deg2Var))
        print("Hyp = {:.2f}".format(AnswerTrig))
        AdjVar = AnswerTrig

    elif (Deg1Var or Deg2Var) and AdjVar > 0:  # Cos Adj and Deg1 or Deg2
        print("Trig 1")

    elif (Deg1Var or Deg2Var) and OppVar > 0:  # Cos Adj and Deg1 or Deg2
        print("Trig 2")


def AngleCal():
    global Deg1Var, Deg2Var
    Deg1Var = degrees(Deg1Var)
    Deg2Var = degrees(Deg2Var)

    if Deg1Var > 0:  # Checking angle 1 value
        if Deg1Var < 90:  # Checks if value is valid
            AnswerDeg = float(90 - Deg1Var)
            print("Angle 2 is {:.2f} Degrees".format(AnswerDeg))
            Deg2Var = AnswerDeg
        else:
            print("{} is an invalid input".format(Deg1Var))

    elif Deg2Var > 0:  # Checking angle 2 value
        if Deg2Var < 90:  # Checks if value is valid
            AnswerDeg = float(90 - Deg2Var)
            print("Angle 1 is {:.2f} Degrees".format(AnswerDeg))
            Deg1Var = AnswerDeg
        else:
            print("{} is an invalid input".format(Deg2Var))


def Pythag():
    global HypVar, OppVar, AdjVar

    if OppVar and HypVar > 0:  # Checking what Py scenario to use
        print("Py 1")
        AnswerPy = float(sqrt(HypVar ** 2 - OppVar ** 2))
        print("Adj is {:.2f}".format(AnswerPy))
        AdjVar = AnswerPy

    elif AdjVar and HypVar > 0:  # Checking what Py scenario to use
        print("Py 2")
        AnswerPy = float(sqrt(HypVar ** 2 - AdjVar ** 2))
        print("Opp is {:.2f}".format(AnswerPy))
        OppVar = AnswerPy

    elif AdjVar and OppVar > 0:  # Checking what Py scenario to use
        print("Py 3")
        AnswerPy = float(sqrt(AdjVar ** 2 + OppVar ** 2))
        print("Hyp is {:.2f}".format(AnswerPy))
        HypVar = AnswerPy


def MainProgram():
    global Exit, Deg1Var, Deg2Var, HypVar, OppVar, AdjVar, delete, HypAnswer
    EntryValue()
    if Exit == 1:
        return
    Deg1Var = radians(Deg1Var)
    Deg2Var = radians(Deg2Var)
    TrigFunc()
    Pythag()
    AngleCal()
    Deg2Var = round(Deg2Var, 2)
    Deg1Var = round(Deg1Var, 2)
    HypVar = round(HypVar, 2)
    OppVar = round(OppVar, 2)
    AdjVar = round(AdjVar, 2)
    Entryboxes()


def Entryboxes():
    global ToggleEntry, Submit, Hyp, Opp, Adj, Angle1, Angle2, delete, HypAnswer, OppAnswer, AdjAnswer, Angle1Answer, Angle2Answer

    HypAnswer = Label(window, fg="Black", font=("arial", 26), text=HypVar)
    OppAnswer = Label(window, fg="Black", font=("arial", 26), text=OppVar)
    AdjAnswer = Label(window, fg="Black", font=("arial", 26), text=AdjVar)
    Angle1Answer = Label(window, fg="Black", font=("arial", 26), text=Deg1Var)
    Angle2Answer = Label(window, fg="Black", font=("arial", 26), text=Deg2Var)

    HypAnswerCover = Label(window, fg="Black", bg="white", font=("arial", 26), text="           ")
    OppAnswerCover = Label(window, fg="Black", bg="white", font=("arial", 26), text="           ")
    AdjAnswerCover = Label(window, fg="Black", bg="white", font=("arial", 26), text="           ")
    Angle1AnswerCover = Label(window, fg="Black", bg="white", font=("arial", 26), text="           ")
    Angle2AnswerCover = Label(window, fg="Black", bg="white", font=("arial", 26), text="           ")

    ReturnButton = Button(window, font=("arial", 32), text="Return", border=0, width=12, command=Entryboxes)

    if ToggleEntry:
        Submit = Button(window, image=Buttonimg, font=("arial", 32), text="Submit", border=0, command=MainProgram)
        Hyp = Entry(window, fg="Black", width="10", font=("arial", 28))
        Opp = Entry(window, fg="Black", width="10", font=("arial", 28))
        Adj = Entry(window, fg="Black", width="10", font=("arial", 28))
        Angle1 = Entry(window, fg="Black", width="10", font=("arial", 28))
        Angle2 = Entry(window, fg="Black", bg="#FFFFFF", width="10", font=("arial", 28))

        HypAnswerCover.place(relx=EntryRelXFloat, rely=Height, anchor=CENTER)
        OppAnswerCover.place(relx=EntryRelXFloat, rely=Height + HeightInc, anchor=CENTER)
        AdjAnswerCover.place(relx=EntryRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)
        Angle1AnswerCover.place(relx=EntryRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)
        Angle2AnswerCover.place(relx=EntryRelXFloat, rely=Height + 4 * HeightInc, anchor=CENTER)

        Hyp.place(relx=EntryRelXFloat, rely=Height, anchor=CENTER)
        Opp.place(relx=EntryRelXFloat, rely=Height + HeightInc, anchor=CENTER)
        Adj.place(relx=EntryRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)
        Angle1.place(relx=EntryRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)
        Angle2.place(relx=EntryRelXFloat, rely=Height + 4 * HeightInc, anchor=CENTER)
        Submit.place(relx=0.734, rely=Height + 5.3 * HeightInc, anchor=CENTER)

    if not ToggleEntry:
        HypAnswer = Label(window, fg="Black", font=("arial", 26), text=HypVar)
        OppAnswer = Label(window, fg="Black", font=("arial", 26), text=OppVar)
        AdjAnswer = Label(window, fg="Black", font=("arial", 26), text=AdjVar)
        Angle1Answer = Label(window, fg="Black", font=("arial", 26), text=Deg1Var)
        Angle2Answer = Label(window, fg="Black", font=("arial", 26), text=Deg2Var)

        HypAnswer.place(relx=EntryRelXFloat, rely=Height, anchor=CENTER)
        OppAnswer.place(relx=EntryRelXFloat, rely=Height + HeightInc, anchor=CENTER)
        AdjAnswer.place(relx=EntryRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)
        Angle1Answer.place(relx=EntryRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)
        Angle2Answer.place(relx=EntryRelXFloat, rely=Height + 4 * HeightInc, anchor=CENTER)

        ReturnButton.place(relx=0.734, rely=Height + 5.3 * HeightInc, anchor=CENTER)
        delete = int(0)

        try:
            Hyp.destroy()
            Opp.destroy()
            Adj.destroy()
            Angle1.destroy()
            Angle2.destroy()
            Submit.destroy()
        except:
            pass

    ToggleEntry = not ToggleEntry


# Tkinter Set up
window = Tk()
canvas = Canvas(window, width=1000, height=1000)  # Defines how big the window can be
img = PhotoImage(file="kinghom.gif")  # Import image
canvas.create_image(500, 500, image=img)  # Creates triangle Graphic
window.resizable(False, False)  # Stop the ability for the window to be resized

LabelRelXFloat = 0.58
EntryRelXFloat = 0.8
Height = 0.08
HeightInc = 0.06

# USER INTERFACE FEATURES
# Title
TitleLabel = Label(window, text="Trig Calculator", font=("arial", 48))
TitleLabel.place(x=20, y=16, anchor=NW)

# Adding button image
Buttonimg = PhotoImage(file="ButtonImage.gif")

# Entries and entry labels

HypLabel = Label(window, text="   H = ", bg="white", font=("arial", 32))
HypLabel.place(relx=LabelRelXFloat, rely=Height, anchor=CENTER)

OppLabel = Label(window, text="   O = ", bg="white", font=("arial", 32))
OppLabel.place(relx=LabelRelXFloat, rely=Height + HeightInc, anchor=CENTER)

AdjLabel = Label(window, text="   A = ", bg="white", font=("arial", 32))
AdjLabel.place(relx=LabelRelXFloat, rely=Height + 2 * HeightInc, anchor=CENTER)

Angle1Label = Label(window, text="∠1 = ", bg="white", font=("arial", 32))
Angle1Label.place(relx=LabelRelXFloat, rely=Height + 3 * HeightInc, anchor=CENTER)

Angle2Label = Label(window, text="∠2 = ", bg="white", font=("arial", 32))
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

Return = Button(window, font=("arial", 32), text="Return", border=0, width=12, command=Entryboxes)

# Initiate buttons and entry boxes
Entryboxes()

window.title("Trig Calculator")  # Sets window name
# canvas.configure(bg="grey50")
window.iconbitmap(bitmap="icon.ico")
canvas.pack()
window.mainloop()
