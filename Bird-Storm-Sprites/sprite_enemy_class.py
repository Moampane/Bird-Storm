"""
File for enemy classes.
"""
import pygame, sprite_bird_class, random

ENEMY_WIDTH = 100
ENEMY_HEIGHT = 100
ENEMY_MOVESPEED = 2
ENEMY_ATK = 2
ENEMY_BASE_MAX_HP = 20


class Enemy(sprite_bird_class.BirdCharacter):
    def __init__(self, image_path, bg, player):
        super().__init__(image_path, bg)
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.max_hp = ENEMY_BASE_MAX_HP
        self.atk = ENEMY_ATK
        self.ms = ENEMY_MOVESPEED
        self.remaining_hp = self.max_hp
        spawn_loc = (
            random.choice([0 - self.width, bg.get_width() + self.width]),
            random.randint(0, bg.get_height() - self.height),
        )
        self.rect = self.image.get_rect(center=spawn_loc)
        self.player = player
        self.is_facing_right = True

    def update(self):
        super().update()

        # Initialize location data
        player_x = self.player.rect.x
        player_y = self.player.rect.y
        enemy_x = self.rect.x
        enemy_y = self.rect.y
        dist_between = 50

        # If enemy is too far left or right of player, move enemy towards
        # left or right depending on which side player is on and flip enemy
        # sprite towards the direction player is in
        if player_x > enemy_x + dist_between:
            if not self.is_facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
                self.is_facing_right = True
            self.rect.x += self.ms
        elif player_x < enemy_x - dist_between:
            if self.is_facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
                self.is_facing_right = False
            self.rect.x -= self.ms

        # If enemy is too far above or below player, move enemy
        # up or down depending on which side player is on
        if player_y > enemy_y + dist_between:
            self.rect.y += self.ms
        elif player_y < enemy_y - dist_between:
            self.rect.y -= self.ms

    def take_damage(self, opponent_atk, environment):
        self.remaining_hp -= opponent_atk
        if self.remaining_hp <= 0:
            self.kill()
            environment.num_enemies_slain += 1


class Projectile_Boss(sprite_bird_class.BirdCharacter):
    def __init__(
        self, max_health, attack, movespeed, image_path, start_pos, size, bg, player
    ):
        super().__init__(image_path, bg)
        self.width = size[0]
        self.height = size[1]
        self.max_hp = max_health
        self.atk = attack
        self.ms = movespeed
        self.remaining_hp = self.max_hp
        self.player = player
        self.incomplete_intro = True
        self.position = "center"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=start_pos)
        self.complete_move = False
        self.move = random.choice(
            [
                self.go_to_center,
                self.go_to_bottom_left,
                self.go_to_bottom_right,
                self.go_to_top_left,
                self.go_to_top_right,
            ]
        )

    def take_damage(self, opponent_atk, environment):
        self.remaining_hp -= opponent_atk
        if self.remaining_hp <= 0:
            self.kill()
            environment.num_enemies_slain += 100

    def update(self, timer):
        super().update()

        print(timer)
        if (
            self.rect.y < self.screen.get_height() / 2 - 100
            and self.incomplete_intro
            and timer % 10 == 0
        ):
            # change back to 1 later
            # Moves boss
            self.rect.y += 40
            # Forces player in place
            self.player.rect.y = self.screen.get_height() - 100
            self.player.rect.x = self.screen.get_width() / 2 - 50
            # Ends intro
            if self.rect.y >= self.screen.get_height() / 2 - 100:
                self.incomplete_intro = False

        # if not self.incomplete_intro and self.timer % 100 == 0:
        # self.go_to_top_left()
        # self.go_to_top_right()
        # self.go_to_bottom_left()
        # self.go_to_bottom_right()

        if not self.incomplete_intro:
            if timer % 250 == 0:
                self.move = random.choice(
                    [
                        self.go_to_center,
                        self.go_to_bottom_left,
                        self.go_to_bottom_right,
                        self.go_to_top_left,
                        self.go_to_top_right,
                    ]
                )
            self.move()

    def go_to_top_left(self):

        if self.position == "center":
            if self.rect.x > 0:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y > 0:
                self.rect.y -= self.screen.get_height() / 200
            if self.rect.x <= 0 and self.rect.y <= 0:
                self.position = "top left"
                self.complete_move = True

        if self.position == "top right":
            if self.rect.x > 0:
                self.rect.x -= 7.35
            if self.rect.x <= 0:
                self.position = "top left"
                self.complete_move = True

        if self.position == "bot left":
            if self.rect.y > 0:
                self.rect.y -= 7.35
            if self.rect.y <= 0:
                self.position = "top left"
                self.complete_move = True

        if self.position == "bot right":
            if self.rect.x > 0:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y > 0:
                self.rect.y -= self.screen.get_height() / 200
            if self.rect.x <= 0 and self.rect.y <= 0:
                self.position = "top left"
                self.complete_move = True

    def go_to_top_right(self):

        if self.position == "center":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y > 0:
                self.rect.y -= self.screen.get_height() / 200
            if self.rect.x >= self.screen.get_width() - 200 and self.rect.y <= 0:
                self.position = "top right"
                self.complete_move = True

        if self.position == "top left":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += 7.35
            if self.rect.x >= self.screen.get_width() - 200:
                self.position = "top right"
                self.complete_move = True

        if self.position == "bot left":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y > 0:
                self.rect.y -= self.screen.get_height() / 200
            if self.rect.x >= self.screen.get_width() - 200 and self.rect.y <= 0:
                self.position = "top right"
                self.complete_move = True

        if self.position == "bot right":
            if self.rect.y > 0:
                self.rect.y -= 7.35
            if self.rect.y <= 0:
                self.position = "top right"
                self.complete_move = True

    def go_to_bottom_left(self):

        if self.position == "center":
            if self.rect.x > 0:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += self.screen.get_height() / 200
            if self.rect.x <= 0 and self.rect.y >= self.screen.get_height() - 200:
                self.position = "bot left"
                self.complete_move = True

        if self.position == "top left":
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += 7.35
            if self.rect.y > self.screen.get_height() - 200:
                self.position = "bot left"
                self.complete_move = True

        if self.position == "top right":
            if self.rect.x > 0:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += self.screen.get_height() / 200
            if self.rect.x <= 0 and self.rect.y >= self.screen.get_height() - 200:
                self.position = "bot left"
                self.complete_move = True

        if self.position == "bot right":
            if self.rect.x > 0:
                self.rect.x -= 7.35
            if self.rect.x <= 0:
                self.position = "bot left"
                self.complete_move = True

    def go_to_bottom_right(self):

        if self.position == "center":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += self.screen.get_height() / 200
            if (
                self.rect.x >= self.screen.get_width() - 200
                and self.rect.y >= self.screen.get_height() - 200
            ):
                self.position = "bot right"
                self.complete_move = True

        if self.position == "top left":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += self.screen.get_height() / 200
            if (
                self.rect.x >= self.screen.get_width() - 200
                and self.rect.y >= self.screen.get_height() - 200
            ):
                self.position = "bot right"
                self.complete_move = True

        if self.position == "top right":
            if self.rect.y < self.screen.get_height() - 200:
                self.rect.y += 7.35
            if self.rect.y >= self.screen.get_height() - 200:
                self.position = "bot right"
                self.complete_move = True

        if self.position == "bot left":
            if self.rect.x < self.screen.get_width() - 200:
                self.rect.x += 7.35
            if self.rect.x >= self.screen.get_width() - 200:
                self.position = "bot right"
                self.complete_move = True

    def go_to_center(self):

        if self.position == "top left":
            if self.rect.x < self.screen.get_width() / 2 - 100:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() / 2 - 100:
                self.rect.y += self.screen.get_height() / 200
            if (
                self.rect.x >= self.screen.get_width() / 2 - 100
                and self.rect.y >= self.screen.get_height() / 2 - 100
            ):
                self.position = "center"
                self.complete_move = True

        if self.position == "top right":
            if self.rect.x > self.screen.get_width() / 2 - 100:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y < self.screen.get_height() / 2 - 100:
                self.rect.y += self.screen.get_height() / 200
            if (
                self.rect.x <= self.screen.get_width() / 2 - 100
                and self.rect.y >= self.screen.get_height() / 2 - 100
            ):
                self.position = "center"
                self.complete_move = True

        if self.position == "bot left":
            if self.rect.x < self.screen.get_width() / 2 - 100:
                self.rect.x += self.screen.get_width() / 200
            if self.rect.y > self.screen.get_height() / 2 - 100:
                self.rect.y -= self.screen.get_height() / 200
            if (
                self.rect.x >= self.screen.get_width() / 2 - 100
                and self.rect.y <= self.screen.get_height() / 2 - 100
            ):
                self.position = "center"
                self.complete_move = True

        if self.position == "bot right":
            if self.rect.x > self.screen.get_width() / 2 - 100:
                self.rect.x -= self.screen.get_width() / 200
            if self.rect.y > self.screen.get_height() / 2 - 100:
                self.rect.y -= self.screen.get_height() / 200
            if (
                self.rect.x <= self.screen.get_width() / 2 - 100
                and self.rect.y <= self.screen.get_height() / 2 - 100
            ):
                self.position = "center"
                self.complete_move = True
