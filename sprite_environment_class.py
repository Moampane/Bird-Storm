"""
File for environment class.
"""
import pygame, sprite_enemy_class

pygame.init()

FONT = pygame.font.SysFont("arial", 30)
VICTORY_FONT = pygame.font.SysFont("arial", 150, True)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LVL_1_INTERVAL = 400
LVL_2_INTERVAL = 200
LVL_3_INTERVAL = 100
MAX_ENEMIES_ON_SCREEN = 8

RONALD_ENEMY_PATH = "Animations/Ronald/Ronald_front_right_idle.png"
ED_ENEMY_PATH = "Animations/Eduardo/Eduardo_front_right_idle.png"
EMILY_ENEMY_PATH = "Animations/Emily/Emily_front_right_idle.png"


class Environment(pygame.sprite.Sprite):
    def __init__(self, bg_path, bg_width, bg_height):
        pygame.sprite.Sprite.__init__(self)
        self._screen_width = bg_width
        self._screen_height = bg_height
        self._image = pygame.image.load(bg_path)
        self._image = pygame.transform.scale(
            self._image, (self._screen_width, self._screen_height)
        )
        self._rect = self._image.get_rect(topleft=(0, 0))
        self.num_enemies = 0
        self.num_enemies_slain = 0
        self.level = 1
        self.spawn_timer = 0
        self._boss_spawned = False
        self._boss_slain = False

    def set_boss_slain_true(self):
        """
        Sets the _boss_slain attribute to True
        """
        self._boss_slain = True

    @property
    def image(self):
        """
        Returns the pygame image.
        """
        return self._image

    @property
    def rect(self):
        """
        Returns the pygame rectangle.
        """
        return self._rect

    def update(self, screen, enemy_group, boss_group, player):
        self.display_num_enemies(screen, enemy_group)
        self.display_level(screen)
        self.display_num_enemies_slain(screen)

        # Level 1
        # put this back to level 1 when done testing
        if self.level == 1:
            if self.num_enemies < 10:
                if self.spawn_timer % LVL_1_INTERVAL == 0:
                    tier1_enemy = sprite_enemy_class.Enemy(
                        image_path=RONALD_ENEMY_PATH,
                        screen=screen,
                        player=player,
                        tier=self.level,
                    )
                    enemy_group.add(tier1_enemy)
                if self.num_enemies_slain >= 2:
                    self.level = 2

        # Level 2
        if self.level == 2:
            if self.num_enemies < 10:
                if self.spawn_timer % LVL_2_INTERVAL == 0:
                    tier2_enemy = sprite_enemy_class.Enemy(
                        image_path=ED_ENEMY_PATH,
                        screen=screen,
                        player=player,
                        tier=self.level,
                    )
                    enemy_group.add(tier2_enemy)
                if self.num_enemies_slain >= 5:
                    self.level = 3

        # Level 3
        if self.level == 3:
            if self.num_enemies < 10:
                if self.spawn_timer % LVL_3_INTERVAL == 0:
                    tier3_enemy = sprite_enemy_class.Enemy(
                        image_path=EMILY_ENEMY_PATH,
                        screen=screen,
                        player=player,
                        tier=self.level,
                    )
                    enemy_group.add(tier3_enemy)
                if self.num_enemies_slain >= 7:
                    self.level = 4

        # Level 4
        if self.level == 4 and self.num_enemies < MAX_ENEMIES_ON_SCREEN:
            if self.spawn_timer % LVL_3_INTERVAL == 0:
                tier1_enemy = sprite_enemy_class.Enemy(
                    image_path=ronald_enemy_path,
                    screen=screen,
                    player=player,
                    tier=self.level - 2,
                )
                enemy_group.add(tier1_enemy)
            if self.spawn_timer % LVL_2_INTERVAL == 0:
                tier2_enemy = sprite_enemy_class.Enemy(
                    image_path=ed_enemy_path,
                    screen=screen,
                    player=player,
                    tier=self.level - 1,
                )
                enemy_group.add(tier2_enemy)
            if self.spawn_timer % LVL_1_INTERVAL == 0:
                tier3_enemy = sprite_enemy_class.Enemy(
                    image_path=emily_enemy_path,
                    screen=screen,
                    player=player,
                    tier=self.level,
                )
                enemy_group.add(tier3_enemy)
            if self.num_enemies_slain >= 15:
                self.level = 5

        # Boss
        # initalize boss
        if self.level == 5 and not self._boss_spawned:
            boss = sprite_enemy_class.Projectile_Boss(
                max_health=200,
                attack=2,
                movespeed=4,
                image_path="graphics/kakapo.png",
                start_pos=(screen.get_width() / 2, -200),
                size=(200, 200),
                bg=screen,
                player=player,
            )
            boss_group.add(boss)
            self._boss_spawned = True

        if self._boss_slain:
            self.level = 6

        # Display win
        if self.level == 6:
            self.display_win(screen)

        # Increment spawn timer
        self.spawn_timer += 1

    def display_num_enemies(self, screen, enemy_group):
        # Number of remaining enemies text
        self.num_enemies = len(pygame.sprite.Group.sprites(enemy_group))
        enemies_counter = FONT.render(
            f"Enemies Remaining: {self.num_enemies}", False, RED
        )
        screen.blit(enemies_counter, (0, 0))

    def display_level(self, screen):
        # Level text
        level_text = FONT.render(f"Level {self.level}", False, RED)
        level_text_size = pygame.font.Font.size(FONT, f"Level {self.level}")
        level_text_width = level_text_size[0]
        screen.blit(
            level_text, (self._screen_width / 2 - level_text_width / 2, 0)
        )

    def display_num_enemies_slain(self, screen):
        # Number of enemies slain text
        enemies_slain_counter = FONT.render(
            f"Enemies Slain: {self.num_enemies_slain}", False, RED
        )
        slain_text_size = pygame.font.Font.size(
            FONT, f"Enemies Slain: {self.num_enemies_slain}"
        )
        slain_text_width = slain_text_size[0]
        screen.blit(
            enemies_slain_counter, (self._screen_width - slain_text_width, 0)
        )

    def display_win(self, screen):
        # Level text
        victory_text = VICTORY_FONT.render("YOU WIN", False, YELLOW)
        victory_text_size = pygame.font.Font.size(VICTORY_FONT, "YOU WIN")
        screen.blit(
            victory_text,
            (
                self._screen_width / 2 - victory_text_size[0] / 2,
                self._screen_height / 2 - victory_text_size[1] / 2,
            ),
        )
