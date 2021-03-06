from gpiozero import Button
from signal import pause
from rpi_backlight import Backlight
import time

backlight = Backlight()

def backlightchanger():
    print("pressed")
    if not backlight.power:
        print("Backlight is off, turning it on now")
        backlight.power = True
        backlight.brightness = 30
    elif backlight.power:
        print("Backlight is on, turning it off")
        with backlight.fade(duration=1):
            backlight.brightness = 0
            backlight.power = False


button1 = Button(21)

while True:
    button1.when_released = backlightchanger
    time.sleep(0.2)