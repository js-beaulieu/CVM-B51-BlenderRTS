import bge
import bgui
import bgui.bge_utils


class MainDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.stats = False

        self.frame = bgui.Frame(self, border=1, size=[1, 0.2], pos=[0, 0])
        self.frame.colors = [(0, 0, 0, 0.4) for i in range(4)]

        # self.constBtn = bgui.ImageButton(self.frame, default_image=('build.png', 1, 1, 1, 1), hover_image=('buildH.png', 1, 1, 1, 1),
        # click_image=('buildH.png', 1, 1, 1, 1), size=[0.1, 0.7], pos=[0.01, 0.05])

        self.background = bgui.Image(self.frame, 'wood.jpg', size=[1, 1], pos=[0, 0])

        self.goldLbl = bgui.Label(self.frame, text='Gold = ' + str(bge.c.game.civilisation.gold),
        pt_size=24, color=(0,0,0,1), pos=[0.8, 0.8])

        self.crtUnitsBtn = bgui.FrameButton(self.frame, text='createUnit', size=[0.1, 0.15], pos=[0.01, 0.08])
        self.constrBtn = bgui.FrameButton(self.frame, text='build', size=[0.1, 0.15], pos=[0.12, 0.08])
        self.statsBtn = bgui.FrameButton(self.frame, text='stats', size=[0.1, 0.15], pos=[0.23, 0.08])

        self.crtUnitsBtn.label.pt_size = 16
        self.constrBtn.label.pt_size = 16
        self.statsBtn.label.pt_size = 16

        self.crtUnitsBtn.on_click = self.button_click
        self.statsBtn.on_click = self.stats_panel

    def button_click(self, widget):
        bge.c.game.civilisation.buildings[0].create_unit()
        # self.goldLbl.text='Gold = ' + str(bge.c.game.civilisation.gold) 


    def stats_panel(self, widget):
        bge.c.display.toggle_overlay(SubDisplay, None)



    def update(self):
        self.goldLbl.text='Gold = ' + str(bge.c.game.civilisation.gold) 



class SubDisplay(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)

        self.statsFrame = bgui.Frame(self, border=1, size=[0.6, 0.5], pos=[0.2, 0.4])
        self.statsFrame.colors = [(0, 0, 0, 0.4) for i in range(4)]
        self.goldLbl = bgui.Label(self.statsFrame, text="Gold = " + str(bge.c.game.civilisation.gold), pos=[0.2, 0.8])
        self.closeBtn = bgui.FrameButton(self.statsFrame, text='close', size=[0.1, 0.15], pos=[0.23, 0.08])
        self.closeBtn.label.pt_size = 16

    def update(self):
        self.goldLbl.text='Gold = ' + str(bge.c.game.civilisation.gold) 




 