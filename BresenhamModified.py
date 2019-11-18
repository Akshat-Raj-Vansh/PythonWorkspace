from graphics import *

win = GraphWin("Modified Bresenham Algorithm", 600, 600)

x1, y1, x2, y2 = [float(x) for x in input("Enter the co-ordinates: ").split()]
dx, dy = int(abs(x2 - x1)), int(abs(y2 - y1))

sx = -1 if x2 - x1 < 0 else 1
sy = -1 if y2 - y1 < 0 else 1

print("dx = ", dx)
print("dy = ", dy)

swap = 0

if dy > dx:
    swap = 1
    dx, dy = dy, dx

dd = 2 * dy - dx
print("dd = ", dd)
x = x1
y = y1
i = 0
for i in range(0, dx):
    Point(x, y).draw(win)
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
