from tkinter import *
from tkinter import messagebox
import connector
import griev


def main(cat):
    root = Tk()
    root.title('trackn')

    # x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    # y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    # root.geometry("+%d+%d" % (x, y))
    root.geometry('400x100+550+200')
    root.resizable(0, 0)
    frame = Frame(root)
    #frame.grid(row=0, column=0)
    frame.pack()

    def notify():
        print(number.get())
        connector.submit(number.get(), cat)
        messagebox.showinfo("Notified", "The user was notified")
        number.delete(0, 'end')
    Label(frame, text="Enter Number           ").grid(row=0, column=2)

    number = Entry(frame, text="")
    number.grid(row=0, column=3)

    Label(frame, text="").grid(row=2, column=1)
    #Label(frame, text="").grid(row=3, column=1)
    # Label(frame, text="").grid(row=4, column=1)
    f2 = Frame(root, height=10, width=100, bd=4, relief="raise")
    f2.pack()

    gr = Button(f2, text="Grievance", padx=3, pady=3, fg="black",
                font=('arial', 12, 'bold'), width=10, height=1, relief="raise",
                command=griev.g)
    print(cat)
    if cat is 1:
        gr.grid(row=5, column=2)
    generate = Button(f2, text="Notify", padx=3, pady=3, fg="black",
                      font=('arial', 12, 'bold'), width=10, height=1, relief="raise",
                      command=notify).grid(row=5, column=3)
    exit_button = Button(f2, text="Exit", padx=3, pady=3, fg="black", font=(
        'arial', 12, 'bold'), width=10, height=1, relief="raise",
        command=root.destroy).grid(row=5, column=4)

    root.mainloop()


if __name__ == "__main__":
    main()
