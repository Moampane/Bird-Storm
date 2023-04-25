from enemy_class import *
from player_class import *
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
test_player = Player(sprite_path="graphics/duck.png", attack_path="graphics/bite.png")

# test enemies
test_enemies = []


# counter for spawn rate
count = 0

# game loop
while True:
    count += 1
    # background
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        # be able to exit game
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()

    # Spawn enemies
    if count % 360 == 0:
        test_enemy = EnemyBird("graphics/penguin.png")
        test_enemies.append(test_enemy)

    # use draw() function to place enemies on screen
    # use player_attack() function to attack enemies
    for enemy in test_enemies:
        enemy.draw(screen, test_player, False)
        test_player.player_attack(screen, enemy)

    # Control player
    test_player.move()

    # Player attack
    # test_player.player_attack(screen, test_enemy)

    # Draw player on screen
    test_player.draw(screen)

    # Draw enemy on screen
    # test_enemy.draw(screen, test_player, False)

    pygame.display.update()
    clock.tick(60)
