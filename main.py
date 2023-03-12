#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main script for my zelda project
"""

import sys
import pygame
from settings import WIDTH, HEIGTH, FPS, TILESIZE, WORLD_MAP  # pylint: disable=W0611


class Game:  # pylint: disable=R0903
    """Game class"""

    def __init__(self):
        # General setup
        pygame.init()  # pylint: disable=E1101
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
        """Game runner"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # pylint: disable=E1101
                    pygame.quit()  # pylint: disable=E1101
                    sys.exit()

            pygame.display.set_caption("Zeelda")
            self.screen.fill("black")
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
