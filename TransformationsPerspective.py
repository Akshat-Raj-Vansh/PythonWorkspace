from graphics import *

win = GraphWin("Midpoint Circle", 600, 600)


def drawLine(x1, y1, x2, y2):
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
    for ii in range(0, dx):
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


def drawShape(points, size):
    for j in range(0, size - 1):
        drawLine(points[j][0], points[j][1], points[j + 1][0], points[j + 1][1])
    drawLine(points[0][0], points[0][1], points[size - 1][0], points[size - 1][1])


def Scale(points, size):
    print("Enter Factors:")
    kx = int(input("Scale x by: "))
    ky = int(input("Scale y by: "))
    Trans = [kx, 0, 0, ky]
    NP = Multiplication(points, size, Trans)
    print(NP)
    drawShape(NP, size)
    return NP


def Multiplication(points, size, trans):
    NP = []
    for z in range(0, size):
        PP = tuple((points[z][0] * trans[0], points[z][1] * trans[3]))
        NP.append(PP)
    return NP


def Reflect(points, size, axis):
    Trans = []
    if axis == 1:
        Trans = [1, 0, 0, -1]
    if axis == 2:
        Trans = [-1, 0, 0, 1]
    if axis == 3:
        Trans = [-1, 0, 0, -1]
    NP = Multiplication(points, size, Trans)
    print(NP)
    drawShape(NP, size)
    return NP


if __name__ == '__main__':
    n = int(input("Enter the number of points you want to enter - "))
    P = []
    Q = []
    T = ()
    for i in range(0, n):
        T = tuple(((300 + int(x) for x in input("Enter Point ").split(','))))
        P.append(T)

    for i in range(0, n):
        print(P[i][0], ",", P[i][1])
    Q = P
    drawShape(P, n)
    c = int(input("Choose:\n1.Scaling\n2.Reflection\n"))
    if c == 1:
        P = Scale(P, n)

    if c == 2:
        k = int(input("Choose Axis about which you need reflection:\n1.X Axis\n2.Y Axis\n3.Origin"))
        if k == 1:
            P = Reflect(P, n, 1)
        if k == 2:
            P = Reflect(P, n, 2)
        if k == 3:
            P = Reflect(P, n, 3)
        drawShape(P, n)
    win.getMouse()
    win.close()

