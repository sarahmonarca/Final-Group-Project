import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

playtime = 1
delay = .5

DEBUG = True

pygame.init()

leds = [6,13,19,21]
switches = [20,16,12,26]

sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def all_on():
    for i in leds:
        GPIO.output(leds,True)
       
def all_off():
    for i in leds:
        GPIO.output(leds,False)
       
def lose():
    for i in range(0,4):
        all_on()
        sleep(.5)
        all_off()
        sleep(.5)

seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))

print("Welcome to simon")
print("Try to play the sequence back by pressing the switches.")
print("Press the Ctrl+C to exit...")

print("Press the switches or Ctrl+C to exit")


try:
    while (True):
#         delay = sleep(.5)
#         plau = sleep(1)
        seq.append(randint(0,3))
        print(seq)
        if(DEBUG):
           
           
            if (len(seq) >= 3):
                print()
           
            print("seq={}".format(seq))
            if (len(seq) >= 5):
                print ("Riddle Complete")
                break
#                  playtime = .2
#                  delay = .1
#             elif (len(seq) >= 7):
#                  playtime = .8
#                  delay = .3
#             elif (len(seq) >= 10):
#                  playtime = .7
#                  delay = .25
#             elif (len(seq) >= 13):
#                  playtime = .6
#                  delay =.15
#              
#                  
        for s in seq:
            if(len(seq) < 15):
                GPIO.output(leds[s], True)
            sounds[s].play()
            sleep(playtime)
            if (len(seq) < 15):
                GPIO.output(leds[s],False)
            sleep(delay)
        switch_count = 0
     
        while(switch_count < len(seq)):
            pressed = False
           
            while(not pressed):
                for i in range(len(switches)):
                    while (GPIO.input(switches[i]) == True):
                        val = i
                        pressed = True
            if (DEBUG):
                print(val),
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val] , False)
            sleep(.25)
           
            if(val != seq[switch_count]):
                lose()
                GPIO.cleanup()
                exit(0)
            switch_count += 1
except KeyboardInterrupt:
    GPIO.cleanup()
    '''
        pressed = False
        while (not pressed):
            for i in range(len(switches)):
                while(GPIO.input(switches[i]) == True):
                      val = i
                      pressed = True
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val],False)
        sleep(0.25)
        '''
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBbye")