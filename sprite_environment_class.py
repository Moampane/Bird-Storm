"""
File for environment class.
"""
import pygame
from sprite_enemy_class import Enemy
from sprite_boss_class import ProjectileBoss

pygame.init()

FONT = pygame.font.Font("fonts/pixel.ttf", 35)
VICTORY_FONT = pygame.font.Font("fonts/pixel.ttf", 150)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LVL_1_INTERVAL = 400
LVL_2_INTERVAL = 200
LVL_3_INTERVAL = 100
MAX_ENEMIES_ON_SCREEN = 8

RONALD_ENEMY_PATH = "Animations/Ronald/Ronald_front_right_idle.png"
ED_ENEMY_PATH = "Animations/Eduardo/Eduardo_front_right_idle.png"
EMILY_ENEMY_PATH = "Animations/Emily/Emily_front_right_idle.png"
BOSS_ENEMY_PATH = "Animations/Philipe/Philipe_front_right_idle.png"

SCREEN_TEXT_GAP = 10


class Environment(pygame.sprite.Sprite):
    """
    A class representing the game environment. Also, controls
    level progression and enemy spawns.
    Attributes:
        _screen_width: an integer representing the width of the screen.
        _screen_height: an integer representing the height of the screen.
        _image: a pygame image representing the game background.
        _rect: a pygame rect representing the bounding box of the background.
        num_enemies: an integer representing the number of enemies currently on
        screen.
        num_enemies_slain: an integer representing the number of enemies slain.
        level: an integer representing the current level.
        spawn_timer: an integer representing the timer used for setting spawn
        rates.
        _boss_spawned: a boolean representing if the boss has spawned.
        _boss_slain: a boolean representing if the boss has been slain.
        _stop_spawning: a boolean saying if the game should stop spawning
        enemies or not
    """

    def __init__(self, bg_path, bg_width, bg_height):
        """
        Initializes an instance of the Environment.
        Args:
            bg_path: a string representing the path to a file containing the
            background image.
            bg_width: an integer representing the width of the screen.
            bg_height: an integer representing the height of the screen.
        """
        pygame.sprite.Sprite.__init__(self)
        self._screen_width = bg_width
        self._screen_height = bg_height
        self._image = pygame.image.load(bg_path)
        self._image = pygame.transform.scale(
            self._image, (self._screen_width + 30, self._screen_height)
        )
        self._rect = self._image.get_rect(topleft=(-20, 0))
        self.num_enemies = 0
        self.num_enemies_slain = 0
        self.level = 1
        self.spawn_timer = 0
        self._boss_spawned = False
        self._boss_slain = False
        self._stop_spawning = False

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

    def update(self, screen, enemy_group, boss_group, player, bullet_group):
        """
        Updates current state of the environment. Controls enemy spawns
        and displays enemies on screen, slain, and level.
        Args:
            screen: a pygame display that the game is being played on.
            enemy_group: a pygame sprite group containing all the enemy sprites.
            boss_group: a pygame sprite group containing the boss sprite.
            player: a player object representing the controllable player.
        """
        self.display_num_enemies(screen, enemy_group)
        self.display_level(screen)
        self.display_num_enemies_slain(screen)
        if not player.alive():
            self.display_loss(screen, player)
            for enemy in enemy_group:
                enemy.kill()
            return

        # Level 1
        # put this back to level 1 when done testing
        if (
            self.level == 1
            and self.num_enemies < MAX_ENEMIES_ON_SCREEN
            and not self._stop_spawning
        ):
            if self.spawn_timer % LVL_1_INTERVAL == 0:
                tier1_enemy = Enemy(
                    image_path=RONALD_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level,
                )
                enemy_group.add(tier1_enemy)
            if self.num_enemies_slain >= 2:
                self.level = 2

        # Level 2
        if (
            self.level == 2
            and self.num_enemies < MAX_ENEMIES_ON_SCREEN
            and not self._stop_spawning
        ):
            if self.spawn_timer % LVL_2_INTERVAL == 0:
                tier2_enemy = Enemy(
                    image_path=ED_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level,
                )
                enemy_group.add(tier2_enemy)
            if self.num_enemies_slain >= 5:
                self.level = 3

        # Level 3
        if (
            self.level == 3
            and self.num_enemies < MAX_ENEMIES_ON_SCREEN
            and not self._stop_spawning
        ):
            if self.spawn_timer % LVL_3_INTERVAL == 0:
                tier3_enemy = Enemy(
                    image_path=EMILY_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level,
                )
                enemy_group.add(tier3_enemy)
            if self.num_enemies_slain >= 7:
                self.level = 4

        # Level 4
        if (
            self.level == 4
            and self.num_enemies < MAX_ENEMIES_ON_SCREEN
            and not self._stop_spawning
        ):
            if self.spawn_timer % LVL_3_INTERVAL == 0:
                tier1_enemy = Enemy(
                    image_path=RONALD_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level - 2,
                )
                enemy_group.add(tier1_enemy)
            if self.spawn_timer % LVL_2_INTERVAL == 0:
                tier2_enemy = Enemy(
                    image_path=ED_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level - 1,
                )
                enemy_group.add(tier2_enemy)
            if self.spawn_timer % LVL_1_INTERVAL == 0:
                tier3_enemy = Enemy(
                    image_path=EMILY_ENEMY_PATH,
                    screen=screen,
                    player=player,
                    tier=self.level,
                )
                enemy_group.add(tier3_enemy)
        if self.level != 5 and self.num_enemies_slain >= 15:
            self._stop_spawning = True
            if self.num_enemies == 0 and self.spawn_timer % LVL_1_INTERVAL != 0:
                self.display_boss_message(screen)
                self.level = 5

        # Boss
        if self.level == 5 and not self._boss_spawned:
            boss = ProjectileBoss(
                image_path=BOSS_ENEMY_PATH,
                bg=screen,
                player=player,
                bullet_group=bullet_group,
            )
            boss_group.add(boss)
            self._boss_spawned = True

        # Display win
        if self._boss_slain:
            self.level = 6
            self.display_win(screen)

        # Increment spawn timer
        self.spawn_timer += 1

    def display_num_enemies(self, screen, enemy_group):
        """
        Displays the number of enemies on screen.
        Args:
            screen: a pygame display that the game is being played on.
            enemy_group: a pygame sprite group containing all the enemy sprites.
        """
        # Number of remaining enemies text
        self.num_enemies = len(pygame.sprite.Group.sprites(enemy_group))
        enemies_counter = FONT.render(
            f"Enemies Remaining: {self.num_enemies}", False, RED
        )
        screen.blit(enemies_counter, (SCREEN_TEXT_GAP, SCREEN_TEXT_GAP))

    def display_level(self, screen):
        """
        Displays the current level.
        Args:
            screen: a pygame display that the game is being played on.
        """
        # Level text
        level_text = FONT.render(f"Level {self.level}", False, RED)
        level_text_size = pygame.font.Font.size(FONT, f"Level {self.level}")
        level_text_width = level_text_size[0]
        screen.blit(
            level_text,
            (self._screen_width / 2 - level_text_width / 2, SCREEN_TEXT_GAP),
        )

    def display_num_enemies_slain(self, screen):
        """
        Displays the number of enemies slain.
        Args:
            screen: a pygame display that the game is being played on.
        """
        # Number of enemies slain text
        enemies_slain_counter = FONT.render(
            f"Enemies Slain: {self.num_enemies_slain}", False, RED
        )
        slain_text_size = pygame.font.Font.size(
            FONT, f"Enemies Slain: {self.num_enemies_slain}"
        )
        slain_text_width = slain_text_size[0]
        screen.blit(
            enemies_slain_counter,
            (
                self._screen_width - slain_text_width - SCREEN_TEXT_GAP,
                SCREEN_TEXT_GAP,
            ),
        )

    def display_win(self, screen):
        """
        Displays victory screen.
        Args:
            screen: a pygame display that the game is being played on.
        """
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

    def display_loss(self, screen, player):
        """
        Displays death screen, offers replay button.
        Args:
            screen: a pygame display that the game is being played on.
            player: a player object representing the controllable player.
        """
        death_text = VICTORY_FONT.render("YOU LOSE", False, RED)
        death_text_size = pygame.font.Font.size(VICTORY_FONT, "YOU LOSE")
        screen.blit(
            death_text,
            (
                self._screen_width // 2 - death_text_size[0] / 2,
                self._screen_height // 2 - death_text_size[1] / 2,
            ),
        )
        restart_text = FONT.render("lol clucking loser", False, RED)
        restart_text_size = pygame.font.Font.size(
            VICTORY_FONT, "lol clucking loser"
        )
        screen.blit(
            restart_text,
            (
                self._screen_width // 2,
                self._screen_height // 2 + death_text_size[1] / 2,
            ),
        )

    def display_boss_message(self, screen):
        """
        Displays a warning about the incoming boss fight.
        Args:
            screen: the pygame display that the game is on
        """
        message = FONT.render("A menacing figure is approaching...", False, RED)
        message_size = pygame.font.Font.size(
            FONT, "A menacing figure is approaching..."
        )
        screen.blit(
            message,
            (
                self._screen_width // 2,
                self._screen_height // 2 + message_size[1] / 2,
            ),
        )
