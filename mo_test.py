import bird_class as bird
import player_class as p
from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("bird-storm")
clock = pygame.time.Clock()

# background
background_image = pygame.image.load("graphics/background.jpeg").convert()
background_image = pygame.transform.scale(background_image, (1500, 750))

# player
test_player = p.Player("graphics/duck.png")

# game loop
while True:

    # background
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        # be able to exit game
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    # Place player on screen
    test_player.draw(screen)

    # Control player
    test_player.move()

    pygame.display.update()
    clock.tick(60)
