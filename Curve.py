from graphics import *

win = GraphWin("3D Transformations", 600, 600)

k = 1
i = 1
j = 1
b = 1
while i < 500:
    while j < 500:
        Point(i, j).draw(win)
        Line(Point(i, j), Point(i - k, j - b)).draw(win)
        i += k
        j += b
        if i <= 100:
            k += 3
        if i > 100:
            k -= 1
        if j <= 300:
            b += 5
        if j > 300:
            b -= 3

win.getMouse()
win.close()
