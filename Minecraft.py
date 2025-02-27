#Name: Zachary Martin
#Minecraft messed up code

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the 3D cube vertices
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Define the surfaces (faces) of the cube
surfaces = [
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
]

# Color scheme for cubes (for a more Minecraft-like feel)
# Let's keep it simple with stone-like and grass-like textures
block_colors = [
    (0.6, 0.6, 0.6),  # Stone
    (0.6, 0.3, 0.1),  # Dirt
    (0.0, 1.0, 0.0),  # Grass (green)
]

# Function to draw a single cube with a specific color
def draw_cube(color):
    glBegin(GL_QUADS)
    glColor3fv(color)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))  # Black for edges (subtle, not neon)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Function to initialize the game window
def init_game():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

# Function to handle user input for camera movement
def handle_input():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glTranslatef(0.1, 0, 0)
    if keys[K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keys[K_UP]:
        glTranslatef(0, 0.1, 0)
    if keys[K_DOWN]:
        glTranslatef(0, -0.1, 0)

# Function to generate a simple world of blocks (dirt, stone, and grass)
def generate_world():
    world = []
    for x in range(-5, 5):
        for y in range(-5, 5):
            for z in range(-5, 5):
                if z == -5:  # Ground level: dirt
                    world.append((x, y, z, block_colors[1]))
                elif z == 0:  # Grass on top of dirt
                    world.append((x, y, z, block_colors[2]))
                else:  # Stone in the air
                    world.append((x, y, z, block_colors[0]))
    return world

# Main game loop
def game_loop():
    init_game()
    world = generate_world()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_input()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for block in world:
            x, y, z, color = block
            glPushMatrix()
            glTranslatef(x, y, z)
            draw_cube(color)
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    game_loop()