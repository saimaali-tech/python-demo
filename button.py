import tkinter as tk

def on_button_click():
    print("Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Button Example")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)

# Pack the button into the window
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()