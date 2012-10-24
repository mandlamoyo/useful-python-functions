import pygame
#from pygame.locals import *

#import settings
#import world
#import input
#import factories

import pygame
import factories
import drawers
import random

class Settings:
	def __init__( self ):			
		self.world = {'size':[700,500],\
					  'caption':'Default',\
					  'walls':0,\
					  'fps':20,\
					  'respawnRate':30,\
					  'population':\
						{'boid':5,\
						 'food':10},\
					  'colours':\
							{'black':[0,0,0],\
							 'white':[255,255,255],\
							 'red':[255,0,0],\
							 'green':[0,255,0],\
							 'blue':[0,0,255],\
							 'yellow':[255,255,0]\
							}}
							 
		self.controller = {'textLocation':[(self.world['size'][0]-15),10]}
		

class World:
	def __init__( self, settings ):
		w = settings.world
		
		self.fps = w['fps']
		self.size = w['size']
		self.colours = w['colours']
		self.caption = w['caption']
		
		self.surface = pygame.display.set_mode(self.size)
		
		self.agentList = {} # add types enemy, predator
		self.agentModifiers = {'boid':[factories.BoidFactory(settings),drawers.BoidDrawer(self.surface,self.colours,settings)],'food':[factories.FoodFactory(self.agentList,settings),drawers.FoodDrawer(self.surface,self.colours)]} #Update as necessary
		self.idFac = factories.IdFactory()
		
	def agentList( self, agentList ):
		self.agentList = agentList
		
	def draw( self, agent ):
		pass
		
	def setCaption( self, newCaption ):
		pygame.display.set_caption(newCaption)
		
	

class Controller:
	def __init__( self ):
		
		self.settings = settings.Settings()
		self.world = world.World(self.settings)
		self.idFactory = factories.IdFactory()
		self.input = input.Input()
		
		self.tPos = [self.settings.controller['textLocation'][0],self.settings.controller['textLocation'][1]]
		
		self.fps = self.world.fps
		self.clock = pygame.time.Clock()
		self.done = False
		self.counter = 0
		
		self.world.buildPopulation()
		
		
	def run( self ):
		pygame.init()
		pygame.display.set_caption(self.world.caption)
		
		while self.done == False:
			self.process()
			
		pygame.quit()
		
		
	def process( self ):
		world.surface.fill(c['black'])
		self.checkQuit()
		self.clock.tick(self.fps)
		pygame.display.flip()
	
	
	#def reset( self ):
	
	
	def getText( self ):
		c = self.world.colours
		basicFont = pygame.font.SysFont(None, 20)
		text = basicFont.render(str(self.counter), True, c['blue'], c['black'])	
		textRect = text.get_rect()
		textRect.centerx = self.tPos[0]
		textRect.centery = self.tPos[1]
		self.world.surface.blit(text, textRect)
	
	def checkBoundaries( self, agent ):
		world = self.world
		if world.walls:
			if agent.position.y > world.size[1] or agent.position.y < 0:
				agent.velocity.Reverse(0,1)
				agent.manager.Divide(agent.velocity,1.5)
			if agent.position.x > world.size[0] or agent.position.x < 0:
				agent.velocity.Reverse(1,0)
				agent.manager.Divide(agent.velocity,1.5)
		else:
			if agent.position.x > world.size[0]:
				agent.setPosition(0,agent.position.y)
			if agent.position.x < 0:
				agent.setPosition(world.size[0],agent.position.y)
			if agent.position.y > world.size[1]:
				agent.setPosition(agent.position.x,0)
			if agent.position.y < 0:
				agent.setPosition(agent.position.x,world.size[1])
	
	def checkQuit( self ):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
				
	def setWorld( self, world ): #
		self.world = world
			
			
def doRectsOverlap( self, rect1, rect2 ):
	for a, b in [(rect1, rect2), (rect2, rect1)]:
		if ((isPointInsideRect(a.left, a.top, b)) or (isPointInsideRect(a.left, a.bottom, b)) or (isPointInsideRect(a.right, a.top, b)) or (isPointInsideRect(a.right, a.bottom, b))):
			return True
	return False
	
def isPointInsideRect( self, x, y, rect):
	if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
		return True
	else:
		return False