from graphics import *
from sys import setrecursionlimit

setrecursionlimit(18000)

win = GraphWin("Filling the Colors in Life", 600, 600)
win.setBackground("Black")


def getColor(x, y):
    overlapping = win.find_overlapping(x, y, x + 1, y)
    if overlapping:
        return win.itemcget(overlapping[-1], "fill")
    else:
        return color_rgb(0, 0, 0)


def floodFill(x, y):
    color = getColor(x, y)
    if color == "#000000":
        win.plotPixel(x, y, "White")
        floodFill(x + 1, y)
        floodFill(x - 1, y)
        floodFill(x + 1, y + 1)
        floodFill(x + 1, y - 1)
        floodFill(x - 1, y + 1)
        floodFill(x - 1, y - 1)
        floodFill(x, y + 1)
        floodFill(x, y - 1)


def drawCircle():
    Circle(Point(200, 200), 100).draw(win)
    floodFill(200, 200)


drawCircle()
win.getMouse()
win.close()
