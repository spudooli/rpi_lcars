from gpiozero import Button
from signal import pause

def say_hello(button, text = ""):
    print(text + str(button.pin.number))


button2 = Button(21)

button1.when_pressed = say_hello


pause()