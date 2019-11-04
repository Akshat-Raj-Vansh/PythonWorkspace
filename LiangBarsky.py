from graphics import GraphWin, Point, Rectangle, Line

x_max = 600
y_max = 600
x_min = 400
y_min = 400
win = GraphWin("Liang_Barsky_Line_Clipping", 780, 780)


def liang_barsky_clip(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    for i, val in enumerate(p):
        if val == 0:
            print("Line is parallel to one of the clipping boundry")
            if q[i] >= 0:
                if i < 2:
                    if y1 < y_min:
                        y1 = y_min
                    if y2 > y_max:
                        y2 = y_max
                    clip_line = Line(Point(x1, y1), Point(x2, y2))
                    clip_line.draw(win)
                if i > 1:
                    if x1 < x_min:
                        x1 = x_min
                    if x2 > x_max:
                        x2 = x_max
                    clip_line = Line(Point(x1, y1), Point(x2, y2))
                    clip_line.draw(win)
    t1 = 0.0
    t2 = 1.0
    r = 0

    print(t1, t2)
    for i in range(4):
        r = q[i] / p[i]
        print(q[i], p[i])
        if p[i] < 0:
            if t1 <= r:
                t1 = r
        else:
            if t2 > r:
                t2 = r
        print(t1, t2, r)
    print(t1, t2)
    if t1 < t2:
        x11 = x1 + t1 * p[1]
        x22 = x1 + t2 * p[1]
        y11 = y1 + t1 * p[3]
        y22 = y1 + t2 * p[3]
        print("(x1: %d , y1 : %d),(x2: %d , y2 : %d)" % (x11, y11, x22, y22))
        clip_line = Line(Point(int(x11), int(y11)), Point(int(x22), int(y22)))
        clip_line.draw(win)


if __name__ == "__main__":
    window = Rectangle(Point(x_min, y_min), Point(x_max, y_max))
    window.draw(win)
    line1 = Line(Point(50, 375), Point(700, 600))
    line1.draw(win)
    line2 = Line(Point(150, 200), Point(300, 500))
    line2.draw(win)
    line3 = Line(Point(425, 425), Point(550, 500))
    line3.draw(win)
    win.getMouse()
    win.delete("all")
    window = Rectangle(Point(x_min, y_min), Point(x_max, y_max))
    window.draw(win)
    liang_barsky_clip(50, 375, 700, 600)
    liang_barsky_clip(150, 200, 300, 500)
    liang_barsky_clip(425, 425, 550, 500)

    win.getMouse()
    win.close()
