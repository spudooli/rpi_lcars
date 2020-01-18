from datetime import datetime
import pygame
from pygame.mixer import Sound

from ui.utils.loadinfo import *
from ui.colours import randomcolor
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
        all_sprites.add(LcarsBackgroundImage("/home/pi/rpi_lcars/assets/lcars_bg.png"), layer=0)

        # Setup time/date display
        self.stardate = LcarsText(colours.BLUE, (12, 380), "", 1.5)
        self.lastClockUpdate = 0
        all_sprites.add(self.stardate, layer=1)

        self.lastbalanceupdate = 0
        self.lastPowerUpdate = 0

        self.indoorTemperaturelabel = LcarsText(colours.BLUE, (163, 182), "INSIDE", 1.2)
        self.indoorTemperature = LcarsText(colours.BLUE, (173, 182), "", 4)
        all_sprites.add(self.indoorTemperature, layer=1)
        all_sprites.add(self.indoorTemperaturelabel, layer=1)

        self.outdoorTemperaturelabel = LcarsText(colours.BLUE, (130, 286), "OUTSIDE", 1.2)
        self.outdoorTemperature = LcarsText(colours.BLUE, (140, 286), "", 4)
        all_sprites.add(self.outdoorTemperature, layer=1)
        all_sprites.add(self.outdoorTemperaturelabel, layer=1)

        self.powerlabel = LcarsText(colours.BLUE, (130, 415), "POWER", 1.2)
        self.power = LcarsText(colours.BLUE, (140, 415), "", 4)
        all_sprites.add(self.power, layer=1)
        all_sprites.add(self.powerlabel, layer=1)

        self.bankaccountlabel = LcarsText(colours.BLUE, (130, 600), "BANK", 1.2)
        self.bankaccount = LcarsText(colours.BLUE, (140, 600), "", 4)
        all_sprites.add(self.bankaccount, layer=1)
        all_sprites.add(self.bankaccountlabel, layer=1)

        # Static text
        all_sprites.add(LcarsText(colours.BLACK, (8, 40), "SPUDOOLI", 1.2), layer=1)
        all_sprites.add(LcarsText(colours.ORANGE, (0, 135), "", 2), layer=1)

        # Buttons
        all_sprites.add(LcarsButton(colours.RED_BROWN, "btn", (6, 660), "LOGOUT", self.load_idle), layer=4)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (145, 15), "LIGHTS", self.load_lights), layer=4)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (200, 15), "WEATHER", self.load_weather), layer=4)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (255, 15), "SENSORS", self.load_sensors), layer=4)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (310, 15), "OPERATIONS", self.load_auth), layer=4)
        all_sprites.add(LcarsButton(randomcolor(), "nav", (365, 15), "", self.load_network), layer=4)

        self.bankaccount.setText(get_statusfiledata("otherbalance").split(".")[0])
        self.power.setText(get_statusfiledata("power"))
        self.indoorTemperature.setText(get_statusfiledata("indoorTemperature"))
        self.outdoorTemperature.setText(get_statusfiledata("outdoorTemperature"))

        # Rotating Deep Space 9
        #all_sprites.add(LcarsGifImage("/home/pi/rpi_lcars/assets/animated/ds9_3d.gif", (148, 475), 100), layer=1)

        self.beep1 = Sound("/home/pi/rpi_lcars/assets/audio/panel/201.wav")
        Sound("/home/pi/rpi_lcars/assets/audio/panel/220.wav").play()

    def update(self, screenSurface, fpsClock):
        if pygame.time.get_ticks() - self.lastClockUpdate > 1000:
            self.stardate.setText("{}".format(datetime.now().strftime("%a %b %d, %Y - %X")))
            self.lastClockUpdate = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.lastbalanceupdate > 1800000:
            self.bankaccount.setText(get_statusfiledata("otherbalance").split(".")[0])
            self.lastbalanceupdate = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.lastPowerUpdate > 60000:
            self.power.setText(get_statusfiledata("power"))
            self.indoorTemperature.setText(get_statusfiledata("indoorTemperature"))
            self.outdoorTemperature.setText(get_statusfiledata("outdoorTemperature"))
            self.lastPowerUpdate = pygame.time.get_ticks()
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

    def load_sensors(self, item, event, clock):
        from screens.sensors import ScreenSensors
        self.loadScreen(ScreenSensors())

    def load_idle(self, item, event, clock):
        from screens.idle import ScreenIdle
        self.loadScreen(ScreenIdle())

    def load_network(self, item, event, clock):
        from screens.network import ScreenNetwork
        self.loadScreen(ScreenNetwork())

    def load_weather(self, item, event, clock):
        from screens.weather import ScreenWeather
        self.loadScreen(ScreenWeather())

    def load_lights(self, item, event, clock):
        from screens.lights import ScreenLights
        self.loadScreen(ScreenLights())
