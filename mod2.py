import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

block_size=20
pixel_x=800
pixel_y=700
FPS =10

gameDisplay = pygame.display.set_mode((pixel_x,pixel_y))

img = pygame.image.load('1.png')


bolder_n= 5



apple_t=20
bolder_t=20

## PARENT CLASS OF THE DIFFERENT LEVEL CLASSES
class snake_game:
	
	
	def __init__(self):
		pass
	## DRAWING THE SNAKE ON THE SCREEN
	def snake(self,snakeList,direction):
	

		if direction == "right":
			head = pygame.transform.rotate(img,270)
		elif direction == "left":
			head = pygame.transform.rotate(img,90)	
		elif direction == "up":
			head = img
		elif direction == "down":
			head = pygame.transform.rotate(img,180)
	
		gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][-1]))
	
		for xny in snakeList[0:-1]:
			pygame.draw.rect(gameDisplay,green,[xny[0],xny[1],block_size,block_size])

	
	## DETECTION OF THE COLLISION OF SNAKE HEAD WITH ANY OBJECT
	def collision(self,lead_x,lead_y,x,y,t):
		if (lead_x>= x and lead_x < x + t)or(lead_x+block_size> x and lead_x+block_size < x+t):
			if (lead_y>= y and lead_y < y+ t)or(lead_y+block_size> y and lead_y+block_size < y+ t):
				return True
		else:
			return False	
	
## CLASS FOR LEVEL 1
class level1(snake_game):
	
	
	def __init__(self):
		snake_game.__init__(self)		
		pass
	## FUNCTION FOR THE RANDOM COORDINATE ALLOCATION TO THE APPLE
	def random_apple(self):        
		apple_x = round(random.randrange(0,(pixel_x -block_size)))
		apple_y = round(random.randrange(65,(pixel_y -block_size)))
		return apple_x,apple_y	
	## FUNCTION TO CHECK THE SNAKE FOR CROSSING THE BOUNDARY OF THE SCREEN
	def snake_bound_check(self,lead_x,lead_y,gameOver):
		if lead_x >(pixel_x-block_size):
			lead_x=0
		elif lead_x<0 :
			lead_x=pixel_x-block_size
		elif lead_y>(pixel_y - block_size):
			lead_y=50
		elif lead_y <50:
			lead_y=pixel_y-block_size
		return lead_x,lead_y,gameOver	
	## CUSTOM FUNCTION FROM SNAKE_GAME CLASS	
	def snake(self,snakeList,direction):
		snake_game.snake(self,snakeList,direction)
	def collision(self,lead_x,lead_y,x,y):
		return snake_game.collision(self,lead_x,lead_y,x,y,apple_t)

class level2(snake_game):
	
	
	def __init__(self):
		snake_game.__init__(self)		
		pass
	## RANDOM APPLE 
	def random_apple(self):        
		apple_x = round(random.randrange(20,(pixel_x -block_size-20)))
		apple_y = round(random.randrange(70,(pixel_y -block_size-20)))
		return apple_x,apple_y	
	
	def snake_bound_check(self,lead_x,lead_y,gameOver):
		if lead_x >(pixel_x-block_size-20):
			gameOver =True
		elif lead_x<10 :
			gameOver =True
		elif lead_y>(pixel_y - block_size-20):
			gameOver =True
		elif lead_y <70:
			gameOver =True
		return lead_x,lead_y,gameOver
	## CUSTOM FUNCTION
	def snake(self,snakeList,direction):
		snake_game.snake(self,snakeList,direction)
	## DRAWING THE MAZE OF THE LEVEL
	def level_block(self):
		pygame.draw.rect(gameDisplay,black,[0,55,10,pixel_y -55])
		pygame.draw.rect(gameDisplay,black,[0,55,pixel_x,10])
		pygame.draw.rect(gameDisplay,black,[0,pixel_y-10,pixel_x,10])
		pygame.draw.rect(gameDisplay,black,[pixel_x-10,55,10,pixel_y-55])
		pygame.display.update()

	## DETECTION OF THE COLLISION		
	def collision(self,lead_x,lead_y,x=0,y=0,typ="apple",bolder=[]):
		if(typ=="apple"):				
			return snake_game.collision(self,lead_x,lead_y,x,y,apple_t)
		elif typ=="bolder":
			for i in range(bolder_n):
				if(snake_game.collision(self,lead_x,lead_y,bolder[i][0],bolder[i][1],bolder_t)):
					return True
			return False

class level3(level2):
	def __init__(self):
		level2.__init__(self)		
		pass	
		
	## CUSTOM FUNCTIONS 
	def random_apple(self):   
		return level2.random_apple(self)

	def level_block(self):
		level2.level_block(self)	  
 				
	def snake(self,snakeList,direction):
		level2.snake(self,snakeList,direction)
	
	def snake_bound_check(self,lead_x,lead_y,gameOver):
		return level2.snake_bound_check(self,lead_x,lead_y,gameOver)
	## CREATION OF COORDINATE LIST OF THE BOLDERS
	def random_bolder(self,bolder_n):        		
		bolder	=[]
		for i in range(bolder_n):		
			a = round(random.randrange(0,(pixel_x -block_size-10)))
			b =  round(random.randrange(70,(pixel_y -block_size-10)))
			while([a,b] in bolder ):
				a = round(random.randrange(0,(pixel_x -block_size-10)))
				b =  round(random.randrange(70,(pixel_y -block_size-10)))
			bolder.append([a,b])
		return bolder
	## CUSTOM FUNCTION FOR DETECTION FOR THE COLLISION WITH BOLDER OR APPLE
	def collision(self,lead_x,lead_y,xi=0,yi=0,typ="apple",bold=[]):
		if(typ=="apple"):				
			return level2.collision(self,lead_x,lead_y,x=xi,y=yi)
		elif typ=="boulder":
			if(level2.collision(self,lead_x,lead_y,x=xi,y=yi,typ="bolder",bolder=bold)):
				return True
			return False
		
	
if __name__=="__main__":
	a = snake_game()
	gameDisplay.fill(white)
	b=[[400,300]]	
	a.snake(b)
	pygame.display.update()	
