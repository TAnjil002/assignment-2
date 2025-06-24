from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Ball state
ball_x = 0.0
ball_y = 0.0
ball_radius = 0.1
velocity_x = 0.01
velocity_y = 0.015

# Window size
window_width = 800
window_height = 600

def draw_circle(x, y, radius):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.5, 0.0)  # Orange color
    glVertex2f(x, y)
    for angle in range(0, 361, 10):
        rad = angle * 3.14159 / 180
        glVertex2f(x + radius * cos(rad), y + radius * sin(rad))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle(ball_x, ball_y, ball_radius)
    glutSwapBuffers()

def update(value):
    global ball_x, ball_y, velocity_x, velocity_y

    # Update position
    ball_x += velocity_x
    ball_y += velocity_y

    # Bounce off walls
    if ball_x + ball_radius > 1 or ball_x - ball_radius < -1:
        velocity_x *= -1
    if ball_y + ball_radius > 1 or ball_y - ball_radius < -1:
        velocity_y *= -1

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 FPS

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)  # 2D coordinates from -1 to 1
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Bouncing Ball - PyOpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

from math import cos, sin  # Needed for circle points
main()