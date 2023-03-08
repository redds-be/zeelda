#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debug script
"""

import pygame

pygame.init()  # pylint: disable=E1101
font = pygame.font.Font(None, 30)


def debug(info, coo_y=10, coo_x=10):
    """Start in debug"""
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, "White")
    debug_rect = debug_surf.get_rect(topleft=(coo_x, coo_y))
    pygame.draw.rect(display_surface, "Black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)
