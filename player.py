import pygame as pg
import sys

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_idle = pg.image.load('art/player/player_idle.png')
        player_attack = pg.image.load('art/player/player_attack.png')
        self.surf = [player_idle, player_attack]
        self.rect = self.surf[0].get_rect()
        self.SPEED = 10
        self.force_x = 0
        self.force_y = 0
        self.attack_index = 0
        self.jump_index = 0
        self.facing_right = 1

    def draw(self, game):
        if self.facing_right:
            game.screen.blit(self.surf[self.attack_index], self.rect)
        else:
            game.screen.blit(pg.transform.flip(self.surf[self.attack_index], True, False), self.rect)
        

    def update(self, game):
        keyboard = pg.key.get_pressed()
        if keyboard[pg.K_w] and self.jump_index == 0:

            self.force_y = -20
            self.jump_index = 1
        
        elif self.jump_index:

            self.force_y += 1
            self.rect.y += self.force_y

            if self.rect.y >= 550:
                self.rect.y = 550
                self.jump_index = 0

        if keyboard[pg.K_a]:
            self.force_x -= 1
            self.facing_right = 0

        if keyboard[pg.K_d]:
            self.force_x += 1
            self.facing_right = 1

        if not keyboard[pg.K_d] and not keyboard[pg.K_a]:
            if self.force_x > 0:
                self.force_x -=1

            if self.force_x < 0:
                self.force_x +=1


        if self.force_x > self.SPEED: self.force_x = self.SPEED
        if self.force_x < -self.SPEED: self.force_x = -self.SPEED

        self.rect.x += self.force_x

        



        
            




