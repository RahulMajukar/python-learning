import tkinter as tk
import time

def update_time():
    # Update the label with the current time
    current_time = time.strftime("%H:%M:%S")
    label.config(text=f"Current time: {current_time}")
    # Call this function again after 1000 ms (1 second)
    window.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the time
label = tk.Label(window, font=("Helvetica", 48))
label.pack()

# Start the time update loop
update_time()

# Run the Tkinter event loop
window.mainloop()
