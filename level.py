from os import kill
import pygame,random
from tiles import *
from config import tile_size,en,boy,level_map
from player import Player

class Level(pygame.sprite.Sprite):
  def __init__(self,level_data,surface):
    self.display_surface=surface
    self.setup_level(level_data)
    self.world_shift=0
    self.player_died_flag = False
    self.font =  pygame.font.Font("game/SHPinscher-Regular.otf", 36)
    self.message = None 
    self.para=10
    self.gold=1
    self.goldd=58.5
    self.euro=1.5
    self.eurok=0
    self.borç=500
    self.show_button = False
    self.show_button2 = False
    self.show_button3 = False
    self.show_button4 = False
    self.show_button5 = False
    self.player_died_flag = False
    self.draw_button3_rect = pygame.Rect(215, 86, 60, 30)
    self.draw_button4_rect = pygame.Rect(215, 126, 60, 30)
    self.draw_button5_rect = pygame.Rect(215, 166, 60, 30)
    self.draw_button2_rect = pygame.Rect(530, 40, 60, 30)
    self.draw_button1_rect = pygame.Rect(530, 85, 60, 30)
    self.clock = pygame.time.Clock()
    self.euro_timer = 1000
    self.goldd_history = []
    self.eurok_history = []
  
  def setup_level(self,layout):
    self.tiles=pygame.sprite.Group()
    self.player=pygame.sprite.GroupSingle()
    self.kasa=pygame.sprite.GroupSingle()
    self.atm=pygame.sprite.GroupSingle()
    for row_index,row in enumerate(layout):
      for col_index,cell in enumerate(row):
        x=col_index*tile_size
        y=row_index*tile_size
        if cell=="X":
          tile=Tile((x,y),tile_size)
          self.tiles.add(tile)
        if cell=="P":
          player_sprite=Player((x,y), self.display_surface)
          self.player.add(player_sprite)
        if cell=="K":
          kasa=Kasa((x,y),tile_size)
          self.kasa.add(kasa)
        if cell=="A":
          atm=ATM((x,y),tile_size)
          self.atm.add(atm)

  
  def collision(self):
    player=self.player.sprite
    player.rect.x+=player.direction.x*player.speed


    for sprite in self.tiles.sprites():
      if sprite.rect.colliderect(player.rect):
        if player.direction.x>0:
          player.rect.right=sprite.rect.left
        elif player.direction.x<0:
          player.rect.left=sprite.rect.right

    kasa_collision = pygame.sprite.spritecollide(player, self.kasa, False)
    if kasa_collision:
        self.message = self.font.render(f"Dollar:{self.para}$", True, (0, 0, 0))
        self.message2 = self.font.render(f"Gold:{self.gold}", True, (0, 0, 0))
        self.message3 = self.font.render(f"EURO:{self.eurok}€", True, (0, 0, 0))
        self.message4 = self.font.render(f"Debts:{self.borç}$", True, (0, 0, 0))
        pygame.draw.rect(self.display_surface, (255, 255, 255), (32, 32, 250, 180)) 
        self.display_surface.blit(self.message, (40, 40))
        self.display_surface.blit(self.message2, (40, 80))
        self.display_surface.blit(self.message3, (40, 120))
        self.display_surface.blit(self.message4, (40, 160))
      
        text_surface = self.font.render("Sell", True, (255, 255, 255))
        button_rect3 = pygame.Rect(215, 86, 60, 30)  # Sell button
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect3)
        text_rect = text_surface.get_rect(center=button_rect3.center)
        self.display_surface.blit(text_surface, text_rect)
        self.show_button3 = True  # Show "Sell" button

        button_rect4 = pygame.Rect(215, 126, 60, 30)  # Sell button
        text_rect = text_surface.get_rect(center=button_rect4.center)
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect4)
        self.display_surface.blit(text_surface, text_rect)
        self.show_button4 = True  # Show "Sell" button
      
        text_surface2 = self.font.render("Pay", True, (255, 255, 255))
        button_rect5 = pygame.Rect(215, 166, 60, 35)  # Sell button
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect5)
        text_rect = text_surface.get_rect(center=button_rect5.center)
        self.display_surface.blit(text_surface2, text_rect)
        self.show_button5 = True  # Show "Sell" button
    
    else:
            self.message = None
            self.show_button3 = False  # Hide "Sell" button
            self.show_button4 = False
            self.show_button5 = False

    ATM_collision = pygame.sprite.spritecollide(player, self.atm, False)
    if ATM_collision:
        self.message2 = self.font.render(f"EURO:{self.euro}$", True, (0, 0, 0))
        self.message = self.font.render(f"Gold:{self.goldd}$", True, (0, 0, 0))
        pygame.draw.rect(self.display_surface, (255, 255, 255), (362, 32, 240, 100)) 
        
        button_rect = pygame.Rect(530, 40, 60, 40)
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect)
        text_surface = self.font.render("Buy", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.display_surface.blit(text_surface, text_rect)
        self.display_surface.blit(self.message, (370, 40))
        self.display_surface.blit(self.message2, (370, 80))

        button_rect2 = pygame.Rect(530, 85, 60, 40)
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect2)
  #  text_surface = font.render("Buy", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect2.center)
        self.display_surface.blit(text_surface, text_rect)
        self.display_surface.blit(self.message, (370, 40))
        self.display_surface.blit(self.message2, (370, 80))

    else:
        self.message = None
      
    ATM_collision = pygame.sprite.spritecollide(player, self.atm, False)
    if ATM_collision:
            self.show_button = True
            self.show_button2 = True
    else:
            self.show_button = False
            self.show_button2=False

  def collision_y(self):
    player=self.player.sprite
    player.apply_gravity()

    for sprite in self.tiles.sprites():
      if sprite.rect.colliderect(player.rect):
        if player.direction.y>0:
          player.is_jumping=False
          player.rect.bottom=sprite.rect.top
          player.direction.y=0
        elif player.direction.y<0:
          player.rect.top=sprite.rect.bottom
          player.direction.y=0

  
  def draw_button(self):
        button_rect = pygame.Rect(450, 50, 60, 30)  # Butonun koordinatları ve boyutu
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect)  # Kırmızı bir dikdörtgen

        # Buton üzerindeki metin
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Buy", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.display_surface.blit(text_surface, text_rect)

  def draw_button2(self):
    button_rect = pygame.Rect(450, 50, 60, 30)  # Butonun koordinatları ve boyutu
    pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect)  # Kırmızı bir dikdörtgen

    # Buton üzerindeki metin
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Buy", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    self.display_surface.blit(text_surface, text_rect)

  def draw_button3(self):
        button_rect = pygame.Rect(165, 86, 60, 30)  # Butonun koordinatları ve boyutu
        pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect)  # Kırmızı bir dikdörtgen

        # Buton üzerindeki metin
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Sell", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.display_surface.blit(text_surface, text_rect)

  def draw_button4(self):
    button_rect = pygame.Rect(165, 126, 60, 30)  # Butonun koordinatları ve boyutu
    pygame.draw.rect(self.display_surface, (255, 0, 0), button_rect)  # Kırmızı bir dikdörtgen

    # Buton üzerindeki metin
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Sell", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button_rect.center)
    self.display_surface.blit(text_surface, text_rect)

  def reset_game(self):
    self.setup_level(level_map)
    self.player.sprite.rect.x = 200
    self.player.sprite.rect.y = 0
    self.world_shift = 0
    self.para = 10
    self.gold = 1
    self.euro = 1.5
    self.eurok = 0
    self.borç = 500
    self.show_button = False
    self.show_button2 = False
    self.show_button3 = False
    self.show_button4 = False
    self.show_button5 = False
    self.player_died_flag = False
    self.euro_timer = 1000

  def draw_graphs(self):
  # Define graph dimensions and position
    graph_width = 200
    graph_height = 100
    graph_x = 10
    graph_y = 10
    pygame.draw.line(self.display_surface, (255, 255, 255), (graph_x, graph_y + graph_height), (graph_x + graph_width, graph_y + graph_height))

    #Draw y-axis
    pygame.draw.line(self.display_surface, (255, 255, 255), (graph_x, graph_y), (graph_x, graph_y + graph_height))
    # Calculate maximum value for scaling
    max_value = max(max(self.goldd_history, default=0), max(self.eurok_history, default=0))

    # Only draw lines if there is more than one point
    if len(self.goldd_history) > 1:
      # Draw goldd line
      for i in range(1, len(self.goldd_history)):
        pygame.draw.line(self.display_surface, (255, 0, 0), 
                        (graph_x + (i - 1) * graph_width / len(self.goldd_history), graph_y + graph_height - (self.goldd_history[i - 1] / max_value) * graph_height), 
                        (graph_x + i * graph_width / len(self.goldd_history), graph_y + graph_height - (self.goldd_history[i] / max_value) * graph_height))

    if len(self.eurok_history) > 1:
      # Draw eurok line
      for i in range(1, len(self.eurok_history)):
        pygame.draw.line(self.display_surface, (0, 255, 0), 
                        (graph_x + (i - 1) * graph_width / len(self.eurok_history), graph_y + graph_height - (self.eurok_history[i - 1] / max_value) * graph_height), 
                        (graph_x + i * graph_width / len(self.eurok_history), graph_y + graph_height - (self.eurok_history[i] / max_value) * graph_height))

  
  def lost(self):
    pygame.time.wait(500)
    font = pygame.font.Font("game/SHPinscher-Regular.otf", 56)
    font2 = pygame.font.Font("game/SHPinscher-Regular.otf", 26)
    self.display_surface.fill((20, 20, 20))
    text = font.render("YOU LOST", True, (255, 0, 0))
    text_rect = text.get_rect(center=(en / 2, boy / 2))
    text2 = font2.render("Press Enter to reboot", True, (255, 0, 0))
    text_rect2= text2.get_rect(center=(120, boy-20))
    self.display_surface.blit(text2, text_rect2)
    self.display_surface.blit(text, text_rect)
    pygame.display.flip()

  def win(self):
    pygame.time.wait(500)
    font = pygame.font.Font("game/SHPinscher-Regular.otf", 56)
    font2 = pygame.font.Font("game/SHPinscher-Regular.otf", 26)
    self.display_surface.fill((20, 20, 20))
    text = font.render("You managed to pay off your debts", True, (255, 0, 0))
    text_rect = text.get_rect(center=(375, boy / 2))
    text2 = font2.render("Press Enter to reboot", True, (255, 0, 0))
    text_rect2= text2.get_rect(center=(120, boy-20))
    self.display_surface.blit(text2, text_rect2)
    self.display_surface.blit(text, text_rect)
    pygame.display.flip()
  
  def run(self):
    self.tiles.update(self.world_shift)
    self.tiles.draw(self.display_surface)
    
    self.kasa.update(self.world_shift)
    self.kasa.draw(self.display_surface)

    self.atm.update(self.world_shift)
    self.atm.draw(self.display_surface)
    self.draw_graphs()

    if self.message:
        self.display_surface.blit(self.message, (370, 50))

    if self.show_button:
      self.draw_button()

    if self.show_button2:
      self.draw_button2()

    if self.show_button3:
      self.draw_button3()

    if self.show_button4:
      self.draw_button4()

    if pygame.time.get_ticks() - self.euro_timer > 1000:  # 1000 milisaniye = 1 saniye
      self.euro = random.choice([1.5, 2, 1, 0.5, 3.5,4.5,3,4,5])
      self.goldd = random.choice([58.5, 60, 59, 62.5, 50.5,55.5,56,63,57])
      self.euro_timer = pygame.time.get_ticks()
      self.borç += random.choice([0,0.5,1,1.5,2])

    if self.para<=0:
      self.para=0
    
    self.player.update()
    self.collision()
    self.collision_y()
    self.player.draw(self.display_surface)

    if self.para==0 and self.eurok==0 and self.gold==0 and self.borç>0:
       self.player_died_flag = True
       if self.player_died_flag==True:
         self.lost()

    if self.para==0 and self.eurok==0 and self.gold==0 and self.borç<=0:
       self.win()
    
    if self.borç<=0:
      self.win()
    self.goldd_history.append(self.goldd)
    self.eurok_history.append(self.euro)
    self.clock.tick(60)