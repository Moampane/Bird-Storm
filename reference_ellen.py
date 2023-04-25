import pygame
from sys import exit
from bird_class import *
from enemy_class import *

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bird Storm")
clock = pygame.time.Clock()

environment_surface = pygame.image.load("test_map_surface.jpg").convert()
environment_surface = pygame.transform.scale(
    environment_surface, (WINDOW_WIDTH, WINDOW_HEIGHT)
)

test_player = EnemyBird("graphics/penguin.png")
test_enemies = []
test_boss = BossEnemyBird("graphics/kakapo.png")

count = 0
while True:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(environment_surface, (0, 0))

    # randomly spawn enemies
    if count % 360 == 0:
        test_bird = EnemyBird("graphics/duck.png")
        test_enemies.append(test_bird)

    # use draw() function to place enemies on screen
    for enemy in test_enemies:
        enemy.draw(screen, test_player, False)
    test_boss.draw(screen, test_player, False)
    test_player.draw(screen, test_player, True)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            test_player.sprite_rect.y -= 5
        if event.key == pygame.K_DOWN:
            test_player.sprite_rect.y += 5
        if event.key == pygame.K_LEFT:
            test_player.sprite_rect.x -= 5
        if event.key == pygame.K_RIGHT:
            test_player.sprite_rect.x += 5

    pygame.display.update()
    clock.tick(60)
