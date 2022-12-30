from __future__ import annotations
from p5 import *
from enum import auto

SQUARE_SIZE = 4
WIDTH = 300
CIRCLE_RAD = SQUARE_SIZE // 2
bg_color = (3, 2, 9)
circle_color = (204, 81, 180, 250)
line_color = (164, 173, 211)


def setup():
    size(WIDTH * SQUARE_SIZE, WIDTH * SQUARE_SIZE)
    no_loop()


class Direction(Enum):
    UP: int = auto()
    LEFT: int = auto()
    DOWN: int = auto()
    RIGHT: int = auto()


class Spiral:

    def __init__(self, trace: bool = True):
        self.x = 0
        self.y = 0
        self.prev_x = 0
        self.prev_y = 0
        self.cur_step = 1
        self.cur_border_len = 2
        self.remaining_border_steps = self.cur_border_len
        self.cur_dir = Direction.UP
        self.history = []
        self.primes = []
        self.trace = trace

    def step(self):

        self.prev_x = self.x
        self.prev_y = self.y
        self.history.append((self.prev_x, self.prev_y))

        if self.cur_dir == Direction.UP:
            if self.remaining_border_steps == self.cur_border_len:
                # right
                self.x += SQUARE_SIZE
            else:
                self.y -= SQUARE_SIZE
        elif self.cur_dir == Direction.LEFT:
            self.x -= SQUARE_SIZE
        elif self.cur_dir == Direction.DOWN:
            self.y += SQUARE_SIZE
        elif self.cur_dir == Direction.RIGHT:
            self.x += SQUARE_SIZE

        self.draw_step()

        # update counters
        self.cur_step += 1
        self.remaining_border_steps -= 1
        if self.remaining_border_steps == 0:
            # if a full round was done increase border len
            if self.cur_dir == Direction.RIGHT:
                self.cur_border_len += 2
                self.cur_dir = Direction.UP
            elif self.cur_dir == Direction.UP:
                self.cur_dir = Direction.LEFT
            elif self.cur_dir == Direction.LEFT:
                self.cur_dir = Direction.DOWN
            elif self.cur_dir == Direction.DOWN:
                self.cur_dir = Direction.RIGHT

            # reset steps after dir swit
            self.remaining_border_steps = self.cur_border_len

    def draw_step(self):
        if self.trace:
            stroke(*line_color, 150)
            line(self.prev_x, self.prev_y, self.x, self.y)
        if is_prime(self.cur_step):
            self.primes.append((self.x, self.y))

    def draw_primes(self):
        for x, y in self.primes:
            no_stroke()
            fill(*circle_color)
            circle((x, y), CIRCLE_RAD)

    def draw_grid(self):
        for x, y in self.history:
            no_fill()
            stroke(*line_color, 15)
            rect(x-CIRCLE_RAD, y - CIRCLE_RAD, SQUARE_SIZE, SQUARE_SIZE)


def is_prime(num: int):
    for i in range(2, int((sqrt(num) + 1))):
        if num % i == 0:
            return False
    return num > 1


def draw():

    # center the coordinate system: width and height are p5 itnernal vars
    translate(width//2, height//2)
    background(*bg_color)

    spiral = Spiral(trace=False)

    while spiral.cur_border_len < WIDTH:
        spiral.step()
    # spiral.draw_grid()
    spiral.draw_primes()


def key_pressed(event):
    if event.key == 's':
        save('gallery.png')


run()
