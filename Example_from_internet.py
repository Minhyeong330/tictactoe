from functools import partial
import tkinter as tk


def change_text(button, text, event=None):
    # Only if the button is empty
    if button.cget("text") == "":
        # Change the button's text to whatever is in the variable `text`
        button.config(text=text)

def clear(event=None):
    for button in buttons:
        button.config(text="")


# Create the tkinter window
root = tk.Tk()
# A list to store all of the buttons
buttons = []

for i in range(9):
    # Create the button:
    button = tk.Label(root, text="", width=3, font=("", 15), bd=3,
                      relief="groove")

    # 1st parameter of `partial` is the function. The rest are just arguments
    command = partial(change_text, button, "X")
    button.bind("<Button-1>", command) # Left click

    command = partial(change_text, button, "O")
    button.bind("<Button-3>", command) # Right click

    # Display the button:
    button.grid(row=i//3, column=i%3)
    # Add the button to the list of buttons:
    buttons.append(button)

clear_button = tk.Label(root, text="Clear screen", width=3, font=("", 15), bd=3,
                        relief="groove")
clear_button.grid(row=4, column=0, columnspan=3, sticky="news")
clear_button.bind("<Button-1>", clear) # Left click

# Run tkinter's mainloop
root.mainloop()