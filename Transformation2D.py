from graphics import *
from math import *

win = GraphWin("2D Transformations", 1500, 500)
win.setBackground("White")

x, y, x1, y1, x2, y2 = (int(x) for x in input("Enter the vertices of triangle : ").split())

Line(Point(750 + x, 250 + y), Point(750 + x1, 250 + y1)).draw(win)
Line(Point(750 + x, 250 + y), Point(750 + x2, 250 + y2)).draw(win)
Line(Point(750 + x2, 250 + y2), Point(750 + x1, 250 + y1)).draw(win)

print("What do you want to do ? ")
print("1. Scaling")
print("2. Rotation")
print("3. Reflection")
print("4. Translation")

choice = int(input())

if choice == 1:
    sx = float(input("Enter x scale factor : "))
    sy = float(input("Enter y scale factor : "))
    x = sx * x
    y = sy * y
    x1 = sx * x1
    x2 = sx * x2
    y1 = sy * y1
    y2 = sy * y2
    Line(Point(750 + x, 250 + y), Point(750 + x1, 250 + y1)).draw(win)
    Line(Point(750 + x, 250 + y), Point(750 + x2, 250 + y2)).draw(win)
    Line(Point(750 + x2, 250 + y2), Point(750 + x1, 250 + y1)).draw(win)

elif choice == 2:
    thetha = float(input("Enter the angle for rotation : "))
    sx = cos(radians(thetha))
    sy = sin(radians(thetha))
    x = sx * x + y * sy
    y = sx * y - x * sy
    x1 = sx * x1 + y1 * sy
    y1 = sx * y1 - x1 * sy
    x2 = sx * x2 + y2 * sy
    y2 = sx * y2 - x2 * sy
    Line(Point(750 + x, 250 + y), Point(750 + x1, 250 + y1)).draw(win)
    Line(Point(750 + x, 250 + y), Point(750 + x2, 250 + y2)).draw(win)
    Line(Point(750 + x2, 250 + y2), Point(750 + x1, 250 + y1)).draw(win)

elif choice == 3:
    ch = int(input("Choose Reflection About- \n1.x axis\n2.y axis\n3.origin\n"))
    if ch == 1:
        x = x
        y = -y
        x1 = x1
        y1 = -y1
        x2 = x2
        y2 = -y2
    elif ch == 2:
        x = -x
        y = y
        x1 = -x1
        y1 = y1
        x2 = -x2
        y2 = y2
    elif ch == 1:
        x = -x
        y = -y
        x1 = -x1
        y1 = -y1
        x2 = -x2
        y2 = -y2
    Line(Point(750 + x, 250 + y), Point(750 + x1, 250 + y1)).draw(win)
    Line(Point(750 + x, 250 + y), Point(750 + x2, 250 + y2)).draw(win)
    Line(Point(750 + x2, 250 + y2), Point(750 + x1, 250 + y1)).draw(win)

elif choice == 4:
    sx = int(input("Enter the x translation value : "))
    sy = int(input("Enter the y translation value : "))
    x += sx
    y += sy
    x1 += sx
    y1 += sy
    x2 += sx
    y2 += sy
    Line(Point(750 + x, 250 + y), Point(750 + x1, 250 + y1)).draw(win)
    Line(Point(750 + x, 250 + y), Point(750 + x2, 250 + y2)).draw(win)
    Line(Point(750 + x2, 250 + y2), Point(750 + x1, 250 + y1)).draw(win)

win.getMouse()
win.close()
