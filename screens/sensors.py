from subprocess import call
from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui.utils.loadinfo import *
from ui.colours import randomcolor
import sys

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton
from ui.widgets.screen import LcarsScreen

# Need to change class name to whatever screen is to be called
class ScreenSensors(LcarsScreen):
    def setup(self, all_sprites):
        # Load BG image
        all_sprites.add(LcarsBackgroundImage("/home/pi/rpi_lcars/assets/lcars_bg.png"), layer=0)

        # Time/Date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "SPUDOOLI"), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (4, 135), "SENSORS", 2), layer=1)

        # Interfaces
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 660), "MAIN", self.logoutHandler), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (145, 15), "ENVIRO", self.display_hw), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (200, 15), "MONEY", self.display_lcars), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (255, 15), "", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (310, 15), "", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (365, 15), "", self.nullfunction), layer=2)

        # Local hardware
        all_sprites.add(LcarsText(colours.ORANGE, (145, 175), "Inside Temperature", 1.4), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (165, 300), get_statusfiledata("indoorTemperature"), 2.2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (140, 390), "Outside Temperature", 1.4), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (165, 520), get_outdoortemperature(), 2.2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (140, 610), "Pressure hPa", 1.4), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (165, 663), get_indoorPressure(), 2.2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 175), "Outside Temperature", 1.4), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (249, 300), get_outdoortemperature(), 2.2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (222, 390), "Kitchen Temperature", 1.4), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (249, 520), get_kitchentemperature(), 2.2), layer=3)

        self.hw = all_sprites.get_sprites_from_layer(3)

        # Add a little flair
        all_sprites.add(LcarsGifImage("assets/animated/fwscan.gif", (320, 556), 100), layer=3)

        # LCARS UI
        # Check for update
        if update_available() == False:
            all_sprites.add(LcarsText(colours.ORANGE, (140, 175), "LATEST VERSION INSTALLED", 2), layer=4)
        elif update_available() == True:
            all_sprites.add(LcarsText(colours.ORANGE, (140, 175), "UPDATE AVAILABLE", 2), layer=4)
            all_sprites.add(LcarsButton(colours.BLUE, "btn", (200, 175), "UPDATE LCARS", self.git_pull), layer=4)

        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (260, 175), "RESTART LCARS", self.exit), layer=4)
        self.lcars = all_sprites.get_sprites_from_layer(4)
        self.toggle_sprites(self.lcars, False)


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
        self.toggle_sprites(self.lcars, False)

    def display_lcars(self, item, event, clock):
        self.toggle_sprites(self.hw, False)
        self.toggle_sprites(self.lcars, True)

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

    def git_pull(self, item, event, clock):
        subprocess.call(["git", "pull"])
        # Force LCARS restart
        sys.exit()

    def exit(self, item, event, clock):
        sys.exit()
