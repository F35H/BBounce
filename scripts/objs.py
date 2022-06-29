from ursina import *

sphere = "sphere"
cube = "cube"
erlFlask = "erlFlask.obj"
bond = "bond.obj"

class SMenBtn(Obj):
	def __init__(self, indx, sInd):
		self.__indx = indx
		self.__sInd = sInd
		self._btnTup = [0,0]
		
		self._load()
	
	def _load():
		
		
	def _create()
	
		
	def _load(self):
		self.btnTup[0] = Button(parent=scene)
		self.btnTup[1] = Text(parent=scene)
		
		self.btnTup[0].visible = False
		self.btnTup[1].visible = False

		self.btnTup[0].position = (1.5,0,-10)
		self.btnTup[1].position = (0,0,-10)
		
class MenScrn(sMenBtn):
	def __init__(self, indx, pos):
		self.__indx = pos
		self.__sInd = sInd
		self.scrnTup = [0,0,0,0]
		
		

class MenBtn():
	def __init__(self, indx, sInd):
		self.__indx = indx
		self.__sInd = sInd
		self.btnTup = [0,0,0,0]
		
		self._load()
		
	def _load(self): 
		self.btnTup[1] = Button(parent=scene)
		self.btnTup[0] = Entity(parent=scene)
		self.btnTup[2] = Entity(parent=scene)
		self.btnTup[3] = Text(parent=scene)
		
		self.btnTup[0].model = erlFlask
		self.btnTup[2].model = erlFlask
 
		self.btnTup[1].visible = False
		self.btnTup[0].visible = False
		self.btnTup[2].visible = False
		self.btnTup[3].visible = False

		self.btnTup[0].position = (1.5,0,-10)
		self.btnTup[1].position = (0,0,-10)
		self.btnTup[2].position = (-1.5,0,-10)
		self.btnTup[3].position = (0,0,-10)
		
		self.btnTup[1].y += self.__sInd
		self.btnTup[0].y += self.__sInd
		self.btnTup[2].y += self.__sInd
		self.btnTup[3].y += self.__sInd
		self.btnTup[3].x -= (self.__sInd * .01)
		
		self.btnTup[0].scale = 0.05
		self.btnTup[1].scale = 0.25
		self.btnTup[2].scale = 0.05
		self.btnTup[3].scale = 2
		
		self.btnTup[0].rotation_z = -40
		self.btnTup[2].rotation_z = 40
		
		self.btnTup[1].scale_x = 2
		
		if (self.__indx) != 1:
			self.btnTup[1].on_mouse_enter = self.__entry
			self.btnTup[1].on_mouse_exit = self.__exit
		
	def __entry(self):
		self.btnTup[0].visible = True
		self.btnTup[2].visible = True
	
	def __exit(self):
		self.btnTup[0].visible = False
		self.btnTup[2].visible = False
		
	def define(self, txt, fnc, t):
		if (t):
			self.btnTup[2].visible = True
			self.btnTup[0].visible = True
			self.btnTup[1].disabled = True
			
		btnTup[3].text = txt  
		btnTup[3].on_click = func 
		
	def __del__(self):
		self.btnTup[0].visible = false
		self.btnTup[1].visible = false
		self.btnTup[2].visible = false
		self.btnTup[3].visible = false
		
		self.btnTup[3].parent = None
		self.btnTup[2].parent = None
		self.btnTup[1].parent = None
		self.btnTup[0].parent = None
		
		

class Atom():
	def __new__(self):
		self.__load__(self)
		return self.atom

	def __load__(self):
		self.atom = Entity(parent=None)
		self.atom.visible = False
		self.atom.model = sphere

class Bond():
	def __new__(self):
		self.__load__()
		return self.bond

	def __load__():
		Bond.bond = Entity(parent=None)
		Bond.bond.visible = False
		Bond.bond.model = bond
