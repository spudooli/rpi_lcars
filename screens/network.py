from subprocess import call
from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui.utils.loadinfo import *

from ui import colours
from ui.widgets.background import LcarsBackgroundImage
from ui.widgets.lcars_widgets import LcarsText, LcarsButton
from ui.widgets.gifimage import LcarsGifImage
from ui.widgets.screen import LcarsScreen

class ScreenNetwork(LcarsScreen):
    def setup(self, all_sprites):
        # Load BG image
        all_sprites.add(LcarsBackgroundImage("assets/lcars_bg.png"), layer=0)

        # Time/Date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "LCARS 1123"), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "NETWORK STATUS", 2), layer=1)

        # Interfaces
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 662), "MAIN", self.logoutHandler), layer=2)
        all_sprites.add(LcarsButton(colours.BEIGE, "nav", (145, 15), "ROUTERS", self.display_routers), layer=2)
        all_sprites.add(LcarsButton(colours.PURPLE, "nav", (200, 15), "SERVERS", self.display_server), layer=2)
        all_sprites.add(LcarsButton(colours.BLUE, "nav", (255, 15), "SENSORS", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(colours.ORANGE, "nav", (310, 15), "STBS", self.nullfunction), layer=2)
        all_sprites.add(LcarsButton(colours.PEACH, "nav", (365, 15), "", self.nullfunction), layer=2)

        # Router heading
        all_sprites.add(LcarsText(colours.ORANGE, (140, 175), "IP ADDRESS", 2), layer=3)
        all_sprites.add(LcarsText(colours.ORANGE, (140, 400), "STATUS", 2), layer=3)
        all_sprites.add(LcarsGifImage("assets/animated/fwscan.gif", (320, 556), 100), layer=3)

        # Load data from file
        returnpayload = read_csv("/var/lib/lcars/routers")

        # Loop through results
        index = 0
        ypos = 200
        while index < 4:
            currentstatus = get_ip_status(returnpayload, index)
            all_sprites.add(LcarsText(colours.BLUE, (ypos, 175), currentstatus['ip'], 2), layer=3)

            # Change color based on status
            if currentstatus['status'] == "ONLINE":
                all_sprites.add(LcarsText(colours.GREEN, (ypos, 400), "ONLINE", 2), layer=3)
            else:
                all_sprites.add(LcarsText(colours.RED, (ypos, 400), "OFFLINE", 2), layer=3)

            # Bump index and vertical pos
            index += 1
            ypos += 50

        # Save layer
        self.routers = all_sprites.get_sprites_from_layer(3)

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
    def display_routers(self, item, event, clock):
        self.show_routers()

    def display_server(self, item, event, clock):
        self.hide_routers()

    def hide_routers(self):
        for sprite in self.routers:
            sprite.visible = False

    def show_routers(self):
        for sprite in self.routers:
            sprite.visible = True

    def hide_sensors(self):
        if self.sensors[0].visible:
            for sprite in self.sensors:
                sprite.visible = False

    def nullfunction(self, item, event, clock):
        print("I am a fish.")

    def logoutHandler(self, item, event, clock):
        from screens.main import ScreenMain
        self.loadScreen(ScreenMain())
