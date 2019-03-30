from tkinter import *
from tkinter import messagebox
import connector


def main(cat):
    root = Tk()
    root.title('CPU Scheduling')

    # x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    # y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    # root.geometry("+%d+%d" % (x, y))
    root.geometry('330x130+550+200')
    root.resizable(0, 0)
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def notify():
        print(number.get())
        connector.submit(number.get(), cat)
        messagebox.showinfo("Notified", "The user was notified")
        number.delete(0, 'end')
    Label(frame, text="Enter Number").grid(row=0, column=1)

    number = Entry(frame, text="")
    number.grid(row=0, column=2)

    Label(frame, text="").grid(row=2, column=1)
    Label(frame, text="").grid(row=3, column=1)
    # Label(frame, text="").grid(row=4, column=1)
    if cat == 'laundry':
        griev = Button(frame, text="Grievance", padx=6, pady=6, fg="black",
                       font=('arial', 12, 'bold'), width=10, height=1,
                       command=notify).grid(row=5, column=1)
    generate = Button(frame, text="Notify", padx=6, pady=6, fg="black",
                      font=('arial', 12, 'bold'), width=10, height=1,
                      command=notify).grid(row=5, column=2)
    exit_button = Button(frame, text="Exit", padx=6, pady=6, fg="black", font=(
        'arial', 12, 'bold'), width=10, height=1,
        command=root.destroy).grid(row=5, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()
