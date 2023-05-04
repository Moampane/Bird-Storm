import pygame
import sys
from sprite_player_class import *
from sprite_environment_class import *
from sprite_atk_class import *
from sprite_bullet_class import *

# Setup
pygame.init()
clock = pygame.time.Clock()
BACKGROUND_IMG_PATH = "Animations/sky.png"

# Game Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background = pygame.image.load("graphics/background.jpeg")
# background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
environment = Environment(
    bg_path=BACKGROUND_IMG_PATH,
    bg_width=SCREEN_WIDTH,
    bg_height=SCREEN_HEIGHT,
)
env_group = pygame.sprite.Group()
env_group.add(environment)

# intro screen
WELCOME_FONT = pygame.font.Font("fonts/pixel.ttf", 95)
START_FONT = pygame.font.Font("fonts/pixel.ttf", 50)
background_img = pygame.image.load(BACKGROUND_IMG_PATH)
background_img = pygame.transform.scale(
    background_img, (SCREEN_WIDTH, SCREEN_HEIGHT)
)
welcome_txt = WELCOME_FONT.render("WELCOME TO BIRD GAME!", False, "Blue")
welcome_txt_size = pygame.font.Font.size(WELCOME_FONT, "WELCOME TO BIRD GAME!")
start_txt = START_FONT.render("Press Enter to start!", False, "Blue")
start_txt_size = pygame.font.Font.size(START_FONT, "Press Enter to start!")
controls_txt_w = START_FONT.render("W: Up", False, "Blue")
controls_txt_a = START_FONT.render("A: Left", False, "Blue")
controls_txt_s = START_FONT.render("S: Down", False, "Blue")
controls_txt_d = START_FONT.render("D: Right", False, "Blue")
controls_txt_space = START_FONT.render("Space: Attack", False, "Blue")
controls_y_gap = start_txt_size[1] + 50

# Player Group
mc = Player("Animations/Steve/Steve_front_right_idle.png", screen)
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
start_not_pressed = True

while start_not_pressed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_not_pressed = False
            if event.key == pygame.K_SPACE and pygame.sprite.Sprite.alive(mc):
                player_atk = Attack(mc, player_atk_group)

    screen.blit(background_img, (0, 0))
    player_group.draw(screen)
    player_group.update()
    player_atk_group.draw(screen)
    player_atk_group.update()

    screen.blit(
        welcome_txt,
        (
            SCREEN_WIDTH / 2 - welcome_txt_size[0] / 2,
            SCREEN_HEIGHT / 3 - welcome_txt_size[1] / 2 - start_txt_size[1],
        ),
    )
    screen.blit(
        start_txt,
        (
            SCREEN_WIDTH / 2 - start_txt_size[0] / 2,
            SCREEN_HEIGHT / 3,
        ),
    )

    screen.blit(
        controls_txt_w,
        (
            start_txt_size[0] / 3,
            SCREEN_HEIGHT / 3 + controls_y_gap,
        ),
    )
    screen.blit(
        controls_txt_a,
        (
            start_txt_size[0] / 3,
            SCREEN_HEIGHT / 3 + controls_y_gap * 1.5,
        ),
    )
    screen.blit(
        controls_txt_s,
        (
            start_txt_size[0] / 3,
            SCREEN_HEIGHT / 3 + controls_y_gap * 2,
        ),
    )
    screen.blit(
        controls_txt_d,
        (
            start_txt_size[0] / 3,
            SCREEN_HEIGHT / 3 + controls_y_gap * 2.5,
        ),
    )
    screen.blit(
        controls_txt_space,
        (
            start_txt_size[0],
            SCREEN_HEIGHT / 3 + controls_y_gap,
        ),
    )
    pygame.display.flip()
    clock.tick(60)


# Game Loop
while not start_not_pressed:
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

    # enemies_hit_player = pygame.sprite.spritecollide(mc, enemy_group, False)
    # for enemy in enemies_hit_player:
    #     mc.take_damage(enemy.atk)

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
