import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Centered Box Example")
root.geometry("400x300")  # Set a fixed window size for better visualization

# Create a frame that acts like a box
box_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20, relief="raised")
box_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add a title label inside the frame
title_label = tk.Label(box_frame, text="Cloud Specialist | AWS EC2, S3, RDS, Lambda", bg="lightblue", fg="black", 
                       font=("Arial", 16, "bold"))
title_label.pack(anchor="center")

# Add a description label inside the frame
description_label = tk.Label(box_frame, text="This is a short description inside the box.", 
                             bg="lightblue", fg="black", font=("Arial", 12), wraplength=300)
description_label.pack(anchor="center")

# Run the Tkinter event loop
root.mainloop()