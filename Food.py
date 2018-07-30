#!/usr/bin/Python3
import pygame
import random

class Food:
	
	red = (255, 0, 0)
	
	def __init__(self, tileSize, worldWidth, worldHeight):
		self.size = tileSize
		self.worldWidth = worldWidth
		self.worldHeight = worldHeight
		self.place()

	def draw(self, gameScreen):
		pygame.draw.rect(gameScreen, self.red, pygame.Rect(self.posX*self.size, self.posY*self.size, self.size, self.size))
	
	def place(self):
		self.posX = random.randint(0, self.worldWidth-1)
		self.posY = random.randint(0, self.worldHeight-1)
			
