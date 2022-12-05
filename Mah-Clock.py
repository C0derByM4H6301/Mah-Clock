from tkinter import *
from tkinter.ttk import *
from time import strftime

pencere = Tk()
pencere.title("Mah-Clock")
label = Label(pencere, font=("ds-digital", 150), background="black",foreground="white")
label.pack(anchor="center")
def time():
    yazi = strftime("%H:%M:%S %p")
    label.config(text=yazi)
    label.after(1000, time)


time()

mainloop()
