import RPi.GPIO as GPIO
import Queue
import time # .sleep, .time

#GPIO.cleanup()

GPIO.setmode(GPIO.BCM) # Broadcom SOC channel

# Right Wheel
M1A = 22
M2A = 23
# Left Wheel
M3A = 24
M4A = 25

# Green Sonar
S1out = 2
S1in = 3
# Blue Sonar
S2out = 18
S2in = 17

# Register inputs/outputs
GPIO.setup(M1A,GPIO.OUT)
GPIO.setup(M2A,GPIO.OUT)
GPIO.setup(M3A,GPIO.OUT)
GPIO.setup(M4A,GPIO.OUT)
GPIO.setup(S1out,GPIO.OUT)
GPIO.setup(S1in,GPIO.IN)
GPIO.setup(S2out,GPIO.OUT)
GPIO.setup(S2in,GPIO.IN)

# Settle ultrasonic sensors
GPIO.output(S1out,GPIO.LOW)
GPIO.output(S2out,GPIO.LOW)
time.sleep(1)

def rForward():
    GPIO.output(M1A,GPIO.HIGH)
    GPIO.output(M2A,GPIO.LOW)
def rStop():
    GPIO.output(M1A,GPIO.LOW)
    GPIO.output(M2A,GPIO.LOW)
def rBack():
    GPIO.output(M1A,GPIO.LOW)
    GPIO.output(M2A,GPIO.HIGH)

def lForward():
    GPIO.output(M3A,GPIO.HIGH)
    GPIO.output(M4A,GPIO.LOW)
def lStop():
    GPIO.output(M3A,GPIO.LOW)
    GPIO.output(M4A,GPIO.LOW)
def lBack():
    GPIO.output(M3A,GPIO.LOW)
    GPIO.output(M4A,GPIO.HIGH)

lStop()
rStop()
