from graphics import *

win = GraphWin("Modified Bresenham Algorithm", 600, 600)
x1 = float(input("Enter the x co-ordinate of starting point: "))
y1 = float(input("Enter the y co-ordinate of starting point: "))
x2 = float(input("Enter the x co-ordinate of end point: "))
y2 = float(input("Enter the y co-ordinate of end point: "))

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

slope = dy / dx
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
