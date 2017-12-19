#    RadialBar widget for Python PIL Images. Shows float and integer values along with progress
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


from PIL import Image, ImageDraw, ImageFont

class RadialBar(object):

    def __init__(self, size=(50,50), width=4, title=None, units=None, imgtype='P',
                 barcol=0, valuecol=1, fillcol=2, bgcol = 1, outlinecol=1, emptycol=2, titlecol=1,
                 font = 'FreeSans.ttf', fontsize=12):
        self._size = (size[0]-1, size[1]-1) # use size as min and max pixel extents
        self.title = title
        self.unit = units
        self.bar_width = width
        self._bar = barcol
        self._text = valuecol
        self._titlecol = titlecol
        self._fill = fillcol
        self._background = bgcol
        self._outline = outlinecol
        self._nobar = emptycol
        self._imgtype = imgtype 
        self._isint = True
        self._val = 0.0
        self._minval = 0.0
        self._maxval = 100.0
        self._precision = 1
        self._squareindicator = True

        self._img = Image.new(imgtype, size)
        self._draw = ImageDraw.Draw(self._img)
        self.set_font(font, fontsize)

    @property
    def bar_col(self):
        return self._bar

    @bar_col.setter
    def bar_col(self,val):
        self._bar = val

    @property
    def empty_col(self):
        return self._nobar

    @empty_col.setter
    def empty_col(self,val):
        self._nobar = val

    @property
    def value_col(self):
        return self._text

    @value_col.setter
    def value_col(self,val):
        self._text = val

    @property
    def title_col(self):
        return self._titlecol

    @title_col.setter
    def title_col(self,val):
        self._titlecol = val

    @property
    def fill_col(self):
        return self._fill

    @fill_col.setter
    def fill_col(self,val):
        self._fill = val

    @property
    def background_col(self):
        return self._background

    @background_col.setter
    def background_col(self,val):
        self._background = val

    @property
    def outline_col(self):
        return self._outline

    @outline_col.setter
    def outline_col(self,val):
        self._outline = val
        
    @property
    def size(self):
        return self._img.size

    def set_font(self, fontname, size):
        self._font = ImageFont.truetype(fontname, size)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title == '':
            self._title = None
        self._title = title

    @property
    def unit(self):
        return self._units

    @unit.setter
    def unit(self, units):
        if units is None:
            self._units = ''
        else:
            self._units = units

    @property
    def bar_width(self):
        return self._width

    @bar_width.setter
    def bar_width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if width < 0:
            raise ValueError("Width must be a positive value")
        self._width = width

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self, val):
        self._isint = isinstance(val, int)
        self._val = float(val)

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, points):
        if points < 0:
            raise ValueError("Precision must be a positive integer")
        self._precision = points

    def square_indicator(self):
        self._squareindicator = True

    def scalable_indicator(self):
        self._squareindicator = False
        
    def set_range(self, minval, maxval):
        if minval > maxval:
            raise ValueError("Min value greater than Max value")

        self._minval = float(minval)
        self._maxval = float(maxval)

    def define_bounding_area(self):
        # Render title text if a title has been defined
        titleheight = 0
        if not self._title is None:
            w, h = self._font.getsize(self._title)
            titleheight = h + 1 # Add 1px border
            xtxt = (self._size[0] - w) / 2
            self._draw.text( (xtxt,0), self._title, fill=self._titlecol, font=self._font)

        x_top = 0
        y_top = titleheight
        x_bottom = self._size[0]
        y_bottom = self._size[1]
        if self._squareindicator:
            # even the sides to appear circular and centred
            # Which is the shortest side?
            width = (x_bottom - x_top)
            height = (y_bottom - y_top)
            if width > height: 
                # Scale width
                x_top = x_top + ((width - height) / 2)
                x_bottom = x_bottom - ((width - height) / 2)
            elif height > width:
                # Scale height
                y_top = y_top + ((height - width) / 2)
                y_bottom = y_bottom - ((height - width) / 2)
            #else they are the same and do nothing

        return ((x_top,y_top),(x_bottom,y_bottom))

        
    def render(self):
        'Render and return a PIL image'
        rng = self._maxval - self._minval

        degree = 0
        if (self._val <= self._minval): degree = 0
        elif (self._val >= self._maxval): degree = 360
        else:
            degree = ((self._val - self._minval) * 360) / rng

        degree_end = (degree - 90)
        if degree_end < 0:
            degree_end = 270 + degree
        
        # Clear background for entire image
        self._draw.rectangle(((0,0),self._size), fill=self._background)

        bounds = self.define_bounding_area()

        # Exception, if zero degrees then skip rendering the bar
        if degree == 0:
            self._draw.ellipse( (bounds[0], bounds[1]), fill=self._nobar)
        else: # Render the progress bar
            self._draw.ellipse( (bounds[0], bounds[1]), fill=self._bar)
            if not degree == 360:
                # Overwrite the indicator with a pie slice unless it's totally full
                self._draw.pieslice( (bounds[0], bounds[1]), degree_end, 270, self._nobar)

        # Draw internal ellipse
        self._draw.ellipse(((self._width+bounds[0][0],self._width+bounds[0][1]),
                            (bounds[1][0]-self._width, bounds[1][1]-self._width)),
                           fill=self._fill, outline=self._outline)

        # Draw final border around external ellipse
        self._draw.ellipse( (bounds[0], bounds[1]), fill=None, outline=self._outline)

        # Format number as integer or floating point according to defined precision
        txtformat = '{0:.0f}{1}'
        if not self._isint:
            txtformat = '{0:.' + "{0:d}".format(self._precision) + 'f}{1}'

        # Encode/decode UTF8 dance (needed for such things as degree symbols)
        txt = txtformat.format(self._val, self._units.encode('utf-8')).decode('utf-8')                               
        w, h = self._font.getsize(txt)

        # render text centrally
        x = bounds[0][0] + (((bounds[1][0] - bounds[0][0]) - w) /2)
        y = bounds[0][1] + (((bounds[1][1] - bounds[0][1]) - h) /2)
        
        self._draw.text( (x,y), txt, fill=self._text, font=self._font)

        # Return the rendered image
        return self._img
        
