from graphics import GraphWin, Rectangle, Point

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

x_max = 600
y_max = 600
x_min = 400
y_min = 400
win = GraphWin("Cohen Sutherland Line Clipping", 800, 800)


def LineDraw(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x2 - x1 > 0:
        s1 = 1
    else:
        s1 = -1

    if y2 - y1 > 0:
        s2 = 1
    else:
        s2 = -1

    if dy > dx:
        dx, dy = dy, dx
        interchange = 1
    else:
        interchange = 0

    e_ = 2 * dy - dx
    for i in range(dx):
        win.plot(x, y)
        while e_ > 0:
            if interchange == 1:
                x += s1
            else:
                y += s2
            e_ -= 2 * dx
        if interchange == 1:
            y += s2
        else:
            x += s1
        e_ += 2 * dy


def computeCode(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP

    return code


def cohenSutherlandClip(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break

        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        LineDraw(x1, y1, x2, y2)
        print("(x1: %d , y1 : %d),(x2: %d , y2 : %d)" % (x1, y1, x2, y2))

    else:
        print("Line rejected")


if __name__ == "__main__":
    window = Rectangle(Point(x_max, y_max), Point(x_min, y_min))
    window.draw(win)
    LineDraw(50, 375, 700, 600)
    win.getMouse()
    win.delete("all")
    window = Rectangle(Point(x_max, y_max), Point(x_min, y_min))
    window.draw(win)
    cohenSutherlandClip(50, 375, 700, 600)
    win.getMouse()
    win.close()
