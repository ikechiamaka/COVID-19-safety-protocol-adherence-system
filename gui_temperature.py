from tkinter import *
import board
import time
import adafruit_mlx90614
import RPi.GPIO as GPIO
import pyttsx3
import os

TRIG = 21
ECHO = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO, GPIO.IN)

i2c = board.I2C()
mlx = adafruit_mlx90614.MLX90614(i2c)

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 5)

root = Tk()
root.resizable(0, 0)
root.geometry("1024x600")

#Setting background image
img = PhotoImage(file="images/temp_bg.png")
label_bg = Label(root, image=img)
label_bg.pack()

#Creating label to display distance
label_dis = Label(root, text="", bg='#4B4B4D', font="Consolas 50", fg='white')
label_dis.place(x=450, y=135)

#Creating label to display temperature
label_temp = Label(root, text="", bg='#4B4B4D', font="Consolas 50", fg='white')
label_temp.place(x=450, y=300)
root.update_idletasks()
engine.say("a Stand within 20 centimeters away from the sensor")
engine.runAndWait()

def getDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        start = time.time()
    while GPIO.input(ECHO)==1:
        end =  time.time()
    duration = end-start
    distance = (duration * 34300) /2
    distance = int(distance)
    label_dis['text'] = distance
    return distance

def checkTemp():
    currentDist = getDistance()
    if currentDist < 20:
        bodyTemperature = round(mlx.object_temperature, 1)
        bodyTemperature+=6
        label_temp ['text'] = bodyTemperature
        root.update_idletasks()
        if bodyTemperature > 37:
            engine.say("a Your body temperature is " +str(bodyTemperature) +" degrees celcius")
            engine.say("a Your temperature level is too high, you need to seek medical advice")
            engine.runAndWait()
            root.destroy()
            GPIO.cleanup()
        else:
            engine.say("a Your body temperature is " +str(bodyTemperature) +" degrees celcius")
            engine.say("a Your temperature level is okay")
            engine.say("a Please do not forget to sanitize your hands properly")
            engine.runAndWait()
            os.system("python3 gui_sanitizer.py")
            root.destroy()
            GPIO.cleanup()
    root.after(500, checkTemp)
        
checkTemp()
root.mainloop()