import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Centered Box Example")
root.geometry("600x500")  # Set a fixed window size for better visualization

# Create a frame that acts like a box
box_frame = tk.Frame(root, bg="lightgreen", padx=30, pady=30, relief="raised")
box_frame.place(relx=0.5, rely=0.5, anchor="center")

# Add a title label inside the frame
title_label = tk.Label(box_frame, text="Cloud Specialist | AWS EC2, S3, RDS, Lambda", bg="lightgreen", fg="black", 
                       font=("Arial", 20, "bold"))
title_label.pack(anchor="center")

# Add a description label inside the frame
description_label = tk.Label(box_frame, text="Hi there! I’m Saima Ali, a dedicated Cloud Engineer with 3+ years of experience and 10+ successfully delivered projects. I specialize in designing secure, scalable, and cost-optimized AWS cloud solutions that help businesses grow faster and operate smarter.", 
                             bg="lightgreen", fg="black", font=("Arial", 20), wraplength=300)
description_label.pack(anchor="center")

# Run the Tkinter event loop
root.mainloop()