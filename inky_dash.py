#!/usr/bin/env python

#    Example code to use the RadialBar class with an Inky pHat screen
#    Copyright (C) 2017  Aidan Holmes
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Email - aholmes@orbitalfruit.co.uk

from PIL import Image
import inkyphat
import time
from radialbar import RadialBar

border = 5
inkyphat.set_border(inkyphat.BLACK)

# Create 2 indicators and set values
indicator = RadialBar(title="Fermenter",
                      imgtype='P',
                      size=((inkyphat.HEIGHT)-(border*2),inkyphat.HEIGHT-(border*2)),
                      width=15,
                      font = inkyphat.fonts.PressStart2P,
                      fontsize=8,
                      emptycol=inkyphat.WHITE,
                      barcol=inkyphat.RED,
                      titlecol=inkyphat.BLACK,
                      valuecol=inkyphat.BLACK,
                      fillcol=inkyphat.WHITE,
                      outlinecol=inkyphat.BLACK,
                      bgcol=inkyphat.WHITE)

indicator.set_range(10, 25)
indicator.unit = u"\N{DEGREE SIGN}C"
indicator.value = 18.775

indicator2 = RadialBar(title="Carbonation",
                      imgtype='P',
                       font = inkyphat.fonts.PressStart2P,
                       size=((inkyphat.HEIGHT)-(border*2),inkyphat.HEIGHT-(border*2)),
                       width=10,
                       fontsize=8,
                       emptycol=inkyphat.WHITE,
                       barcol=inkyphat.RED,
                       titlecol=inkyphat.BLACK,
                       valuecol=inkyphat.WHITE,
                       fillcol=inkyphat.BLACK,
                       outlinecol=inkyphat.BLACK,
                       bgcol=inkyphat.WHITE)

indicator2.set_range(15, 35)
indicator2.unit = u"\N{DEGREE SIGN}C"
indicator2.value = 21.23

img = Image.new('P', (inkyphat.WIDTH, inkyphat.HEIGHT))

img.paste(indicator.render(), (border,border))
img.paste(indicator2.render(), (inkyphat.WIDTH/2,border))

inkyphat.set_image(img)
inkyphat.show()

time.sleep(1)

# Change bar appearance and reshow
indicator2.value = 30.3
indicator2.bar_col = inkyphat.RED

img.paste(indicator.render(), (border,border))
img.paste(indicator2.render(), (inkyphat.WIDTH/2,border))

inkyphat.set_image(img)
inkyphat.show()
