import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Cube(vertices):
    glBegin(GL_LINES)
    vertices = tuple(map(tuple, vertices))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def overall_scaling(vert):
    vert = np.hstack((vert, np.ones((vert.shape[0], 1), dtype=vert.dtype)))
    print("Enter the scaling factor")
    s = float(input())
    trasn = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, s]], dtype=float)
    vert = vert.dot(trasn)
    vert = vert / s
    vert = np.delete(vert, 3, 1)
    print(vert)
    return vert


def local_scaling(vert):
    vert = np.hstack((vert, np.ones((vert.shape[0], 1), dtype=vert.dtype)))
    print("Enter the scaling factor in x,y and z")
    x, y, z = [float(x) for x in input().split()]
    trans = np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]], dtype=float)
    vert = vert.dot(trans)
    vert = np.delete(vert, 3, 1)
    print(vert)
    return vert


def translation(vert):
    vert = np.hstack((vert, np.ones((vert.shape[0], 1), dtype=vert.dtype)))
    x, y, z = [float(x) for x in input("Enter the translation in x,y and z").split()]
    trans = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]], dtype=float)
    vert = vert.dot(trans)
    vert = np.delete(vert, 3, 1)
    print(vert)
    return vert


def rotation(vert):
    vert = np.hstack((vert, np.ones((vert.shape[0], 1), dtype=vert.dtype)))
    angle = float(input("Enter the angle")) * 3.14 / 180
    axis = input("Enter the axis of rotation:")
    if axis == 'x':
        trans = np.array([[0, 0, 1, 0], [cos(angle), sin(angle), 0, 0], [-sin(angle), cos(angle), 0, 0], [0, 0, 0, 1]],
                         dtype=float)
    if axis == 'y':
        trans = np.array([[cos(angle), 0, -sin(angle), 0], [0, 1, 0, 0], [sin(angle), 0, cos(angle), 0], [0, 0, 0, 1]],
                         dtype=float)
    if axis == 'z':
        trans = np.array([[cos(angle), sin(angle), 0, 0], [-sin(angle), cos(angle), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
                         dtype=float)

    vert = vert.dot(trans)
    vert = np.delete(vert, 3, 1)
    print(vert)
    return vert


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    vert = np.asarray(vertices, dtype=float)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    glRotatef(15, 1, 0, 0)
                if event.key == K_DOWN:
                    glRotatef(-15, 1, 0, 0)
                if event.key == K_LEFT:
                    glRotatef(15, 0, 1, 0)
                if event.key == K_RIGHT:
                    glRotatef(-15, 0, 1, 0)
                if event.key == K_RSHIFT:
                    glTranslatef(0.0, 0.0, -3)
                if event.key == K_RCTRL:
                    glTranslatef(-3, 0.0, 0)
                if event.key == K_LCTRL:
                    glTranslatef(3, 0.0, 0)
                if event.key == K_s:
                    vert = overall_scaling(vert)
                if event.key == K_l:
                    vert = local_scaling(vert)
                if event.key == K_t:
                    vert = translation(vert)
                if event.key == K_r:
                    vert = rotation(vert)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube(vertices)
        Cube(vert)
        pygame.display.flip()
        pygame.time.wait(10)


main()
