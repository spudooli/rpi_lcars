from gpiozero import Button
from signal import pause
from rpi_backlight import Backlight

backlight = Backlight()

def backlightchanger():
    if backlight.brightness > "0"
        print("Backlight is off, turning it on now")
        with backlight.fade(duration=1):
            backlight.brightness = 100

    if backlightState =="0":
        print("Backlight is on, turning it off")
        with backlight.fade(duration=1):
            backlight.brightness = 0

button1 = Button(21,bounce_time=2)

button1.when_pressed = backlightchanger

pause()