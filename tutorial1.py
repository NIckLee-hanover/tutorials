from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# color variabls
red = Color(0xff0000, 0.7)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

# 1 Pixel wide line
thinline = LineStyle(1, black)
# rectangle
rectangle = RectangleAsset(50, 50, thinline, blue)
ellipse = EllipseAsset(25, 25, thinline, blue)
polygon = PolygonAsset([(15,60), (75,60), (90,0), (45,-30), (0,0)], thinline, red)

# display the shapes
Sprite(rectangle, (0,0))
Sprite(rectangle, (25,25))
Sprite(ellipse, (100,100))
Sprite(polygon, (80,80))

myapp = App()
myapp.run()