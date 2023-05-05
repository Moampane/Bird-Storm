"""
File containing functions for creating start screen and resetting.
"""

import pygame
import sys
from sprite_atk_class import Attack
from sprite_environment_class import Environment
from sprite_player_class import Player

BACKGROUND_IMG_PATH = "Animations/sky.png"
PLAYER_IMG_PATH = "Animations/Steve/Steve_front_right_idle.png"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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


def reset_environment():
    environment = Environment(
        bg_path=BACKGROUND_IMG_PATH,
        bg_width=SCREEN_WIDTH,
        bg_height=SCREEN_HEIGHT,
    )
    return environment


def reset_mc(screen):
    mc = Player(PLAYER_IMG_PATH, screen)
    return mc


def intro_screen(
    screen,
    environment,
    mc,
    player_atk_group,
    player_group,
):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                environment.start_not_pressed = False
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
