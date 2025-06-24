from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_pentagon_triangles():
    glBegin(GL_TRIANGLES)
    # Center of the pentagon
    center = (0, 0.6)
    vertices = [
        (-0.4, 0.2), (-0.2, 0.9), (0.2, 0.9), (0.4, 0.2), (0, -0.2)
    ]
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]

    for i in range(5):
        glColor3f(*colors[i])
        glVertex2f(*center)
        glVertex2f(*vertices[i])
        glVertex2f(*vertices[(i + 1) % 5])
    glEnd()

def draw_pentagon_lines():
    glColor3f(1, 1, 0)  # Yellow
    glBegin(GL_LINES)
    vertices = [
        (-0.4, 0.2), (-0.2, 0.9), (0.2, 0.9), (0.4, 0.2), (0, -0.2)
    ]
    for i in range(5):
        glVertex2f(*vertices[i])
        glVertex2f(*vertices[(i + 1) % 5])
    glEnd()

def draw_house():
    glColor3f(1, 0, 1)  # Magenta

    # Draw house square base
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, -0.2)
    glVertex2f(-0.6, 0.4)
    glVertex2f(0.6, 0.4)
    glVertex2f(0.6, -0.2)
    glEnd()

    # Draw roof (triangle)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.6, 0.4)
    glVertex2f(0, 0.8)
    glVertex2f(0.6, 0.4)
    glEnd()

    # Left window
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, 0.1)
    glVertex2f(-0.5, 0.3)
    glVertex2f(-0.3, 0.3)
    glVertex2f(-0.3, 0.1)
    glEnd()

    # Right window
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.3, 0.1)
    glVertex2f(0.3, 0.3)
    glVertex2f(0.5, 0.3)
    glVertex2f(0.5, 0.1)
    glEnd()

    # Door
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.15, -0.2)
    glVertex2f(-0.15, 0.2)
    glVertex2f(0.15, 0.2)
    glVertex2f(0.15, -0.2)
    glEnd()

    # Door knob
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(0.1, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pentagon_triangles()
    draw_pentagon_lines()
    draw_house()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"OpenGL Pentagon and House")
    glutDisplayFunc(display)
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Black background
    glutMainLoop()

if __name__ == '__main__':
    main()
