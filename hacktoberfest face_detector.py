from tkinter import *
from PIL import ImageTk, Image

window = Tk()

def wtitle(head, temp):
    space1 = Label(temp, text="\n", font=("Helvetica", 8)).pack()
    heading = Label(temp, text=head, fg='red', font=("Helvetica", 16)).pack()
    space2 = Label(temp, text="\n", font=("Helvetica", 8)).pack()

def facemask():
    nw = Tk()
    nw.geometry("300x300+10+20")
    window.destroy()
    wtitle("FACE DETECTOR", nw)
    btn2 = Button(nw, text="See Statistics", padx=20, pady=10, fg='blue').pack()
    nw.mainloop()
 
# main menu
def mainmenu():
    welLbl1 = Label(window, text="\n", font=("Helvetica", 8))
    welLbl3 = Label(window, text="COVID RAKSHAK", fg='red', font=("Helvetica", 16))
    welLbl4 = Label(window, text="\n", font=("Helvetica", 8))
    welLbl1.pack()
    welLbl3.pack()
    welLbl4.pack()
    window.geometry("300x300+10+20")

    window.mainloop()


mainmenu()
