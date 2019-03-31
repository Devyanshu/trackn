from tkinter import *
from tkinter import messagebox
from connector import griev


def g():
    root = Tk()
    root.title('Grievances')
    root.geometry('300x300+550+200')
    root.resizable(0, 0)
    gr = griev()
    Label(root, text=gr['number']+" - "+gr['griev']).grid(row=2, column=1)
    root.mainloop()


if __name__ == "__main__":
    g()
