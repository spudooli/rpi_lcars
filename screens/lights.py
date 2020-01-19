from subprocess import call
from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui.utils.loadinfo import *
from ui.colours import randomcolor
import sys
import paho.mqtt.client as paho
import random

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton
from ui.widgets.screen import LcarsScreen

# Need to change class name to whatever screen is to be called
class ScreenLights(LcarsScreen):
    broker="192.168.1.2"
    port=1883
    client1 = paho.Client(random.random())
    client1.connect(broker,port)

    def setup(self, all_sprites):
        # Load BG image
        all_sprites.add(LcarsBackgroundImage("/home/pi/rpi_lcars/assets/lcars_bg.png"), layer=0)

        # Time/Date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "SPUDOOLI", 1.2), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (4, 135), "LIGHTS", 2), layer=1)

        # Interfaces
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 660), "MAIN", self.logoutHandler), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (145, 15), "ALL LIGHTS", self.display_hw), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (200, 15), "OUTSIDE", self.display_outside), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (255, 15), "BEDROOM", self.display_bedroom), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (310, 15), "LIVING ROOM", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (365, 15), "", self.nullfunction), layer=2)

        # Main lights control
        all_sprites.add(LcarsText(colours.BLUE, (140, 175), "All Lights", 2), layer=3)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (140, 460), "ON", self.alllightson), layer=3)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (140, 610), "OFF", self.alllightsoff), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (200, 175), "All Outside", 2), layer=3)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (200, 460), "ON", self.outsidelightson), layer=3)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (200, 610), "OFF", self.outsidelightsoff), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (260, 175), "Living Room", 2), layer=3)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (260, 460), "ON", self.livingroomlightson), layer=3)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (260, 610), "OFF", self.livingroomlightson), layer=3)

        self.hw = all_sprites.get_sprites_from_layer(3)

        # LCARS UI
        # Outside sub-menu
        all_sprites.add(LcarsText(colours.BLUE, (140, 175), "All Outside", 2), layer=4)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (140, 460), "ON", self.outsidelightson), layer=4)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (140, 610), "OFF", self.outsidelightsoff), layer=4)
        all_sprites.add(LcarsText(colours.BLUE, (200, 175), "Front Door", 2), layer=4)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (200, 460), "ON", self.frontdoorlightson), layer=4)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (200, 610), "OFF", self.frontdoorlightsoff), layer=4)
        all_sprites.add(LcarsText(colours.BLUE, (260, 175), "Verandah", 2), layer=4)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (260, 460), "ON", self.verandahlightson), layer=4)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (260, 610), "OFF", self.verandahlightsoff), layer=4)
        all_sprites.add(LcarsText(colours.BLUE, (320, 175), "Garden", 2), layer=4)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (320, 460), "ON", self.gardenlightson), layer=4)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (320, 610), "OFF", self.gardenlightsoff), layer=4)

        self.outside = all_sprites.get_sprites_from_layer(4)

                # Bedroom sub-menu
        all_sprites.add(LcarsText(colours.ORANGE, (140, 175), "All Bedroom", 2), layer=5)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (140, 460), "ON", self.allbedroomlightson), layer=5)
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (140, 610), "OFF", self.allbedroomlightsoff), layer=5)
        #all_sprites.add(LcarsText(colours.ORANGE, (200, 175), "Front Door", 2), layer=5)
        #all_sprites.add(LcarsButton(colours.ORANGE, "btn", (200, 460), "ON", self.frontdoorlightson), layer=5)
        #all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (200, 610), "OFF", self.frontdoorlightsoff), layer=5)
        #all_sprites.add(LcarsText(colours.ORANGE, (260, 175), "Verandah", 2), layer=5)
        #all_sprites.add(LcarsButton(colours.ORANGE, "btn", (260, 460), "ON", self.verandahlightson), layer=5)
        #all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (260, 610), "OFF", self.verandahlightsoff), layer=5)
        #all_sprites.add(LcarsText(colours.ORANGE, (320, 175), "Garden", 2), layer=5)
        #all_sprites.add(LcarsButton(colours.ORANGE, "btn", (320, 460), "ON", self.gardenlightson), layer=5)
        #all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (320, 610), "OFF", self.gardenlightsoff), layer=5)

        self.bedroom = all_sprites.get_sprites_from_layer(5)
        self.toggle_sprites(self.outside, False)
        self.toggle_sprites(self.bedroom, False)


        # SFX
        self.beep1 = Sound("/home/pi/rpi_lcars/assets/audio/panel/201.wav")
        Sound("/home/pi/rpi_lcars/assets/audio/hail_2.wav").play()

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("{}".format(datetime.now().strftime("%a %b %d, %Y - %X")))
            self.lastClockUpdate = pygame.time.get_ticks()
        LcarsScreen.update(self, screenSurface, fpsClock)

    def handleEvents(self, event, fpsClock):
        LcarsScreen.handleEvents(self, event, fpsClock)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.beep1.play()

        if event.type == pygame.MOUSEBUTTONUP:
            return False

    # Button functions
    def display_hw(self, item, event, clock):
        self.toggle_sprites(self.hw, True)
        self.toggle_sprites(self.outside, False)
        self.toggle_sprites(self.bedroom, False)

    def display_outside(self, item, event, clock):
        self.toggle_sprites(self.hw, False)
        self.toggle_sprites(self.outside, True)
        self.toggle_sprites(self.bedroom, False)
    
    def display_bedroom(self, item, event, clock):
        self.toggle_sprites(self.hw, False)
        self.toggle_sprites(self.outside, False)
        self.toggle_sprites(self.bedroom, True)


    def toggle_sprites(self, object, status):
        for sprite in object:
            sprite.visible = status

    def nullfunction(self, item, event, clock):
        print("I am a fish.")

    def logoutHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())

    def reboot(self, item, event, clock):
        subprocess.call(["reboot"])

    def shutdown(self, item, event, clock):
        subprocess.call(["shutdown"])
    
    def alllightson(self, item, event, clock):
        self.client1.publish("house/lights/all", "on")
    
    def alllightsoff(self, item, event, clock):
        self.client1.publish("house/lights/all", "off")

    def outsidelightson(self, item, event, clock):
        self.client1.publish("house/lights/outside", "on")
    
    def outsidelightsoff(self, item, event, clock):
        self.client1.publish("house/lights/outside", "off")
    
    def livingroomlightson(self, item, event, clock):
        self.client1.publish("house/lights/livingroom", "on")
    
    def livingroomlightsoff(self, item, event, clock):
        self.client1.publish("house/lights/livingroom", "off")
    
    def frontdoorlightson(self, item, event, clock):
        self.client1.publish("house/lights/frontdoor", "on")
    
    def frontdoorlightsoff(self, item, event, clock):
        self.client1.publish("house/lights/frontdoor", "off")
    
    def verandahlightson(self, item, event, clock):
        self.client1.publish("house/lights/verandah", "on")
    
    def verandahlightsoff(self, item, event, clock):
        self.client1.publish("house/lights/verandah", "off")
    
    def gardenlightson(self, item, event, clock):
        self.client1.publish("house/lights/garden", "on")
    
    def gardenlightsoff(self, item, event, clock):
        self.client1.publish("house/lights/garden", "off")
    
    def allbedroomlightson(self, item, event, clock):
        self.client1.publish("house/lights/bedroom", "on")
    
    def allbedroomlightsoff(self, item, event, clock):
        self.client1.publish("house/lights/bedroom", "off")

    def exit(self, item, event, clock):
        sys.exit()
