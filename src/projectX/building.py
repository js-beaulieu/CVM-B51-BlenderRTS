import bge
from unit import *


class Building(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.state = 1
        self.owner = None
        self.selected = False
        self.count = 1
        self.creating_unit = []
        self.way_point = False
        self.hp = 500
        self.stage_1 = "QG_stage_1"
        self.stage_2 = "QG_stage_2"
        self.id_nb = "Build_" + str(bge.c.frame)

    def build_init(self, owner, const):
        """param: self, Civilisation owner, Unit const"""
        self.const = const
        const.const_build = self
        self.owner = owner
        self.applyRotation([0, 0, 0.785398], False)

    def build_update(self):
        if self.state == 1:  # placing
            cont = bge.logic.getCurrentController()
            mouse_pos = cont.sensors["Mouse_Pos"]
            self.worldPosition.x = mouse_pos.hitPosition[0] 
            self.worldPosition.y = mouse_pos.hitPosition[1]+1
        elif self.state == 2:  # construction
            if self.hp != self.max_hp:
                self.hp += 1
        elif self.state == 3:  # create unit
            for obj in self.creating_unit:
                pass  # increment chrono for creating the unit
        elif self.state == 4:  # stand
            pass
        self.construct()
        if self.hp <= 0:
            self.die()

    def construct(self):
        if self.hp < self.max_hp / 3 * 2:
            self.children[self.stage_2].visible = False
        else:
            self.children[self.stage_2].visible = True
        if self.hp < self.max_hp / 3:
            self.children[self.stage_1].visible = False
        else:
            self.children[self.stage_1].visible = True

    def die(self):
        pass  # will be redeclared un sub_objects

    def place_unit(self):
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

        if self.way_point:
            self.count += 1
            new_unit = Harvester(scene.addObject('Unit', scene.objects['SpawnP']))
            new_unit.moving = True
            bge.c.game.moving_units.append(new_unit)
            new_unit.destination = scene.objects['Way_Circle'].worldPosition
            self.owner.gold -= 50
            self.owner.harvester += 1


class Headquarter(Building):

    def __init__(self, parent):
        super(Headquarter, self).__init__(parent)
        self.max_hp = 1200
        self.hp = 2
        self.stage_1 = "QG_stage_1"
        self.stage_2 = "QG_stage_2"

    def die(self):
        if self in bge.c.game.selected_units:
            bge.c.game.selected_units.remove(self)
        self.owner.buildings['headquarters'].remove(self)
        self.endObject()


class Barrack(Building):

    def __init__(self, parent):
        super(Barrack, self).__init__(parent)
        self.max_hp = 1000
        self.hp = 2
        self.stage_1 = "B_stage_1"
        self.stage_2 = "B_stage_2"
        self.id_nb = "Barrack_" + str(bge.c.frame)

    def die(self):
        if self in bge.c.game.selected_units:
            bge.c.game.selected_units.remove(self)
        self.owner.buildings['barracks'].remove(self)
        self.endObject()


class Tower(Building):

    def __init__(self, parent):
        super(Tower, self).__init__(parent)
        self.max_hp = 800
        self.hp = 1
        self.stage_1 = "T_stage_1"
        self.stage_2 = "T_stage_2"
        self.stage_3 = "T_stage_3"
        self.stage_4 = "T_stage_4"
        self.stage_5 = "T_stage_5"
        self.stage_6 = "T_stage_6"
        self.stage_7 = "T_stage_7"
        self.id_nb = "Tower_" + str(bge.c.frame)

    def construct(self):
        if self.hp < self.max_hp / 7 * 6.8:
            self.children[self.stage_7].visible = False
        else:
            self.children[self.stage_7].visible = True
        if self.hp < self.max_hp / 7 * 6:
            self.children[self.stage_6].visible = False
        else:
            self.children[self.stage_6].visible = True
        if self.hp < self.max_hp / 7 * 5:
            self.children[self.stage_5].visible = False
        else:
            self.children[self.stage_5].visible = True
        if self.hp < self.max_hp / 7 * 4:
            self.children[self.stage_4].visible = False
        else:
            self.children[self.stage_4].visible = True
        if self.hp < self.max_hp / 7 * 3:
            self.children[self.stage_3].visible = False
        else:
            self.children[self.stage_3].visible = True
        if self.hp < self.max_hp / 7 * 2:
            self.children[self.stage_2].visible = False
        else:
            self.children[self.stage_2].visible = True
        if self.hp < self.max_hp / 7:
            self.children[self.stage_1].visible = False
        else:
            self.children[self.stage_1].visible = True

    def die(self):
        if self in bge.c.game.selected_units:
            bge.c.game.selected_units.remove(self)
        self.owner.buildings['towers'].remove(self)
        self.endObject()
