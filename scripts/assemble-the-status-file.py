#!/usr/bin/env python
# Script to assemble the status file for the main page

BASEDIR = "/home/pi/rpi_lcars/"

ob = open(BASEDIR + "scripts/otherbalance.txt", "r")
otherbalance = ob.read()

po = open(BASEDIR + "scripts/power.txt", "r")
wholehouse = po.read()
wholehouse = wholehouse.split(",")[0]

st = open(BASEDIR + "scripts/status.txt", "w")
st.write("Status\n" + "Bank Balance: " + otherbalance + "\nPower: " + wholehouse + "kw/h")
st.close


