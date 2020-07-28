import tkinter as tk
from math import*
from PIL import Image, ImageTk

#Tkinter Things
window=tk.Tk()
window.mainloop()

#main Program
Deg=int(input("Input angle: "))
H=int(input("Input Length: "))
Rad=radians(Deg)
O=H*sin(Rad)
print(O)
