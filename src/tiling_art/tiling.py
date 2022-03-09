from p5 import *
from datetime import datetime


def show_tile(row, col):
    x = col * scale + scale // 2
    y = row * scale + scale // 2

    alpha = remap((col + row), (0, rows + cols), (0, 220))
    with push_matrix():
        translate(x, y)
        no_fill()
        # stroke(0, 0, 0, alpha)
        # stroke_weight(2)
        # circle(0, 0, scale*(random_uniform(0.5, 3)))
        # rect_len = scale*(random_uniform(1, 2))
        # rect(-rect_len//2, - rect_len//2, rect_len, rect_len)
        stroke(0)
        hs = scale//2
        if random_uniform() > 0.5:
            line(-hs, 0, hs, 0)
        else:
            line(0, -hs, 0, hs)


def setup():
    size(800, 800)
    # no_loop()
    global scale, rows, cols
    scale = 20
    rows = height // scale
    cols = width // scale


def draw():
    background(255)

    for row in range(rows):
        for col in range(cols):
            show_tile(row, col)


def key_pressed(event):
    if event.key == 's':
        stamp = int(datetime.timestamp(datetime.now()))
        # save_frame(f"{stamp}.png")
    elif event.key == 'r':
        draw()


run()
