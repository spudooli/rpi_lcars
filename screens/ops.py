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
class ScreenOps(LcarsScreen):
    def setup(self, all_sprites):
        # Load BG image
        all_sprites.add(LcarsBackgroundImage("assets/lcars_bg.png"), layer=0)

        # Time/Date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "LCARS 1123"), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "OPERATIONS", 2), layer=1)

        # Interfaces
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 660), "MAIN", self.logoutHandler), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (145, 15), "TERMINAL", self.display_hw), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (200, 15), "LCARS UI", self.display_lcars), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (255, 15), "BUTTON 3", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (310, 15), "BUTTON 4", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (365, 15), "", self.nullfunction), layer=2)

        # Local hardware
        all_sprites.add(LcarsText(colours.ORANGE, (140, 175), "UPTIME", 2), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (200, 175), get_uptime(), 2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (260, 175), "SYSTEM LOAD AVG", 2), layer=3)
        all_sprites.add(LcarsText(colours.BLUE, (320, 175), get_load(), 2), layer=3)
        all_sprites.add(LcarsButton(colours.ORANGE, "btn", (380, 175), "REBOOT", self.reboot), layer=3)
        all_sprites.add(LcarsButton(colours.RED, "btn", (380, 350), "SHUTDOWN", self.shutdown), layer=3)
        self.hw = all_sprites.get_sprites_from_layer(3)

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
