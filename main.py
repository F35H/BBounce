from direct.showbase.ShowBase import ShowBase

from panda3d.core import	AmbientLight, PointLight
from panda3d.core import	PerspectiveLens

import math
"""
class ComFunc():
	def CircFunc(self, amp, x, y)
	x += math.cos()
	y += math.sin()
		return dict(x=x,y=y)
"""
class StartSet(ShowBase):
	
	_sphere = None	#Model
	__aL = None	#AmbientLight
	__sP = None #Spotlight
	
	__aLN = "AmbientLight"
	__sPN = "Spotlight"
	
	def __init__(self):
		ShowBase.__init__(self)
		self.__GameSet()
		self.__ModelLoad()
		self.__GameBackground()
		
	def __GameSet(self):
		self.disableMouse()

	
	def __GameBackground(self):
		tempSP = None
		tempAL = None
		
		self.__aL = AmbientLight(self.__aLN)
		self.__sP = PointLight(self.__aLN)
		
		self.__aL.setColor((0.5,0.5,0.5,1))
		self.__sP.setColor((200,200,200,1))
		self.__sP.setLens(PerspectiveLens())
		
		self.setBackgroundColor(0.53, 0.80, 0.92, 1)
		
		tempSP = self.render.attachNewNode(self.__sP)
		tempAL = self.render.attachNewNode(self.__aL)
		
#		self.__sP = tempSP
#		self.__aL = tempAL
		
		tempSP.setPos(0,15,0)
#		tempSP.lookAt(self._sphere)
		
		self.render.setLight(tempAL)
#		self.render.setLight(tempSP)
		
	def __ModelLoad(self):
		self._sphere = self.loader.loadModel("bam/sphere.bam")
		self._sphere.reparentTo(self.render)
#		self.sphere.setScale(0.25, 0.25, 0.25)
		self._sphere.setPos(0, 10, 0)
		self._sphere.setColor(0.0,0.5,0.5,1)
		self._sphere.setTwoSided(True)


__game = StartSet()
__game.run()
