from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui.utils.loadinfo import *

from ui import colours
from ui.widgets.background import LcarsBackgroundImage, LcarsImage
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton
from ui.widgets.screen import LcarsScreen
from ui.widgets.sprite import LcarsMoveToMouse

class ScreenMain(LcarsScreen):
    def setup(self, all_sprites):
        # Load standard LCARS BG image
        all_sprites.add(LcarsBackgroundImage("assets/lcars_bg.png"), layer=0)

        # Setup time/date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "LCARS 1123"), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "MAIN MENU", 2), layer=1)

        # Buttons
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 662), "LOGOUT", self.load_idle), layer=4)
        all_sprites.add(LcarsButton(colours.BEIGE, "nav", (145, 15), "ENVIRO", self.load_enviro), layer=4)
        all_sprites.add(LcarsButton(colours.PURPLE, "nav", (200, 15), "NETWORK", self.load_network), layer=4)
        all_sprites.add(LcarsButton(colours.BLUE, "nav", (255, 15), "POWER", self.load_power), layer=4)
        all_sprites.add(LcarsButton(colours.ORANGE, "nav", (310, 15), "OPERATIONS", self.load_auth), layer=4)
        all_sprites.add(LcarsButton(colours.PEACH, "nav", (365, 15), "", self.load_template), layer=4)

        # Load data from file
        returnpayload = read_txt("/var/lib/lcars/alert")

        all_sprites.add(LcarsText(colours.ORANGE, (137, 133), returnpayload[0], 1.8), layer=3)

        # Loop through results
        index = 1
        ypos = 190
        while index < 5:
            all_sprites.add(LcarsText(colours.BLUE, (ypos, 150), returnpayload[index], 1.5), layer=3)
            # Bump index and vertical pos
            index += 1
            ypos += 50

        self.info_text = all_sprites.get_sprites_from_layer(3)

        # Rotating Deep Space 9
        all_sprites.add(LcarsGifImage("assets/animated/ds9_3d.gif", (148, 475), 100), layer=1)

        self.beep1 = Sound("assets/audio/panel/201.wav")
        Sound("assets/audio/panel/220.wav").play()

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

    def nullfunction(self, item, event, clock):
        print("I am a fish.")

    def load_template(self, item, event, clock):
        from screens.template import ScreenTemplate
        self.loadScreen(ScreenTemplate())

#    def load_auth(self, item, event, clock):
#        from screens.authorize import ScreenAuthorize
#        self.loadScreen(ScreenAuthorize())

    def load_auth(self, item, event, clock):
        from screens.ops import ScreenOps
        self.loadScreen(ScreenOps())

    def load_power(self, item, event, clock):
        from screens.power import ScreenPower
        self.loadScreen(ScreenPower())

    def load_idle(self, item, event, clock):
        from screens.idle import ScreenIdle
        self.loadScreen(ScreenIdle())

    def load_network(self, item, event, clock):
        from screens.network import ScreenNetwork
        self.loadScreen(ScreenNetwork())

    def load_enviro(self, item, event, clock):
        from screens.enviro import ScreenEnviro
        self.loadScreen(ScreenEnviro())
