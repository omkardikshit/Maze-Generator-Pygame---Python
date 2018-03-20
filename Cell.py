from settings import *
import random
import pygame as pg

class Cell():
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.walls = [True,True,True,True]
        self.visited = False

    def head(self):
        x = self.i * w;
        y = self.j * w;
        pg.draw.rect(screen,P_RED,(x,y,w,w))

    def show(self):
        x = self.i * w;
        y = self.j * w;
        if self.walls[0]:
            pg.draw.line(screen,white,(x,y),(x+w,y),3) #top
        if self.walls[1]:
            pg.draw.line(screen,white,(x+w,y),(x+w,y+w),3) #right
        if self.walls[2]:
            pg.draw.line(screen,white,(x+w,y+w),(x,y+w),3) #bottom
        if self.walls[3]:
            pg.draw.line(screen,white,(x,y+w),(x,y),3) # left

        if self.visited:
            pg.draw.rect(screen,P_GREEN,(x,y,w,w))

    def index(self,i,j):
        if i < 0 or j < 0 or i > cols-1 or j > rows-1:
            return -1
        return i + j * cols

    def checkSides(self):
        Sides = []

        top = grid[self.index(self.i,self.j-1)]
        right = grid[self.index(self.i+1,self.j)]
        bottom = grid[self.index(self.i,self.j+1)]
        left = grid[self.index(self.i-1,self.j)]

        if top and top.visited == False:
            Sides.append(top)

        if right and right.visited == False:
            Sides.append(right)

        if bottom and bottom.visited == False:
            Sides.append(bottom)

        if left and left.visited == False:
            Sides.append(left)


        if len(Sides) > 0:
            r = math.floor(random.randrange(0,len(Sides)))
            return Sides[r]
        else:
            pass


def removeWalls(a,b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False

    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False
