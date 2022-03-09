from p5 import *


def setup():
    size(800, 800)
    no_loop()
    global n, d
    n = 6
    d = 127


# ? Maurer rose reference: https://en.wikipedia.org/wiki/Maurer_rose
# n = 6
# d = 90, 99, 114

# 128


def draw():
    global n, d
    background(0)
    with push_matrix():
        translate(width//2, height//2)

        # draw rose
        no_fill()
        stroke(255)
        begin_shape()
        for theta in range(361):
            k = theta * d * PI / 180
            r = 350 * sin(n * k)
            x = r * cos(k)
            y = r * sin(k)
            vertex(x, y)

        end_shape()
    print(f"{n=}; {d=}")
    # d += 1


def key_pressed(event):
    if event.key == 's':
        save_frame(f"maurer_n{n}_d{d}.png")


run(frame_rate=1)
