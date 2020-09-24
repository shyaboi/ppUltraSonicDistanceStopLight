import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# doing this first, since we're using a while True.
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 18
GREEN = 21
YELLOW=20
RED=16
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def green():
    GPIO.output(GREEN, GPIO.HIGH)
def yellow():
    GPIO.output(YELLOW, GPIO.HIGH)
def red():
    GPIO.output(RED, GPIO.HIGH)
def off(colour):
    GPIO.output(colour, GPIO.LOW)
    
def get_distance():


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = sig_time / 0.000058

    #inches:
    #distance = sig_time / 0.000148
    #print('Distance: {} centimeters'.format(distance))

    return distance

def writeToDB():
    dd = round(distance)
    if dd % 5 == 0:
        print(dd)
while True:
    distance = get_distance()
    writeToDB()
    if distance <100:
        off(GREEN)
        off(YELLOW)
        if distance <100:
            red()
            off(GREEN)
            off(YELLOW)
    elif distance <315:
        off(GREEN)
        off(RED)
        if distance <315:
            yellow()
            off(GREEN)
            off(RED)
        if distance < 100:
            off(YELLOW)
            off(GREEN)
    elif distance > 2000:
        off(YELLOW)
        off(RED)
        if distance > 2000:
            green()
            off(YELLOW)
            off(RED)
        if distance < 315:
            off(GREEN)
        
    time.sleep(0.05)