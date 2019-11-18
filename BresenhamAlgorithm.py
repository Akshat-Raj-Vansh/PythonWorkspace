from graphics import *

win = GraphWin("Bresenham Algorithm", 600, 600)
x1, y1, x2, y2 = [float(x) for x in input("Enter the co-ordinates: ").split()]

dx, dy = (x2 - x1), (y2 - y1)
dd = 2 * dy - dx
print("dx = ", dx)
print("dy = ", dy)
print("dd = ", dd)
x = x1
y = y1

while x < x2 or y < y2:
    x = x + 1
    if dd >= 0:
        y = y + 1
        dd = dd - 2 * dx
    print("dd = ", dd)
    print("x = ", x)
    print("y = ", y)
    Point(x, y).draw(win)
    dd = dd + 2 * dy

print("x = ", x)
print("y = ", y)
win.getMouse()
win.close()
