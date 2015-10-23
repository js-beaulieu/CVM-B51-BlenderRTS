from bge import logic, events, render
from mathutils import Vector
from time import clock
from bpy import *

class Game:
    dmouse = logic.mouse
    keyboard = logic.keyboard
    
def mouse():
    Game.player.applyRotation((0,0,-(round(logic.mouse.position[0],2)-0.5)), True)
    Game.cam.applyRotation((-(round(logic.mouse.position[1],2)-0.5),0,0), True)
    logic.mouse.position = 0.5,0.5

def mouseVisibility():
    render.showMouse(True)
    
    
def mousePosition():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    cont = logic.getCurrentController()
    obj = cont.owner
    print(obj)
    dmouse = logic.mouse
    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_ACTIVATED:
        x1 = round(logic.mouse.position[0] * render.getWindowWidth())
        y1 = round(logic.mouse.position[1] * render.getWindowHeight())
        print("activated = " + str(x1) + ", " + str(y1)) 
    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_RELEASED:
        x2 = round(logic.mouse.position[0] * render.getWindowWidth())
        y2 = round(logic.mouse.position[1] * render.getWindowHeight())
        print("released = " + str(x2) + ", " + str(y2)) 
        
    
    
def launch():
    control = logic.getCurrentController()
    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_ACTIVATED:
        Game.startclock1 = clock()
    elif logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT] == logic.KX_INPUT_JUST_ACTIVATED:
        Game.startclock2 = clock()
    elif logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_RELEASED:
        addobj = control.actuators["Edit Object"]
        addobj.linearVelocity = (-1, 20*(clock() - Game.startclock1), 0)
        control.activate(addobj)
    elif logic.mouse.events[logic.KX_MOUSE_BUT_RIGHT] == logic.KX_INPUT_JUST_RELEASED:
        addobj = control.actuators["Edit Object"]
        addobj.linearVelocity = (-1, 20*(clock() - Game.startclock2), 0)
        control.activate(addobj)
        
def deleteSelect():
    print("okay")
    for ob in context.scene.objects:
        ob.select = ob.type == 'MESH' and ob.name.startswith("Sphe")
        ops.object.delete()
        print("okay2")
        #ob.delete() NNOOOOOOOOOOOOOOOOOO!!!
