from ursina import *

sphere = "sphere"
cube = "cube"
erlFlask = "erlFlask.obj"
bond = "bond.obj"

class MenBtn():

	btnTup = [0,0,0,0]

	def __new__(self, indx, sInd):
		self.__indx = indx
		self.__sInd = sInd
		
		self.__load__(self)
		
		return btnTup
		
	def __load__(self): 
		btnTup[1] = Button(parent=scene)
		btnTup[0] = Entity(parent=scene)
		btnTup[2] = Entity(parent=scene)
		btnTup[3] = Text(parent=scene)
		
		btnTup[0].model = erlFlask
		btnTup[2].model = erlFlask
 
		btnTup[1].visible = False
		btnTup[0].visible = False
		btnTup[2].visible = False
		btnTup[3].visible = False

		btnTup[0].position = (1.5,0,-10)
		btnTup[1].position = (0,0,-10)
		btnTup[2].position = (-1.5,0,-10)
		btnTup[3].position = (0,0,-10)

		btnTup[1].y += MenBtn.sInd
		btnTup[0].y += MenBtn.sInd
		btnTup[2].y += MenBtn.sInd
		btnTup[3].y += MenBtn.sInd
		btnTup[3].x -= (MenBtn.sInd * .01)
			
		btnTup[0].scale = 0.05
		btnTup[1].scale = 0.25
		btnTup[2].scale = 0.05
		btnTup[3].scale = 2
		
		btnTup[0].rotation_z = -40
		btnTup[2].rotation_z = 40
		
		btnTup[1].scale_x = 2
		
		if MenBtn.indx != 1:
			btnTup[1].on_mouse_enter = self.__entry
			btnTup[1].on_mouse_exit = self.__exit
		
	def __entry():
		btnTup[0].show()
		btnTup[2].show()
	
	def __exit():
		btnTup[0].hide()
		btnTup[2].hide()
		

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
		Bond.bond = Entity()
		Bond.bond.visible = False
		Bond.bond.model = bond
