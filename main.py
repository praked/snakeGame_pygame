import pygame
import time
import random
from mod1 import *
from mod2 import *

pygame.init()

## GLOBAL INITIALISATION
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

block_size=20
pixel_x=800
pixel_y=700
FPS =10
## SCREEN CREATION
gameDisplay = pygame.display.set_mode((pixel_x,pixel_y))

## IMAGE LOADING
img = pygame.image.load('1.png')

apple_x = round(random.randrange(20,(pixel_x -block_size-20)))
apple_y = round(random.randrange(70,(pixel_y -block_size-20)))

bolder_n= 5

direction= "up"

apple_t=20
bolder=[]
bolder_t=20

## CREATION AND UPDATION OF THE COORDINATES OF SNAKE LIST
def snake_make(lead_x,lead_y,gameOver,snakeList,snakeLength):
	snakeHead =[]
	snakeHead.append(lead_x)
	snakeHead.append(lead_y)
	snakeList.append(snakeHead)
	if len(snakeList) >snakeLength:
		del snakeList[0]
	if len(snakeList) <=1:
		return False 
	elif snakeHead in snakeList[:-1]:
		return True
## INTRODUCTION SCREEN OF THE GAME
def game_intr():
	game = game_intro()
	intro = True 
	while intro:
			gameDisplay.fill(white)
			game.message_to_screen("Welcome to Snake",green,-60,"large")
			game.message_to_screen("Press 1 for Level 1 or 2 for Level 2 or 3 for Level 3 .",black,-10)
			game.message_to_screen("Press q (twice)to Quit",green,10,)
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						intro=False
						
					elif event.key == pygame.K_1:
						intro=False
						game_level1()		
					elif event.key == pygame.K_2:
						intro=False
						game_level2()				
					elif event.key == pygame.K_3:
						intro=False
						game_level3()
					
## GAME LEVEL 1	
def game_level1():
	global direction
	global apple_x
	global apple_y		
	gameExit = False
	gameOver =False
	lead_x=pixel_x/2
	lead_y=pixel_y/2
	lead_x_change=0
	lead_y_change=-block_size

	snakeList = []
	snakeLength = 3
	score=0
	
	level=level1()	
	apple_x,apple_y=level.random_apple()
	direction="up"
	
	game =game_intro()
	
	gameOver = game.intro_l1()
	while not gameExit:
		## OUTER LOOP FOR GAME  
		
		while gameOver == True :
			## INNER LOOP FOR GAME OVER
			gameDisplay.fill(white)
			game.message_to_screen("Game over",red,y_displace=-50,size="large")
			game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="medium")
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver =False
					gameExit = True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver =False
						gameExit = True
					elif event.key == pygame.K_c:
						gameOver =False
						gameExit = True
						game_intr()	
			
		## READING OF THE USER INPUT THROUGH KEYBOARD

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True		
				elif event.key == pygame.K_LEFT and direction!="right": 	
					direction ="left"
					lead_x_change =-block_size
					lead_y_change =0
				elif event.key == pygame.K_RIGHT and direction!= "left":	
					direction ="right"
					lead_x_change =block_size
					lead_y_change =0
				elif event.key == pygame.K_UP and direction!="down":	
					direction ="up"
					lead_y_change =-block_size
					lead_x_change =0
				elif event.key == pygame.K_DOWN and direction!="up":	
					direction ="down"
					lead_y_change =block_size
					lead_x_change =0	
	
		
		lead_x += lead_x_change
	        lead_y += lead_y_change
		lead_x,lead_y,gameOver = level.snake_bound_check(lead_x,lead_y,gameOver)
		gameDisplay.fill(white)## ERASING ALL PREVIOUS OBJECTS ON SCREEN
		
		game.display_score("Score : " +str(score))## DISPLAYING SCORE

		pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,apple_t,apple_t])

		if(gameOver!=True):		
			gameOver = snake_make(lead_x,lead_y,gameOver,snakeList,snakeLength)		


		level.snake(snakeList,direction)
		
		pygame.draw.line(gameDisplay,black,(0,50),(pixel_x,50),3)       		
		game.message_to_screen(" Press Q to QUIT level ",black,y_displace = -320,size="small")		
		pygame.display.update()
				
		if (level.collision(lead_x,lead_y,x =apple_x,y=apple_y)):
				apple_x,apple_y=level.random_apple()
				snakeLength += 1
				score +=1
		
		clock.tick(FPS)
## GAME LEVEL 2
def game_level2():
	global direction
	global apple_x
	global apple_y		
	gameExit = False
	gameOver =False
	lead_x=pixel_x/2
	lead_y=pixel_y/2
	lead_x_change=0
	lead_y_change=-block_size

	snakeList = []
	snakeLength = 3
	score=0
	
	level=level2()	
	apple_x,apple_y=level.random_apple()
	direction="up"
	
	game= game_intro()	
	gameOver = game.intro_l2()
	while not gameExit:
		
		
		while gameOver == True :
			gameDisplay.fill(white)
			game.message_to_screen("Game over",red,y_displace=-50,size="large")
			game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="medium")
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver =False
					gameExit = True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver =False
						gameExit = True
					elif event.key == pygame.K_c:
						gameOver =False
						gameExit = True
						game_intr()	
			
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True
										
				elif event.key == pygame.K_LEFT and direction!="right": 	
					direction ="left"
					lead_x_change =-block_size
					lead_y_change =0
				elif event.key == pygame.K_RIGHT and direction!= "left":	
					direction ="right"
					lead_x_change =block_size
					lead_y_change =0
				elif event.key == pygame.K_UP and direction!="down":	
					direction ="up"
					lead_y_change =-block_size
					lead_x_change =0
				elif event.key == pygame.K_DOWN and direction!="up":	
					direction ="down"
					lead_y_change =block_size
					lead_x_change =0	
		
  		lead_x += lead_x_change
	        lead_y += lead_y_change
		lead_x,lead_y,gameOver = level.snake_bound_check(lead_x,lead_y,gameOver)
		gameDisplay.fill(white)
		
		game.display_score("Score : " +str(score))
		
		pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,apple_t,apple_t])
		
		if(gameOver!=True):		
			gameOver = snake_make(lead_x,lead_y,gameOver,snakeList,snakeLength)		

		
		level.snake(snakeList,direction)
		
		level.level_block()              
		
		pygame.draw.line(gameDisplay,black,(0,50),(pixel_x,50),3)       		
		game.message_to_screen(" Press Q to QUIT level ",black,y_displace = -320,size="small")		
		pygame.display.update()
		if (level.collision(lead_x,lead_y,x=apple_x,y=apple_y)):
				apple_x,apple_y=level.random_apple()
				snakeLength += 1
				score +=1
		
		clock.tick(FPS)
## GAME LEVEL 3
def game_level3():
	global direction
	global bolder
	global bolder_n	
	global apple_x
	global apple_y		
	gameExit = False
	gameOver =False
	lead_x=pixel_x/2
	lead_y=pixel_y/2
	lead_x_change=0
	lead_y_change=-block_size

	snakeList = []
	snakeLength = 3
	score=0
	level = level3()
	        
	bolder=level.random_bolder(bolder_n)	
	apple_x,apple_y=level.random_apple()
	direction="up"
	
	
	game = game_intro()
	gameOver = game.intro_l3()
	while not gameExit:
		
		
		while gameOver == True :
			gameDisplay.fill(white)
			game.message_to_screen("Game over",red,y_displace=-50,size="large")
			game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="medium")
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver =False
					gameExit = True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver =False
						gameExit = True
					elif event.key == pygame.K_c:
						gameOver =False
						gameExit = True
						game_intr()	
			
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True
						
				elif event.key == pygame.K_LEFT and direction!="right": 	
					direction ="left"
					lead_x_change =-block_size
					lead_y_change =0
				elif event.key == pygame.K_RIGHT and direction!= "left":	
					direction ="right"
					lead_x_change =block_size
					lead_y_change =0
				elif event.key == pygame.K_UP and direction!="down":	
					direction ="up"
					lead_y_change =-block_size
					lead_x_change =0
				elif event.key == pygame.K_DOWN and direction!="up":	
					direction ="down"
					lead_y_change =block_size
					lead_x_change =0	
	
  		lead_x += lead_x_change
	        lead_y += lead_y_change
		lead_x,lead_y,gameOver = level.snake_bound_check(lead_x,lead_y,gameOver)
		gameDisplay.fill(white)
		
		game.display_score("Score : " +str(score))
		
		pygame.draw.rect(gameDisplay,red,[apple_x,apple_y,apple_t,apple_t])
		
		if(gameOver!=True):		
			gameOver = snake_make(lead_x,lead_y,gameOver,snakeList,snakeLength)		

		
		
		level.snake(snakeList,direction)
		
		level.level_block()               
		for i in range(bolder_n):
			pygame.draw.rect(gameDisplay,black,[bolder[i][0],bolder[i][1],bolder_t,bolder_t])
		
		pygame.draw.line(gameDisplay,black,(0,50),(pixel_x,50),3)       		
		game.message_to_screen(" Press Q to QUIT level ",black,y_displace = -320,size="small")		
		pygame.display.update()
		if (level.collision(lead_x,lead_y,xi=apple_x,yi=apple_y)):
						
				apple_x,apple_y=level.random_apple()
				snakeLength += 1
				score +=1
				
		if(gameOver!=True):		
			gameOver = level.collision(lead_x,lead_y,typ="boulder",bold=bolder)
		clock.tick(FPS)
		

game_intr()
pygame.quit()
quit()
