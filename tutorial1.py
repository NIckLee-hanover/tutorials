from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# color variabls
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# 1 Pixel wide line
thinline = LineStyle(1, black)
# rectangle
rectangle = RectangleAsset(50, 50, 100, 100 thinline, blue)

# display a rectangle
Sprite(rectangle)

myapp = App()
myapp.run()