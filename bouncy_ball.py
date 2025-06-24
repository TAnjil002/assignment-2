from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi
import sys

# Window dimensions
width, height = 800, 600

# Ball properties
ball_radius = 20
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 4, 3  # Velocity

def draw_ball():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(ball_x, ball_y)
    for angle in range(0, 361, 10):
        rad = angle * pi / 180
        glVertex2f(ball_x + ball_radius * cos(rad),
                   ball_y + ball_radius * sin(rad))
    glEnd()

def update(value):
    global ball_x, ball_y, ball_dx, ball_dy, width, height, ball_radius

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_dx *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_dy *= -1

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Call update every ~16ms (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_ball()
    glutSwapBuffers()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bouncy Ball Game")
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()

if __name__ == '__main__':
    main()
