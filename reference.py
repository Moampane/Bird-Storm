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
player_heading = 0
player_hitbox = player_image.get_rect(center=(200, 500))

# player starting position
# mouse_pos = (0, 0)

# stats
health = 100

# enemy
penguin_image = pygame.image.load("graphics/penguin.png").convert_alpha()
penguin_image = pygame.transform.scale(penguin_image, (100, 100))
penguin_alive = True
px = 1500
py = 650

# attack
attack_image = pygame.image.load("graphics/bite.png").convert_alpha()
attack_image = pygame.transform.scale(attack_image, (300, 100))
attack_hitbox = attack_image.get_rect(center=(-50, -50))


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

    # attack
    # mouse_buttons = pygame.mouse.get_pressed()
    # if mouse_buttons[0]:
    #     mouse_pos = pygame.mouse.get_pos()
    #     attack_hitbox = attack_image.get_rect(
    #         topleft=(player_hitbox.x + 100, player_hitbox.y)
    #     )
    #     screen.blit(attack_image, attack_hitbox)
    # print(mouse_pos)

    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_hitbox.x -= 5
    if keys[pygame.K_d]:
        player_hitbox.x += 5
    if keys[pygame.K_w]:
        player_hitbox.y -= 5
    if keys[pygame.K_s]:
        player_hitbox.y += 5

    # player rotation
    if keys[pygame.K_UP]:
        if player_heading == 0:
            change = 90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 180:
            change = -90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 270:
            change = -180
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
    if keys[pygame.K_DOWN]:
        if player_heading == 0:
            change = 270
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 90:
            change = 180
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 180:
            change = 90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
    if keys[pygame.K_LEFT]:
        if player_heading == 0:
            change = 180
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 90:
            change = 90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 270:
            change = -90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
    if keys[pygame.K_RIGHT]:
        if player_heading == 90:
            change = -90
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 180:
            change = -180
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change
        elif player_heading == 270:
            change = -270
            player_image = pygame.transform.rotate(player_image, change)
            player_heading += change

    # player attack
    if keys[pygame.K_SPACE]:
        if player_heading == 0:
            attack_image = pygame.transform.scale(attack_image, (100, 300))
            attack_hitbox = attack_image.get_rect(
                center=(player_hitbox.x + 150, player_hitbox.y + 50)
            )

        if player_heading == 90:
            attack_image = pygame.transform.scale(attack_image, (300, 100))
            attack_hitbox = attack_image.get_rect(
                center=(player_hitbox.x + 50, player_hitbox.y - 50)
            )
        if player_heading == 180:
            attack_image = pygame.transform.scale(attack_image, (100, 300))
            attack_hitbox = attack_image.get_rect(
                center=(player_hitbox.x - 50, player_hitbox.y + 50)
            )
        if player_heading == 270:
            attack_image = pygame.transform.scale(attack_image, (300, 100))
            attack_hitbox = attack_image.get_rect(
                center=(player_hitbox.x + 50, player_hitbox.y + 150)
            )
        screen.blit(attack_image, attack_hitbox)

    # player
    # screen.blit(player_image, player_hitbox)
    # player_hitbox.x = mouse_pos[0]
    # player_hitbox.y = mouse_pos[1]
    screen.blit(player_image, player_hitbox)

    # updating health
    health_display = test_font.render(f"Health = {health}", False, "Red")
    screen.blit(health_display, (600, 0))

    # player_hitbox.x += 1
    if penguin_alive:
        penguin_hitbox = penguin_image.get_rect(topleft=(px, py))
        # penguin_hitbox.x -= 4
        px -= 4
        # if penguin_hitbox.x < -500:
        #     penguin_hitbox.x = 1500
        if px < -500:
            px = 1500
        screen.blit(penguin_image, penguin_hitbox)
        # attack detection
        if attack_hitbox.colliderect(penguin_hitbox):
            penguin_hitbox = penguin_image.get_rect(topleft=(-1000, -1000))
            penguin_alive = False

    # collision detection
    if player_hitbox.colliderect(penguin_hitbox):
        health -= 1
        print(health)

    # reset attack hitbox
    attack_hitbox = attack_image.get_rect(topleft=(-1000, -1000))

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
