import pygame as pg
import math
from settings import *
from Cell import *
pg.init()

for j in range(rows):
    for i in range(cols):
        c = Cell(i,j)
        grid.append(c)

current = grid[0]

running = True

clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



    clock.tick(fps)
    screen.fill(BLACK)
    for i in grid:
        i.show()
    current.visited = True
    current.head()
    next = current.checkSides()
    if next:
        next.visited = True
        stack.append(current)
        removeWalls(current,next)
        current = next
    elif len(stack)>0:
        current = stack.pop()

    pg.display.update()

pg.quit()
quit()
