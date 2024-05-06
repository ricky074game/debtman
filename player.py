import pygame
from config import *
class Player(pygame.sprite.Sprite):
  def __init__(self,pos,display_surface):
    super().__init__() 
    self.image = pygame.image.load("game/c1.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (64, 100)) 
    self.rect = self.image.get_rect(topleft=pos)
    self.display_surface = display_surface
    
    self.images_left =[pygame.image.load("game/c1.png").convert_alpha(),
                        pygame.image.load("game/cl2.png").convert_alpha(),
                        pygame.image.load("game/cl3.png").convert_alpha(),
                        pygame.image.load("game/c1.png").convert_alpha(),
                        pygame.image.load("game/cl4.png").convert_alpha(),
                        pygame.image.load("game/cl5.png").convert_alpha(),
                        ]
    
    self.images_right = [pygame.image.load("game/c2.png").convert_alpha(),
                        pygame.image.load("game/cr2.png").convert_alpha(),
                        pygame.image.load("game/cr3.png").convert_alpha(),
                        pygame.image.load("game/c2.png").convert_alpha(),
                        pygame.image.load("game/cr4.png").convert_alpha(),
                        pygame.image.load("game/cr5.png").convert_alpha(),
                        ]
    
    self.direction=pygame.math.Vector2(0,0)
    self.speed=10
    self.gravity=1
    self.jump_speed=-13
    self.is_jumping = False
    self.animation_counter = 0 
    self.facing="right"
    
    self.total_distance = 0
    
  def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x<=700:
            self.direction.x = 0.7
            self.facing="right"
            
        elif keys[pygame.K_LEFT] and self.rect.x>=0:
            self.direction.x = -0.7
            self.facing="left"

        if keys[pygame.K_d] and self.rect.x<=700:
            self.direction.x = 0.7
            self.facing="right"
            
        elif keys[pygame.K_a] and self.rect.x>=0:
            self.direction.x = -0.7
            self.facing="left"

    
        else:
            self.direction.x = 0
            self.animation_counter = 0

        if keys[pygame.K_SPACE] and not self.is_jumping:
          #  self.facing="up"
            self.jump()

  def animate(self):
        if self.facing == "right":self.image = self.images_right[self.animation_counter // 3 % len(self.images_right)]
        elif self.facing == "left":self.image = self.images_left[self.animation_counter // 3 % len(self.images_left)]

        self.animation_counter += 1
        font = pygame.font.Font(None, 24)  # Change the size as needed
        text_surface = font.render("Willy", True, (255, 255, 255))  # Change the color as needed
        self.display_surface.blit(text_surface, (self.rect.x, self.rect.y - text_surface.get_height()))
  
  def apply_gravity(self):
    self.direction.y+=self.gravity
    self.rect.y+=self.direction.y
  
  def jump(self):
    self.direction.y=self.jump_speed
    self.is_jumping = True
    
  def update(self):
        self.get_input()
        self.animate()