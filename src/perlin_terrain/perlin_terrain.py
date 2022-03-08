import matplotlib
from p5 import *

cmap = matplotlib.cm.get_cmap('gist_earth')

scale = 50
terrain_width = 4000
terrain_height = 3000
terrain_range = (-800, 600)


def setup():
    size(1000, 1000)
    global rows, cols, y_offset, terrain, perlin_step_size
    rows = terrain_height // scale
    cols = terrain_width // scale
    y_offset = 0
    perlin_step_size = 0.1
    terrain = [[] for _ in range(cols)]
    # init terrain
    for y in range(rows):
        for x in range(cols):
            val = remap(noise(
                x * perlin_step_size, (y_offset + y) * perlin_step_size), (0, 1), terrain_range)
            terrain[y].append(val)


def update_terrain():
    global terrain, y_offset
    # pop first row
    terrain.pop(0)
    # add new row
    terrain.append([])
    for x in range(cols):
        val = remap(noise(
            x * perlin_step_size, (y_offset + (rows-1)) * perlin_step_size), (0, 1), terrain_range)
        terrain[rows-1].append(val)
    y_offset += 0.5


def draw():
    update_terrain()
    background(0)
    # translate(width/2, height/2)
    rotate_x(-PI/3)
    translate(-terrain_width/2, -height - 100)

    stroke_weight(1)
    stroke(255)
    no_fill()

    for row in range(rows - 1):
        alpha = remap(row, (0, rows), (255, 0))
        for col in range(cols - 1):
            begin_shape()
            # color
            c_index = remap(terrain[row][col], terrain_range, (0, 1))
            r, g, b, _ = cmap(c_index)
            stroke(255*r, 255*g, 255*b, alpha)
            # shape
            vertex(col * scale, row*scale, terrain[row][col])
            vertex(col * scale, (row + 1)*scale, terrain[row + 1][col])
            vertex((col + 1) * scale, (row + 1) *
                   scale, terrain[row + 1][col + 1])
            end_shape()


run(mode='P3D')
