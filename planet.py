# class for the planets

import pygame.draw
import vector
from vector import Vector
import commons


class Planet:
    def __init__(self, position: Vector, velocity: Vector = Vector(0,0), mass: int = 50, radius: float = 8, color=(255, 255, 255)):
        self.position = vector.copy(position)
        self.velocity = vector.copy(velocity)

        self.radius = radius
        self.diameter = radius * 2.0
        self.mass = mass
        self.color = color

    def update(self, acc):
        self.velocity += (acc * commons.delta_time)
        self.position += (self.velocity * commons.delta_time)

    def draw(self):
        top_left_position = self.position - self.radius
        pygame.draw.circle(commons.screen, self.color, top_left_position.make_int_tuple(), 10)

