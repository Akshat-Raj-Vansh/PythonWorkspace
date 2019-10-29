from graphics import *

win = GraphWin("DDA", 600, 600)
x1 = int(input("Enter the x co-ordinate of starting point: "))
y1 = int(input("Enter the y co-ordinate of starting point: "))
x2 = int(input("Enter the x co-ordinate of end point: "))
y2 = int(input("Enter the y co-ordinate of end point: "))
if abs(x2 - x1) >= abs(y2 - y1):
    length = abs(x2 - x1)
else:
    length = abs(y2 - y1)
dx = (x2 - x1) / length
dy = (y2 - y1) / length
x = x1 + 0.5
y = y1 + 0.5
i = 1
while i <= length:
    point = Point(x, y)
    point.draw(win)
    x = x + dx
    y = y + dy
    i += 1
win.getMouse()
win.close()
