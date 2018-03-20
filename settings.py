import pygame as pg
import math
width = 400
height = 400
fps = 10
w = 20
r = 5

cols = math.floor(width/w);
rows = math.floor(height/w);

grid = []
stack = []
screen = pg.display.set_mode((width,height))

TITLE = "GAME"

WHITE = (228, 241, 254)
BLACK = (51,51,51)
RED = (246, 36, 89)
GREEN = (0,230,64)
BLUE = (89, 171, 227)
YELLOW = (247, 202, 24)

white = (255, 255, 255)
P_BLACK = (0,0,0)
P_RED = (255, 0, 0)
P_GREEN = (0,255,0,1)
P_BLUE = (0, 0, 255)
P_YELLOW = (255, 255, 0)
