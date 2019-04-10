#Assignment No.:10
#Problem Statement : Write an application using Raspberry-Pi /Beagle board to control the
#operation of a hardware simulated traffic signal.
#Name :Mayur Deshmukh
#TE A 17


import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pirPin = 15
GPIO.setup(pirPin,GPIO.IN)

camera = PiCamera()
while True:
    pirValue = GPIO.input(pirPin)
    if pirValue == 0:
        print"Movement not detected"
    if pirValue == 1:
        print"Movement Detected"
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/image1.jpg')
        camera.stop_preview()





