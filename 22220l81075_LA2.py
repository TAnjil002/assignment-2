from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

# Window dimensions
width, height = 600, 600

def draw_pentagon_with_triangles():
    glBegin(GL_TRIANGLES)
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]
    center = (0.0, 0.0)
    radius = 0.5
    for i in range(5):
        glColor3fv(colors[i % len(colors)])
        angle1 = 2 * math.pi * i / 5
        angle2 = 2 * math.pi * (i + 1) / 5
        glVertex2fv(center)
        glVertex2f(math.cos(angle1) * radius, math.sin(angle1) * radius)
        glVertex2f(math.cos(angle2) * radius, math.sin(angle2) * radius)
    glEnd()

def draw_pentagon_with_lines():
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glBegin(GL_LINE_LOOP)
    radius = 0.5
    for i in range(5):
        angle = 2 * math.pi * i / 5
        glVertex2f(math.cos(angle) * radius, math.sin(angle) * radius - (-0.5))  # move down
    glEnd()

def draw_house():
    glColor3f(1.0, 0.0, 1.0)  # Pink

    # House base
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, -0.8)
    glVertex2f(0.6, -0.8)
    glVertex2f(0.6, 0.0)
    glVertex2f(-0.6, 0.0)
    glEnd()

    # Roof (triangle)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, 0.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.6)
    glEnd()

    # Left window
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, -0.3)
    glVertex2f(-0.2, -0.3)
    glVertex2f(-0.2, -0.05)
    glVertex2f(-0.5, -0.05)
    glEnd()

    # Right window
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.5, -0.3)
    glVertex2f(0.5, -0.05)
    glVertex2f(0.2, -0.05)
    glEnd()

    # Door
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.15, -0.8)
    glVertex2f(0.15, -0.8)
    glVertex2f(0.15, -0.4)
    glVertex2f(-0.15, -0.4)
    glEnd()

    # Doorknob
    glBegin(GL_POINTS)
    glVertex2f(0.1, -0.6)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw each item with a small vertical offset
    draw_pentagon_with_triangles()
    draw_pentagon_with_lines()
    draw_house()

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
    glColor3f(1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.5, 1.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Shapes - Pentagon and House")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
