from tkinter import *


def button_clicked():
    print("I got clicked>")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=600)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.config(text="New text.")
my_label.grid(row=1, column=1)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=2, column=2)

new_button = Button(text="New button")
new_button.grid(row=1, column=3)

input = Entry(width=30)
input.grid(row=3, column=4)
input.get()


window.mainloop()
