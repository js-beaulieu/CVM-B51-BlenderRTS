import bge
import math


class Building(bge.types.KX_GameObject):

    def __init__(self, parent):
    	self.selected = false
    	self.countSpawnP = 0

   	def createUnit(self):
   		spawnX = self.worldLocation[0] 
   		spawnY = self.worldLocation[1]
   		spawnZ = self.worldLocation[2]

   		if self.count == 1:
   			spawnX -= 2
   			spawnY += 2
   		if self.count == 2:
   			spawnX -= 1
   			spawnY += 2
   		if self.count == 3:
   			spawnX += 0
   			spawnY += 2
   		if self.count == 4:
   			spawnX += 1
   			spawnY += 1
   		'''if self.count == 5:
   			spawnX += 2
   			spawnY += 0
   		if self.count == 6:
   			spawnX += 2
   			spawnY += 1
   		if self.count == 7:
   			spawnX += 1
   			spawnY += 1
   		if self.count == 8:
   			spawnX += 1
   			spawnY += 1
   		if self.count == 9:
   			spawnX += 1
   			spawnY += 1
   		if self.count == 10:
   			spawnX += 1
   			spawnY += 1
   		if self.count == 11:
   			spawnX += 1
   			spawnY += 1
   		if self.count == 12:
   			spawnX += 1
   			spawnY += 1'''

   		scene = bge.logic.getCurrentScene()
   		scene.objects['SpawnP'].worldLocation = [spawnX, spawnY, spawnZ]
   		scene.addObject('Unit', scene.objects['SpawnP'])
   		self.count += 1

def subBuildcont):
    """used to subclass the object when created, attached to a... sensor, i know, sorry
    will find a python way later ^^"""
    owner = bge.logic.getCurrentController().owner
    Building(owner)