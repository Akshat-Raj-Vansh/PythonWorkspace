from graphics import *

win = GraphWin("Bresenham Circle Algorithm", 600, 600)
r = int(input("Enter the radius of the circle."))
x = 0
y = r
dd = 3 - 2 * r
allPoints = [[x, y]]


def drawPoints(xx, yy):
    point = Point(xx + r, yy + r)
    point.draw(win)


while x <= y:
    # drawPoints(x, y)
    # drawPoints(-x, y)
    # drawPoints(x, -y)
    # drawPoints(-x, -y)
    # drawPoints(y, x)
    # drawPoints(-y, -x)
    # drawPoints(-y, x)
    # drawPoints(y, -x)
    if dd < 0:
        dd = dd + 4 * x + 6
    else:
        dd = dd + 4 * (x - y) + 10
        y = y - 1
    x += 1
    allPoints.append([x, y])

for x in range(0, len(allPoints)):
    allPoints.append([allPoints[x][1], allPoints[x][0]])
for x in range(0, len(allPoints)):
    allPoints.append([allPoints[x][0], -allPoints[x][1]])
for x in range(0, len(allPoints)):
    allPoints.append([-allPoints[x][0], allPoints[x][1]])

for x in range(0, len(allPoints)):
    drawPoints(allPoints[x][0], allPoints[x][1])

win.getMouse()
win.close()
