from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Login")
root.geometry('300x300+550+200')
root.resizable(0, 0)
Tops = Frame(root, height=50, bd=4, relief="ridge")
Tops.pack(fill=X)
Label(Tops, font=('arial', 25, 'bold'),
      text="    Login Credentials   ", bd=5).grid(row=0, column=0)

def iExit():
        qExit = messagebox.askyesno("Login", "Do you want to exit?")
        if qExit > 0:
            root.destroy()
            return

def go():
    return

username= StringVar()
password=StringVar()
u=Label(root, font=('arial', 20),text="Username ",justify=LEFT, padx=20).pack()
u_entry = Entry(root, textvariable=username)
u_entry.pack()
Label(root, text="").pack()
p=Label(root, font=('arial', 20),text="Password ",justify=LEFT, padx=20).pack()
p_entry = Entry(root, textvariable=password, show= '*')
p_entry.pack()
Label(root, text="").pack()
f2 = Frame(root, height=10, width=100, bd=4, relief="raise")
f2.pack()

Label(root, text="").pack()
btnGo = Button(f2, text="Go", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=go).grid(row=0,
                                                                   column=0)
btnExit = Button(f2, text="Exit", padx=6, pady=6, bd=2, fg="black", font=(
        'arial', 12, 'bold'), width=14, height=1, command=iExit).grid(row=0,
                                                                      column=1)

if __name__ == "__main__":
    root.mainloop()
