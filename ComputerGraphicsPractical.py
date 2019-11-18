from graphics import *

win = GraphWin("Computer Graphics", 600, 600)


def drawCircle(x_centre, y_centre, r):
    x = r
    y = 0
    Points = []
    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y:
            break

        plotPoints(x + x_centre, y + y_centre)
        plotPoints(-x + x_centre, y + y_centre)
        plotPoints(x + x_centre, -y + y_centre)
        plotPoints(-x + x_centre, -y + y_centre)
        Points.append(tuple((x + x_centre, y + y_centre)))
        Points.append(tuple((-x + x_centre, y + y_centre)))
        Points.append(tuple((x + x_centre, -y + y_centre)))
        Points.append(tuple((-x + x_centre, -y + y_centre)))

        if x != y:
            plotPoints(y + x_centre, x + y_centre)
            plotPoints(-y + x_centre, x + y_centre)
            plotPoints(y + x_centre, -x + y_centre)
            plotPoints(-y + x_centre, -x + y_centre)
            Points.append(tuple((y + x_centre, x + y_centre)))
            Points.append(tuple((-y + x_centre, x + y_centre)))
            Points.append(tuple((y + x_centre, -x + y_centre)))
            Points.append(tuple((-y + x_centre, -x + y_centre)))
    return Points


def drawSmile(x_centre, y_centre, r):
    x = r
    y = 0
    Points = []
    P = 1 - r
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if x < y:
            break

        if x != y:
            plotPoints(y + x_centre, x + y_centre)
            plotPoints(-y + x_centre, x + y_centre)
            Points.append(tuple((y + x_centre, x + y_centre)))
            Points.append(tuple((-y + x_centre, x + y_centre)))

    return Points


def plotPoints(x, y):
    Point(x, y).draw(win)


def Scale(points):
    NewPoints = []
    for point in points:
        NewPoints.append(tuple((point[0] * 2)))
        NewPoints.append(tuple((point[1] * 2)))
    return NewPoints


if __name__ == '__main__':
    Face = drawCircle(300, 300, 300)
    EyeL = drawCircle(150, 200, 50)
    EyeR = drawCircle(450, 200, 50)
    Smile = drawSmile(300, 350, 150)
    print(Face)
    # print(EyeL)
    # print(EyeR)
    # print(Smile)
    #Face = Scale(Face)
    print(Face)
    win.getMouse()
    win.delete("all")

    win.getMouse()
    win.close()
