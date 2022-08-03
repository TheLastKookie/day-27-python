from tkinter import *


def calculate():
    km = round(float(miles_entry.get()) * 1.60934)
    km_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(pady=10, padx=10)

# Miles Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Km Result Label
km_result = Label(text="0")
km_result.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Equals Label
equals_label = Label(text="is equals to")
equals_label.grid(column=0, row=1)

# Calculate button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()
