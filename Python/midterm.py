import pygame, sys
from pygame.locals import *
from random import *
from sys import exit

pygame.init()

pygame.display.set_caption('Jackspers Rectangles')

screen = pygame.display.set_mode((800,800),0,32)

PURPLE=(160,32,240)

screen.fill(PURPLE)

class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        size = (10,10)
    def draw(self):
        pygame.draw.rect(screen, self.color, Rect(self.pos, (10,10)))

rectangles = []

for count in range(4096):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    #random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))
    size = (10,10)
    rectangles.append(Rectangle(random_pos, random_color, size))
        
                    

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #screen.lock()
    for rectangle in rectangles:
        rectangle.draw()
    #screen.unlock()
    pygame.display.update()

