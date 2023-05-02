import pygame
import sys
from sprite_player_class import *
from sprite_environment_class import *
from sprite_atk_class import *

# Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background = pygame.image.load("graphics/background.jpeg")
# background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
environment = Environment(
    bg_path="graphics/background.jpeg",
    bg_width=SCREEN_WIDTH,
    bg_height=SCREEN_HEIGHT,
)
env_group = pygame.sprite.Group()
env_group.add(environment)

# Player Group
mc = Player("Animations/Steve/Steve_front_right_idle.png", screen)
player_group = pygame.sprite.Group()
player_group.add(mc)

# attack placeholder
attack = pygame.sprite.Sprite()
enemy_atk = pygame.sprite.Sprite()

# Attack groups
player_atk_group = pygame.sprite.Group()
enemy_atk_group = pygame.sprite.Group()

# Enemy Group
enemy_group = pygame.sprite.Group()

# Boss Group
boss_group = pygame.sprite.Group()

timer = 0

# Game Loop
while True:
    timer += 1
    # Background
    env_group.draw(screen)
    env_group.update(screen, enemy_group, boss_group, mc)

    # Enemies
    enemy_group.draw(screen)
    enemy_group.update()

    # Boss
    boss_group.draw(screen)
    boss_group.update(environment.spawn_timer)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pygame.sprite.Sprite.alive(mc):
                attack = Attack(mc, player_atk_group)

    if timer % 100 == 0:
        for enemy in enemy_group:
            enemy_atk = Attack(enemy, enemy_atk_group)

    # Player
    player_group.draw(screen)
    player_group.update()

    # Attacks
    player_atk_group.draw(screen)
    enemy_atk_group.draw(screen)
    player_atk_group.update()
    enemy_atk_group.update()

    # Attacks hit enemy
    if pygame.sprite.Sprite.alive(attack):
        attack_hit_enemy = pygame.sprite.spritecollide(
            attack, enemy_group, False
        )
        for enemy in attack_hit_enemy:
            enemy.take_damage(mc.atk, environment)

    # Enemies hit player
    for enemy in enemy_group:
        if pygame.sprite.Sprite.alive(enemy_atk):
            for enemy_atk in enemy_atk_group:
                enemy_atk_hit_player = pygame.sprite.spritecollide(
                    enemy_atk, player_group, False
                )
                for mc in enemy_atk_hit_player:
                    mc.take_damage(enemy.atk)

    # enemies_hit_player = pygame.sprite.spritecollide(mc, enemy_group, False)
    # for enemy in enemies_hit_player:
    #     mc.take_damage(enemy.atk)

    # Attacks hit boss
    if pygame.sprite.Sprite.alive(attack):
        attack_hit_boss = pygame.sprite.spritecollide(attack, boss_group, False)
        for boss in attack_hit_boss:
            boss.take_damage(mc.atk, environment)

    # Boss hits player
    boss_hits_player = pygame.sprite.spritecollide(mc, boss_group, False)
    for boss in boss_hits_player:
        mc.take_damage(boss.atk)

    pygame.display.flip()
    clock.tick(60)
