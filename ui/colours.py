from random import randint

# Solid colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

# Standard LCARS colors
ORANGE = 255, 153, 0
PURPLE = 204, 153, 204
GREY_BLUE = 153, 153, 204
RED_BROWN = 204, 102, 102
BEIGE = 255, 204, 153
BLUE = 153, 153, 255
PEACH = 255, 153, 102
PINK = 204, 102, 153

# Return randomized LCARS color
def randomcolor():
    # Generate random number between 0 and 7
    rand = randint(0,7)

    if rand == 0:
        RANDCOLOR = ORANGE
    elif rand == 1:
        RANDCOLOR = PURPLE
    elif rand == 2:
        RANDCOLOR = GREY_BLUE
    elif rand == 3:
        RANDCOLOR = RED_BROWN
    elif rand == 4:
        RANDCOLOR = BEIGE
    elif rand == 5:
        RANDCOLOR = BLUE
    elif rand == 6:
        RANDCOLOR = PEACH
    elif rand == 7:
        RANDCOLOR = PINK

    return RANDCOLOR;
