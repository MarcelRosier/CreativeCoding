import matplotlib
import uuid
from p5 import *
cmap = matplotlib.cm.get_cmap('magma')


class Part():

    def __init__(self, parent: 'Part' = None, length: int = 100, rotating_speed: float = 0.01, trace: bool = True, color: Color = None, show: bool = True):
        self.parent = parent
        self.angle = 0
        self.length = length
        self.rotating_speed = rotating_speed
        self.cur_pos = Vector(cos(self.angle) * self.length,
                              sin(self.angle) * self.length)
        self.trace = trace
        self.color: Color = color if color else Color(255)
        self.show = show

    def update(self):
        self.angle += self.rotating_speed
        self.cur_pos = Vector(cos(self.angle) * self.length,
                              sin(self.angle) * self.length)

    def draw(self):
        if not self.show and self.trace:
            return
        if self.parent:
            translate(*self.parent.cur_pos)

        r, g, b, a = self.color.rgba
        stroke(r, g, b, a)
        fill(r, g, b)

        if self.trace:

            # ellipse(self.cur_pos.x, self.cur_pos.y,
            #         random_uniform(1.4, 4), random_uniform(1.4, 4))
            circle(self.cur_pos.x, self.cur_pos.y, random_uniform(2, 4))
        else:
            if not self.parent:
                circle(0, 0, 10)
            line(0, 0, self.cur_pos.x, self.cur_pos.y)
            circle(self.cur_pos.x, self.cur_pos.y, 6)


def setup():
    size(1000, 1000)
    global parts, trace, first_frame
    trace = True
    first_frame = True
    parts = []
    parts.append(Part(parent=None, length=random_uniform(
        60, 120), rotating_speed=random_uniform(0.01, 0.05), trace=trace,
        show=random_uniform(0, 1) > 0.9))
    n = int(random_uniform(3, 12))
    for i in range(n):
        prev: Part = parts[-1]
        r, g, b, a = cmap(remap(i, (n, 0), (0, 1)))
        color = Color(r*255, g*255, b*255, a*255)
        temp = Part(parent=prev,
                    length=prev.length *
                    random_uniform(0.3, 1.6) *
                    (1 if random_uniform(0, 1) > 0.5 else -1),
                    rotating_speed=prev.rotating_speed *
                    random_uniform(0.2, 2.2) *
                    (1 if random_uniform(0, 1) > 0.5 else -1),
                    color=color,
                    trace=trace,
                    show=random_uniform(0, 1) > 0.4)
        parts.append(temp)


def update():
    for part in parts:
        part.update()


def draw():

    update()
    translate(width//2, height//2)

    global first_frame
    if not trace:
        background(0)
    if first_frame:
        r, g, b, _ = cmap(0.05)
        background(r * 255, g * 255, b*255)
        first_frame = False

    for part in parts:
        part.draw()


def key_pressed(event):
    if event.key == 'n':
        setup()
    elif event.key == 's':

        save(f"lj_{uuid.uuid4()}.png")


run()
