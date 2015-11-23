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
        self.stats = False
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
        self.label_wood = bgui.Label(self.panel, text=str(bge.c.game.civilisation.gold),  # WRONG
                                     pt_size=COUNT_PT_SIZE, font=COUNT_FONT, color=COUNT_COLOR, pos=[0.58, 0.175])

        # line 4 - Crystal + Petrol
        bgui.Image(self.panel, bge.logic.expandPath('//ui//ResCrystal.png'), size=[0.42, 0.065], pos=[0.12, 0.22])
        self.label_crystal = bgui.Label(self.panel, text=str(bge.c.game.civilisation.gold),  # WRONG
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
        self.label_gold.text = str(bge.c.game.civilisation.gold)
        self.label_wood.text = str(bge.c.game.civilisation.gold)  # line 42
        self.label_crystal.text = str(bge.c.game.civilisation.gold)  # line 47
        self.label_petrol.text = str(bge.c.game.civilisation.gold)  # line 50


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
