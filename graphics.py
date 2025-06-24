from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

window = 0
width, height = 600, 600

def draw_pentagon_with_triangles():
    glBegin(GL_TRIANGLES)
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]
    cx, cy = 0, 0
    r = 0.5
    for i in range(5):
        glColor3f(*colors[i % len(colors)])
        angle1 = 2 * math.pi * i / 5
        angle2 = 2 * math.pi * ((i + 1) % 5) / 5
        x1, y1 = r * math.cos(angle1), r * math.sin(angle1)
        x2, y2 = r * math.cos(angle2), r * math.sin(angle2)
        glVertex2f(cx, cy)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()

def draw_pentagon_with_lines():
    glColor3f(1, 1, 0)  # Yellow
    glBegin(GL_LINES)
    r = 0.5
    for i in range(5):
        angle1 = 2 * math.pi * i / 5
        angle2 = 2 * math.pi * ((i + 1) % 5) / 5
        glVertex2f(r * math.cos(angle1), r * math.sin(angle1))
        glVertex2f(r * math.cos(angle2), r * math.sin(angle2))
    glEnd()

def draw_house():
    glColor3f(1, 0, 1)
    
    # Draw base (square)
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

    # Windows
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, -0.3)
    glVertex2f(-0.2, -0.3)
    glVertex2f(-0.2, -0.05)
    glVertex2f(-0.5, -0.05)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.5, -0.3)
    glVertex2f(0.5, -0.05)
    glVertex2f(0.2, -0.05)
    glEnd()

    # Door
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.15, -0.8)
    glVertex2f(0.15, -0.5)
    glVertex2f(0.15, 0.0)
    glVertex2f(-0.15, 0.0)
    glEnd()

    # Door knob (point)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(0.1, -0.25)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(-0.75, 0.5, 0)
    draw_pentagon_with_triangles()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 0.5, 0)
    draw_pentagon_with_lines()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -0.6, 0)
    draw_house()
    glPopMatrix()

    glutSwapBuffers()

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"OpenGL House and Pentagon")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
