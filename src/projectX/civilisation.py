import bge
from building import *
from unit import *


class Civilisation():

    def __init__(self, id_nb):
        self.id_nb = id_nb
        self.selected_unit = None
        self.buildings = {
            'headquarters': [],
            'barracks': [],
            'towers': []
        }
        self.units = {
            'harvesters': [],
            'marksmans': [],
            'shockers': []
        }
        self.placing_build = None
        self.gold = 11250
        self.wood = 11100
        self.crystal = 15
        self.computer = False
        self.play_stage = 0
        self.atk_count = 0
        self.atk_list = []

    def civ_init(self):
        scene = bge.logic.getCurrentScene()
        hq_loc = [[1, -7, 1], [42, -7, 1]]
        scene.objects['SpawnB'].worldPosition = hq_loc[self.id_nb]

        if self.id_nb == 0:
            scene.objects['SpawnB'].worldPosition = [1, -7, 0.4]
            #self.computer = True
            new_building = Headquarter(scene.addObject('Build', scene.objects['SpawnB']))
            new_building.owner = self
            new_building.color = [0, 1, 0, 1]
            new_building.state = 4
            new_building.hp = new_building.max_hp
            new_building.applyRotation([0, 0, 0.785398], False)
            self.buildings["headquarters"].append(new_building)
            # for i in range(4):
            # self.selected_unit = new_building
            # self.create_harvester()

        if self.id_nb == 1:
            scene.objects['SpawnB'].worldPosition = [42, -7, 0.4]
            #self.computer = True
            new_building = Headquarter(scene.addObject('Build', scene.objects['SpawnB']))
            new_building.owner = self
            new_building.color = [1, 0, 0, 1]
            new_building.state = 4
            new_building.hp = new_building.max_hp
            new_building.applyRotation([0, 0, 0.785398], False)
            self.buildings["headquarters"].append(new_building)
            for i in range(4):
                self.selected_unit = new_building
                self.create_harvester()

    def civ_update(self):
        for i in self.units:
            for obj in self.units[i]:
                obj.act()
        for i in self.buildings:
            for obj in self.buildings[i]:
                obj.build_update()
        if self.computer:
            self.play()

    def play(self):
        """Ai"""

        def play_stage_init():
            """sends standing harvesters harvesting closest ressource for a ratio trees/mines
            and determinate the actual play_stage, called every second frame"""

            def find_close_res(key):
                """param: key of ressouces lib"""
                temp_dist = 1000
                temp_ressource = None
                for res in bge.c.game.ressources[key]:
                    dist = self.calcDistance(obj.worldPosition[0], obj.worldPosition[1], res.worldPosition[0], res.worldPosition[1])
                    if dist < temp_dist:
                        temp_dist = dist
                        temp_ressource = res
                return temp_ressource

            def get_ratio():
                mine_count = 1
                tree_count = 1
                for harv in self.units["harvesters"]:
                    if isinstance(harv.harv_mine, Mine):
                        mine_count += 1
                    if isinstance(harv.harv_mine, Tree):
                        tree_count += 1
                return tree_count / mine_count

            # MAIN INIT #
            for obj in self.units["harvesters"]:
                if obj.state == 1:
                    if get_ratio() > 0.5:
                        obj.harv_mine = find_close_res("mines")
                    else:
                        obj.harv_mine = find_close_res("trees")
                    obj.harv_dest = obj.harv_mine.worldPosition
                    obj.destination = obj.harv_mine.worldPosition
                    for civ in bge.c.game.civilisations:
                        if civ == obj.owner:
                            obj.base_dest = civ.buildings["headquarters"][0].worldPosition
                    obj.state = 4
            if len(self.units["harvesters"]) < 6:
                self.play_stage = 1
            elif len(self.buildings["barracks"]) == 0:
                self.play_stage = 2
            elif len(self.units["marksmans"]) < 4:
                self.play_stage = 3
            elif len(self.units["shockers"]) < 2:
                self.play_stage = 4

        def play_stage_1():
            """create harvesters till total == 6"""
            self.selected_unit = self.buildings["headquarters"][0]
            self.create_harvester()
            self.play_stage = 0

        def play_stage_2():
            """create first barrack"""
            scene = bge.logic.getCurrentScene()
            self.selected_unit = self.units["harvesters"][0]
            scene.objects['SpawnB'].worldPosition[0] = self.buildings["headquarters"][0].worldPosition[0] + 7
            scene.objects['SpawnB'].worldPosition[1] = self.buildings["headquarters"][0].worldPosition[1] - 7
            self.create_barrack(2)
            self.play_stage = 0

        def play_stage_3():
            """create marksmans till total == 4"""

            def attack_stage_1():
                """attack with 4 marksmans"""
                self.atk_list = []
                self.atk_target = None
                for obj in self.units['marksmans']:
                    self.atk_list.append(obj)
                for civ in bge.c.game.civilisations:
                    if civ != self:
                        self.atk_target = civ.buildings["headquarters"][0]
                for obj in self.atk_list:
                    obj.target = self.atk_target
                    obj.state = 3
                    obj.attacking = True
                self.atk_count += 1
                self.play_stage = 0

            # MAIN PLAY_STAGE_3 #
            self.selected_unit = self.buildings["barracks"][0]
            self.create_marksman()
            self.play_stage = 0
            if len(self.units["marksmans"]) == 4 and self.atk_count == 0:
                attack_stage_1()

        def play_stage_4():
            """create shockers till total == 2"""

            def attack_stage_2():
                """attack with 4 marksmans and 2 shockers"""
                self.atk_list = []
                self.atk_target = None
                for obj in self.units["marksmans"]:
                    self.atk_list.append(obj)
                for obj in self.units["shockers"]:
                    self.atk_list.append(obj)
                for civ in bge.c.game.civilisations:
                    if civ != self:
                        self.atk_target = civ.buildings["headquarters"][0]
                for obj in self.atk_list:
                    obj.target = self.atk_target
                    obj.state = 3
                    obj.attacking = True
                #self.atk_count += 1
                self.play_stage = 0

            # MAIN PLAY_STAGE_4 #
            self.selected_unit = self.buildings["barracks"][0]
            self.create_shocker()
            self.play_stage = 0
            if len(self.units["shockers"]) == 2 and self.atk_count == 1:
                attack_stage_2()

        # MAIN SELECTION #
        if self.play_stage == 0:
            play_stage_init()
        elif self.play_stage == 1:
            play_stage_1()
        elif self.play_stage == 2:
            play_stage_2()
        elif self.play_stage == 3:
            play_stage_3()
        elif self.play_stage == 4:
            play_stage_4()

        if self.atk_list:
            for obj in self.atk_list:
                obj.state = 3
                if not obj.target:
                    obj.target = self.atk_target

    def create_headquarter(self):
        if self.calcPrice(300, 500, 0):
            scene = bge.logic.getCurrentScene()
            new_building = Headquarter(scene.addObject('Build', scene.objects['SpawnB']))
            new_building.build_init(self, self.selected_unit)
            self.buildings["headquarters"].append(new_building)
            self.placing_build = new_building
            return True
        else:
            return False

    def create_barrack(self, state):
        if self.calcPrice(120, 250, 0):
            scene = bge.logic.getCurrentScene()
            new_building = Barrack(scene.addObject('Barrack', scene.objects['SpawnB']))
            new_building.build_init(self, self.selected_unit)
            new_building.state = state
            self.buildings["barracks"].append(new_building)
            self.placing_build = new_building
            return True
        else:
            return False

    def create_tower(self, state):
        if self.calcPrice(100, 180, 0):
            scene = bge.logic.getCurrentScene()
            new_building = Tower(scene.addObject('Tower', scene.objects['SpawnB']))
            new_building.build_init(self, self.selected_unit)
            new_building.state = state
            self.buildings["towers"].append(new_building)
            self.placing_build = new_building
            return True
        else:
            return False

    def create_harvester(self):  # for some weird reasons, cant move this into Headquarter class5
        if self.calcPrice(50, 20, 0):
            scene = bge.logic.getCurrentScene()
            self.selected_unit.place_unit()
            new_unit = Harvester(scene.addObject('Unit', scene.objects['SpawnP']))
            new_unit.unit_init(self)
            self.units["harvesters"].append(new_unit)
            return True
        else:
            return False

    def create_marksman(self):
        if self.calcPrice(75, 35, 0):
            scene = bge.logic.getCurrentScene()
            self.selected_unit.place_unit()
            new_unit = Marksman(scene.addObject('Marksman', scene.objects['SpawnP']))
            new_unit.unit_init(self)
            self.units["marksmans"].append(new_unit)
            return True
        else:
            return False

    def create_shocker(self):
        if self.calcPrice(100, 60, 1):
            scene = bge.logic.getCurrentScene()
            self.selected_unit.place_unit()
            new_unit = Shocker(scene.addObject('Shocker', scene.objects['SpawnP']))
            new_unit.unit_init(self)
            self.units["shockers"].append(new_unit)
            return True
        else:
            return False

    def calcDistance(self, x1, y1, x2, y2):
        """param: self, self.worldPosition x, self.worldPosition y, self.destination x, self.destination y"""
        dx = abs(x2-x1)**2
        dy = abs(y2-y1)**2
        distance = math.sqrt(dx + dy)
        return distance

    def calcPrice(self, G, W, C):
        if self.gold >= G and self.wood >= W and self.crystal >= C:
            self.gold -= G
            self.wood -= W
            self.crystal -= C
            return True
        else:
            return False  # TODO insuficient vespeen gaz :)

