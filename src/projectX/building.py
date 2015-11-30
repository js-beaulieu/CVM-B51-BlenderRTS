import bge
import math
from unit import *


class Building(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.state = 1
        self.construction = 0
        self.selected = False
        self.count = 1
        self.creating_unit = []
        self.way_point = False
        self.hp = 2000
        self.id_nb = "Build_" + str(bge.c.frame)

    def build_init(self, owner):
        self.owner = owner
        self.applyRotation([0, 0, 0.785398], False)

    def build_update(self):
        if self.state == 1:  # placing
            cont = bge.logic.getCurrentController()
            mouse_pos = cont.sensors["Mouse_Pos"]
            self.worldPosition.x = mouse_pos.hitPosition[0]
            self.worldPosition.y = mouse_pos.hitPosition[1]
        elif self.state == 2:  # construction
            if self.construction == 0:
                self.owner.placing_build = None
            self.construction += 1
            if self.construction == 180:
                self.children['stage 1'].visible = True
            if self.construction == 250:
                self.children['stage 2'].visible = True
                self.state = 4
        elif self.state == 3:  # create unit
            for obj in creating_unit:
                pass  # increment chrono for creating the unit
        elif self.state == 4:  # stand
            pass  # building with attack will do on sight
        if self.hp <= 0:
            self.owner.buildings.remove(self)
            self.endObject()

    def create_harvester(self):
        if self.owner.gold >= 50:
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
                scene.objects['SpawnP'].worldPosition = [spawnX, spawnY, spawnZ]
                new_unit = Harvester(scene.addObject('Unit', scene.objects['SpawnP']))
                new_unit.unit_init(self.owner)
                self.owner.units.append(new_unit)
                self.owner.gold -= 50

            if self.way_point:
                self.count += 1
                new_unit = Harvester(scene.addObject('Unit', scene.objects['SpawnP']))
                new_unit.moving = True
                bge.c.game.moving_units.append(new_unit)
                new_unit.destination = scene.objects['Way_Circle'].worldPosition
                self.owner.gold -= 50


class Barrack(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.state = 1
        self.construction = 0
        self.selected = False
        self.count = 1
        self.creating_unit = []
        self.way_point = False
        self.hp = 1500
        self.id_nb = "Barrack_" + str(bge.c.frame)

    def build_init(self, owner):
        self.owner = owner
        self.applyRotation([0, 0, 0.785398], False)

    def build_update(self):
        if self.state == 1:  # placing
            cont = bge.logic.getCurrentController()
            mouse_pos = cont.sensors["Mouse_Pos"]
            self.worldPosition.x = mouse_pos.hitPosition[0]
            self.worldPosition.y = mouse_pos.hitPosition[1]
        if self.state == 2:  # construction
            if self.construction == 0:
                self.owner.placing_build = None
            self.construction += 1
            if self.construction == 180:
                self.children['B_stage_1'].visible = True
            if self.construction == 250:
                self.children['B_stage_2'].visible = True
                self.state = 4
        if self.state == 3:  # create unit
            for obj in creating_unit:
                pass  # increment chrono for creating the unit
        if self.state == 4:  # stand  
            pass  # building with attack will do on sight

    def create_mman(self):
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
            scene.objects['SpawnP'].worldPosition = [spawnX, spawnY, spawnZ]
            new_unit = Marksman(scene.addObject('Marksman', scene.objects['SpawnP']))
            new_unit.unit_init(self.owner)
            self.owner.units.append(new_unit)

    def create_shocker(self):
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
            scene.objects['SpawnP'].worldPosition = [spawnX, spawnY, spawnZ]
            new_unit = Shocker(scene.addObject('Shocker', scene.objects['SpawnP']))
            new_unit.unit_init(self.owner)
            self.owner.units.append(new_unit)