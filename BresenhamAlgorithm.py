from graphics import *

win = GraphWin("Bresenham Algorithm", 600, 600)
x1 = float(input("Enter the x co-ordinate of starting point: "))
y1 = float(input("Enter the y co-ordinate of starting point: "))
x2 = float(input("Enter the x co-ordinate of end point: "))
y2 = float(input("Enter the y co-ordinate of end point: "))

dx = (x2 - x1)
dy = (y2 - y1)
dd = 2 * dy - dx
print("dx = ", dx)
print("dy = ", dy)
print("dd = ", dd)
x = x1
y = y1

while x < x2 or y < y2:
    dd = dd + 2 * dy
    x = x + 1
    if dd >= 0:
        y = y + 1
        dd = dd + 2 * dx
    print("dd = ", dd)
    print("x = ", x)
    print("y = ", y)
    point = Point(x, y)
    point.draw(win)

print("x = ", x)
print("y = ", y)
win.getMouse()
win.close()
