from graphics import *

win = GraphWin("Midpoint Ellipse", 600, 600)


def midpointEllipse(rx, ry, xc, yc):
    x = 0
    y = ry

    d1 = ((ry * ry) - (rx * rx * ry) +
          (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while dx < dy:
        Point(x + xc, y + yc).draw(win)
        Point(-x + xc, y + yc).draw(win)
        Point(x + xc, -y + yc).draw(win)
        Point(-x + xc, -y + yc).draw(win)
        dx = dx + (2 * ry * ry)
        x += 1

        if d1 < 0:
            d1 = d1 + dx + (ry * ry)
        else:
            y -= 1
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))

    while y >= 0:
        Point(x + xc, y + yc).draw(win)
        Point(-x + xc, y + yc).draw(win)
        Point(x + xc, -y + yc).draw(win)
        Point(-x + xc, -y + yc).draw(win)
        y -= 1
        dy = dy - (2 * rx * rx)

        if d2 > 0:
            d2 = d2 + (rx * rx) - dy
        else:
            x += 1
            dx = dx + (2 * ry * ry)
            d2 = d2 + dx - dy + (rx * rx)

    win.getMouse()
    win.close()


midpointEllipse(50, 25, 150, 150)
