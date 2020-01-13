![screenshot](screenshot.png)

# Raspberry Pi LCARS Interface
This project is an attempt to create a functional [LCARS](https://en.wikipedia.org/wiki/LCARS) interface for the [Raspberry Pi](https://raspberrypi.org/) using [Pygame](http://www.pygame.org). It's based heavily on the pioneering work of [Toby Kurien](https://tobykurien.com/) and forked from [HoECoder](https://github.com/HoECoder/rpi_lcars).

# Changes/Additions
- Functional navigation buttons on side panel
- Raspberry Pi touchscreen Backlight control with physical button and [rpi_backlight](https://github.com/linusg/rpi-backlight)
- Light control (actually everything control) publishing to mqtt


# Branches
The master branch of this repository is the code running on my personal hardware setup. It may or may not be useful for others as-is. The secondary "core" branch is intended to be suitable for upstream merges or for other users who wish to customize their own version.

Changes made in "core" will, whenever possible, retain backwards compatibility with the original code.

# Acknowledgements
- Orignal code by Toby Kurien
- Forked from [HoECoder](https://github.com/HoECoder/rpi_lcars)
- Deep Space 9 3D model by [David Metlesits](http://thefirstfleet.deviantart.com/)
- LCARS images and audio assets from [lcarscom.net](http://www.lcarscom.net)
- LCARS is copyright [CBS Studios Inc.](http://www.cbs.com/) and is subject to [the fair use statute](http://www.lcars.mobi/legal/)

# License
> **Note**: Original code from Toby Kurien was released under the MIT license. HoECoder invoked the right to sublicense that project and have released this fork under the GPLv3. For merging purposes, the "core" branch retains its original MIT license. I retain the same license.

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.

![](https://www.gnu.org/graphics/gplv3-127x51.png)

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For details, see the file "COPYING" in the source directory.
