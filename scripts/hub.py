from ursina import *

import threading
import math
import time

base = 0
butList = []
atomList = []
bondList = []

class Models():
  _sphere = "sphere.obj"
  _cube = "cube.obj"
  _erlFlask = "erlFlask.obj"
  _sphere = "buttons.obj"

class MenuBut():
  def __new__(self, selectNum):
    self.modTup = self.__ModLoad(selection)
    self.endSet(selection)
    return self.modTup
    
  def __ModLoad(num):
    MenBut.modTup = [0,0,0]
    
    MenBut.modTup[0] = Entity(model="logo.obj") 

class GInit():  
  def __init__(self):
    base = Ursina()
    self.__LoadSet()
    self.__LoadInit()
    
  def __LoadSet(self):
    mouse.enabled = false;
    window.title = "Beaker Bounce"
    
  def __LoadInit(self):
    #Vars for Bubble Pop
    self.__modThreads = []
    self.__frames = 0
    self.bondNum = 150
    self.bondCheck = self.bondNum
    self.menNum = 5
    self.cubNum = 1
    self.atomNum = 
      math.floor(((2/3)*self.bondNum))
    
    #Vars for LoadInit
    self.__erlFlask = Entity(parent=None)
    self.__bubbleOne = Entity(parent=None)
    self.__bubbleTwo = Entity(parent=None)
    self.__bubbleThree = Entity(parent=None)
    self.__loadingText = Text(parent=None)
    
    self.__erlFlask.model = "models/erlflask"
    self.__bubbleOne.model = "models/sphere"
    self.__bubbleTwo.model = "models/sphere"
    self.__bubbleThree.model = "models/sphere"
    self.__loadingText.text = "models/sphere"
    
    self.__erlFlask.color = color.rgb(1, 1, 1, 1)
    self.__bubbleOne.color = color.rgb(1, 1, 1, 1)
    self.__bubbleTwo.color = color.rgb(1, 1, 1, 1)
    self.__bubbleThree.color = color.rgb(1, 1, 1, 1)
    self.__loadingText.color = color.rgb(1, 1, 1, 1)
    
    self.__erlFlask.position = (0,0,0)
    self.__bubbleOne.position  = (0,0,0)
    self.__bubbleTwo.position = (0,0,0)
    self.__bubbleThree.position = (0,0,0)
    self.__loadingText.position = (0,-0.3,0)    
    
    self.__erlFlask.scale = 0.2
    self.__bubbleOne.scale = 0.19
    self.__bubbleTwo.scale = 0.15
    self.__bubbleThree.scale = 0.1
    self.__loadingText.scale = .07
    
    camera.position  = self.__erlFlask.position    
    camera.y = (self.__erlFlask.y + 20)
    
    self.__erlFlask.parent = scene        
    self.__bubbleOne.parent = scene        
    self.__bubbleTwo.parent = scene        
    self.__bubbleThree.parent = scene        
    self.__loadingText.parent = scene
    
    base.taskMgr.add(self.__BubblePop, "Pop")
    
def __BubblePop(self, task):
  if self.__frames % 10 == 0:
    if self.__frames % 7 == 0: 
      self.__bubbleOne.hide() 
    else self.__bubblesOne.show()
    
    if self.__frames % 4 == 0: 
      self.__bubbleThree.hide() 
    else self.__bubblesThree.show()
    
    if self.__frames % 3 == 0: 
      self.__bubbleTwo.hide() 
    else self.__bubblesTwo.show()
    
  if self.__frames >= self.bondCheck:
    for i in range(len(self.__modThreads)):
      self.__modThrreads[i][0].join()
      self.__modThrreads[i][1].join()
      self.__modThrreads[i][2].join()
    self.__LoadClose()
  else:
    threading.Thread(target = self.MThreadLoad())
    
    self.bondNum -= 1
    self.__frames += 1
  
  return task.count
        
  def MThreadLoad(self):
    lock = threading.Lock()
    
    with lock:
      self.__modThreads.append(
        (threading.Thread(target = self.EssentialModLoad()),
      threading.Thread(target = self.AtomLoad()),
      threading.Thread(target = self.BondLoad())))
      
      self.__modThreads[self.__frames][0].start()    
      self.__modThreads[self.__frames][0].start()    
      self.__modThreads[self.__frames][0].start()
        
  def EssentialModLoad(self):
    global butList
    
    if self.bondNum <= self.cubNum:
      self.__centrlCube = Entity()
      self.__centrlCube.model = "models/cube"
      
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
    taskMgr.remove("Pop")
    
    self.__erlFlask.detachNode()
    self.__bubbleOne.detachNode()
    self.__bubbleTwo.detachNode()
    self.__bubb;eThree.detachNode()
    self.__loadingText.detachNode()
    
    mod = 0
    for i in range(len(butList)):
      butList[i][0].parent = scene
      butList[i][1].parent = scene
      butList[i][2].parent = scene
      
      butList[i][0].z += mod
      butList[i][1].z += mod
      butList[i][2].z += mod
      
      butList[i][1].look_at(camera)
      
      butList[i][0].hide()
      butList[i][2].hide()
      
      mod += (15/self.menNum)
      
    butList[1][1].rotation_x = 100
    camera.look_at(butList[mat.floor(self.menNum/2][1])
        
    
    
    
 
    
