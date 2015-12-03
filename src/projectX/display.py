import bge
import bgui
import bgui.bge_utils

COUNT_FONT = bge.logic.expandPath("//ui//abril.otf")
COUNT_COLOR = (255, 255, 255, 1)
COUNT_PT_SIZE = 12


class MainDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        # Initializing the side panel
        super().__init__(sys, data)
        self.current_panel = 0
        self.panel = bgui.Frame(self, border=1, size=[0.2, 1], pos=[0.8, 0])
        self.panel.colors = [(0, 0, 0, 0.4) for i in range(4)]

        # line 1 - Menu & Stats
        bgui.Image(self.panel, bge.logic.expandPath('//ui//Panel.png'), size=[1, 1], pos=[0, 0])
        btn_menu = bgui.ImageButton(self.panel, default_image=(bge.logic.expandPath('//ui//MenuNormal.png'), 0, 0, 1, 1),
                                    hover_image=(bge.logic.expandPath('//ui//MenuHover.png'), 0, 0, 1, 1),
                                    click_image=(bge.logic.expandPath('//ui//MenuClicked.png'), 0, 0, 1, 1),
                                    size=[0.42, 0.065], pos=[0.12, 0.01])
        btn_menu.on_click = self.menu_panel
        btn_stats = bgui.ImageButton(self.panel, default_image=(bge.logic.expandPath('//ui//StatsNormal.png'), 0, 0, 1, 1),
                                     hover_image=(bge.logic.expandPath('//ui//StatsHover.png'), 0, 0, 1, 1),
                                     click_image=(bge.logic.expandPath('//ui//StatsClicked.png'), 0, 0, 1, 1),
                                     size=[0.42, 0.065], pos=[0.56, 0.01])
        btn_stats.on_click = self.stats_panel

        # line 2 - XP
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResXP.png'), size=[0.85, 0.065], pos=[0.12, 0.08])
        self.label_xp = bgui.Label(self.panel, text=str(42),  # WRONG
                                   pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.31, 0.105])

        # line 3 - Gold + Wood
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResGold.png'), size=[0.42, 0.065], pos=[0.12, 0.15])
        self.label_gold = bgui.Label(self.panel, text=str(bge.c.game.civilisation.gold),
                                     pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.31, 0.175])
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResWood.png'), size=[0.42, 0.065], pos=[0.56, 0.15])
        self.label_wood = bgui.Label(self.panel, text=str(bge.c.game.civilisation.wood),  # WRONG
                                     pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.58, 0.175])

        # line 4 - Crystal + Petrol
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResCrystal.png'), size=[0.42, 0.065], pos=[0.12, 0.22])
        self.label_crystal = bgui.Label(self.panel, text=str(bge.c.game.civilisation.crystal),  # WRONG
                                        pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.31, 0.245])
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResPetrol.png'), size=[0.42, 0.065], pos=[0.56, 0.22])
        self.label_petrol = bgui.Label(self.panel, text=str(bge.c.game.civilisation.gold),  # WRONG
                                       pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.58, 0.245])

    def button_click(self, widget):
        bge.c.game.civilisation.buildings[0].create_unit()
        # self.goldLbl.text='Gold = ' + str(bge.c.game.civilisation.gold)

    def menu_panel(self, widget):
        pass

    def stats_panel(self, widget):
        bge.c.display.toggle_overlay(SubDisplay, None)

    def update(self):
        # TODO - update all label references in bge.c.game
        self.label_xp.text = str(42)  # line 34
        self.label_gold.text = str(bge.c.game.civilisations[0].gold)
        self.label_wood.text = str(bge.c.game.civilisations[0].wood)  # line 42
        self.label_crystal.text = str(bge.c.game.civilisations[0].crystal)  # line 47
        self.label_petrol.text = str(bge.c.game.civilisation.gold)  # line 50
        if bge.c.display_update:
            if bge.c.ui_panel != self.current_panel:
                if bge.c.ui_panel == 1:
                    self.remove_all()
                    bge.c.display.add_overlay(buildDisplay, None)
                    self.current_panel = 1
                elif bge.c.ui_panel == 2:
                    self.remove_all()
                    bge.c.display.add_overlay(scavengerDisplay, None)
                    self.current_panel = 2
                elif bge.c.ui_panel == 3:
                    self.remove_all()
                    bge.c.display.add_overlay(barrackDisplay, None)
                    self.current_panel = 3
                elif bge.c.ui_panel == 4:
                    self.remove_all()
                    self.current_panel = 0
            bge.c.display_update = False

    def remove_all(self):
        if self.current_panel == 1:
            bge.c.display.remove_overlay(buildDisplay)
        elif self.current_panel == 2:
            bge.c.display.remove_overlay(scavengerDisplay)
        elif self.current_panel == 3:
            bge.c.display.remove_overlay(barrackDisplay)


class SubDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.statsFrame = bgui.Frame(self, border=1, size=[0.6, 0.5], pos=[0.2, 0.4])
        self.statsFrame.colors = [(0, 0, 0, 0.4) for i in range(4)]
        self.goldLbl = bgui.Label(self.statsFrame, text="Gold = " + str(bge.c.game.civilisation.gold), pos=[0.2, 0.8])
        self.closeBtn = bgui.FrameButton(self.statsFrame, text='close', size=[0.1, 0.15], pos=[0.23, 0.08])
        self.closeBtn.label.pt_size = 16

    def update(self):
        self.goldLbl.text = 'Gold = ' + str(bge.c.game.civilisation.gold)


class buildDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.buildFrame = bgui.Frame(self, border=0, size=[0.2, 0.4], pos=[0.81875, 0.32])
        self.buildFrame.colors = [(0.0, 0.0, 0.0, 0.0) for i in range(4)]
        self.btn_create = bgui.FrameButton(self.buildFrame, text='Unit 1', size=[0.2, 0.15], pos=[0.025, 0.8])
        self.btn_create.label.pt_size = 16
        self.btn_create.on_click = self.create_harvester

    def update(self):
        pass

    def create_harvester(self, widget):
        bge.c.game.selected_units[0].owner.create_harvester()
        bge.c.ui_panel = 1
        bge.c.button_clicked = 10


class scavengerDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.scavFrame = bgui.Frame(self, border=0, size=[0.2, 0.4], pos=[0.81875, 0.32])
        self.scavFrame.colors = [(0.0, 0.0, 0.0, 0.0) for i in range(4)]
        self.btn_headquarter = bgui.FrameButton(self.scavFrame, text='main', size=[0.2, 0.15], pos=[0.025, 0.8])
        self.btn_headquarter.label.pt_size = 16
        self.btn_headquarter.on_click = self.headquarter
        self.btn_barrack = bgui.FrameButton(self.scavFrame, text='barrack', size=[0.2, 0.15], pos=[0.25, 0.8])
        self.btn_barrack.label.pt_size = 16
        self.btn_barrack.on_click = self.barrack
        self.btn_tower = bgui.FrameButton(self.scavFrame, text='tower', size=[0.2, 0.15], pos=[0.475, 0.8])
        self.btn_tower.label.pt_size = 16
        self.btn_tower.on_click = self.tower

    def update(self):
        pass

    def headquarter(self, widget):
        bge.c.game.selected_units[0].owner.create_headquarter()
        bge.c.button_clicked = 10
        bge.c.ui_panel = 2

    def barrack(self, widget):
        bge.c.game.selected_units[0].owner.create_barrack(1)
        bge.c.button_clicked = 10
        bge.c.ui_panel = 2

    def tower(self, widget):
        bge.c.game.selected_units[0].owner.create_tower(1)
        bge.c.button_clicked = 10
        bge.c.ui_panel = 2


class barrackDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.barFrame = bgui.Frame(self, border=0, size=[0.2, 0.4], pos=[0.81875, 0.32])
        self.barFrame.colors = [(0.0, 0.0, 0.0, 0.0) for i in range(4)]
        self.btn_create_mman = bgui.FrameButton(self.barFrame, text='Marksman', size=[0.2, 0.15], pos=[0.025, 0.8])
        self.btn_create_mman.label.pt_size = 16
        self.btn_create_mman.on_click = self.create_marksman
        self.btn_create_shocker = bgui.FrameButton(self.barFrame, text='Shocker', size=[0.2, 0.15], pos=[0.25, 0.8])
        self.btn_create_shocker.label.pt_size = 16
        self.btn_create_shocker.on_click = self.create_shocker

    def update(self):
        pass

    def create_marksman(self, widget):
        bge.c.game.selected_units[0].owner.create_marksman()
        bge.c.ui_panel = 3
        bge.c.button_clicked = 10

    def create_shocker(self, widget):
        bge.c.game.selected_units[0].owner.create_shocker()
        bge.c.ui_panel = 3
        bge.c.button_clicked = 10
