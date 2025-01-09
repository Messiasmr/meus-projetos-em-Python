import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("python teteris")

clock = pygame.time.Clock

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
    clock.tick(60)
        