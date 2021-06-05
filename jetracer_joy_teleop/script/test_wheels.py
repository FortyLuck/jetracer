#! /usr/bin/python3

from jetracer.nvidia_racecar import NvidiaRacecar
from time import sleep

CAR = NvidiaRacecar()

for i in range(-10, 12, 5):
    s = i/10
    print(f"steering: {s}")
    CAR.steering = s
    sleep(1)
CAR.steering = 0

for i in range(-10, 12, 5):
    t = i/10
    print(f"throttle: {t}")
    CAR.throttle = t
    sleep(1)
CAR.throttle = 0
