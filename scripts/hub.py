from objs import *

import threading
import math
import time

butList = []
atomList = []
bondList = []

class GInit():  
  def __init__(self):
    base = Ursina()
    self.__LoadSet()
    self.__LoadInit()
    
  def __LoadSet(self):
    mouse.enabled = False
    window.title = "Beaker Bounce"

  def __LoadInit(self):
    #Vars for Bubble Pop
    self.__modThreads = []
    self.__frames = 0
    self.bondNum = 150
    self.bondCheck = self.bondNum
    self.menNum = 5
    self.cubNum = 1
    self.menPos = 0
    self.atomNum = math.floor(((2/3)*self.bondNum))
    
    #Vars for LoadInit
    self.__erlFlask = Entity(parent=None)
    self.__bubbleOne = Entity(parent=None)
    self.__bubbleTwo = Entity(parent=None)
    self.__bubbleThree = Entity(parent=None)
    self.__loadingText = Text(parent=None)
    
    self.__loadingText.text = "Dummy"
    
    self.__erlFlask.model = erlFlask
    self.__bubbleOne.model = sphere
    self.__bubbleTwo.model = sphere
    self.__bubbleThree.model = sphere
    
    self.__erlFlask.color = color.rgb(1, 1, 1, 1)
    self.__bubbleOne.color = color.rgb(1, 1, 1, 1)
    self.__bubbleTwo.color = color.rgb(1, 1, 1, 1)
    self.__bubbleThree.color = color.rgb(1, 1, 1, 1)
    self.__loadingText.color = color.rgb(1, 1, 1, 1)
    
    
    #Bezier Curves Go Here!
    self.__erlFlask.position = (0,0,0)
    self.__bubbleOne.position  = (0,1,0)
    self.__bubbleTwo.position = (-0.25,1.25,0)
    self.__bubbleThree.position = (-0.5,1.5,0)
    self.__loadingText.position = (0,-1,0)    
    
    self.__erlFlask.scale = 0.2
    self.__bubbleOne.scale = 0.20
    self.__bubbleTwo.scale = 0.15
    self.__bubbleThree.scale = 0.1
    self.__loadingText.scale = .10
    
#    camera.position  = self.__erlFlask.y = -20    
#    camera.y = (self.__erlFlask.y + 20)
    
    self.__erlFlask.parent = scene        
    self.__bubbleOne.parent = scene        
    self.__bubbleTwo.parent = scene        
    self.__bubbleThree.parent = scene        
    self.__loadingText.parent = scene
    
    taskMgr.add(self.__BubblePop, "Pop")
    
  def __BubblePop(self, task):
    if self.__frames % 7 == 0: 
      self.__bubbleOne.hide() 
    else: 
      self.__bubbleOne.show()
      
    if self.__frames % 4 == 0: 
      self.__bubbleThree.hide() 
        
    else: 
      self.__bubbleThree.show()
      
    if self.__frames % 3 == 0: 
      self.__bubbleTwo.hide() 
    else: 
      self.__bubbleTwo.show()
      
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
      self.__modThreads.append(
        (threading.Thread(target = self.EssentialModLoad()),
      threading.Thread(target = self.AtomLoad()),
      threading.Thread(target = self.BondLoad())))
      
      self.__modThreads[self.__frames][0].start()    
      self.__modThreads[self.__frames][1].start()    
      self.__modThreads[self.__frames][2].start()
        
  def EssentialModLoad(self):
    global butList
    
    if self.bondNum <= self.cubNum:
      self.__centrlCube = Entity(parent=None)
      self.__centrlCube.model = cube
      self.__centrlCube.hide()
   
    if self.bondNum <= self.menNum:
      butList.append(MenBtn(self.bondNum, 
        self.menPos))
        
      self.menPos += (.15*self.menNum)
    
  def AtomLoad(self):
    global atomList

    if self.bondNum < self.atomNum:
      atomList.append(Atom()) 
      
  def BondLoad(self):
    global bondList
    bondList.append(Bond())      
    
  def __LoadClose(self):
    taskMgr.remove("Pop")
    
    self.__erlFlask.parent = None
    self.__bubbleOne.parent = None
    self.__bubbleTwo.parent = None
    self.__bubbleThree.parent = None
    self.__loadingText.parent = None
    
    for i in range(len(butList)):
      butList[i][0].visible = True
      butList[i][1].visible = True
      butList[i][2].visible = True
      butList[i][3].visible = True
      
      
    camera.look_at(
      butList[math.floor(self.menNum/2)][1])
        
    
    
    
 
    
