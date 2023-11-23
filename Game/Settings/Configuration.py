import pygame

cellSize = 80
cellNumberX = 16
cellNumberY = 9

screenWidth = cellSize * cellNumberX
screenHeight = cellSize * cellNumberY

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)