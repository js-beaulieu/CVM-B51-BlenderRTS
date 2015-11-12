import bge
import bgui
import bgui.bge_utils


class Display(bgui.bge_utils.Layout):

    def __init__(self, sys, data):
        super().__init__(sys, data)
        self.stats = False

        self.frame = bgui.Frame(self, border=1, size=[1, 0.2], pos=[0, 0])
        self.frame.colors = [(0, 0, 0, 0.4) for i in range(4)]

        # self.constBtn = bgui.ImageButton(self.frame, default_image=('build.png', 1, 1, 1, 1), hover_image=('buildH.png', 1, 1, 1, 1),
        # click_image=('buildH.png', 1, 1, 1, 1), size=[0.1, 0.7], pos=[0.01, 0.05])

        self.background = bgui.Image(self.frame, 'wood.jpg', size=[1, 1], pos=[0, 0])

        self.uselessLbl = bgui.Label(self.frame, text='createUnit', pt_size=16, pos=[0.01, 0.25])

        self.crtUnitsBtn = bgui.FrameButton(self.frame, text='createUnit', size=[0.1, 0.15], pos=[0.01, 0.08])
        self.constrBtn = bgui.FrameButton(self.frame, text='build', size=[0.1, 0.15], pos=[0.12, 0.08])
        self.statsBtn = bgui.FrameButton(self.frame, text='stats', size=[0.1, 0.15], pos=[0.23, 0.08])

        self.crtUnitsBtn.label.pt_size = 16
        self.constrBtn.label.pt_size = 16
        self.statsBtn.label.pt_size = 16 

        self.crtUnitsBtn.on_click = self.button_click
        self.statsBtn.on_click = self.stats_panel

    def button_click(self, widget):
        bge.c.buildings[0].createUnit()
        self.uselessLbl.text = 'Yippie! You clicked the button! ^_^'

    def stats_panel(self, widget):
        self.statsFrame = bgui.Frame(self, border=1, size=[0.6, 0.5], pos=[0.2, 0.4])
        self.statsFrame.colors = [(0, 0, 0, 0.4) for i in range(4)]
        self.statsLbl = bgui.Label(self.statsFrame, text="Gold = "+ str(bge.c.gold), pos=[0.2, 0.8])   # + str(bge.c.gold)

        """if not self.stats:
            self.stats = True
        elif self.stats:
            self.stats = False"""


 