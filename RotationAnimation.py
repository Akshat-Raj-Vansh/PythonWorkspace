from graphics import *
from math import *

win = GraphWin("Rolling down the hill", 600, 600)
height = int(input("Enter the height of the wedge "))
width = int(input("Enter the width of the wedge "))
radius = int(input("Enter the diameter of the disc ")) / 2
theta = atan(height / width)


def drawLine(x1, y1, x2, y2):
    dx = int(abs(x2 - x1))
    dy = int(abs(y2 - y1))

    if x2 - x1 < 0:
        sx = -1
    else:
        sx = 1
    if y2 - y1 < 0:
        sy = -1
    else:
        sy = 1

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
    for ii in range(0, dx):
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


def getCentres():
    global theta
    x = radius * sin(theta)
    y = radius * (1 - cos(theta))
    b = width
    while x < width:
        win.delete("all")
        x = x + 1
        y = y + height / width
        drawWedge()
        theta -= x / b
        b += 10
        drawSpokes(x, y)
        midPointCircleDraw(x, y, radius)


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

        plotPoints(x + x_centre, y + y_centre)
        plotPoints(-x + x_centre, y + y_centre)
        plotPoints(x + x_centre, -y + y_centre)
        plotPoints(-x + x_centre, -y + y_centre)

        if x != y:
            plotPoints(y + x_centre, x + y_centre)
            plotPoints(-y + x_centre, x + y_centre)
            plotPoints(y + x_centre, -x + y_centre)
            plotPoints(-y + x_centre, -x + y_centre)


def drawWedge():
    drawLine(0, radius, 0, radius + height)
    drawLine(0, radius, width, radius + height)
    drawLine(0, radius + height, width, radius + height)


def drawSpokes(x, y):
    Line(Point(x, y), Point(x + radius * sin(theta), y + radius * cos(theta))).draw(win)
    Line(Point(x, y), Point(x + radius * sin(theta + pi / 2), y + radius * cos(theta + pi / 2))).draw(win)
    Line(Point(x, y), Point(x - radius * sin(theta), y - radius * cos(theta))).draw(win)
    Line(Point(x, y), Point(x - radius * sin(theta + pi / 2), y - radius * cos(theta + pi / 2))).draw(win)


def plotPoints(x, y):
    point = Point(x, y)
    point.draw(win)


if __name__ == '__main__':
    getCentres()
    win.getMouse()
    win.close()
