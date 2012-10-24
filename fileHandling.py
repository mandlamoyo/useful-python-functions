import os

class FileContainer:
	def __init__( self, rType = 'txt', wType = 'txt' ):
		self.savedPath = os.getcwd()
		self.fileName = None
		self.readFile = None
		self.writeFile = None
		self.currentTrans = None
		
		self.setTypes(rType, wType)

	def setTypes( self, rType = None, wType = None ):
		if rType:
			self.readType = rType
		if wType:
			self.writeType = wType

	def changeFilePath( self, newPath ):
		os.chdir(newPath)
	
	def loadFile( self, name, mode = 'r', pickle = 0 ):
		#Modes: r = read, r+ = read/write, a = append
	#	if self.readFile:
	#		self.readFile.close()

		if mode == 'w': mode = 'r+'

		self.readFile = open(name + '.' + self.readType,mode)
		self.fileName = name

		if mode != 'r':
	#		if self.writeFile:
	#			self.writeFile.close()
			self.writeFile = self.readFile

	#	print name + '\n\n'
	#	self.printFile('r')
			
	def updateTranslation( self, trans ):
		self.currentTrans = trans
		
	def getFile( self, code ):
		files = {'c':self.currentTrans, 'r':self.readFile, 'w':self.writeFile}
		return files[code]
		
	def getString( self, code ):
		f = self.getFile(code)
		fstr = ''
		for line in f:
			fstr += line
		f.seek(0)
		return fstr
		
	def createFile( self, name ):
		self.writeFile = open(name + '.' + self.readType,"w")
		
	def writeToFile( self, text ):
		if self.writeFile:
			self.writeFile.write( text )
		else: print 'No file to save to'
		
	def saveFile( self, name, sfile = None, oneTime = 1, pickle = 0 ):
		if name == None:
			if self.fileName:
				name = self.fileName
			else: return False
			
		if self.writeFile == None:
			self.createFile(name)
			
		if self.currentTrans:
			self.writeToFile(self.currentTrans)
			self.writeFile.close()
		elif sfile:
			self.writeToFile(sfile)
			self.writeFile.close()
		else: 
			print 'Nothing to save'
			return False
		
		if( oneTime ): self.writeFile = None
		return True

	#	if pickle:

		
	def printFile( self, code ):
		f = self.getFile(code)
		if isinstance(f,file):
			f.seek(0)
			for line in f:
				print line	
			f.seek(0)
		else: print f
		
	def closeFiles( self ):
		if isinstance(self.readFile,file):
			self.readFile.close()
		if isinstance(self.readFile,file):
			self.writeFile.close()

	def __del__( self ):
		os.chdir( self.savedPath )
		#self.closeFiles()
