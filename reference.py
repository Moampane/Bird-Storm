from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("bird-storm")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/vinque rg.otf", 50)

# background
background_image = pygame.image.load("graphics/background.jpeg").convert()
background_image = pygame.transform.scale(background_image, (1500, 750))

# player
player_image = pygame.image.load("graphics/duck.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (100, 100))
player_hitbox = player_image.get_rect(topleft=(200, 500))

# player starting position
# mouse_pos = (0, 0)

# stats
health = 100

# enemy
penguin_image = pygame.image.load("graphics/penguin.png").convert_alpha()
penguin_image = pygame.transform.scale(penguin_image, (100, 100))
penguin_hitbox = penguin_image.get_rect(topleft=(1500, 650))


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_pos = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_hitbox.y -= 50
            if event.key == pygame.K_DOWN:
                player_hitbox.y += 50
            if event.key == pygame.K_LEFT:
                player_hitbox.x -= 50
            if event.key == pygame.K_RIGHT:
                player_hitbox.x += 50
        # if event.type == pygame.KEYUP:
        #     print("up")

    # background
    screen.blit(background_image, (0, 0))

    # player
    # screen.blit(player_image, player_hitbox)
    # player_hitbox.x = mouse_pos[0]
    # player_hitbox.y = mouse_pos[1]
    screen.blit(player_image, player_hitbox)

    # updating health
    health_display = test_font.render(f"Health = {health}", False, "Red")
    screen.blit(health_display, (600, 0))

    # penguin
    penguin_hitbox.x -= 4
    if penguin_hitbox.x < -500:
        penguin_hitbox.x = 1500
    # player_hitbox.x += 1
    screen.blit(penguin_image, penguin_hitbox)

    # collision detection
    if player_hitbox.colliderect(penguin_hitbox):
        health -= 1
        print(health)

    pygame.display.update()
    clock.tick(60)


# main = True

# while main:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#             main = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT or event.key == ord("a"):
#                 print("left")
#             if event.key == pygame.K_RIGHT or event.key == ord("d"):
#                 print("right")
#             if event.key == pygame.K_UP or event.key == ord("w"):
#                 print("jump")

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == ord("a"):
#                 print("left stop")
#             if event.key == pygame.K_RIGHT or event.key == ord("d"):
#                 print("right stop")
#             if event.key == ord("q"):
#                 pygame.quit()
#                 sys.exit()
#                 main = False
