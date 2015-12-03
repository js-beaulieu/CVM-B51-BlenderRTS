from bge import logic, events, render
from unit import *
from building import *
from ressource import *

ZOOM_STEPS = 5
ZOOM_MIN = 10
ZOOM_MAX = 35
SCROLL_SPEED = 0.25


class Mouse(object):

    def __init__(self, parent):
        self.parent = parent
        self.events_populate()

    def events_populate(self):
        self.key = {
            "LeftClick": logic.mouse.events[logic.KX_MOUSE_BUT_LEFT],
            "RightClick": logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT],
            "MiddleClick": logic.mouse.events[logic.KX_MOUSE_BUT_MIDDLE],
            "ScrollDown": logic.mouse.events[events.WHEELDOWNMOUSE],
            "ScrollUp": logic.mouse.events[events.WHEELUPMOUSE]
        }

    def select(self, cont):
        """ main mouse fonction, will be extended as we add mouse controls
        It is called from bge.c (controller) if mouse.events = True"""
        scene = logic.getCurrentScene()
        cam = scene.active_camera
        mouse_pos = cont.sensors["Mouse_Pos"]

        self.events_populate()
        self.edge_scroll(scene, cam, mouse_pos)
        self.left_click(scene, mouse_pos)
        self.right_click(mouse_pos)
        self.scroll_wheel(scene, cam, mouse_pos)

    ############################################################################
    # Mouse movement                                                           #
    ############################################################################
    def edge_scroll(self, scene, cam, mouse_pos):
        """Detect if mouse is close to the screen edge
        and if so, move the camera."""
        if mouse_pos.position[0] <= 5:
            self.move_cam(scene, cam, 1)
            if mouse_pos.position[0] < 0:
                render.setMousePosition(2, mouse_pos.position[1])
        elif mouse_pos.position[1] <= 5:
            self.move_cam(scene, cam, 2)
            if mouse_pos.position[1] < 0:
                render.setMousePosition(mouse_pos.position[0], 2)
        elif mouse_pos.position[0] >= render.getWindowWidth() - 5:
            self.move_cam(scene, cam, 3)
            if mouse_pos.position[0] > render.getWindowWidth():
                render.setMousePosition(render.getWindowWidth(), mouse_pos.position[1] - 2)
        elif mouse_pos.position[1] >= render.getWindowHeight() - 5:
            self.move_cam(scene, cam, 4)
            if mouse_pos.position[1] > render.getWindowHeight():
                render.setMousePosition(mouse_pos.position[0], render.getWindowHeight() - 2)

    def move_cam(self, scene, cam, side):
        """Moves the camera in a given direction."""
        camX = cam.position[0]
        camY = cam.position[1]
        camZ = cam.position[2]

        if side == 1:
            cam.position = [camX - SCROLL_SPEED, camY, camZ]
        elif side == 2:
            cam.position = [camX, camY + SCROLL_SPEED, camZ]
        elif side == 3:
            cam.position = [camX + SCROLL_SPEED, camY, camZ]
        elif side == 4:
            cam.position = [camX, camY - SCROLL_SPEED, camZ]

    ############################################################################
    # Left click                                                               #
    ############################################################################
    def left_click(self, scene, mouse_pos):
        """Handling left click actions."""

        # Local helper functions
        def draw_square():
            render.drawLine((self.x1, self.y1, z), (self.x2, self.y1, z), (1, 0, 0))
            render.drawLine((self.x1, self.y1, z), (self.x1, self.y2, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x2, self.y1, z), (1, 0, 0))
            render.drawLine((self.x2, self.y2, z), (self.x1, self.y2, z), (1, 0, 0))

        def unit_select(scene, mouse_pos):
            jin = mouse_pos.hitObject
            for civ in bge.c.game.civilisations:
                for i in civ.units:
                    for obj in civ.units[i]:
                        x = obj.worldPosition[0]
                        y = obj.worldPosition[1]

                        if x > self.x1 and y > self.y1 and x < self.x2 and y < self.y2:    # si a linterieur du rectangle
                            obj.owner.selected_unit = obj
                            self.parent.game.selected_units.append(obj)
                            obj.selected = True
                        if obj.owner.selected_unit:

                            if isinstance(obj.owner.selected_unit, Harvester):
                                bge.c.ui_panel = 2
                                bge.c.display_update = True

            if isinstance(jin, Building):
                jin.owner.selected_unit = jin

                if isinstance(jin, Headquarter):
                    self.parent.game.selected_units.append(jin)
                    bge.c.ui_panel = 1
                    bge.c.display_update = True

                elif isinstance(jin, Barrack):
                    self.parent.game.selected_units.append(jin)
                    bge.c.ui_panel = 3
                    bge.c.display_update = True

            elif isinstance(jin, Unit):
                jin.owner.selected_unit = jin

                if isinstance(jin, Harvester):
                    self.parent.game.selected_units.append(jin)
                    jin.selected = True
                    bge.c.ui_panel = 2
                    bge.c.display_update = True

                elif isinstance(jin, Marksman):
                    self.parent.game.selected_units.append(jin)
                    jin.selected = True
                    bge.c.ui_panel = 4
                    bge.c.display_update = True

                elif isinstance(jin, Shocker):
                    self.parent.game.selected_units.append(jin)
                    jin.selected = True
                    bge.c.ui_panel = 4
                    bge.c.display_update = True

        # Handling the click
        if self.key["LeftClick"] == logic.KX_INPUT_JUST_ACTIVATED:
            jin = mouse_pos.hitObject
            if isinstance(jin, Building):
                """construct building"""
                if jin.owner.placing_build and bge.c.button_clicked == 0:
                    print("ok")
                    posX = jin.worldPosition[0] - 2
                    posY = jin.worldPosition[1] - 2
                    posZ = jin.worldPosition[2]
                    for obj in bge.c.game.selected_units:
                        if isinstance(obj, Harvester):
                            obj.destination = [posX, posY, posZ]
                            obj.state = 5
                    jin.state = 2
                    jin.owner.placing_build = None

            if not isinstance(jin, Building) and not isinstance(jin, Unit) and bge.c.button_clicked == 0:
                """remove ui"""
                bge.c.ui_panel = 4
                bge.c.display_update = True

            if bge.c.button_clicked == 0:
                for obj in bge.c.game.selected_units:
                    obj.selected = False
                bge.c.game.selected_units = []
            self.x1 = mouse_pos.hitPosition[0]
            self.y1 = mouse_pos.hitPosition[1]

        if self.key["LeftClick"] == logic.KX_INPUT_ACTIVE:
            self.x2 = mouse_pos.hitPosition[0]
            self.y2 = mouse_pos.hitPosition[1]
            z = mouse_pos.hitPosition[2] + 0.1
            draw_square()

        if self.key["LeftClick"] == logic.KX_INPUT_JUST_RELEASED:
            if self.x1 > self.x2:
                self.x1, self.x2 = self.x2, self.x1
            if self.y1 > self.y2:   # met en ordre croissant
                self.y1, self.y2 = self.y2, self.y1
            unit_select(scene, mouse_pos)

    ############################################################################
    # Right click                                                              #
    ############################################################################
    def right_click(self, mouse_pos):
        """Handling right click actions."""
        if self.key["RightClick"] == logic.KX_INPUT_JUST_ACTIVATED:
            if bge.c.game.selected_units:
                if isinstance(mouse_pos.hitObject, Unit):
                    for obj in bge.c.game.selected_units:
                        if obj.owner != mouse_pos.hitObject.owner:
                            obj.target = mouse_pos.hitObject
                            obj.destination = mouse_pos.hitObject.worldPosition
                            obj.state = 3

                elif isinstance(mouse_pos.hitObject, Building):
                    for obj in bge.c.game.selected_units:
                        if obj.owner != mouse_pos.hitObject.owner:
                            obj.target = mouse_pos.hitObject
                            obj.destination = mouse_pos.hitObject.worldPosition
                            obj.state = 3

                elif isinstance(mouse_pos.hitObject, Ressource):
                    for obj in bge.c.game.selected_units:
                        obj.harv_mine = mouse_pos.hitObject
                        obj.harv_dest = mouse_pos.hitObject.worldPosition
                        for civ in bge.c.game.civilisations:
                            if civ == obj.owner:
                                obj.base_dest = civ.buildings["headquarters"][0].worldPosition  # TODO find closest HQ
                        obj.destination = mouse_pos.hitObject.worldPosition
                        obj.state = 4

                else:
                    dist = 0
                    for obj in self.parent.game.selected_units:
                        obj.destination = [mouse_pos.hitPosition[0] + dist,
                                           mouse_pos.hitPosition[1],
                                           obj.worldPosition[2]]
                        dist += 0.7
                        obj.state = 2

    ############################################################################
    # Scroll wheel                                                             #
    ############################################################################
    def scroll_wheel(self, scene, cam, mouse_pos):
        if self.key["MiddleClick"] == logic.KX_INPUT_JUST_ACTIVATED:
            scene.objects['Way_Circle'].worldPosition.x = mouse_pos.hitPosition[0]
            scene.objects['Way_Circle'].worldPosition.y = mouse_pos.hitPosition[1]
            bge.c.game.civilisation.buildings[0].way_point = True
            scene.objects['Way_Circle'].setVisible(True)

        if self.key["ScrollDown"] == logic.KX_INPUT_JUST_ACTIVATED:
            cam = scene.cameras["Camera"]
            if cam.ortho_scale <= ZOOM_MAX:
                for i in range(ZOOM_STEPS):
                    cam.ortho_scale += 1

        if self.key["ScrollUp"] == logic.KX_INPUT_JUST_ACTIVATED:
            cam = scene.cameras["Camera"]
            if cam.ortho_scale >= ZOOM_MIN:
                for i in range(ZOOM_STEPS):
                    cam.ortho_scale -= 1
