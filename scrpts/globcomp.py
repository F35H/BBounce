from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

#Game Objects

class MenBut():
	def __new__(self, selectNum):
		self.modTup = self.__ModLoad(selectNum)
		self.__EndSet(selectNum)	
		return self.modTup
	
	def __ModLoad(num):
		MenBut.modTup = [0,0,0]
		
		MenBut.modTup[0] = base.loader.loadModel("bam/erlflask.bam")
		if num == 1:
			MenBut.modTup[1] = base.loader.loadModel("bam/logo.egg")
		else:
			MenBut.modTup[1] = base.loader.loadModel("bam/menBut.bam")
		MenBut.modTup[2] = base.loader.loadModel("bam/erlflask.bam")
		
		return MenBut.modTup
		
	def __EndSet(num):
			
		if num == 1:
			MenBut.modTup[1].setPos(0,-20, 1)
			
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
		
#Interface 

class ButInter():
	
	#Raycast function goes here.
