import tkinter as tk

def on_button1_click():
    print("Button 1 was clicked!")

def on_button2_click():
    print("Button 2 was clicked!")

def on_button3_click():
    print("Button 3 was clicked!")

# Create the main window
root = tk.Tk()
root.title("Multiple Buttons Example")

# Create button widgets
button1 = tk.Button(root, text="Button 1", command=on_button1_click)
button2 = tk.Button(root, text="Button 2", command=on_button2_click)
button3 = tk.Button(root, text="Button 3", command=on_button3_click)

# Pack the buttons into the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()