from graphics import *

win = GraphWin("Filling the Colors in Life", 600, 600)
win.setBackground("White")


def getColor(x, y):
    overlapping = win.find_overlapping(x, y, y, x)
    if overlapping:
        return win.itemcget(overlapping[0], "fill")


def floodFill(x, y):
    color = getColor(x, y)
    if color == "White":
        win.plotPixel(x, y, "Black")
        floodFill(x + 1, y)
        floodFill(x - 1, y)
        floodFill(x, y + 1)
        floodFill(x, y - 1)


def drawCircle():
    Circle(Point(300, 300), 200).draw(win)
    floodFill(150, 150)


drawCircle()
win.getMouse()
win.close()
