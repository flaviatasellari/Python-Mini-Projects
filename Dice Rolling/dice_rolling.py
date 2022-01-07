import tkinter
from PIL import Image, ImageTk
import random

# Widget that shows the main window 
root = tkinter.Tk()
root.geometry ('600x600')
root.title ('Dice Rolling')

l0 = tkinter.Label(root, text="")
l0.pack()

# Images of dice
dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']

image1 = ImageTk.PhotoImage (Image.open (random.choice(dice))) # Random numbers of dice between 0 to 6

label1 = tkinter.Label (root, image = image1)
label1.image = image1
label1.pack (expand = True)

# Function used when pressing the button
def dice_roll ():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure (image = image1)
    label1.image = image1


# The button to roll the dice
button = tkinter.Button (root, text = 'Roll the Dice', fg = 'red', command = dice_roll)

button.pack (expand = True)

root.mainloop()