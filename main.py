import pygame
import sys
from constants import *

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
screen.fill(BGCOLOR)

class Board:
    def __init__(self):
        screen.fill(BGCOLOR)
        self.board()
        
    def board(self):
        screen.fill(BGCOLOR)
        for row in range(1,ROWS):
            self.drawLines((0,row*SQSIZE),(ROWS*SQSIZE,row*SQSIZE),LINECOLOR)
        
        for col in range(1,COLS):
            self.drawLines((col*SQSIZE,0),(col*SQSIZE,COLS*SQSIZE),LINECOLOR)

        # RED SPOT
        self.playerSpot(RED,(0,0))
        self.playerSpot(GREEN,(9*SQSIZE,0))
        self.playerSpot(BLUE,(0,9*SQSIZE))
        self.playerSpot(YELLOW,(9*SQSIZE,9*SQSIZE))

    def drawLines(self,start,end,color):
        pygame.draw.line(screen,color,start,end)

    def drawCircle(self,radius,center,color):
        pygame.draw.circle(screen,color,center,radius)
    
    def playerSpot(self,color,pos):
        x,y = pos
        outer_rect = pygame.Rect(x,y,SPOTSIZE,SPOTSIZE)
        pygame.draw.rect(screen,color,outer_rect)

        inner_rect = pygame.Rect(x+SQSIZE,y+SQSIZE,SQSIZE*4,SQSIZE*4)
        pygame.draw.rect(screen,WHITE,inner_rect)

        self.drawCircle(RADIUS,(x+2*SQSIZE,y+2*SQSIZE),color)
        self.drawCircle(RADIUS,(x+2*SQSIZE,y+4*SQSIZE),color)
        self.drawCircle(RADIUS,(x+4*SQSIZE,y+2*SQSIZE),color)
        self.drawCircle(RADIUS,(x+4*SQSIZE,y+4*SQSIZE),color)

def main():
    
    board = Board()
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()