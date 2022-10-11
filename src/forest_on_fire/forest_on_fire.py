import pygame as pg
import random as rnd


def spread_fire(trees, fire):
    return {(row+d_row, col+d_col) for row, col in fire
            for d_row in range(-1, 2) for d_col in range(-1, 2)
            if (row+d_row, col+d_col) in trees}


def draw(trees, fire):
    for (row, col) in trees | fire:
        color = '#FF0000' if (row, col) in fire else '#00FF00'
        pg.draw.rect(canvas, color, (row*PXL, col*PXL, PXL, PXL))


pg.init()

SIZE, PXL, FPS = 200, 4, 25

canvas = pg.display.set_mode((SIZE * PXL, SIZE * PXL))

clock = pg.time.Clock()

# probabilities
p_spawn_init_trees, p_fire, p_growth = 0.2, 0.0005, 0.01

space = {(row, col) for row in range(SIZE) for col in range(SIZE)}
trees = set(rnd.sample(space, int(len(space) * p_spawn_init_trees)))
fire = set()

# game loop
while True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT or \
           event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            quit()

    # sim logic
    empty_space = space - trees - fire
    trees |= set(rnd.sample(space-trees, int(len(space-trees) * p_growth)))
    fire |= set(rnd.sample(trees-fire, int(len(trees-fire)*p_fire)))
    fire = spread_fire(trees-fire, fire)
    trees -= fire
    # draw simulation
    canvas.fill('black')
    draw(trees, fire)

    pg.display.flip()
