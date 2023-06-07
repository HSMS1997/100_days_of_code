from tkinter import *


def button_clicked():
    miles = float(entrada.get())
    km = miles * 1.609
    final_label_middle.config(text=f"{km}")


window = Tk()
window.title("Distance converter.")
window.minsize(width=300, height=120)
window.config(padx=20, pady=20)


entrada = Entry(width=5)
entrada.grid(row=1, column=2)
entrada.get()


miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

final_label_start = Label(text="is equal to ")
final_label_start.grid(row=2, column=1)

final_label_middle = Label(text="0")
final_label_middle.grid(row=2, column=2)

final_label_end = Label(text="Km.")
final_label_end.grid(row=2, column=3)


button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

window.mainloop()
