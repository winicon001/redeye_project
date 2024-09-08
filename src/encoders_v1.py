# File name   : encoders.py
# Description : Python Wheel Encoder code for LM393 H2010
# Product     : smilebot  
# E-mail      : winicon@live.com
# Author      : Semiu ADEBAYO
# Date        : 2024/08/15
# credit      : SciJoy @ https://www.youtube.com/watch?v=cLtMcqRetO0&t=101s

import RPi.GPIO as GPIO
import time
#from adafruit_Motorkit import Motorkit

# Encoders Pins Declaration
leftencoder = 15
rightencoder = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(leftencoder, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightencoder, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


Encoder1StateLast = GPIO.input(leftencoder)
enc1_revCount = 0
enc1count = 0
enc1countTotal = 0

Encoder2StateLast = GPIO.input(rightencoder)
enc2_revCount = 0
enc2count = 0
enc2countTotal = 0

# Right Wheel Encoder
def wheelEncodersReading():

    Encoder1StateLast = GPIO.input(leftencoder)
    enc1_revCount = 0
    enc1count = 0
    enc1countTotal = 0

    Encoder2StateLast = GPIO.input(rightencoder)
    enc2_revCount = 0
    enc2count = 0
    enc2countTotal = 0

    # Right Wheel Calculation
    wheelCircumference = 204 # Wheel Circumference in mm
    EncodercountPerRev = 40 #Encoder Count Per Wheel Encoder1rotation
    dist_per_tic = wheelCircumference/EncodercountPerRev # Calculating the Encoder1distance travelled per wheel encoder tick

    # Left Wheel Calculation
    wheelCircumference = 207 # Wheel Circumference in mm
    EncodercountPerRev = 40 #Encoder Count Per Wheel Encoder2rotation
    dist_per_tic = wheelCircumference/EncodercountPerRev # Calculating the Encoder2distance travelled per wheel encoder tick

    while True:

        #GPIO.output(outputLED, GPIO.HIGH)
        Encoder1StateCurrent = GPIO.input(leftencoder)
        if Encoder1StateCurrent != Encoder1StateLast: # If the read value is different from the previous
            Encoder1StateLast = Encoder1StateCurrent # Increment the count
            enc1count +=1
            enc1countTotal +=1
        
        
        if enc1count == EncodercountPerRev:
            enc1_revCount +=1
            enc1count = 0
        
        Encoder1distance = dist_per_tic * enc1countTotal



         #GPIO.output(outputLED, GPIO.HIGH)
        Encoder2StateCurrent = GPIO.input(rightencoder)
        if Encoder2StateCurrent != Encoder2StateLast: # If the read value is different from the previous
            Encoder2StateLast = Encoder2StateCurrent # Increment the count
            enc2count +=1
            enc2countTotal +=1
            
            
        if enc2count == EncodercountPerRev:
            enc2_revCount +=1
            enc2count = 0
        
        Encoder2distance = dist_per_tic * enc2countTotal

        print('   enc1count =  ', enc1count  , end=' ')
        print('   enc1countTotal =  ', enc1countTotal, end=' ')
        print('   Encoder1distance =  ', Encoder1distance , end= '  ')

        print('   enc2count =  ', enc2count  , end=' ')
        print('   enc2countTotal =  ', enc2countTotal, end=' ')
        print('   Encoder2distance =  ', Encoder2distance, 'mm')

    #except KeyboardInterrupt: # If CTRL+C is pressed
       # kit.motor1.throttle = 0
        #GPIO.cleanup() # End the Process
