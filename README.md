# pil-widget
PIL graphic widgets for use on small eink and other displays

## RadialBar

from radialbar import RadialBar

Creates a PIL image of a radial progress bar. Limits can be set and colours defined as required.
Designed for e-ink screens; Papirus and Inky pHat

### __init__

Lots of parameters for the initialiser. All are optional

size - a tuple to define the width and height of the widget

width - width of the progress bar in pixels

padding - border padding in pixels around the indicator

title - optional text title. Set to None if not required

units - optional text to display after the value. Set to None to hide

imgtype - specify the type of PIL image required. See PIL libary for all options

barcol - colour of the progress bar. Needs to correspond to the image type

valuecol - colour of the value text displayed centrally in the widget

titlecol - colour of the title text

fillcol - colour to use for the internal circle

bgcol - colour of the background surrounding the progress control. This is also the title background

outlinecol - colour to use for circle outlines

emptycol - colour for the empty parts of the progress bar

font - file name of a true type font to use for the font face. Defaults to use the free font library

fontsize - size to use for the title and value text

### set_font(fontname, size)
Specify the file name to use for the font and required size. Overrides the values set in __init__

### square_indicator()
Sets the display of the progress bar to have equal height and width which is more eye pleasing

### scalable_indicator()
The progress widget can be an ellipse shape to fit the full extent of the widget canvas

### set_range(minval, maxval)
Specify float values of the minimum value and maximum values represented in the widget. Values can be outside these ranges without error.

### render()
Returns a PIL image which can be used to display the control. Renders to all settings and current value.

### Attributes
#### precision (read/write)
define the number of decimal places to show

#### size (read)
Read the size of the widget image. The overall size cannot change once the widget has been created.

#### title (read/write)
Set the title text to display. Text longer than the widget will appear clipped.
Empty string or a None value will remove the title.

#### unit (read/write)
Set the unit specifier which follows the value number. Set to None or an empty string to remove.

#### bar_width (read/write)
Change or read the bar width set for the widget. Changes will be reflected in the next call to render()
Can throw exceptions.

#### padding (read/write)
Query or change the padding value used to render the graphic. Pads edges around the indicator graphic

#### value (read/write)
Set or read the integer or floating value specified for the control. Integer values will not display a decimal point. Floating point numbers will display according to the precision attribute.

#### bar_col (read/write)
Read or write the colour of the progress bar

#### empty_col (read/write)
Read or write the colour of the empty part of the progress bar

#### value_col (read/write)
Read or write the colour of the value text

#### title_col (read/write)
Read or write the colour of the title text

#### fill_col (read/write)
Read or write the colour to use for the internal fill (background of the value)

#### background_col (read/write)
Read or write the colour to use for the widget background (remaining canvas colour)

#### outline_col (read/write)
Read or write the colour to use for outlines of the progress bar





