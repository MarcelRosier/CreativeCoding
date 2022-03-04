import matplotlib
from p5 import *

cmap = matplotlib.cm.get_cmap('viridis')


class Boundary:

    def __init__(self, x1, y1, x2, y2, wiggle=False):
        self.start = Vector(x1, y1)
        self.end = Vector(x2, y2)
        self.wiggle = wiggle
        self.x_off = random_uniform(10000)
        self.y_off = random_uniform(10000)

    def draw(self):
        stroke(150, 0, 0)
        stroke_weight(4)
        line(self.start, self.end)

    def update(self):
        self.x_off += 0.02
        self.y_off += 0.02
        if self.wiggle:
            dx = (0.6 - noise(self.x_off)) * 6
            dy = (0.6 - noise(self.y_off)) * 6
            self.start.x += dx
            self.start.y += dy
            self.end.x += dx
            self.end.y += dy


class RotatingBoundary(Boundary):

    def __init__(self, x1, y1, x2, y2, length: int = 250, is_rotating: bool = False, rotating_speed=2):
        self.start = Vector(x1, y1)
        self.end = Vector(x2, y2)
        self.degrees = 0
        self.is_rotating = is_rotating
        self.length = length
        self.rotating_speed = rotating_speed

    def update(self):
        if self.is_rotating:
            direction = Vector.from_angle(radians(self.degrees))
            self.end.x = self.start.x + direction.x * self.length
            self.end.y = self.start.y + direction.y * self.length
            self.degrees += self.rotating_speed


class Ray:

    def __init__(self, pos, rad, boundaries):
        self.pos = pos
        self.rad = rad
        self.orientation = Vector.from_angle(rad)
        self.boundaries = boundaries
        self.rays = []

    def draw(self):
        border_point = None
        min_u = None
        for bound in self.boundaries:
            intersects = self.intersects(bound=bound)
            if intersects:
                intersection_point, _, u = intersects
                if not min_u or abs(u) < min_u:
                    proportional_length = 1 - u/width
                    # print(proportional_length)
                    min_u = abs(u)
                    border_point = intersection_point

        if border_point:
            r, g, b, _ = cmap(proportional_length)
            # r, g, b = 255, 255, 255
            stroke(r*255, g*255, b*255, proportional_length * 255)
            stroke_weight(1)
            line(self.pos, border_point)

    def intersects(self, bound):
        # reference: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection - Given two points on each line segment
        x1 = bound.start.x
        x2 = bound.end.x
        x3 = self.pos.x
        x4 = self.pos.x + self.orientation.x
        y1 = bound.start.y
        y2 = bound.end.y
        y3 = self.pos.y
        y4 = self.pos.y + self.orientation.y

        denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denom == 0:
            return None

        t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)) / denom
        u = ((x1-x3)*(y1-y2)-(y1-y3)*(x1-x2)) / denom

        if t >= 0 and t <= 1 and u >= 0:
            return Vector(x1 + t * (x2-x1), y1 + t * (y2-y1)), t, u
        return None


class LightSource:

    def __init__(self, x, y, boundaries, n_rays=10):
        self.pos = Vector(x, y)
        self.dir = Vector(x - 10, y)
        self.boundaries = boundaries
        self.rays = []
        self.x_off = 0
        self.y_off = 1000
        for angle in range(0, 360, 360//n_rays):
            rad = radians(angle)
            self.rays.append(
                Ray(pos=self.pos, rad=rad, boundaries=self.boundaries))

        print(self.rays)

    def draw(self):
        for ray in self.rays:
            ray.draw()

    def update(self):
        self.x_off += 0.01
        self.y_off += 0.01
        self.pos.x = noise(self.x_off) * width
        self.pos.y = noise(self.y_off) * height


def init_bounds(boundaries):
    # frame
    boundaries.clear()
    boundaries.append(Boundary(-10, -10, width + 10, -10))
    boundaries.append(Boundary(-10, -10, -10, height + 10))
    boundaries.append(Boundary(width + 10, -10, width + 10, height + 10))
    boundaries.append(Boundary(-10, height + 10, width + 10, height + 10))
    # visible borders
    # static
    boundaries.append(Boundary(100, 100, 300, 400, wiggle=True))
    boundaries.append(RotatingBoundary(500, 500, 800, 400, is_rotating=True))
    boundaries.append(Boundary(1100, 100, 1000, 500))
    # random
    for _ in range(int(random_uniform(8, 4))):

        start_x = random_uniform(0.9*width, 0.1 * width)
        start_y = random_uniform(0.9*height, 0.1*height)
        dx = random_uniform(width/2, -width/2)
        dy = random_uniform(height/2, -height/2)
        if random_uniform(3) > 1:
            boundaries.append(
                Boundary(start_x, start_y, start_x + dx, start_y+dy))
        else:
            boundaries.append(RotatingBoundary(start_x, start_y, start_x + dx, start_y+dy,
                                               length=random_uniform(300, 100),
                                               is_rotating=True,
                                               rotating_speed=random_uniform(5, 1)))

    return boundaries


def setup():
    size(1280, 720)
    # frame
    global boundaries
    boundaries = []
    init_bounds(boundaries)
    global light_source
    light_source = LightSource(500, 200, boundaries, n_rays=100)


def update():
    light_source.update()
    for bound in boundaries:
        bound.update()


def draw():
    update()
    # draw
    background(0)
    light_source.draw()
    for bound in boundaries:
        bound.draw()


def key_pressed(event):
    init_bounds(boundaries)


run(frame_rate=30)
