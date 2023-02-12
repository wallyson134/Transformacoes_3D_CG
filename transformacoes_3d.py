import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glScalef(1.0, 1.0, 1.0)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == K_UP:
                    glTranslatef(0, 0.5, 0)
                if event.key == K_DOWN:
                    glTranslatef(0, -0.5, 0)
                if event.key == K_a:
                    glRotatef(-5, 0, 5, 0)
                
                # girar cubo pra cima
                if event.key == K_w:
                    glRotatef(-5, 5, 0, 0)
                    
                # girar cubo pra baixo
                if event.key == K_s:
                    glRotatef(5, 5, 0, 0)
                
                # girar cubo pra direita
                if event.key == K_d:
                    glRotatef(5, 0, 5, 0)
                
                if event.key == K_e:
                    glScalef(1.1, 1.1, 1.1)
                if event.key == K_q:
                    glScalef(0.9, 0.9, 0.9)
                if event.key == K_j:
                    glTranslatef(-0.5, 0, 0)
                    glRotatef(20, 50, 20, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
