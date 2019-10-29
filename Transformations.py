from graphics import *

win = GraphWin("Transformations", 600, 600)


def product(a=0, b=0):
    return a * b


x, y = int(input("x: ")), int(input("y: "))
point = Point(x+200, y+200)
point.draw(win)
c = int(input("Choose:\n1.Scaling\n2.Reflection\n"))
T = []
if c == 1:
    print("Enter Factors:")
    kx = int(input("Scale x by: "))
    ky = int(input("Scale y by: "))
    T = [kx, 0, 0, ky]
if c == 2:
    k = int(input("Choose Axis about which you need reflection:\n1.X Axis\n2.Y Axis\n3.Origin"))
    if k == 1:
        T = [1, 0, 0, -1]
    if k == 2:
        T = [-1, 0, 0, 1]
    if k == 3:
        T = [-1, 0, 0, -1]

X = product(T[0], x) + product(T[2], y)
Y = product(T[1], x) + product(T[3], y)
point = Point(X+200, Y+200)
print("New Point: ", X, Y)
point.draw(win)
win.getMouse()
win.close()
