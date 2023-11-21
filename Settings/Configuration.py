import pygame

cellSize = 64
cellNumberX = 20
cellNumberY = 11.25

screenWidth = cellSize * cellNumberX
screenHeight = int(cellSize * cellNumberY)

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)