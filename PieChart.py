from math import *
from random import *
from graphics import *

print("Enter the co.ordinates of the center.")
xc, yc = int(input("x: ")), int(input("y: "))
r = int(input("Enter the radius"))

win = GraphWin("Pie_Chart", 780, 780)


def drawLine(xc, yc, x2, y2, R, G, B):
    x, y = xc, yc
    dx = abs(x2 - xc)
    dy = abs(y2 - yc)

    if (x2 - xc) < 0:
        sx = -1
    else:
        sx = 1
    if (y2 - yc) < 0:
        sy = -1
    else:
        sy = 1
    if dy > dx:
        dy, dx = dx, dy
        interchange = 1
    else:
        interchange = 0
    dd = 2 * dy - dx
    for i in range(dx):
        win.plot(x, y, color_rgb(R, G, B))
        while dd > 0:
            if interchange == 1:
                x += sx
            else:
                y += sy
            dd = dd - 2 * dx
        if interchange == 1:
            y += sy
        else:
            x += sx
        dd = dd + 2 * dy


def drawCircle(r):
    P = []
    x, y, di = 0, r, 3 - 2 * r
    while x <= y:
        P.append((x, y))
        if di < 0:
            di += 4 * x + 6
        else:
            di += 4 * (x - y) + 10
            y -= 1
        x += 1
    return P


def Plot(P):
    swap = lambda x: (x[1], x[0])
    quadrants = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    new = [swap(x) for x in P]
    new.reverse()
    P += new

    point = []
    for i in quadrants:
        new = [((xc + i[0] * x[0]), (yc + i[1] * x[1])) for x in P]  # list comprehension
        if i[1] * i[0] == 1:
            new.reverse()
        point += new
    print(point)
    return point


def drawSector(points):
    angle = 90
    color = []
    lent = len(points)
    p1 = 0
    n = int(input("Enter the number of divisions : "))
    for i in range(n): color.append([randint(0, 255), randint(0, 255), randint(0, 255)])
    # generating random colors for sectors
    drawLine(xc, yc, xc, xc - r, color[0][0], color[0][1], color[0][2])
    for x in color[1:]:
        per = float(input("Enter percentage for division: "))
        angle = per * 3.6 + angle
        x2 = xc + r * cos(radians(angle))
        y2 = yc + r * sin(radians(angle))
        p2 = p1 + (lent * per) / 100
        print(p1, p2)
        val = points[int(p1) + 1:int(p2)]
        print(lent, len(val))
        drawLine(xc, yc, int(x2), int(y2), x[0], x[1], x[2])
        for i in val:
            win.plot(i[0], i[1], color_rgb(x[0], x[1], x[2]))
            drawLine(xc, yc, i[0], i[1], x[0], x[1], x[2])
        print("x2 " + str(x2) + "y2 " + str(y2))
        p1 = p2

    val = points[int(p1) + 1:]
    for i in val:
        win.plot(i[0], i[1], color_rgb(color[0][0], color[0][1], color[0][2]))
        drawLine(xc, yc, i[0], i[1], color[0][0], color[0][1], color[0][2])


if __name__ == "__main__":
    points = drawCircle(r)
    point = Plot(points)
    drawSector(point)
    win.getMouse()
    win.close()
