from Ursina import *

obj = "models/sphere.obj"
obj = "models/erlFlask.obj"
obj = "models/sphere.obj
obj = models/sphere.obj

class MenBut():
  def __new__(self, selectNum):
    self.modTup = self.__ModLoad(selectNum)
    self.endSet(selectNum)
    return self.modTup
    
  def __ModLoad(num):
    MenBut.modTup = [0,0,0]
    
    MenButmodTup[0] = Entity()

