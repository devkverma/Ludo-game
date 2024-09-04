import pygame
import sys
import numpy as np
from constants import *

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LUDO')
screen.fill(BGCOLOR)

class Board:
    def __init__(self):
        screen.fill(BGCOLOR)
        self.squares = np.zeros((ROWS,COLS))
        self.board()
        
    def board(self):
        screen.fill(BGCOLOR)

        #Lanes
        self.victoryLane((1,6),RED,1)
        self.victoryLane((8,1),GREEN,2)
        self.victoryLane((6,13),BLUE,3)
        self.victoryLane((13,8),YELLOW,4)

        self.grid()

        # SPOTS
        self.playerSpot(RED,(0,0),1)
        self.playerSpot(GREEN,(9,0),2)
        self.playerSpot(BLUE,(0,9),3)
        self.playerSpot(YELLOW,(9,9),4)

        

    def grid(self):
        for row in range(1,ROWS):
            self.drawLines((0,row*SQSIZE),(ROWS*SQSIZE,row*SQSIZE),LINECOLOR)
        
        for col in range(1,COLS):
            self.drawLines((col*SQSIZE,0),(col*SQSIZE,COLS*SQSIZE),LINECOLOR)

    def drawLines(self,start,end,color):
        pygame.draw.line(screen,color,start,end)

    def drawCircle(self,radius,center,color):
        pygame.draw.circle(screen,color,center,radius)
    
    def playerSpot(self,color,pos,player):
        x,y = pos
        outer_rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SPOTSIZE,SPOTSIZE)
        pygame.draw.rect(screen,color,outer_rect)

        inner_rect = pygame.Rect((x+1)*SQSIZE,(y+1)*SQSIZE,SQSIZE*4,SQSIZE*4)
        pygame.draw.rect(screen,WHITE,inner_rect)

        self.drawCircle(RADIUS,((x+2)*SQSIZE,(y+2)*SQSIZE),color)
        self.drawCircle(RADIUS,((x+2)*SQSIZE,(y+4)*SQSIZE),color)
        self.drawCircle(RADIUS,((x+4)*SQSIZE,(y+2)*SQSIZE),color)
        self.drawCircle(RADIUS,((x+4)*SQSIZE,(y+4)*SQSIZE),color)

        for i in range(6):
            for j in range(6):
                self.squares[y+j][x+i] = player

    def victoryLane(self,pos,color,player):
        x,y = pos
        rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SQSIZE,SQSIZE)
        pygame.draw.rect(screen,color,rect)
        self.squares[y][x] = player*10
        
        if abs(7-x) == 1:
            if x > 7:
                x -= 1
                while y < 6:
                    rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SQSIZE,SQSIZE)
                    pygame.draw.rect(screen,color,rect)
                    self.squares[y][x] = player*10 + 1
                    y += 1
            else:
                x += 1
                while y > 8:
                    rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SQSIZE,SQSIZE)
                    pygame.draw.rect(screen,color,rect)
                    self.squares[y][x] = player*10 + 1
                    y -= 1
        else:
            if y > 7:
                y -= 1
                while x > 8:
                    rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SQSIZE,SQSIZE)
                    pygame.draw.rect(screen,color,rect)
                    self.squares[y][x] = player*10 + 1
                    x -= 1
            else:
                y += 1
                while x < 6:
                    rect = pygame.Rect(x*SQSIZE,y*SQSIZE,SQSIZE,SQSIZE)
                    pygame.draw.rect(screen,color,rect)
                    self.squares[y][x] = player*10 + 1
                    x += 1


def main():
    
    board = Board()
    print(board.squares)
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


main()
