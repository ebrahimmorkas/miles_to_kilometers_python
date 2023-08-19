from tkinter import *
gui = Tk()
gui.minsize(width=200, height=200)

# Creating the is equal to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)

# Creating the textield in which user will enter miles
miles_textfield = Entry()
miles_textfield.insert(0, "0")
miles_textfield.grid(column=2, row=1)

# Creating the label that will show the "miles" word after the textfield of miles
miles_label = Label(text="miles")
miles_label.grid(column=3, row=1)

# Creating the textfield that will be disabled and it will show the kilometers when user will click on calculate button
kilometer_textfield = Entry()
# kilometer_textfield.config(state="disabled")
kilometer_textfield.grid(column=2, row=2)

# Creating the textfield that will displayed besides the kilometers textfield
kilometer_label = Label(text="km")
kilometer_label.grid(column=3, row=2)

# Function that will convert the mile to km
def convert_mile_to_km():
    # print("Button clicked")
    miles = int(miles_textfield.get())
    kilometers = miles * 1.60934
    kilometer_textfield.insert(0, kilometers)

# Creating the button that will convert the miles to kilometers
calculate_button = Button(text="calculate", command=convert_mile_to_km)
calculate_button.grid(column=2, row=3)

gui.mainloop()
