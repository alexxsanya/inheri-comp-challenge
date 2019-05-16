import datetime
import random


Time = datetime.datetime.now().hour
def evening_time(time):
    if (time in range(19, 23)) or (time in range(0, 6)):
        return True
    else:
        return False

person_moving = random.randint(0,1)

def movement(person_movingi):
    tym_now = evening_time(Time)
    if person_movingi == 1 and tym_now == True:
        return True
    else:
        return False

def lights_on(person_movingi):
    detected = movement(person_moving)
    if detected == True:
        lights = "ON"
        print("Now Lights are " + lights)
    else:
        lights = "OFF"
        print("Now Lights are " + lights)

