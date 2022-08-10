# Import modules
import pygame
import os
import numpy as np
import sys


class MyGame:

    def __init__(self) -> None:

        # Initialize pygame
        pygame.init()

        # Make the screen and set caption
        self.WIDTH = 700
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Space Invaders!')

        # Set icon
        icon_name = "icon.png"
        self.path = os.path.split(os.path.abspath(__file__))[0]
        icon_path = os.path.join(self.path, "photos\{}".format(icon_name))
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)

        # Create spaceship
        spaceship_file = "spaceship.png"
        spaceship_path = os.path.join(
            self.path, "photos\{}".format(spaceship_file))
        self.spaceship = pygame.image.load(spaceship_path)
        self.shipX = (self.WIDTH / 2) - (self.spaceship.get_width() / 2)
        self.shipY = (self.HEIGHT / 1.25)
        self.speedX = 0

        # Initialize the background
        bg_name = "background.jpg"
        bg_file = os.path.join(self.path, "photos\{}".format(bg_name))
        self.background = pygame.image.load(bg_file).convert()

        # Initialize the bullet
        bullet_file_name = "bullet.png"
        bullet_file = os.path.join(
            self.path, "photos\{}".format(bullet_file_name))
        self.bullet = pygame.image.load(bullet_file)
        self.bulletX = self.shipX + self.spaceship.get_width() / 4
        self.bulletY = self.shipY - 10

        # Create alien
        alien_file = "alien.png"
        alien_path = os.path.join(self.path, "photos\{}".format(alien_file))
        self.alien = pygame.image.load(alien_path)
        self.alienX = np.random.randint(1, self.WIDTH - 32, 1)[0]
        self.alienY = np.random.randint(35, 150, 1)[0]

        # Make the alien move to the right initially
        self.dir = +1

        # Initialize the bullet state to "ready".
        # When state is "ready" the bullet is not blitted on the screen.
        # When state is "fire", the bullet is blitted.
        self.bullet_state = "ready"

    def check_keypress(self):

        for event in pygame.event.get():

            # For quitting the game
            if event.type == pygame.QUIT:
                sys.exit()

            # Check for arrow key press or spacebar
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.speedX = -0.5
                elif event.key == pygame.K_RIGHT:
                    self.speedX = 0.5

                if event.key == pygame.K_SPACE:
                    self.create_bullet()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.speedX = 0.0

        self.shipX += self.speedX

    def check_boundary(self):

        if self.shipX >= self.WIDTH - self.spaceship.get_width():
            self.shipX = self.WIDTH - self.spaceship.get_width()
        elif self.shipX <= 0:
            self.shipX = 0

    def create_bullet(self):

        self.bullet_state = "fire"
        self.bulletX = self.shipX + self.spaceship.get_width() / 4
        self.bulletY = self.shipY - 10
        self.screen.blit(self.bullet, (self.bulletX, self.bulletY))

    def move_alien(self):

        self.alienX += self.dir * 0.1
        if self.alienX + self.alien.get_width() > self.WIDTH:
            self.dir = -1
            self.alienY = self.alienY + self.alien.get_height() - 20

        elif self.alienX <= 0:
            self.dir = +1
            self.alienY = self.alienY + self.alien.get_height() - 20

    def main(self):

        # Start
        running = True
        while running:

            # Fill the background
            self.screen.blit(self.background, (0, 0))

            # check for keyboard presses
            self.check_keypress()

            # Blit the spaceship to the screen.
            self.screen.blit(self.spaceship, (self.shipX, self.shipY))

            # Check boundaries of spaceship
            self.check_boundary()

            # Blit the alien spaceship.
            self.screen.blit(self.alien, (self.alienX, self.alienY))

            # Move the alien.
            self.move_alien()

            # Blit the bullet on the screen
            if self.bullet_state == "fire":
                self.bulletY -= 0.5
                if not self.bulletY <= 0:
                    self.screen.blit(self.bullet, (self.bulletX, self.bulletY))

            pygame.display.update()


if __name__ == "__main__":
    game = MyGame()
    game.main()
