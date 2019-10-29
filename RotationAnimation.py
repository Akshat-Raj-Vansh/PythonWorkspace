from graphics import *
from math import *

win = GraphWin("Transformations", 600, 600)


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


def getCentre(x1, y1, x2, y2):
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
        time.sleep(0.5)
        win.delete("all")
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
        drawWedge()
        midPointCircleDraw(x, y, radius)


def getCentres():
    x = radius * sin(theta)
    y = radius * (1 - cos(theta))
    while x < width:
        time.sleep(0.5)
        win.delete("all")
        x = x + 1
        y = y + height / width
        drawWedge()
        midPointCircleDraw(x, y, radius)


def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    print("(", x + x_centre, ", ", y + y_centre, ")")

    if r > 0:
        print("({xval}, {yval})".format(xval=x + x_centre, yval=y + y_centre))
        print("(", y + x_centre, ", ", x + y_centre, ")")
        print("(", -y + x_centre, ", ", x + y_centre, ")")

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

        print("(", x + x_centre, ", ", y + y_centre, ")")
        print("(", -x + x_centre, ", ", y + y_centre, ")")
        print("(", x + x_centre, ", ", -y + y_centre, ")")
        print("(", -x + x_centre, ", ", -y + y_centre, ")")
        plotPoints(x + x_centre, y + y_centre)
        plotPoints(-x + x_centre, y + y_centre)
        plotPoints(x + x_centre, -y + y_centre)
        plotPoints(-x + x_centre, -y + y_centre)

        if x != y:
            print("(", y + x_centre, ", ", x + y_centre, ")")
            print("(", -y + x_centre, ", ", x + y_centre, ")")
            print("(", y + x_centre, ", ", -x + y_centre, ")")
            print("(", -y + x_centre, ", ", -x + y_centre, ")")
            plotPoints(y + x_centre, x + y_centre)
            plotPoints(-y + x_centre, x + y_centre)
            plotPoints(y + x_centre, -x + y_centre)
            plotPoints(-y + x_centre, -x + y_centre)


def drawWedge():
    drawLine(0, radius, 0, radius + height)
    drawLine(0, radius, width, radius + height)
    drawLine(0, radius + height, width, radius + height)


def plotPoints(x, y):
    point = Point(x, y)
    point.draw(win)


if __name__ == '__main__':
    height = int(input("Enter the height of the wedge"))
    width = int(input("Enter the width of the wedge"))
    radius = int(input("Enter the diameter of the disc.")) / 2
    theta = radians((360 * sqrt(height ** 2 + width ** 2)) / (width * pi * radius * 2))
    getCentres()
    win.getMouse()
    win.close()
