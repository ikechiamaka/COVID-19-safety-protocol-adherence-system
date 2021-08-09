from tkinter import *
import os
import time

splash_root = Tk()
splash_root.resizable(0, 0)
splash_root.geometry("1024x600")
splash_root.title("splash")

#Setting background image
img = PhotoImage(file="images/splash_bg.png")
label_bg = Label(splash_root, image=img)
label_bg.pack()

def main():
    #Speaker should switch mode here
    time.sleep(5)
    splash_root.destroy()
    os.system('python3 gui_main.py')
    
    
splash_root.after(1000, main)

mainloop()