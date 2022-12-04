import pygame as pg
import sys

from settings import *
from player import *
from bullet import *


class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        #define instances here
        self.player = Player()
        self.map = pg.image.load('art/map/map.png')

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)   
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

        self.player.update(game)

    def draw(self):
        self.screen.blit(self.map, (0,0))
        self.player.draw(game)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            


    def run(self):
        while True:
           #insert code here



             
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()