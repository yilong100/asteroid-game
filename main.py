import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    infinite_loop_running = 1
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while infinite_loop_running != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
       


if __name__ == "__main__":
    main()
