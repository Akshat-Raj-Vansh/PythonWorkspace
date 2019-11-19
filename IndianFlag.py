from graphics import *
from sys import setrecursionlimit
from math import *

setrecursionlimit(18000)

win = GraphWin("Indian Flag", 400, 250)


def drawLine(x1, y1, x2, y2):
    dx, dy = int(abs(x2 - x1)), int(abs(y2 - y1))

    sx = -1 if x2 - x1 < 0 else 1
    sy = -1 if y2 - y1 < 0 else 1

    print("dx = ", dx)
    print("dy = ", dy)

    swap = 0
    if dy > dx:
        swap = 1
        dx = dx + dy
        dy = dx - dy
        dx = dx - dy

    dd = 2 * dy - dx
    print("dd = ", dd)
    x = x1
    y = y1
    i = 0
    for i in range(0, dx):
        point = Point(x, y)
        point.draw(win)
        while dd >= 0:
            if swap:
                x = x + sx
            else:
                y = y + sy
                dd = dd - 2 * dx

        if swap:
            y = y + sy
        else:
            x = x + sx
        dd = dd + 2 * dy


def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y:
            break
        win.plot(x + x_centre, y + y_centre)
        win.plot(-x + x_centre, y + y_centre)
        win.plot(x + x_centre, -y + y_centre)
        win.plot(-x + x_centre, -y + y_centre)
        win.plot(y + x_centre, x + y_centre)
        win.plot(-y + x_centre, x + y_centre)
        win.plot(y + x_centre, -x + y_centre)
        win.plot(-y + x_centre, -x + y_centre)


def getColor(x, y):
    overlapping = win.find_overlapping(x, y, x + 1, y)
    if overlapping:
        return win.itemcget(overlapping[-1], "fill")
    else:
        return color_rgb(255, 255, 255)


def floodFill(x, y, c):
    color = getColor(x, y)
    if color == "#ffffff":
        win.plotPixel(x, y, c)
        floodFill(x + 1, y, c)
        floodFill(x - 1, y, c)
        floodFill(x + 1, y + 1, c)
        floodFill(x + 1, y - 1, c)
        floodFill(x - 1, y + 1, c)
        floodFill(x - 1, y - 1, c)
        floodFill(x, y + 1, c)
        floodFill(x, y - 1, c)


def drawSpokes(x0=400, y0=250, r=50, ang=20):
    rad1 = (3.14 * ang) / 180
    rad2 = (3.14 * (90 - ang)) / 180
    Line(Point(x0, y0), Point(x0 + r * sin(rad1), y0 + r * cos(rad1))).draw(win)
    Line(Point(x0, y0), Point(x0 + r * sin(rad2), y0 + r * cos(rad2))).draw(win)
    Line(Point(x0, y0), Point(x0 - r * sin(rad1), y0 - r * cos(rad1))).draw(win)
    Line(Point(x0, y0), Point(x0 - r * sin(rad2), y0 - r * cos(rad2))).draw(win)


if __name__ == "__main__":
    drawLine(50, 50, 350, 50)
    drawLine(50, 100, 350, 100)
    drawLine(50, 150, 350, 150)
    drawLine(50, 200, 350, 200)
    drawLine(50, 50, 50, 200)
    drawLine(350, 50, 350, 200)
    for i in range(15, 361, 15):
        drawSpokes(200, 125, 25, i)

    midPointCircleDraw(200, 125, 25)
    floodFill(200, 75, "Orange")
    floodFill(200, 175, "Green")

    win.getMouse()
    win.close()
