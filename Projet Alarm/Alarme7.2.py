import RPi.GPIO as GPIO
import sys
import signal
import time
import logging
from enum import Enum
from courriel import *
from log import *

#Pin setup

DOOR = 6
BOUTON = 17
LED_ROUGE = 18
LED_JAUNE = 12

class States(Enum):
    DESARMER = 1
    ARMER = 2
    ALARME = 3

class Events(Enum):
    Bouton = 1
    Porte =2   

def getEvent():
    while True:
        if  GPIO.input(BOUTON) == GPIO.HIGH:
            time.sleep(0.2 )
            return Events.Bouton

        elif GPIO.input(DOOR) == GPIO.HIGH:
            time.sleep(0.2 )
            return Events.Porte

def setState(event):
    global state 
    global start 

    #Etat desarmer
    if event == States.DESARMER:
        GPIO.output(LED_ROUGE, GPIO.LOW)
        GPIO.output(LED_JAUNE, GPIO.LOW)
        log.debug("DESARMER")
        state = States.DESARMER
        print("Systeme desarmer")

    #Etat armer
    elif event == States.ARMER:
        GPIO.output(LED_ROUGE, GPIO.HIGH)
        log.debug("ARMER")
        state = States.ARMER
        print("Systeme armer!")
    
    #Etat Alarm
    elif event == States.ALARME:
        GPIO.output(LED_JAUNE, GPIO.HIGH)
        mail = email("202195882@collegeahuntsic.qc.ca",
                     "Stephan Whittick",
                     "stephan.whittick@hotmail.com",
                     "Stephan Whittick")
        mail.send("Alarme", "Il y a eu intrustion pendant que l'alarme etait armer!!")
        log.critical("ALARM")
        state = States.ALARME
        print("Systeme enclancher, alarme sonne")

#I\O Setup
def setup():
    #Pour terminer
    signal.signal(signal.SIGINT, terminate)
    #log
    global log
    log = logHistory()
    log.debug("setup")
    #GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #input
    GPIO.setup(BOUTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(DOOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    #Output
    GPIO.setup(LED_ROUGE, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(LED_JAUNE, GPIO.OUT, initial = GPIO.LOW)

#FOnction main
def main():

    log.debug("main")
    setState(States.DESARMER)
    print("Initialisation")

    while True:
        event = getEvent()
        #Quand le bouton est presser
        if event == Events.Bouton:
            if state == States.DESARMER:
                setState(States.ARMER)
            elif state == States.ARMER:
                setState(States.DESARMER)
            elif state == States.ALARME:
                setState(States.DESARMER)

        #Quand la porte est ouverte
        elif event == Events.Porte:
            if state == States.ARMER:
                setState(States.ALARME)

def terminate(signum, frame):
    log.debug("terminate")
    GPIO.output(LED_ROUGE, GPIO.LOW)
    GPIO.output(LED_JAUNE, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)

if __name__ == '__main__':
    setup()
    main()















