import bge
from building import *


class Civilisation():

    def __init__(self, id_nb):
        self.id_nb = id_nb
        self.buildings = []
        self.units = []
        self.placing_build = None
        self.gold = 250
        self.wood = 700
        self.crystal = 50
        self.constructing = False
        self.computer = False
        self.play_stage = 1

    def civ_init(self):
        scene = bge.logic.getCurrentScene()
        if self.id_nb == 0:
            self.create_building()
            self.buildings[0].color = [0, 1, 0, 1]
            self.buildings[0].state = 2
            for i in range(4):
                self.buildings[0].create_harvester()
        if self.id_nb == 1:
            self.computer = True
            scene.objects['SpawnB'].worldPosition[0] = 4
            scene.objects['SpawnB'].worldPosition[1] = -15
            self.create_building()
            self.buildings[0].color = [1, 0, 0, 1]
            self.buildings[0].state = 2
            for i in range(4):
                self.buildings[0].create_harvester()

    def civ_update(self):
        scene = bge.logic.getCurrentScene()
        for obj in self.units:
            obj.act()
        for obj in self.buildings:
            obj.build_update()
        if self.computer:
            for obj in self.units:
                if isinstance(obj, Harvester) and obj.state == 1:
                    temp_dist = 1000
                    temp_ressource = None
                    for res in bge.c.game.ressources:
                        if isinstance(res, Mine):
                            dist = self.calcDistance(res.worldPosition[0], res.worldPosition[1], obj.worldPosition[0], obj.worldPosition[1])
                            if dist < temp_dist:
                                temp_dist = dist
                                temp_ressource = res
                    obj.harv_mine = temp_ressource
                    obj.harv_dest = temp_ressource.worldPosition
                    for civ in bge.c.game.civilisations:
                        if civ == obj.owner:
                            obj.base_dest = civ.buildings[0].worldPosition
                    obj.destination = temp_ressource.worldPosition
                    obj.state = 4

            if self.play_stage == 1:
                if len(self.units) < 6 and self.gold >= 50:
                    self.buildings[0].create_harvester()
                if len(self.units) == 5:
                    self.play_stage = 2

            elif self.play_stage == 2 and self.gold >= 100:
                scene.objects['SpawnB'].worldPosition[0] = 2
                scene.objects['SpawnB'].worldPosition[1] = -22
                self.create_barrack(2)
                self.gold -= 100
                self.play_stage = 3

            elif self.play_stage == 3 and self.gold >= 70:
                total = 0
                for i in self.units:
                    if isinstance(i, Marksman):
                        total += 1
                if total < 2:
                    for build in self.buildings:
                        if isinstance(build, Barrack):
                            self.current_building = build
                    self.current_building.create_mman()
                    self.gold -= 70
                else:
                    self.play_stage = 4
    
            elif self.play_stage == 4:
                self.atk_list = []
                self.atk_target = None
                for obj in self.units:
                    if isinstance(obj, Marksman):
                        self.atk_list.append(obj)
                for civ in bge.c.game.civilisations:
                    if civ != self:
                        self.atk_target = civ.buildings[0]
                for obj in self.atk_list:
                    obj.target = self.atk_target
                    obj.state = 3
                self.play_stage = 5
                
            elif self.play_stage == 5:
                pass
                '''
                if self.gold > 150:
                    for build in self.buildings:
                        if isinstance(build, Barrack):
                            self.current_building = build
                    if isinstance(self.current_building, Barrack):
                        self.current_building.create_mman()
                        self.gold -= 70
                if not self.atk_list:
                    self.play_stage = 6
                for obj in self.atk_list:
                    for civ in bge.c.game.civilisations:
                        if self != civ:
                            for i in civ.units:
                                dist = obj.getDistanceTo(i)
                                if dist < obj.field:
                                    obj.target = i
                                    obj.destination = i.worldPosition
                                    obj.state = 3
                                    
            elif self.play_stage == 6:
                for obj in self.units:
                    if isinstance(obj, Marksman):
                        self.atk_list.append(obj)
                    if len(self.atk_list) < 8 and self.gold >= 70:
                        for build in self.buildings:
                            if isinstance(build, Barrack):
                                self.current_building = build
                    self.current_building.create_mman()'''

    def create_building(self):
        scene = bge.logic.getCurrentScene()
        new_building = Building(scene.addObject('Build', scene.objects['SpawnB']))
        new_building.build_init(self)
        self.buildings.append(new_building)
        self.placing_build = new_building

    def create_barrack(self, state):
        scene = bge.logic.getCurrentScene()
        new_building = Barrack(scene.addObject('Barrack', scene.objects['SpawnB']))
        new_building.build_init(self)
        if state == 2:
            new_building.state = 2
        self.buildings.append(new_building)
        self.placing_build = new_building

    def calcDistance(self, x1, y1, x2, y2):
        """param: self, self.worldPosition x, self.worldPosition y, self.destination x, self.destination y"""
        dx = abs(x2-x1)**2
        dy = abs(y2-y1)**2
        distance = math.sqrt(dx + dy)
        return distance