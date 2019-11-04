from graphics import *
from math import *

x0, y0 = 100, 27
r = 50
h, l = 500, 500
win = GraphWin("Rolling_ball", 1000, 1000)
theta = (sqrt((h ** 2) + (l ** 2)) * 360) / (pi * l * 2 * r)
b = l
for x in range(100, 1000):
    rad1 = theta * 3.14 / 180
    rad2 = (theta + 90) * 3.14 / 180
    # drawing the wedge
    Line(Point(100, 100), Point(100, 100 + h)).draw(win)
    Line(Point(100, 100 + h), Point(1000, 100 + h)).draw(win)
    Line(Point(100, 100), Point(100 + l, 100 + h)).draw(win)

    # drawing the circle
    Circle(Point(x0, y0), 50).draw(win)
    # drawing the spikes of the circle
    Line(Point(x0, y0), Point(x0 + r * sin(rad1), y0 + r * cos(rad1))).draw(win)
    Line(Point(x0, y0), Point(x0 + r * sin(rad2), y0 + r * cos(rad2))).draw(win)
    Line(Point(x0, y0), Point(x0 - r * sin(rad1), y0 - r * cos(rad1))).draw(win)
    Line(Point(x0, y0), Point(x0 - r * sin(rad2), y0 - r * cos(rad2))).draw(win)
    # win.delete("all")
    # theta-=8
    # time.sleep(.1)
    x0 = x
    if 120 + l <= x < 900:
        win.delete("all")
        theta -= 6.5 * x / b
        b += 10
        time.sleep(b / (150 * x))

    elif x < 125 + l:
        win.delete("all")
        y0 += h / l
        theta -= 7.5 * x / l
        time.sleep(l / (150 * x))
    else:
        win.getMouse()
        break

win.getMouse()
win.close()
