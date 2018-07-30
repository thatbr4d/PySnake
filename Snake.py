#!/usr/bin/Python
import pygame

class Snake:
	
	white = (255,255,255)

	def __init__(self, x, y, tileSize, worldWidth, worldHeight):
		self.size = tileSize
		self.worldWidth = worldWidth
		self.worldHeight = worldHeight
		self.dir_x = 0
		self.dir_y = -1
		self.body = [[0,0],[0,0],[0,0]]
		for i in range(len(self.body)):
			self.body[i][0] = x
			self.body[i][1] = y + i


	def draw(self, gameScreen):
		for i in range(len(self.body)):
			pygame.draw.rect(gameScreen, self.white, pygame.Rect(self.body[i][0]*self.size, self.body[i][1]*self.size, self.size, self.size)) 
		
	def update(self):
		i = len(self.body)-1
		while i >= 1:
			self.body[i][0] = self.body[i-1][0];
			self.body[i][1] = self.body[i-1][1];
			i -= 1

		self.body[0][0] += self.dir_x
		self.body[0][1] += self.dir_y

		self.checkBounds()
		
	
	def checkBounds(self):
		if self.body[0][0] >= self.worldWidth:
			self.body[0][0] = 0
		elif self.body[0][0] < 0:
			self.body[0][0] = self.worldWidth
		elif self.body[0][1] >= self.worldHeight:
			self.body[0][1] = 0
		elif self.body[0][1] < 0:
			self.body[0][1] = self.worldHeight	
	
	def eat(self):
		self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])


