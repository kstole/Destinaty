import RPi.GPIO as GPIO
import time # .sleep, .time

GPIO.setmode(GPIO.BCM) # Broadcom SOC channel

# Program Toggle
toggl = 27

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
GPIO.setup(toggl,GPIO.IN)

# Settle ultrasonic sensors
GPIO.output(S1out,GPIO.LOW)
GPIO.output(S2out,GPIO.LOW)
time.sleep(1)

def main():
    while True:
        if not GPIO.input(toggl):
            continue
        qNum = 5
        while True:
            forward()
            time.sleep(0.5)
            green = get_dist_green()
            blue = get_dist_blue()
            print green
            print blue
            print "\n\n"
            if not GPIO.input(toggl):
                break
            if green < 50.0 or blue < 50.0:
                gCount = 100.0
                bCount = 100.0
                while gCount > 30.0 and bCount > 30.0:
                    gCount = 0.0
                    bCount = 0.0
                    for x in range(qNum):
                        time.sleep(0.01)
                        gCount += get_dist_green()
                        bCount += get_dist_blue()
                    gCount /= qNum
                    bCount /= qNum
                    print "gCount"
                    print(gCount)
                    print "bCount"
                    print(bCount)
                print "gCount Final"
                print(gCount)
                print "bCount Final"
                print(bCount)
                stop()
                if gCount < bCount:
                    right()
                    while get_dist_green() < 100.0:
                        print "turing right"
                        time.sleep(0.05)
                else:
                    left()
                    while get_dist_blue() < 100.0:
                        print "turning left"
                        time.sleep(0.05)
                stop()
                print "finished turn"
                if not GPIO.input(toggl):
                    # GPIO.cleanup()
                    break

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

def stop():
    lStop()
    rStop()
def forward():
    rForward()
    lForward()
def back():
    lBack()
    rBack()
def right():
    rBack()
    lForward()
def left():
    lBack()
    rForward()

def get_dist_green():
    pulse_start = 0.0
    pulse_end = 100000
    GPIO.output(S1out,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(S1out,GPIO.LOW)
    while (GPIO.input(S1in)==0):
        pulse_start = time.time()
    while (GPIO.input(S1in)==1):
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

def get_dist_blue():
    pulse_start = 0.0
    pulse_end = 100000
    GPIO.output(S2out,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(S2out,GPIO.LOW)
    while (GPIO.input(S2in)==0):
        pulse_start = time.time()
    while (GPIO.input(S2in)==1):
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

main()


