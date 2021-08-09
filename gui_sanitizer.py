from tkinter import *
import RPi.GPIO as GPIO
import board
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

root = Tk()
root.resizable(0, 0)
root.geometry("1024x600")

#Setting background image
img = PhotoImage(file="images/sanitize_bg.png")
label_bg = Label(root, image=img)
label_bg.pack()

def checkPresence():
    while True:
        sensor = GPIO.input(17)
        if sensor==0: #Presence is detected
            GPIO.output(22, 1)
            time.sleep(1)
            GPIO.output(22, 0)
            GPIO.cleanup()
            os.system('python3 New_folder/speaker.py')
            root.destroy()
    
root.after(800, checkPresence)
root.mainloop()