from tkinter import *


def bear():
    print("the bear")


def main():
    ChosenClass = 0

    root = Tk()

    root.geometry("1000x1000+0+0")

    bearImage = PhotoImage(file="bear.png")
    bear = Label(image=bearImage).place(x=50, y=50)
    BearButton = Button(root, text="Battle Bear", command=lambda: bear()).place(x=200, y=420)

    palidinImage = PhotoImage(file="palidin.png")
    palidin = Label(image=palidinImage).place(x=500, y=50)

    wizardImage = PhotoImage(file="wizard.png")
    wizard = Label(image=wizardImage).place(x=50, y=500)

    babydoctorImage = PhotoImage(file="babydoctor.png")
    babydoctor = Label(image=babydoctorImage).place(x=500, y=500)

    root.mainloop()


main()
