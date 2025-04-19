import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get()) # Evaluate the entered expression
        entry_var.set(result)          # Display the result in the entry field
    except:
        entry_var.set("Error")    # Display "Error" if the input is invalid

# Function to update the entry field
def button_click(value):
    entry_var.set(entry_var.get() + str(value))  #appends the clicked button's value to the existing text in the entry field

# Function to clear the entry field
def clear():
    entry_var.set("")

# Create main window
window = tk.Tk()
window.title("Calculator")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 20), justify="left")  #creates an input field inside window.
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    action = lambda t=text: button_click(t) if t not in ("=", "C") else calculate() if t == "=" else clear()
    tk.Button(window, text=text, font=("Arial", 16), command=action, width=6, height=2).grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()
