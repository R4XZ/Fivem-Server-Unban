
# Python program to create a close button
# using destroy Non-Class method
import os
import shutil
import subprocess
from tkinter import *
from os.path import dirname  
# Creating the tkinter window
root = Tk()
root.geometry("700x300")
root.title('FivemCleaner')  

  
def Close():
    exit()

 
# Button for closing
exit_button = Button(root, text="Exit", command=Close)
exit_button.pack(pady=20)
  
root.mainloop()