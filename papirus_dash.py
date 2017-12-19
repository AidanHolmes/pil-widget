#!/usr/bin/env python

#    Example code to use the RadialBar class with a Papirus screen
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
from papirus import Papirus
from radialbar import RadialBar

eink = Papirus(rotation=180)

border = 5

indicator1 = RadialBar(title="Temperature #1",
                       size=(eink.size[1] - (border*2), eink.size[1] - (border*2)),
                       width=10,
                       imgtype='1',
                       barcol=0,
                       emptycol=1,
                       fillcol=1,
                       bgcol=1,
                       valuecol=0,
                       outlinecol=0,
                       titlecol=0)

indicator1.set_range(10,26)
indicator1.unit = u"\N{DEGREE SIGN}C"
indicator1.value = 18.775

indicator2 = RadialBar(title=None,
                       size=(eink.size[1] - (border*2), eink.size[1] - (border*2)),
                       width=10,
                       imgtype='1',
                       barcol=0,
                       emptycol=1,
                       fillcol=1,
                       bgcol=1,
                       valuecol=0,
                       outlinecol=0,
                       titlecol=0)

indicator2.set_range(15,35)
indicator2.unit = u"\N{DEGREE SIGN}C"
indicator2.value = 20.2

img = Image.new('1', eink.size, 1)

img.paste(indicator1.render(), (border,border))
img.paste(indicator2.render(), (border*2+indicator1.size[0],border))

eink.display(img)
eink.update()

for i in range(10,27):
    indicator1.value = i
    indicator2.value = indicator2.value + 0.6
    if indicator2.value > 28:
        indicator2.fill_col = abs(indicator2.fill_col - 1)
        indicator2.value_col = abs(indicator2.value_col - 1)
    
    img.paste(indicator2.render(), (border*2+indicator1.size[0],border))
    img.paste(indicator1.render(), (border,border))
    eink.display(img)
    eink.partial_update()
    
