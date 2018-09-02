
from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

import math

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

thinline = LineStyle(1, black)
bluecircle = CircleAsset(7,thinline, blue)
whitecircle = CircleAsset(7,thinline, white)
redcircle = CircleAsset(7,thinline, red)
xcoordinates = range(100, 600, 10)

sprites = [Sprite(redcircle, (x, x*0.5 + 100)) for x in xcoordinates]
sprites = [Sprite(whitecircle, (x, x*0.5 + 120)) for x in xcoordinates]
sprites = [Sprite(bluecircle, (x, x*0.5 + 140)) for x in xcoordinates]

myapp = App()
myapp.run()