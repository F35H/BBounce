from ursina import *

sphere = "sphere"
cube = "cube"
erlFlask = "erlFlask.obj"
bond = "bond.obj"

class MenBtn():
	def __new__(self, indx, sInd):
		self.indx = indx
		self.sInd = sInd
		self.btnTup = [0,0,0,0]
		
		self.__load__()
		
		return self.btnTup
		
	def __load__(): 
		MenBtn.btnTup[1] = Button(parent=scene)
		MenBtn.btnTup[0] = Entity(parent=scene)
		MenBtn.btnTup[2] = Entity(parent=scene)
		MenBtn.btnTup[3] = Text(parent=scene)
 
		MenBtn.btnTup[1].visible = False
		MenBtn.btnTup[0].visible = False
		MenBtn.btnTup[2].visible = False
		MenBtn.btnTup[3].visible = False
 
		MenBtn.btnTup[0].model = erlFlask
		MenBtn.btnTup[2].model = erlFlask

		MenBtn.btnTup[0].position = (1.5,0,-10)
		MenBtn.btnTup[1].position = (0,0,-10)
		MenBtn.btnTup[2].position = (-1.5,0,-10)
		MenBtn.btnTup[3].position = (0,0,-10)

		MenBtn.btnTup[1].y += MenBtn.sInd
		MenBtn.btnTup[0].y += MenBtn.sInd
		MenBtn.btnTup[2].y += MenBtn.sInd
		MenBtn.btnTup[3].y += MenBtn.sInd
			
		MenBtn.btnTup[0].scale = 0.05
		MenBtn.btnTup[1].scale = 0.25
		MenBtn.btnTup[2].scale = 0.05
		MenBtn.btnTup[3].scale = 0.50
		
		MenBtn.btnTup[0].rotation_z = -40
		MenBtn.btnTup[2].rotation_z = 40
		
		MenBtn.btnTup[1].scale_x = 2
		
		if != 1:
			MenBtn.btnTup[1].on_mouse_enter = MenBtn.__entry
			MenBtn.btnTup[1].on_mouse_exit = MenBtn.__exit
		
	def __entry():
		MenBtn.btnTup[0].show()
		MenBtn.btnTup[2].show()
	
	def __exit():
		MenBtn.btnTup[0].hide()
		MenBtn.btnTup[2].hide()
		

class Atom():
	def __new__(self):
		self.__load__()
		return self.atom

	def __load__():
		Atom.atom = Entity()
		Atom.atom.visible = False
		Atom.atom.model = sphere

class Bond():
	def __new__(self):
		self.__load__()
		return self.bond

	def __load__():
		Bond.bond = Entity()
		Bond.bond.visible = False
		Bond.bond.model = bond
