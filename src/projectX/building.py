import bge
import math
from unit import *


class Building(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.selected = False
        self.count = 1
        self.way_point = False
        self.id_nb = "Build_" + str(bge.c.count)
        bge.c.buildings.append(self)

    def createUnit(self):
        scene = bge.logic.getCurrentScene()
        spawnX = self.worldPosition[0]
        spawnY = self.worldPosition[1]
        spawnZ = self.worldPosition[2]
        if not self.way_point:
            if self.count == 1:
                spawnX -= 2
                spawnY += 2
            elif self.count == 2:
                spawnX -= 1
                spawnY += 2
            elif self.count == 3:
                spawnX += 0
                spawnY += 2
            elif self.count == 4:
                spawnX += 1
                spawnY += 2
            elif self.count == 5:
                spawnX += 2
                spawnY += 2
            elif self.count == 6:
                spawnX += 2
                spawnY += 1
            elif self.count == 7:
                spawnX += 2
                spawnY += 0
            elif self.count == 8:
                spawnX += 2
                spawnY -= 1
            elif self.count == 9:
                spawnX += 2
                spawnY -= 2
            elif self.count == 10:
                spawnX += 1
                spawnY -= 2
            elif self.count == 11:
                spawnX += 0
                spawnY -= 2
            elif self.count == 12:
                spawnX -= 1
                spawnY -= 2
            elif self.count == 13:
                spawnX -= 2
                spawnY -= 2
            elif self.count == 14:
                spawnX -= 2
                spawnY -= 1
            elif self.count == 15:
                spawnX -= 2
                spawnY += 0
            elif self.count == 16:
                spawnX -= 2
                spawnY += 1
                self.count = 0

            self.count += 1
            bge.c.count += 1
            scene.objects['SpawnP'].worldPosition = [spawnX, spawnY, spawnZ]
            new_unit = Unit(scene.addObject('Unit', scene.objects['SpawnP']))

        if self.way_point:
            self.count += 1
            bge.c.count += 1
            new_unit = Unit(scene.addObject('Unit', scene.objects['SpawnP']))
            new_unit.moving = True
            bge.c.movingUnits.append(new_unit)
            new_unit.destination = scene.objects['Way_Circle'].worldPosition

