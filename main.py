from direct.showbase.ShowBase import ShowBase

from panda3d.core import	AmbientLight, PointLight
from panda3d.core import	ClockObject

import math

class StartSet(ShowBase):
	
	#Base
	__centrlCube = None
	__keyMap = None
	__camTime = 0
	frameDegree = 90
	#Molecules
	__sphere = None
	__bond = None
	
	def __init__(self):
		ShowBase.__init__(self)
		self.__GameSet()
		self.__BaseLoad()
		
	def __GameSet(self):
		globalClock.setMode(ClockObject.MLimited)
		globalClock.setFrameRate(60)
		
		self.disableMouse()

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
			deltaTime = base.clock.dt
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

__game = StartSet()
__game.run()
