import sys
import pygame
from cake import Cake
from tab_cakes import TabCakes
"""
Développeur: Pascal,Amir,Dina,Dave
Designer: Emy LIM

"""

pygame.init()
pygame.display.set_caption("CakeCrush")
clock = pygame.time.Clock()



format = width, height = 1200, 800
screen = pygame.display.set_mode(format)
background = pygame.image.load('Fond.jpg')

tabCakes = TabCakes(300, 100, 10, 8)
cakes = tabCakes.getGroup()
font=pygame.font.Font(None, 100)

running = True
Finish = False
SCORE_ATTEINDRE = 18000

while running:
  screen.blit(background, (0,0))
  clock.tick(90)
  cakes.draw(screen)
  for event in pygame.event.get():
    if event.type == pygame.QUIT :
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN and not Finish:
      pos = pygame.mouse.get_pos()
      clicked_cakes = [c for c in cakes if c.rect.collidepoint(pos)]
      if len(clicked_cakes) > 0:
        cCake = clicked_cakes.pop()
        tabCakes.onclick(cCake)


  score = tabCakes.get_score()
  score_display = font.render(str(score),1,(59,111,171))
  nb_clicked = tabCakes.get_clicked()
  nb_clicked_display = font.render(str(nb_clicked),1,(59,111,171))
  screen.blit(score_display, (50, 25))
  if nb_clicked >9 :
    screen.blit(nb_clicked_display, (90, 380))
  else :
    screen.blit(nb_clicked_display, (110, 380))

  tabCakes.update()
  if score > SCORE_ATTEINDRE:
    Congratulations = pygame.image.load('Congratulations.png')
    Finish = True
    screen.blit(Congratulations,(0,0))
  if nb_clicked == 0 and score < SCORE_ATTEINDRE:
    Game_Over = pygame.image.load('GA.png')
    screen.blit(Game_Over,(0,0))
    Finish = True

  pygame.display.update()

pygame.quit()