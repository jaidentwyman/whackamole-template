from colorsys import yiq_to_rgb

import pygame
import random

from pygame import MOUSEBUTTONDOWN


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.image.load("../../../Downloads/whackamole-template/mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_position_y = 0
        mole_position_x = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(0, 512 + 32, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))

            for i in range(0, 640 + 32, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position_x, mole_position_y)))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (mole_position_y <= y <= mole_position_y + 32) and (mole_position_x <= x <= mole_position_x + 32):
                    mole_position_x = (random.randrange(0, 640) // 32) * 32
                    mole_position_y = (random.randrange(0, 512) // 32) * 32
                    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position_x, mole_position_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

    if __name__ == "__main__":
        main()
