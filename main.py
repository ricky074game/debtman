import sys,pygame
from config import *
from level import Level
from player import *
import asyncio

pygame.init()

ekran = pygame.display.set_mode((en, boy))
clock=pygame.time.Clock()
level=Level(level_map,ekran)
pygame.display.set_caption("WILLY TRYS TO MAKE MONEY")
arkaplan_resmi = pygame.image.load("game/bg.png") 
async def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and level.player_died_flag == True:
                  level.player_died_flag = False
                  level.reset_game()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
          player = level.player.sprite
          if level.show_button and level.para>=level.euro:  
            if level.draw_button1_rect.collidepoint(event.pos):
              level.para -= level.euro
              level.eurok+=level.euro
          if level.show_button2 and level.para>=level.goldd:  
            if level.draw_button2_rect.collidepoint(event.pos):
              level.para -= level.goldd
              level.gold+=1
          if level.show_button3 and level.gold>0:  
            if level.draw_button3_rect.collidepoint(event.pos):
              level.para += level.goldd*level.gold
              level.gold=0
          if level.show_button4 and level.eurok>0:  
            if level.draw_button4_rect.collidepoint(event.pos):
              level.para += level.euro*level.eurok
              level.eurok = 0
          if level.show_button5 and level.para>0:  
            if level.draw_button5_rect.collidepoint(event.pos):
              level.borç -= level.para
              level.para = 0
    
    ekran.fill((10,50,10))
    ekran.blit(arkaplan_resmi, (0, 0))
    ekran.blit(arkaplan_resmi, (448, 0))
    level.run()
    pygame.display.update()
    clock.tick(60)
    await asyncio.sleep(0)
asyncio.run(main())