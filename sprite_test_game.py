import pygame, sys, sprite_player_class, sprite_environment_class

# Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background = pygame.image.load("graphics/background.jpeg")
# background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
environment = sprite_environment_class.Environment(
    bg_path="graphics/background.jpeg", bg_width=SCREEN_WIDTH, bg_height=SCREEN_HEIGHT
)
env_group = pygame.sprite.Group()
env_group.add(environment)

# Player Group
mc = sprite_player_class.Player(
    "Animations/Eduardo/Eduardo_front_right_idle.png", screen
)
player_group = pygame.sprite.Group()
player_group.add(mc)

# attack placeholder
attack = pygame.sprite.Sprite()

# Enemy Group
enemy_group = pygame.sprite.Group()

# Boss Group
boss_group = pygame.sprite.Group()

# Game Loop
while True:

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
                attack = sprite_player_class.Attack(mc, player_group)

    # Player
    player_group.draw(screen)
    player_group.update()

    # Attacks hit enemy
    if pygame.sprite.Sprite.alive(attack):
        attack_hit_enemy = pygame.sprite.spritecollide(attack, enemy_group, False)
        for enemy in attack_hit_enemy:
            enemy.take_damage(mc.atk, environment)

    # Enemies hit player
    enemies_hit_player = pygame.sprite.spritecollide(mc, enemy_group, False)
    for enemy in enemies_hit_player:
        mc.take_damage(enemy.atk)

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
