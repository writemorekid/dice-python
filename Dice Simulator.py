import tkinter as tk
from PIL import ImageTk, Image
import random

# Function to roll the dice
def roll_dice():
    # Update label with rolling text
    rolling_text.config(text='Rolling...')
    window.update()
    
    # Pause for a moment
    window.after(1000)  # Adjust the time in milliseconds as needed
    
    # Roll the dice
    result = random.randint(1, 6)
    dice_label.config(image=dice_images[result-1], text=f'Result: {result}')
    
    # Reset label text after a delay
    window.after(2000, lambda: rolling_text.config(text=''))

# Function to create a bouncing effect when rolling
def bounce_effect(iterations, delay):
    # Calculate the number of iterations needed for bouncing
    total_iterations = iterations * 2
    
    # Bounce the button and dice label
    for i in range(total_iterations):
        if i % 2 == 0:
            dx = 10
        else:
            dx = -10
        window.update()
        window.after(delay * i, lambda dx=dx: window.geometry(f'+{window.winfo_x() + dx}+{window.winfo_y()}'))

# Create the main window
window = tk.Tk()
window.geometry('100x100')
window.title('Dice Roll')

# Load dice images
dice_images = [ImageTk.PhotoImage(Image.open(f'dice-{i}.png')) for i in range(1, 7)]

# Create button to roll the dice
button = tk.Button(window, text='Roll Dice', command=lambda: [roll_dice(), bounce_effect(5, 50)])
button.pack(pady=10)

# Create label to display dice image
dice_label = tk.Label(window)
dice_label.pack()

# Create label to display rolling text
rolling_text = tk.Label(window, text='', font=('Helvetica', 10, 'italic'))
rolling_text.pack()

#Background Color
window.configure(bg='lightblue')

# Start the GUI event loop
window.mainloop()
