import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Adding pygame groups
    # All the objects that can be updated:
    updatable = pygame.sprite.Group()
    # All the objects that can be drawn:
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        # player.update(dt)
        # Using the updatable group container now:
        for thing in updatable:
            thing.update(dt)
        
        # player.draw(screen)
        # Using the drawable group container:
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()