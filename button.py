import tkinter as tk
from tkinter import font as tkfont

def on_button1_click():
    print("Button 1 was clicked!")

def on_button2_click():
    print("Button 2 was clicked!")

def on_button3_click():
    print("Button 3 was clicked!")

# Create the main window
root = tk.Tk()
root.title("Multiple Buttons Example")

# Define a custom font
custom_font = tkfont.Font(family="Arial", size=15, weight="bold")

# Create button widgets with larger size, custom font, and colors
button1 = tk.Button(root, text="Button 1", command=on_button1_click, width=25, height=3,
                    font=custom_font, bg="red", fg="white")
button2 = tk.Button(root, text="Button 2", command=on_button2_click, width=25, height=3,
                    font=custom_font, bg="blue", fg="white")
button3 = tk.Button(root, text="Button 3", command=on_button3_click, width=25, height=3,
                    font=custom_font, bg="green", fg="white")

# Pack the buttons into the window with some padding
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()