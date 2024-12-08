# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return

            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
