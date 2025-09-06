import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        #HEART OF MAIN LOOP
        screen.fill((0,0,0))
        player.update(dt)
        
        clkReturn = gameClock.tick(60)
        dt = clkReturn / 1000
        player.draw(screen)
        pygame.display.flip()  
        

if __name__ == "__main__":
    main()
