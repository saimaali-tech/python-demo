import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Centered Box Example")
root.geometry("400x300")  # Set a fixed window size for better visualization

# Create a label that acts like a box with some content
box = tk.Label(root, text="Some Content Here", bg="lightblue", fg="black", 
               font=("Arial", 14), padx=20, pady=20, relief="raised")

# Place the box at the center of the window
box.place(relx=0.5, rely=0.5, anchor="center")

# Run the Tkinter event loop
root.mainloop()