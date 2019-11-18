from graphics import *

win = GraphWin("Midpoint Circle", 600, 600)
win.setCoords(-300, -300, 300, 300)


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
        plotPoints(y + x_centre, x + y_centre)
        plotPoints(-y + x_centre, x + y_centre)
        plotPoints(y + x_centre, -x + y_centre)
        plotPoints(-y + x_centre, -x + y_centre)


def getInput():
    x = int(input("Enter the x coordinate of the centre: "))
    y = int(input("Enter the y coordinate of the centre: "))
    r = int(input("Enter the radius of the circle: "))
    return x, y, r


def plotPoints(x, y):
    point = Point(x, y)
    point.draw(win)


if __name__ == '__main__':
    xc, yc, rc = getInput()
    midPointCircleDraw(xc, yc, rc)
    win.getMouse()
    win.close()
