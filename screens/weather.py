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
class ScreenWeather(LcarsScreen):
    def setup(self, all_sprites):
        # Load BG image
        all_sprites.add(LcarsBackgroundImage("assets/lcars_bg.png"), layer=0)

        # Time/Date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "SPUDOOLI", 1.2), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (4, 135), "WEATHER", 2), layer=1)

        # Interfaces
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 660), "MAIN", self.logoutHandler), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (145, 15), "", self.display_hw), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (200, 15), "", self.display_lcars), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (255, 15), "", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (310, 15), "", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (365, 15), "", self.nullfunction), layer=2)

        # Load data from file
        returnpayload = read_txt("/home/pi/rpi_lcars/scripts/weather.txt")

        # First line in file is always going to be heading
        all_sprites.add(LcarsText(colours.ORANGE, (137, 133), returnpayload[0], 1.8), layer=3)

        # Loop through results starting at second element
        index = 1
        ypos = 190
        while index < len(returnpayload):
            all_sprites.add(LcarsText(colours.BLUE, (ypos, 150), returnpayload[index], 1.5), layer=3)
            # Bump index and vertical pos
            index += 1
            ypos += 50

        # SFX
        self.beep1 = Sound("assets/audio/panel/201.wav")
        Sound("assets/audio/hail_2.wav").play()

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

    def exit(self, item, event, clock):
        sys.exit()
