# Read and process data from files/system
import subprocess
import json

# Return lines of text
def read_txt(filename):
    lines = []
    with open(filename, mode='r') as infile:
        lines = infile.read().splitlines()

    return lines

# Return current uptime
def get_uptime():
    ps = subprocess.Popen("uptime -p", shell=True, stdout=subprocess.PIPE)
    uptime = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return uptime.rstrip()[3:]

# Return system load
def get_load():
    ps = subprocess.Popen("uptime", shell=True, stdout=subprocess.PIPE)
    uptime = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    return uptime.rstrip()[-16:]

# Check version against GitHub
def update_available():
    ps = subprocess.Popen("git remote update >/dev/null 2>&1 && git status | grep behind | wc -l", shell=True, stdout=subprocess.PIPE)
    gitstatus = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    # Return value
    if gitstatus[0] == "0":
        return 0
    elif gitstatus[0] == "1":
        return 1

#Get the balance
def get_balance():
    fr = open("/home/pi/rpi_lcars/scripts/otherbalance.txt", "r")
    otherbalance = fr.read()
    return otherbalance

#Get the inside temperature
def get_insidetemperature():
    jsonFile = open("/home/pi/rpi_lcars/scripts/statusfile.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    indoorTemperature = data["indoorTemperature"]
    return indoorTemperature

#Get the outdoor temperature
def get_outdoortemperature():
    jsonFile = open("/home/pi/rpi_lcars/scripts/statusfile.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    outdoorTemperature = data["outdoorTemperature"]
    return outdoorTemperature

#Get the kitchen temperature
def get_kitchentemperature():
    jsonFile = open("/home/pi/rpi_lcars/scripts/statusfile.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    kitchenTemperature = data["kitchenTemperature"]
    return kitchenTemperature

#Get the inside pressure
def get_indoorPressure():
    jsonFile = open("/home/pi/rpi_lcars/scripts/statusfile.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    indoorPressure = data["indoorPressure"]
    indoorPressure = indoorPressure[:4]
    return indoorPressure
