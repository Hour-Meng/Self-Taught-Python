import pygame
import pymunk
import pymunk.pygame_util # We need this one so that pymunk can run a simulation inside of pygame
import math

pygame.init()

width, height = 1000, 800

window = pygame.display.set_mode((width, height))

def draw(space, window, draw_option):
    window.fill("white")
    space.debug_draw(draw_option)
    pygame.display.update()

def create_ball(space, radius, mass):

    body = pymunk.Body()
    body.position = (300,300) #remember in pymunk (0,0) isn't in the center. It's actually at the top left of the screen
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255,0,0,100) # ( R value, G value, B value, Transparency value)
    space.add(body,shape)
    return shape

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps  #dt stands for delta in time

    space = pymunk.Space()
    space.gravity = (0, 989) # Our earth gravity is 9.98 m/s^2 but in this simulation we use 989 to make it faster

    ball = create_ball(space, 300, 10)

    draw_option = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(space, window, draw_option)

        space.step(dt)
        clock.tick(fps)

        clock.tick(fps)

if __name__ == "__main__":
    run(window, width, height)
