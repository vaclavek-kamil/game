import pygame as pg
import sys

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.image.load('art/bullet/bullet.png')
        self.rect = self.surf.get_rect()
        self.SPEED = 50