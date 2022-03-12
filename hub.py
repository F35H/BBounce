from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

from panda3d.core import	AmbientLight, PointLight
from panda3d.core import	ClockObject

import threading
import math
import time

butList = []
atomList = []
bondList = []

class GameMain(ShowBase):
	
	
	def __init__(self):
		print("Hello!")
		
	def _GameSet(self):
		Clock.setMode(ClockObject.MLimited)
		Clock.setFrameRate(60)
		
		self.disableMouse()
	

class MenBut():
	def __new__(self, selectNum):
		self.modTup = self.__ModLoad(selectNum)
		self.__EndSet(selectNum)	
		return self.modTup
	
	def __Texload(num):
		match num:
			case 0: return base.loader.loadTexture("texture/MenBut/BBLogo.png")
			case 1: return base.loader.loadTexture("texture/MenBut/BBPlay.png")
			case 2: return base.loader.loadTexture("texture/MenBut/BBAbout.png")
			case 3: return base.loader.loadTexture("texture/MenBut/BBHow.png")
			case 4: return base.loader.loadTexture("texture/MenBut/BBExit.png")
			case _: print("Caution: wrong Variable in menbut!")
	
	def __ModLoad(num):
		MenBut.modTup = [0,0,0]
		
		MenBut.modTup[0] = base.loader.loadModel("bam/erlflask.bam")
		if num == 1:
			MenBut.modTup[1] = base.loader.loadModel("bam/logo.bam")
		else:
			MenBut.modTup[1] = base.loader.loadModel("bam/menBut.bam")
		MenBut.modTup[2] = base.loader.loadModel("bam/erlflask.bam")
		
		return MenBut.modTup
		
	def __EndSet(num):
#			self.modTup[0]
#		MenBut.modTup[0].setTexture(MenBut.textTup[1], 1)
#		MenBut.modTup[2]
			
		if num == 1:
			MenBut.modTup[0].hide()
			MenBut.modTup[1].setPos(0,-20, 1)
			MenBut.modTup[2].hide()
			
			
		else:
			MenBut.modTup[0].setPos(7,-20,-0.4)
			MenBut.modTup[1].setPos(0,-20,-0)
			MenBut.modTup[2].setPos(-7,-20,-0.4)
			
		MenBut.modTup[0].setScale(0.20)
		MenBut.modTup[1].setScale(0.75)
		MenBut.modTup[2].setScale(0.20)
		
		MenBut.modTup[0].setHpr(0,0,-40)
		MenBut.modTup[2].setHpr(0,0,40)
		
		
			
class Atom():
	def __new__(self):
		self.__load__()
		return self.atom
		
	def __load__():
		Atom.atom = base.loader.loadModel("bam/sphere.bam")
		
		Atom.atom.setColor(0,0,0,1)
	
class Bond():
	def __new__(self):
		self.__load__()
		return self.bond
		
	def __load__():
		Bond.bond = base.loader.loadModel("bam/bond.bam")
		
		Bond.bond.setColor(0,0,0,1)

class GameInit(ShowBase):

	__camTime = 0
	frameDegree = 90
	
	def __init__(self):
		self.__WinInit()
#		GameMain()

	def __WinInit(self):
		global base
		base = ShowBase()
		self.__LoadSet()

	def __LoadSet(self):
		base.disableMouse()
		base.clock.setMode(ClockObject.MLimited)
		#The loading sequence loads significantly slower when unlimited.
		base.clock.setFrameRate(10000)
		base.setBackgroundColor(0, 0, 0, 1)
		self.__LoadInit() 

	def __LoadInit(self):
		#Vars for Bubble Pop
		self.__modThreads = []
		self.__frames = 0
		self.bondNum = 150
		self.bondCheck = self.bondNum
		self.menNum = 5
		self.cubeNum = 1
		self.atomNum = math.floor((.6666 * self.bondNum))
		
		#Vars for LoadInit
		self.__erlFlask = base.loader.loadModel("bam/erlflask.bam")
		self.__bubbleOne = base.loader.loadModel("bam/sphere.bam")
		self.__bubbleTwo = base.loader.loadModel("bam/sphere.bam")
		self.__bubbleThree = base.loader.loadModel("bam/sphere.bam")
		self.__loadingText = OnscreenText("Loading!",
		style=1, fg=(1, 1, 1, 1), shadow=(0, 0, 0, 0),
			pos=(0,-0.3), scale = .07)
		
		self.__erlFlask.setColor(1,1,1,0.7)
		self.__bubbleOne.setColor(1,1,1,1)
		self.__bubbleTwo.setColor(1,1,1,1)
		self.__bubbleThree.setColor(1,1,1,1)
		
		self.__erlFlask.setPos(0,0,0)
		self.__bubbleOne.setPos(0.05,0,2.1)
		self.__bubbleTwo.setPos(0.25,0,2.5)
		self.__bubbleThree.setPos(0.6,0,2.7)
		
		self.__erlFlask.setScale(0.20)
		self.__bubbleOne.setScale(0.19)
		self.__bubbleTwo.setScale(0.15)
		self.__bubbleThree.setScale(0.1)
		
		base.camera.setPos(self.__erlFlask.getX(),
			self.__erlFlask.getY() + 20, 0)
		base.camera.lookAt(self.__erlFlask)
			
		self.__erlFlask.reparentTo(base.render)
		self.__bubbleOne.reparentTo(base.render)
		self.__bubbleTwo.reparentTo(base.render)
		self.__bubbleThree.reparentTo(base.render)	
		
		base.taskMgr.add(self.__BubblePop, "BubblePop")
		
	def __BubblePop(self, task):
		if self.__frames % 10 == 0:
			self.__bubbleOne.hide() if self.__frames % 7 == 0 else self.__bubbleOne.show() 
			self.__bubbleThree.hide() if self.__frames % 4 == 0 else self.__bubbleThree.show()
			self.__bubbleTwo.hide() if self.__frames % 3 == 0 else self.__bubbleTwo.show() 
		
		if self.__frames >= self.bondCheck:
			for i in range(len(self.__modThreads)):
				self.__modThreads[i][0].join()
				self.__modThreads[i][1].join()
				self.__modThreads[i][2].join()
			self.__LoadClose()
		else:
			threading.Thread(target = self.MThreadLoad()) 	
			
			self.bondNum -= 1
			self.__frames += 1
		return task.cont
	
	def MThreadLoad(self):	
		lock = threading.Lock()
		
		with lock:
			self.__modThreads.append((threading.Thread(target = self.EssentialModLoad()),
			threading.Thread(target = self.AtomLoad()),
			threading.Thread(target = self.BondLoad())))
			
			self.__modThreads[self.__frames][0].start()
			self.__modThreads[self.__frames][1].start()
			self.__modThreads[self.__frames][2].start()
			
	def EssentialModLoad(self):
		global butList
		
		if self.bondNum <= self.cubeNum:
			self.__centrlCube = base.loader.loadModel("bam/cube.bam")
		if self.bondNum <= self.menNum:
			butList.append(MenBut(self.bondNum))
			
	def AtomLoad(self):
		global atomList
		
		if self.bondNum < self.atomNum: 
			atomList.append(Atom())
			
	def BondLoad(self):
		global bondList
		bondList.append(Bond())

	def __LoadClose(self):
		taskMgr.remove("BubblePop")	
		
		self.__erlFlask.detachNode()
		self.__bubbleOne.detachNode()
		self.__bubbleTwo.detachNode()
		self.__bubbleThree.detachNode()
		self.__loadingText.detachNode()
		
		del self.__erlFlask
		del self.__bubbleOne
		del self.__bubbleTwo
		del self.__bubbleThree
		del self.__loadingText
		
		mod = 0
		for i in range(len(butList)):
			butList[i][0].reparentTo(base.render)
			butList[i][1].reparentTo(base.render)
			butList[i][2].reparentTo(base.render)
			
			butList[i][0].setZ(butList[i][0].getZ() + mod)
			butList[i][1].setZ(butList[i][1].getZ() + mod)
			butList[i][2].setZ(butList[i][2].getZ() + mod)
			
			butList[i][1].lookAt(base.camera)
			
			mod += (15/self.menNum)
			
		base.camera.lookAt(butList[math.floor(self.menNum/2)][1])			
		
		
		
	def __BaseLoad(self):
		self.__centrlCube = self.loader.loadModel("bam/cube.bam")
		self.__keyMap = [0] * 2
			
		self.__centrlCube.setPos(0,0,0)
#		self.__centrlCube.setColor()
		
		self.accept("space", self.__KeySet, [0,0])

		self.__centrlCube.reparentTo(self.render)
		
		self.camera.setPos(self.__centrlCube.getX(),
			self.__centrlCube.getY() + 20, 0)

		self.taskMgr.add(self.__KeySwitch, "moveTask")
		
	def __KeySet(self, index, dummy):
		match index:
			case 0:
				if self.__keyMap[index]:
					self.__keyMap[index] = False
				else:
					self.__keyMap[index] = True 
				 
	def __KeySwitch(self, task):
		if self.__keyMap[0]:
			self.__CameraMV(True)
		else:
			self.__CameraMV(False)
		return task.cont	
		
	def __CameraMV(self, boolean):
		if boolean:
			self.frameDegree += 1
			cos = math.cos(math.radians(self.frameDegree))
			cosval = cos*20
			sin = math.sin(math.radians(self.frameDegree))
			sinval = sin*20
			self.camera.setPos(self.__centrlCube.getX() + cosval,
				self.__centrlCube.getY() + sinval, 0)
				
			self.__camTime += 1
		else:
			self.__camTime = 0
			
		self.camera.lookAt(self.__centrlCube)
