from random import random, randint, choice
import sys
import os

def build( extension = None ):
	"""
	#Appends desired path (default = python docs file) to sys filepath
	#Place in main python folder, then import as is needed
	"""
#	import sys
	filePath = "C:\Users\Owner\Documents\Python"
	if extension:
		filePath += '\\' + extension
	sys.path.append(filePath)
	print 'Filepath added: ' + filePath

def fill( i, buffer=3 ):
	"""
	Given a number, returns the equivalent string, preceded
	by zeroes until it fills the buffer length.
	"""
	
	c = str(i)
	while(len(c) < buffer):
		c = "0"+c
	return c

def rAlloc( points, alloc, allocMax = [] ):
	"""
	Function to allocate points randomly into a range of categories.

	Takes a dictionary with zeroed values, and the number of points to
	allocate, and returns the appropriately incremented dictionary.

	'allocMax', if entered, is a list with the maximum value allowed for 
	each dictionary value. Requires an entry for each category.
	"""

	if allocMax:
		total = 0
		for v in allocMax:
			total += v
		if points > total:
			points = total
		sml = min(allocMax)
		aTemp = []
		for i in range(len(allocMax)):
			aTemp.append(allocMax[i]/sml)

		while points > 0:
			index = lottery(aTemp)
			alloc[index] += 1
			points -= 1
			if alloc[index] > allocMax[index]:
				alloc[index] -= 1
				points += 1
	else:
		while points > 0:
			stat = randint(0,(len(alloc)-1))
			alloc[stat] +=1
			points -= 1

	return alloc


def lottery(items):
	"""
	Simulates a lottery draw

	Input 'items' is a list, with each index position
	representing a unique entrant in the lottery, and
	each value representing the number of tickets held
	by that entrant.

	Returns the winning entrant's index number.
	"""

	l 		= len(items)
	pointer = 0
	votes 	= []

	for n in items:
		for i in range(n):
			votes.append(pointer)
		pointer += 1

	winningIndex = choice(votes)
	return winningIndex

def freq(li):
	#returns a dictionary showing how often each element occurs in a list
	fDict = {}
	for i in li:
		if i in fDict:
			fDict[i] += 1
		else: fDict[i] = 1
	return fDict
	
def cFreq(items,n):
	"""
	Given a 'lottery' list and a number of lottery runs,
	function returns a dictionary showing how many times
	each entrant was selected.
	"""
	
	choiceList = []
	freqDict = {index:0 for index in items}
	
	for i in range(n):
		choiceList.append(lottery(items))
	
	for i in choiceList:
		freqDict[items[i]] += 1
		
	return freqDict
		
def listFromFreqDict( dic, minToMax=False ):
	"""
	Returns an ordered list from a frequency dictionary
	(Ordered from most to least frequent by default)
	"""
	
	freqList = [[dic.values()[i],dic.keys()[i]] for i in range(len(dic.items()))]
	freqList.sort( reverse = not minToMax )
	
	li = []
	for entry in range(len(freqList)):
		li.append(freqList[entry][1])
	
	return li
	
def percentCheck( n ):
	"""
	Generates a random number between 0-100, and checks 
	whether it is less than a given value.

	Returns 1 if random number < n, otherwise returns 0
	"""

	r = randint(0,100) 
	if r < n:
		return 1
	else: return 0


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

def listify( self, *entity ):
#Returns a list of non-list entities
	if isinstance(entity,list):
		return entity
	list = []
	for e in entity:
		if isinstance(e,list) == False:
			list.append(e)
	return list

def unzip(li):
#turns list: [[a,b],[c,d]...[y,z]] into list [[a,c...y],[b,d...z]]
	x = []
	y = []
	for i in li:
		x.append(i[0])
		y.append(i[1])
	return [x,y]
	
def match(vn,wn):
	#from [[v1,n1],[v2,n2]...] and [[w1,n1],[w2,n2]...]
	#to [v1,v2,v3,v4],[w1,w2,w3,w4]
		v = []
		w = []
		for i in vn:
			for j in wn:
				if i[1] == j[1]:
					v.append(i[0])
					w.append(j[0])
		return [v,w]
	
	
def pfac(n):
	#returns list of the prime factors of 'n' (non-unique)
	r = n
	f = 2
	pfs = []
	while r > 1:
		if r%f == 0:
			pfs.append(f)
			r = r/f
		else:
			if f==2: f+=1
			else: f+=2
	return pfs

def checkdiv(n,x = [3,5]):
	#returns the sum of all number smaller than 'n' that are divisible by all the numbers in list 'x'
	li = []
	s = 0
	for i in range(n):
		for j in x:
			if (i/float(j))%1 == 0:
				li.append(i)
				break
	return sum(li)
	
def findLargest(string,ss=5):
	#Given a string of integers, returns the largest product of every possible 'n'-sized sequence
	sarray = []
	seq = 0
	p = 0
	for i in string:
		sarray.append(int(i))
	for j in range(len(sarray)-(ss-1)):
		tseq = 1
		for k in range(ss):
			tseq *= sarray[j+k]
		if tseq > seq:
			seq = tseq
			p = j
	return seq, p

	

		
