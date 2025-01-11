import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50)

    updatable.add(player)
    drawable.add(player)

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)

    asteroid_field = AsteroidField()  # ????

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill((0, 0, 0))
        for item in updatable:
            if item == player:
                player.update(dt, shots, drawable, updatable)
            else:
                item.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                raise SystemExit

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    print("collision!")
                    asteroid.split(asteroids)
                    shot.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
