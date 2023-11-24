import pygame
from pygame.math import Vector2
from Settings.Configuration import screen, screenHeight, screenWidth, cellSize
from Models.Characters.Wizard import Wizard
from Models.Characters.Mob import Mob
from Models.States import States

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class HUD:
    def __init__(self, playerChars, enemyChars, gameFont):
        self.height = screenHeight/4
        self.y = screenHeight - self.height
        self.surface = pygame.Surface((screenWidth, self.height))
        self.playerChars = playerChars
        self.enemyChars = enemyChars
        self.gameFont = gameFont
        self.currentArrow = pygame.image.load("Game/Graphics/Current.png").convert_alpha()
        self.targetArrow = pygame.image.load("Game/Graphics/Target.png").convert_alpha()
        self.textStats = "Character  |  Life  |  Mana"
        self.alliesStatRect = []
        self.enemiesStatRect = []
        self.currentChar = None
        self.currentTarget = None
        
        
    def update(self, currentChar):
        self.currentChar = currentChar
        pass
    
    def draw(self):
        self.surface.fill("Blue")
        screen.blit(self.surface, (0, self.y))
        self.drawSelected()
        self.drawTeamStats()
        self.drawEnemyTeamStats()
        self.drawActions()
        
        
    def drawActions(self):
        self.distance=25
        text = "Atacar"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        self.attackRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(self.attackRect.left-8, self.attackRect.top+4, self.attackRect.width + 14 ,self.attackRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, self.attackRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        
        self.distance+=55
        text = "Habilidade 1"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        self.firstSkillRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(self.firstSkillRect.left-8, self.firstSkillRect.top+4, self.firstSkillRect.width + 14 ,self.firstSkillRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, self.firstSkillRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        
        self.distance+=55
        text = "Habilidade 2"
        actionSuface = self.gameFont.render(text, False, (255, 255, 255))
        actionPos = Vector2((screenWidth*3/6),  self.y+self.distance)
        self.secondSkillRect = actionSuface.get_rect(center = (actionPos.x, actionPos.y))
        bgRect = pygame.Rect(self.secondSkillRect.left-8, self.secondSkillRect.top+4, self.secondSkillRect.width + 14 ,self.secondSkillRect.height)
        pygame.draw.rect(screen, ("Blue"), bgRect)
        screen.blit(actionSuface, self.secondSkillRect)
        pygame.draw.rect(screen,(255, 255, 255), bgRect, 2)
        pass
     
    def drawSelected(self):
        currentChar = self.currentChar
        currentTarget = self.currentTarget
        distanceY= -1.5
        distanceX = 0
        if isinstance(currentChar, Mob):
            arrowRect = pygame.Rect((currentChar.pos.x+distanceX)*cellSize, (currentChar.pos.y+distanceY)*cellSize, cellSize, cellSize)
            screen.blit(self.currentArrow, arrowRect) 
            if currentChar.state == States.DEAD:
                colorImage = pygame.Surface(self.currentArrow.get_size()).convert_alpha()
                colorImage.fill((255,255,255, 0))
                self.currentArrow.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        if isinstance(currentTarget, Mob):   
            arrowRect = pygame.Rect((currentTarget.pos.x+distanceX)*cellSize, (currentTarget.pos.y+distanceY)*cellSize, cellSize, cellSize)
            screen.blit(self.targetArrow, arrowRect)
            if currentTarget.state == States.DEAD:
                colorImage = pygame.Surface(self.targetArrow.get_size()).convert_alpha()
                colorImage.fill((255,255,255, 0))
                self.targetArrow.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
      
    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.enemiesStatRect[0].collidepoint(event.pos):
                print("Difiniu 1 como target")
                self.currentTarget = self.enemyChars[0]
                return self.enemyChars[0]
            elif self.enemiesStatRect[1].collidepoint(event.pos):
                print("Difiniu 2 como target")
                self.currentTarget = self.enemyChars[1]
                return self.enemyChars[1]
            elif self.enemiesStatRect[2].collidepoint(event.pos):
                print("Difiniu 3 como target")
                self.currentTarget = self.enemyChars[2]
                return self.enemyChars[2]
            if isinstance(self.currentChar.target, Mob):
                if self.attackRect.collidepoint(event.pos):
                    return 0
                elif self.firstSkillRect.collidepoint(event.pos):
                    return 1
                elif self.secondSkillRect.collidepoint(event.pos):
                    return 2

    def drawTeamStats(self):
        self.distance = 20
        textSurface = self.gameFont.render(self.textStats, False, (255, 255, 255))
        textPos = Vector2((screenWidth*1/6), self.y+self.distance)
        textRect = textSurface.get_rect(center = (textPos.x, textPos.y))
        screen.blit(textSurface, textRect)
        for index, char in enumerate(self.playerChars):
            self.distance+=40
            text = char.className +"     |     "+ str(char.health) + "     |     " + str(char.mana)
            statsSurface = self.gameFont.render(text, False, (255, 255, 255))
            statPos = Vector2((screenWidth*1/6) , self.y+self.distance)
            self.alliesStatRect.append(statsSurface.get_rect(center = (statPos.x, statPos.y)))
            screen.blit(statsSurface, self.alliesStatRect[index])
            
    def drawEnemyTeamStats(self):
        self.distance = 20
        textSurface = self.gameFont.render("Enemies", False, (255, 255, 255))
        textPos = Vector2((screenWidth*5/6), self.y+self.distance)
        textRect = textSurface.get_rect(center = (textPos.x, textPos.y))
        screen.blit(textSurface, textRect)
        for index, char in enumerate(self.enemyChars):
            self.distance+=40
            text = char.className
            enemyStatSurface = self.gameFont.render(text, False, (255, 255, 255))
            enemyStatPos = Vector2((screenWidth*5/6) , self.y+self.distance)
            self.enemiesStatRect.append(enemyStatSurface.get_rect(center = (enemyStatPos.x, enemyStatPos.y)))
            screen.blit(enemyStatSurface, self.enemiesStatRect[index])
            
            