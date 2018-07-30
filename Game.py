#!/usr/bin/python3
# 
# Brad Wilcox
# 
# Getting familiar with python and pygame
# by making a 'snake' like game
#
# Tools used: Linux, Nano, Terminal
#

import pygame
from Snake import Snake
from Food import Food

pygame.init()

display_width = 800
display_height = 600
tileSize = 20
tileCountX = display_width / tileSize
tileCountY = display_height / tileSize

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("PySnake")

clock = pygame.time.Clock()
fps = 30
tickInterval = .5
tickTime = 0
deltaTime = clock.tick(fps)

snake = Snake(tileCountX / 2 , tileCountY / 2, tileSize, tileCountX, tileCountY)
food = Food(tileSize, tileCountX, tileCountY)

def update():
	global tickInterval
	snake.update()
 
	if snake.body[0][0] == food.posX and snake.body[0][1] == food.posY:
		food.place()
		snake.eat()
		tickInterval -= .05
		if tickInterval < .05:
			tickInterval = .05
	checkGameOver()

def checkGameOver():
	global snake, tickInterval
	for i in range(1, len(snake.body)):
		print(i)
		if snake.body[0][0] == snake.body[i][0] and snake.body[0][1] == snake.body[i][1]:
			snake = Snake(tileCountX / 2, tileCountY / 2, tileSize, tileCountX, tileCountY)
			tickInterval = .5
			break

def draw():
	snake.draw(gameDisplay)
	food.draw(gameDisplay)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				snake.dir_x = -1
				snake.dir_y = 0
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				snake.dir_x = 1
				snake.dir_y = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				snake.dir_y = -1
				snake.dir_x = 0
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				snake.dir_y = 1
				snake.dir_x = 0
	
	gameDisplay.fill((0,0,0))
	
	tickTime += deltaTime	

	while tickTime > tickInterval:
		tickTime -= tickInterval
		update()		

	draw()
	
	pygame.display.update()
	deltaTime = clock.tick(fps)/1000.0
