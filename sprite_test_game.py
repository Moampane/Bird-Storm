"""
File for running the main game loop.
"""
import sys
import pygame
from sprite_player_class import Player
from sprite_environment_class import Environment
from sprite_atk_class import Attack
from start_game import intro_screen, reset_mc, reset_environment

# Setup
pygame.init()
clock = pygame.time.Clock()

BACKGROUND_IMG_PATH = "Animations/sky.png"
PLAYER_IMG_PATH = "Animations/Steve/Steve_front_right_idle.png"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
environment = Environment(
    bg_path=BACKGROUND_IMG_PATH,
    bg_width=SCREEN_WIDTH,
    bg_height=SCREEN_HEIGHT,
)
env_group = pygame.sprite.Group()
env_group.add(environment)

# Player Group
mc = Player(PLAYER_IMG_PATH, screen)
player_group = pygame.sprite.Group()
player_group.add(mc)

# attack placeholder
player_atk = pygame.sprite.Sprite()
enemy_atk = pygame.sprite.Sprite()

# Attack groups
player_atk_group = pygame.sprite.Group()
enemy_atk_group = pygame.sprite.Group()
boss_bullet_group = pygame.sprite.Group()

# Enemy Group
enemy_group = pygame.sprite.Group()

# Boss Group
boss_group = pygame.sprite.Group()

timer = 0

reset_game = False

# Game Loop
while True:
    # Option to reset the game (runs once the game is over)
    if environment.reset_game:
        mc = reset_mc(screen)
        environment = reset_environment()

        # reset attack placeholders
        player_atk = pygame.sprite.Sprite()
        enemy_atk = pygame.sprite.Sprite()

        # reset groups
        player_atk_group = pygame.sprite.Group()
        enemy_atk_group = pygame.sprite.Group()
        boss_bullet_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        boss_group = pygame.sprite.Group()

        environment.set_reset_game(False)
        timer = 0
        environment.set_start_not_pressed(True)

    # displays introduction screen
    while environment.start_not_pressed:
        intro_screen(
            screen,
            environment,
            mc,
            player_atk_group,
            player_group,
        )
        player_group.add(mc)
        env_group.add(environment)
        pygame.display.flip()
        clock.tick(60)

    timer += 1
    # Background
    env_group.draw(screen)
    env_group.update(screen, enemy_group, boss_group, mc, boss_bullet_group)

    # Enemies
    enemy_group.draw(screen)
    enemy_group.update()

    # Bullets
    boss_bullet_group.draw(screen)
    boss_bullet_group.update()

    # Boss
    boss_group.draw(screen)
    boss_group.update()

    # Be able to quit game and attack
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pygame.sprite.Sprite.alive(mc):
                player_atk = Attack(mc, player_atk_group)

    for enemy in enemy_group:
        if enemy.atk_timer % 69 == 0:
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
    if pygame.sprite.Sprite.alive(player_atk):
        attack_hit_enemy = pygame.sprite.spritecollide(
            player_atk, enemy_group, False
        )
        for enemy in attack_hit_enemy:
            if player_atk.first_hit:
                enemy.take_damage(mc.atk, environment)
                player_atk.set_first_hit_false()

    # Enemies hit player
    for enemy in enemy_group:
        if pygame.sprite.Sprite.alive(enemy_atk):
            for enemy_atk in enemy_atk_group:
                enemy_atk_hit_player = pygame.sprite.spritecollide(
                    enemy_atk, player_group, False
                )
                if enemy_atk.first_hit:
                    for mc in enemy_atk_hit_player:
                        mc.take_damage(enemy.atk)
                    enemy_atk.set_first_hit_false()

    # Attacks hit boss
    if pygame.sprite.Sprite.alive(player_atk):
        attack_hit_boss = pygame.sprite.spritecollide(
            player_atk, boss_group, False
        )
        for boss in attack_hit_boss:
            if player_atk.first_hit:
                boss.take_damage(mc.atk, environment)
                player_atk.set_first_hit_false()

    # Boss hits player
    boss_hits_player = pygame.sprite.spritecollide(mc, boss_group, False)
    for boss in boss_hits_player:
        mc.take_damage(boss.atk)

    # Bullet hits player
    if len(boss_bullet_group.sprites()) > 0:
        bullet_hits_player = pygame.sprite.spritecollide(
            mc, boss_bullet_group, False
        )
        for bullet in bullet_hits_player:
            if bullet.first_hit:
                mc.take_damage(bullet.damage)
                bullet.set_first_hit_false()
                bullet.kill()

    pygame.display.flip()
    clock.tick(60)
