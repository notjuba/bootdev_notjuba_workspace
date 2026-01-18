import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import player
from circlehsape import CircleShape
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000
        player.draw(screen)
        pygame.display.flip()

    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


