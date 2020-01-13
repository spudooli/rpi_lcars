from gpiozero import Button
from signal import pause

backlightState = True


def backlight():
    if backlightState:
        print("Backlight is off")
        backlightState = False
    if not backlightState:
        print("Backlight is on")
        backlightState = True
    
button1 = Button(21,bounce_time=2)

button1.when_pressed = backlight


pause()