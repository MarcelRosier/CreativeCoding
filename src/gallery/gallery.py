from __future__ import annotations
from typing import List
from p5 import *


class Frame():

    def __init__(self, img: PImage, x: int, y: int, width: int, height: int):
        self.img: PImage = img
        self.x: int = x
        self.y: int = y
        self.frame = load_image('../../media/assets/frame.png')
        self.padding = 25
        self.width: int = width - 2*self.padding
        self.height: int = height - 2*self.padding

    def draw(self):
        image(self.img, self.x + self.padding, self.y +
              self.padding, self.width, self.height)
        image(self.frame, self.x+self.padding, self.y +
              self.padding, self.width, self.height)


class FrameWall():

    def __init__(self, frames_imgs):
        self.frames = []
        self.rows = 3
        self.cols = ceil(len(frames_imgs)/self.rows)
        self.width = 300

        for y in range(self.rows):
            for x in range(self.cols):
                index = y*self.rows + x
                if index >= len(frames_imgs):
                    break
                self.frames.append(Frame(img=frames_imgs[index],
                                         x=x*self.width,
                                         y=y*self.width,
                                         width=self.width,
                                         height=self.width))
        print(self.frames)

    def draw(self):
        for frame in self.frames:
            frame.draw()


def load_frame_imgs(folder_path: str) -> List(PImage):
    import os
    import random
    files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    random.shuffle(files)
    imgs = [load_image(f"{folder_path}/{file}") for file in files]
    return imgs


def setup():
    size(1200, 1200)
    no_loop()
    global wall
    frame_imgs = load_frame_imgs('../maurer_rose')[:16]
    wall = FrameWall(frame_imgs)


def draw():
    background(10)
    wall.draw()


def key_pressed(event):
    if event.key == 's':
        save('gallery.png')
    if event.key == 'n':
        setup()
        draw()


run()
