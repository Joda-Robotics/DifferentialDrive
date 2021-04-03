from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=23, trigger=24)

def getDist():
    return int(sensor.distance * 100)


print(getDist())
