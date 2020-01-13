from gpiozero import Button
from signal import pause
import subprocess

def backlight():
    bl = open(BASEDIR + "/sys/class/backlight/rpi_backlight/bl_power", "r")
    backlightState = ob.read()
    if backlightState =="1"
        print("Backlight is off, turning it on now")
        subprocess.Popen(['echo','0','|','sudo','tee','/sys/class/backlight/rpi_backlight/bl_power'
    if backlightState =="0":
        print("Backlight is on, turning it off")
        subprocess.Popen(['echo','1','|','sudo','tee','/sys/class/backlight/rpi_backlight/bl_power'

button1 = Button(21,bounce_time=2)

button1.when_pressed = backlight

pause()