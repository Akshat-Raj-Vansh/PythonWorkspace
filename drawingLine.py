from graphics import *


def main():
    win = GraphWin("My Circle", 1000, 1000)
    for x in range (1, 1000):
        point = Point(x, x)
        point.draw(win)
    win.getMouse()
    # pause for click in windows
    win.close()


main()
