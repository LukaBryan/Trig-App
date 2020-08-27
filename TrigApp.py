from tkinter import *
from math import *

DegEntry = 0
HypEntry = 0
ObEntry = 0
AjEntry = 0

# Functions
def TrigFunc():
    print("bruh")

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
Submit = Button(window, image=Buttonimg, font=("arial", 32), text="Submit", border=0, command=TrigFunc())
Submit.place(relx=0.734, rely=Height + 5.3 * HeightInc, anchor=CENTER)

window.title("Trig Calculator")  # Sets window name
###canvas.configure(bg="grey50")
window.iconbitmap(bitmap="icon.ico")
canvas.pack()
window.mainloop()
