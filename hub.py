from direct.showbase.ShowBase import ShowBase

from panda3d.core import	AmbientLight, PointLight
from panda3d.core import	ClockObject

import math


class GameMain(ShowBase):
	
	def __init__(self):
		print("Hello!")
		
	def _GameSet(self):
		Clock.setMode(ClockObject.MLimited)
		Clock.setFrameRate(60)
		
		self.disableMouse()


class GameInit(ShowBase):
	
	#Base
	__centrlCube = None
	__keyMap = None
	__camTime = 0
	frameDegree = 90
	#Molecules
	__sphere = None
	__bond = None
	
	def __init__(self):
		self.__LoadSet()
		self.__LoadInit() 
		self.__ModelLoad()
#		self.__LoadClose()
#		GameMain()

	def __LoadSet(self):
		base.disableMouse()
		base.clock.setMode(ClockObject.MLimited)
		base.clock.setFrameRate(2)
		
		base.setBackgroundColor(0, 0, 0, 1)

	def __LoadInit(self):
		self.__frames = 0 #BubblePopVar
		
		self.__erlFlask = base.loader.loadModel("bam/erlflask.bam")
		self.__bubbleOne = base.loader.loadModel("bam/sphere.bam")
		self.__bubbleTwo = base.loader.loadModel("bam/sphere.bam")
		self.__bubbleThree = base.loader.loadModel("bam/sphere.bam")
		
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
		
		self.__bubbleOne.hide()
		self.__bubbleTwo.hide()
		self.__bubbleThree.hide()
		
		base.camera.setPos(self.__erlFlask.getX(),
			self.__erlFlask.getY() + 20, 0)
		base.camera.lookAt(self.__erlFlask)
			
		self.__erlFlask.reparentTo(base.render)
		self.__bubbleOne.reparentTo(base.render)
		self.__bubbleTwo.reparentTo(base.render)
		self.__bubbleThree.reparentTo(base.render)
		
		base.taskMgr.add(self.__BubblePop, "BubblePop")
		
	def __BubblePop(self, task):
		self.__frames += 1
		self.__bubbleOne.hide() if self.__frames % 2 == 0 else self.__bubbleOne.show() 
		self.__bubbleTwo.hide() if self.__frames % 3 == 0 else self.__bubbleTwo.show() 
		self.__bubbleThree.hide() if self.__frames % 4 == 0 else self.__bubbleThree.show() 
		return task.cont
				
	def __WinInit(self)
		global base
		base = ShowBase()
		
	def __ModelLoad(self):
		global sphere
		global bond
		
		sphere = [0] * 10
		bond = [0] * 15
		
		centrlCube = base.loader.loadModel("bam/cube.bam")
		sphere[0] = base.loader.loadModel("bam/sphere.bam")
		sphere[1] = base.loader.loadModel("bam/sphere.bam")
		sphere[2] = base.loader.loadModel("bam/sphere.bam")
		sphere[3] = base.loader.loadModel("bam/sphere.bam")
		sphere[4] = base.loader.loadModel("bam/sphere.bam")
		sphere[5] = base.loader.loadModel("bam/sphere.bam")
		sphere[6] = base.loader.loadModel("bam/sphere.bam")
		sphere[7] = base.loader.loadModel("bam/sphere.bam")
		sphere[8] = base.loader.loadModel("bam/sphere.bam")
		sphere[9] = base.loader.loadModel("bam/sphere.bam")
#		sphere[10] = base.loader.loadModel("bam/sphere.bam")
		bond[0] = base.loader.loadModel("bam/bond.bam")
		bond[1] = base.loader.loadModel("bam/bond.bam")
		bond[2] = base.loader.loadModel("bam/bond.bam")
		bond[3] = base.loader.loadModel("bam/bond.bam")
		bond[4] = base.loader.loadModel("bam/bond.bam")
		bond[5] = base.loader.loadModel("bam/bond.bam")
		bond[6] = base.loader.loadModel("bam/bond.bam")
		bond[7] = base.loader.loadModel("bam/bond.bam")
		bond[8] = base.loader.loadModel("bam/bond.bam")
		bond[9] = base.loader.loadModel("bam/bond.bam")
		bond[10] = base.loader.loadModel("bam/bond.bam")
		bond[11] = base.loader.loadModel("bam/bond.bam")
		bond[12] = base.loader.loadModel("bam/bond.bam")
		bond[13] = base.loader.loadModel("bam/bond.bam")
		bond[14] = base.loader.loadModel("bam/bond.bam")
#		bond[15] = base.loader.loadModel("bam/bond.bam")
		"""
		erlOne = self.loader.loadModel("bam/erlflask.bam")
		erlTwo = self.loader.loadModel("bam/erlflask.bam")
		erlThree = self.loader.loadModel("bam/erlflask.bam")
		erlFour = self.loader.loadModel("bam/erlflask.bam")
		playBut = loadObject("PlayBut.png")
		howBut = loadObject("HowPlayBut.png")
		aboutBut = loadObject("aboutbut.png")
		exitBut = loadObject("exitBut.png")
		"""
		
	def __LoadClose(self):
		taskMgr.remove("BubblePop")
		
		
		
		
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
		
		return True
		
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
