#RANGE SENSOR CODE
import RPi.GPIO as GPIO
from time import sleep, time
#constants
DEBUG = False
SETTLE_TIME = 2
CALIBRATIONS = 5
CALIBRATION_DELAY = 1
TRIGGER_TIME = 0.00001
SPEED_OF_SOUND = 343
#set the raspberry Pi to the Broadcom pin layout
GPIO.setmode(GPIO.BCM)
#gpio pins
Trig = 18
Echo = 27
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
def getDistance():
    GPIO.output(Trig,GPIO.HIGH)
    sleep(TRIGGER_TIME)
    GPIO.output(Trig, GPIO.LOW)
    while(GPIO.input(Echo)==GPIO.LOW):
        start = time()
    while(GPIO.input(Echo)==GPIO.HIGH):
        end=time()
    duration = end-start
    distance = SPEED_OF_SOUND * duration
    distance /= 2
    distance *=100
    return distance  
def calibrate():
    print("Calibrating...")
    #prompt the uder for an objects known distance
    print("-Place the sensor a measured distance away from an object.")
    known_distance = float(input("-What is the measured distance (cm)?"))
    print("-Getting calibration measurements...")
    distance_avg = 0
    for i in range (CALIBRATIONS):
        distance = getDistance()
        if(DEBUG):
            print("-Got{}cm".format(distance))
        distance_avg+=distance
        sleep(CALIBRATION_DELAY)
    distance_avg/=CALIBRATIONS
    if(DEBUG):
        print("-Average is {}cm".format(distance_avg))
    correction_factor = known_distance/ distance_avg
    if(DEBUG):
        print("--Correction factor is {}".format(correction_factor))
    return correction_factor
#MAIN#
#first allow the sensor to settle for a bit
print("Waiting for the sensor to settle({}s)...".format(SETTLE_TIME))
GPIO.output(Trig,GPIO.LOW)
sleep(SETTLE_TIME)
#next.calibrate the sensor
correction_factor = calibrate()
#then, measure
input("Press enter to begin...")
print("Getting measurements:")
while(True):
    print("Measuring...")
    distance = getDistance() * correction_factor
    sleep(1)
    distance = round(distance, 4)
    print ("Distance measured: {}cm". format (distance))
    i = input ("--Get another measurment (Y/n)?")
    if (not i in ["y", "Y", "yes", "Yes", ""]):
        break
#finally, cleanup the GPIO pins
print("dOnE.")
GPIO.cleanup()

##
distances = []

