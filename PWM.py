from __main__ import *
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

PWM = GPIO.PWM(11, 100)
PWM.start(50)
PWM.ChangeDutyCycle(100)
PWM.ChangeFrecuency(1000)
PWM.stop()
GPIO.cleanup()
