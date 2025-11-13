import tkinter as tk
import random

# Define 7 symbols for the slot machine
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]

def spin():
    """Spin the reels and update the display."""
    reels = [random.choice(symbols) for _ in range(3)]
    reel1_label.config(text=reels[0])
    reel2_label.config(text=reels[1])
    reel3_label.config(text=reels[2])
    
    if reels[0] == reels[1] == reels[2]:
        result_label.config(text="Congratulations! You win!", fg="green")
    else:
        result_label.config(text="Try again!", fg="red")

# Create the main window
root = tk.Tk()
root.title("Slot Machine with 7 Symbols")
root.geometry("300x250")

# Labels for the reels
reel1_label = tk.Label(root, text="?", font=("Arial", 24), width=10, height=2, relief="sunken")
reel1_label.pack(pady=5)

reel2_label = tk.Label(root, text="?", font=("Arial", 24), width=10, height=2, relief="sunken")
reel2_label.pack(pady=5)

reel3_label = tk.Label(root, text="?", font=("Arial", 24), width=10, height=2, relief="sunken")
reel3_label.pack(pady=5)

# Spin button
spin_button = tk.Button(root, text="Spin the Reels", command=spin, font=("Arial", 16))
spin_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Start the GUI event loop
root.mainloop()