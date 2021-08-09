from tkinter import *
import os
import time

root = Tk()
root.resizable(0, 0)
root.title("menu")
root.geometry("1024x600")


def startprogram(event):
        os.system('python3 detect_mask_video.py')
        root.destroy()
        
def exitprogram(event):
        root.destroy()
    
#Setting background image
img = PhotoImage(file="images/main_bg.png")
label_bg = Label(root, image=img)
label_bg.pack()

#Start program button
img1 = PhotoImage(file="images/start_system.png")
label_start =  Label(root, image=img1, bg='#4B4B4D')
label_start.place(x=100, y=60)
label_start.bind("<Button>", startprogram)

#Exit program button
img2 = PhotoImage(file="images/exit_system.png")
label_exit =  Label(root, image=img2, bg='#4B4B4D')
label_exit.place(x=100, y=300)
label_exit.bind("<Button>", exitprogram)
    
mainloop()