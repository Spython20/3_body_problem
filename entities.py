# creates the planets

from planet import Planet

planets = []


def update_planets(acc1, acc2, acc3):
   # for i in range(len(planets) - 1, -1, -1):
        planets[0].update(acc1)
        planets[1].update(acc2)
        planets[2].update(acc3)

def draw_planets():
    for i in range(len(planets)):
        planets[i].draw()

