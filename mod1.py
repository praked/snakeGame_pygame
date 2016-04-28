import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

pixel_x=800
pixel_y=700

gameDisplay = pygame.display.set_mode((pixel_x,pixel_y))
## CLASS FOR THE TEXT SENT TO THE SCREEN
class message:
	## VARIOUS FONTS STYLES
	small_font =  pygame.font.SysFont(None,25)
	med_font =  pygame.font.SysFont(None,50)
	large_font =  pygame.font.SysFont(None,80)
	
	def __init__(self):
		pass
	## MAKING TEXT MSG ENTERED TO AN OBJECT
	def text_objects(self,text,color,size="small"):
		if size =="small":
			textSurface = message.small_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="medium":
			textSurface = message.med_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="large":
			textSurface = message.large_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
	## DISPLAYING SCORE	
	def display_score(self,msg):
		screen_text = message.med_font.render(msg,True,black)	
		gameDisplay.blit(screen_text,[0,0])

	## DISPLAYING  THE TEXT OBJECT
	def message_to_screen(self,msg,color,y_displace=0,size="small"):
		textSurf , textRect = self.text_objects(msg,color,size)
		textRect.center = (pixel_x/2),(pixel_y/2)+y_displace
		gameDisplay.blit(textSurf,textRect)	
## CLASS FOR VARIOUS INTRO TO ALL LEVEL AND SPECIFIC TO THEM
class game_intro(message):

	def __init__(self):
		message.__init__(self)		
		pass
	
		
	## CUSTOM FUNCTION OF THE PARENT CLASS	
	def message_to_screen(self,msg,color,y_displace=0,size="small"):
		message.message_to_screen(self,msg,color,y_displace,size)
        
	def display_score(self,msg):
		message.display_score(self,msg)
	## INTRO TO THE LEVEL 1
	def intro_l1(self):
		intro = True 
		while intro:
			gameDisplay.fill(white)
			message.message_to_screen(self,"Welcome to Level 1",green,-100,"large")
			message.message_to_screen(self,"The objective of the Level is to eat red apples",black,-30)
			message.message_to_screen(self,"The more apples you eat,the longer you get",black,-10)
			message.message_to_screen(self,"Press c to Continue or q (twice)to Quit",black,10)
			
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro =False					
					return True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						intro =False					
						return True
					elif event.key == pygame.K_c:
						intro =False					
						return False
	##INTRO TO THE LEVEL 2	
	def intro_l2(self):
		intro = True 
		while intro:
			gameDisplay.fill(white)
			
			message.message_to_screen(self,"Welcome to Level 2",green,-100,"large")
			message.message_to_screen(self,"The objective of the Level is to eat red apples",black,-30)
			message.message_to_screen(self,"The more apples you eat,the longer you get",black,-10)
			message.message_to_screen(self,"Protect yourself from the colliding with black borders",black,10)
			message.message_to_screen(self,"Press c to Continue or q (twice)to Quit",black,30)
			
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro =False					
					return True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						intro =False					
						return True
					elif event.key == pygame.K_c:
						intro =False					
						return False
	## INTRO OF THE LEVEL 3		
	def intro_l3(self):
		intro = True
		while intro:
			gameDisplay.fill(white)
			
			message.message_to_screen(self,"Welcome to Level 3",green,-100,"large")
			message.message_to_screen(self,"The objective of the Level is to eat red apples",black,-30)
			message.message_to_screen(self,"The more apples you eat,the longer you get",black,-10)
			message.message_to_screen(self,"Protect yourself from the colliding with black borders and boulders",black,10)				
			message.message_to_screen(self,"boulders may change position in every game",black,30)			
			message.message_to_screen(self,"Press c to Continue or q (twice)to Quit",black,50)
			
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					intro =False					
					return True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						intro =False					
						return True
					elif event.key == pygame.K_c:
						intro =False					
						return False
		
if __name__=="__main__":
	a =message()
	b= game_intro()
	gameDisplay.fill(white)
	a.display_score('msg')	
	a.message_to_screen("Pranav",black,size="large")
	pygame.display.update()	
	print b.intro_l2()
