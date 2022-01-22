# from pygame.sprite import Sprite
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        # super().__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,20))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.speed=0
    
    def update(self):
        self.speed=0
        tuslar = pygame.key.get_pressed()
        # print(tuslar)
        if tuslar[pygame.K_LEFT]:
            self.speed=-5
        elif tuslar[pygame.K_RIGHT]:
            self.speed=5
        self.rect.x+=self.speed
        if self.rect.left>360:
            self.rect.right=0
        elif self.rect.right<0:
            self.rect.left=360
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,color,speed=-10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speed=speed
    def update(self):
        self.rect.y+=self.speed
        if self.rect.bottom<0:
            self.kill()