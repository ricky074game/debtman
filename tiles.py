import pygame
from os import walk

class Tile(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
   # self.image.fill("grey")
    self.image = pygame.image.load("game/game_wall.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (32, 32))
    self.rect = self.image.get_rect(topleft=pos)

  def update(self,x_shift):
    self.rect.x+=x_shift

class Kasa(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
   # self.image.fill("grey")
    self.image = pygame.image.load("game/kasa.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (128, 128))
    self.rect = self.image.get_rect(topleft=pos)

  def update(self,x_shift):
    self.rect.x+=x_shift

class ATM(pygame.sprite.Sprite):

  def __init__(self, pos, size):
    super().__init__()
    self.image=pygame.Surface((size,size))
   # self.image.fill("grey")
    self.image = pygame.image.load("game/atm.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (128, 224))
    self.rect = self.image.get_rect(topleft=pos)

  def update(self,x_shift):
    self.rect.x+=x_shift
