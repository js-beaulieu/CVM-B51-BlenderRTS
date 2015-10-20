import random
import math
import bge

from unit import *

class Model():
	def __init__(self, map):
		self.mapNb = mapNb
		self.units = []
		self.idNb = 0


	def update(self):
		self.move()

	def createUnit(self):
		new_unit = Unit(idNb)
		self.units.append(new_unit)
		self.idNb += 1

	def move(self):
		for i in self.units:
			if self.units[i].state == 1:
				self.units[i].move()

	def selectTargets(self):
		pass

	def mouse():
    obj=bge.logic.getCurrentController()
    
    
    if obj.sensors["Mouse"].positive and obj.sensors["Mouse1"].positive:
        print(obj.sensors)
        print("OK",obj.sensors["Mouse"].hitPosition,obj.sensors["Mouse"].hitObject)



