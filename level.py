#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Level Module
"""

import pygame


class Level:  # pylint: disable=R0903
    """Contains sprites for the level"""

    def __init__(self):
        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        """Updates and draws the game"""
        pass  # pylint: disable=W0107
