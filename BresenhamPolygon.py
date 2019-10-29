from graphics import *

win = GraphWin("Bresenham Polygon Algorithm", 600, 600)


def drawLine(x1, y1, x2, y2):
    dx = int(abs(x2 - x1))
    dy = int(abs(y2 - y1))
    sx = (x2 - x1) / abs(x2 - x1)
    sy = (y2 - y1) / abs(y2 - y1)

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
    win.getMouse()
    win.close()


n = int(input("Enter the number of sides of polygon"))
allPoints = []
for x in range(0, n):
    allPoints[x] = allPoints.append([int(input("x: ")), int(input("y: "))])
for x in range(0, len(allPoints)):
    if x != len(allPoints) - 1:
        drawLine(allPoints[x][0], allPoints[x][1], allPoints[x+1][0], allPoints[x+1][1])
    else:
        drawLine(allPoints[x][0], allPoints[x][1], allPoints[0][0], allPoints[0][1])
