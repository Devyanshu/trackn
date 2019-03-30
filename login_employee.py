from tkinter import *
from tkinter import messagebox
import screen
root = Tk()
root.title("Login")
root.geometry('300x250+550+200')
root.resizable(0, 0)
Tops = Frame(root, height=50, bd=4, relief="ridge")
Tops.pack(fill=X)
Label(Tops, font=('arial', 18, 'bold'),
      text="     Login Credentials  ", bd=5).grid(row=0, column=0)
Label(root, text="").pack()


def iExit():
    qExit = messagebox.askyesno("Login", "Do you want to exit?")
    if qExit > 0:
        root.destroy()
        return


def go():
    user, pas = u_entry.get(), p_entry.get()
    f = list(open('bin.txt'))
    for i in range(len(f)):
        f[i] = f[i].split(',')
    flag = False
    for i in f:
        if user in i:
            if pas == i[1]:
                flag = True
                print("Password Correct")
                root.destroy()
                screen.main(int(i[2]))
            else:
                messagebox.showinfo("Wrong Credentials",
                                    "The password is wrong")
                print('Wrong pass')

    if not flag:
        messagebox.showinfo("Wrong Credentials",
                            "The username is wrong")
        print('Wrong username')


u = Label(root, font=('arial', 12), text="Username ",
          justify=LEFT, padx=20).pack()
u_entry = Entry(root)
u_entry.pack()
Label(root, text="").pack()
p = Label(root, font=('arial', 12), text="Password ",
          justify=LEFT, padx=20).pack()
p_entry = Entry(root, show='*')
p_entry.pack()
Label(root, text="").pack()
f2 = Frame(root, height=10, width=100, bd=4, relief="raise")
f2.pack()

Label(root, text="").pack()
Label(root, text="").pack()
btnGo = Button(f2, text="Go", padx=3, pady=3, bd=2, fg="black", font=(
    'arial', 10, 'bold'), width=14, height=1, command=go).grid(row=0,
                                                               column=0)
btnExit = Button(f2, text="Exit", padx=3, pady=3, bd=2, fg="black", font=(
    'arial', 10, 'bold'), width=14, height=1, command=iExit).grid(row=0,
                                                                  column=1)

if __name__ == "__main__":
    root.mainloop()
