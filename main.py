import pygame
import entities
import vector
from planet import Planet
from vector import Vector
import commons


def update(acc1, acc2, acc3):
    entities.update_planets(acc1, acc2, acc3)


def draw():
    commons.screen.fill((50, 50, 50))
    entities.draw_planets()


pygame.init()

commons.screen = pygame.display.set_mode((commons.screen_w, commons.screen_h))

pygame.display.set_caption('three body system')

app_running = True
delta_time = 0.0
clock = pygame.time.Clock()

# creates planets
# presets: 50, 300,  200, 230,  550, 270
entities.planets.append(Planet(Vector(50, 300), Vector(10, 10), 5, 8, (255, 255, 255)))
entities.planets.append(Planet(Vector(200, 230), Vector(0, 0), 5, 8, (255, 0, 0)))
entities.planets.append(Planet(Vector(550, 270), Vector(0, 0), 5, 8, (0, 0, 255)))

while app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_running = False

    # the math begins

    # distance between planet 0 and 1
    d01 = vector.dist(entities.planets[0].position, entities.planets[1].position)
    # force of gravity between 0 and 1
    FG01 = ((-commons.G * entities.planets[0].mass * entities.planets[1].mass) / d01**2)
    FG01 = FG01 * vector.normalize(entities.planets[1].position - entities.planets[0].position)
    FG01 = -1 * FG01

    # FOG between planet 1 and 2
    d12 = vector.dist(entities.planets[1].position, entities.planets[2].position)
    FG12 = ((-commons.G * entities.planets[1].mass * entities.planets[2].mass) / d12 ** 2)
    FG12 = FG12 * vector.normalize(entities.planets[2].position - entities.planets[1].position)
    FG12 = -1 * FG12

    # FOG between planet 0 and 2
    d02 = vector.dist(entities.planets[0].position, entities.planets[2].position)
    FG02 = ((-commons.G * entities.planets[0].mass * entities.planets[2].mass) / d02 ** 2)
    FG02 = FG02 * vector.normalize(entities.planets[2].position - entities.planets[0].position)

    # accelerations
    A0 = (FG01 + (-1 * FG02)) / entities.planets[0].mass
    A1 = ((-1 * FG01) + FG12) / entities.planets[1].mass
    A2 = (FG02 + (-1 * FG12)) / entities.planets[2].mass

    update(A0, A1, A2)
    draw()

    pygame.display.flip()

    delta_time = 0.001 * clock.tick(144)

pygame.quit()
