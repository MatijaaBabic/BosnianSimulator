import pygame
import random
from pygame import mixer
from AM import MAIN_FOLDER

class Board(pygame.sprite.Sprite):                  #board class
    def __init__(self, width, height, type):
       super().__init__()
       self.W = width
       self.H = height
       self.type = type


class Mine(pygame.sprite.Sprite):                #class for the mine
    def __init__(self, x, y, type):
       super().__init__()