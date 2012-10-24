from brain import makerandomtree, node, paramnode
from random import random,randint,choice
from copy import deepcopy
from math import log

def mutate(t,pc,probchange=0.1):
	if random()<probchange:
		return makerandomtree(pc)
	else:
		result=deepcopy(t)
		if isinstance(t,node):
			result.children=[mutate(c,pc,probchange) for c in t.children]
		return result
		
		
def crossover(t1,t2,probswap=0.7,top=1):
	if random()<probswap and not top:
		return deepcopy(t2)
	else:
		result=deepcopy(t1)
		if isinstance(t1,node) and isinstance(t2,node):
			result.children=[crossover(c,choice(t2.children),probswap,0) for c in t1.children]
		return result	

def fix( n, pc ):
	if( isinstance( n, paramnode ) and n.idx >= pc ):
		n.idx = randint( 0, pc-1 )
	elif( isinstance( n, node ) ):
		for c in n.children:
			fix( c, pc )
		
			
def evolve(pc,popsize,rankfunction,maxgen=500,mutationrate=0.1,breedingrate=0.4,pexp=0.7,pnew=0.05,previouswinner=0):
	def selectindex():
		return int(log(random())/log(pexp))
	
	population=[makerandomtree(pc) for i in range(popsize)]
	if previouswinner!=0:
			population.pop()
			population.append(previouswinner)
			
	for i in range(maxgen):
		scores=rankfunction(population)
		print scores[0][0]
		if scores[0][0]==0: break
		
		newpop=[scores[0][1],scores[1][1]]
		
		while len(newpop)<popsize:
			if random()>pnew:
				newpop.append(mutate(crossover(scores[selectindex()][1],scores[selectindex()][1],probswap=breedingrate),pc,probchange=mutationrate))
			else:
				newpop.append(makerandomtree(pc))
				
		population=newpop
	scores[0][1].display()
	return scores[0][1]
	
def tournament( pl, game ):
	"""
	Stages a tournament in which each player competes with every other player.

	Takes a list of players, and the desired game to be played, and returns a
	zipped list of each player and their score.
	
	'game' syntax: 
		Parameters: List of players
		return: 0 if pl[0] wins
				1 if pl[1] wins
				-1 if tie
	"""
	losses=[0 for p in pl]
	for i in range(len(pl)):
		for j in range(len(pl)):
			if i==j: continue
			winner=game([pl[i],pl[j]])
			
			if winner==0:
				losses[j]+=2
			elif winner==1:
				losses[i]+=2
			elif winner==-1:
				losses[i]+=1
				losses[j]+=1
				pass
	z=zip(losses,pl)
	z.sort()
	return z
	
	
class GenomeFactory:
	def __init__( self, settings, type ):
		#all INT values in 'settings' file
				
		#pass default unit-specific settings, not generic object
		self.settings = settings.genomes[type]
		self.domain = self.settings['domain']
		self.constants = self.settings['constants']
		#((500,5000),(5,150),(2,20),(20,200),(20,200),(500,1500),(0,200),(0,200),(0,200),(0,1))
		
	def createRandom( self ):
		genome = []
		for i in range(len(self.domain)):
	#		WON'T WORK, NOT TYPE SPECIFIC
	#		if i == (genderposition):
	#			g = self.getGender()
	#			genome.append(g)
	#			continue
			l = self.domain[i][0]
			u = self.domain[i][1]
			
			g = randint(l,u)
			genome.append(g)
			
		return genome
		
	def createDefault( self ):
		s = self.default
		
		genome = []
		for i in s:
			if i == 'gender':
				g = self.getGender()
				genome.append(g)
				continue
			genome.append(s[i])
		return genome
		
	def getGender( self, fpp = 55 ): #female percent of population
		g = randint(0,100)
		if g > fpp:
			return 1
		else: 
			return 0
			
#Domain is a list of 2 tuples that specify min/max values for each variable
def mutateGene( domain, li, mr = 0.5 ):
	l2 = []
	for i in range(len(li)):
		if random()<mr:
			l2.append(li[i]+randint(-10,10))
			if l2[i] < domain[i][0]: l2[i] = domain[i][0]
			elif l2[i] > domain[i][1]: l2[i] = domain[i][1]
		else: l2.append(li[i])
	return l2

def mgFloat( domain, li, mr = 0.5 ):
	l2 = []
	for i in range(len(li)):
		if random()<mr:
			l2.append(li[i]+randint(-1,1)*random())
			if l2[i] < domain[i][0]: l2[i] = domain[i][0]
			elif l2[i] > domain[i][1]: l2[i] = domain[i][1]
		else: l2.append(li[i])
	return l2
	
def mutateGene2( domain, vec, step = 1 ): 
	i = randint(0,len(domain)-1)
	if random()<0.5 and vec[i]>domain[i][0]:
		return vec[0:i]+[vec[i]-step]+vec[i+1:]
	elif vec[i]<domain[i][1]:
		return vec[0:i]+[vec[i]+step]+vec[i+1:]
			
def crossoverGenes( domain, r1, r2, cr = 0.5 ):
	r = randint(0,1)
	if r: r1,r2 = r2,r1
	if random() < cr:
		i = randint(0,len(domain))
		j = randint(i,len(domain))
		return r1[0:i]+r2[i:j]+r1[j:]
	return r1

def crossoverGenes2( domain, r1, r2 ):
	i = randint(1,len(domain)-2)
	return r1[0:i]+r2[i:]
	