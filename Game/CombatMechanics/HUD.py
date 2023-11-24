import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, screenHeight, screenWidth, cellNumberX
from Models.Characters.Wizard import Wizard

class HUD:
    def __init__(self, playerChars, gameFont):
        self.height = screenHeight/4
        self.y = screenHeight - self.height
        self.surface = pygame.Surface((screenWidth, self.height))
        self.playerChars = playerChars
        self.gameFont = gameFont
        self.textStats = "Character  |  Life  |  Mana"
        self.stats = []
        
        
    def update(self):
        pass
    
    def draw(self):
        self.surface.fill("Blue")
        screen.blit(self.surface, (0, self.y))
        self.drawTeamStats()
        self.drawActions()
        
    def drawActions(self):
        COLOR_INACTIVE = pygame.Color('lightskyblue3')
        COLOR_ACTIVE = pygame.Color('dodgerblue2')

        
        self.distance=25
        text = "Atacar"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        actionRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(actionRect.left-8, actionRect.top+4, actionRect.width + 14 ,actionRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, actionRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        
        self.distance+=55
        text = "Habilidade 1"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        actionRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(actionRect.left-8, actionRect.top+4, actionRect.width + 14 ,actionRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, actionRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        
        self.distance+=55
        text = "Habilidade 2"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        actionRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(actionRect.left-8, actionRect.top+4, actionRect.width + 14 ,actionRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, actionRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        pass
      
        
    def drawTeamStats(self):
        self.distance = 20
        textSurface = self.gameFont.render(self.textStats, False, (255, 255, 255))
        textPos = Vector2((screenWidth*1/6), self.y+self.distance)
        textRect = textSurface.get_rect(center = (textPos.x, textPos.y))
        screen.blit(textSurface, textRect)
        for char in self.playerChars:
            self.distance+=40
            text = char.className +"     |     "+ str(char.health) + "     |     " + str(char.mana)
            statsSurface = self.gameFont.render(text, False, (255, 255, 255))
            statPos = Vector2((screenWidth*1/6) , self.y+self.distance)
            statRect = statsSurface.get_rect(center = (statPos.x, statPos.y))
            screen.blit(statsSurface, statRect)
            
            
            