from bge import logic, events
from mathutils import Vector
from time import clock

class Game:
    mouse = logic.mouse
    keyboard = logic.keyboard
    
def mouse():
    Game.player.applyRotation((0,0,-(round(logic.mouse.position[0],2)-0.5)), True)
    Game.cam.applyRotation((-(round(logic.mouse.position[1],2)-0.5),0,0), True)
    logic.mouse.position = 0.5,0.5
    
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
        addobj = control.actuators["Edit Object1"]
        addobj.linearVelocity = (-1, 20*(clock() - Game.startclock2), 0)
        control.activate(addobj)
        
def mouseView():
    obj=bge.logic.getCurrentController()
    
    
    if obj.sensors["Mouse"].positive and obj.sensors["Mouse1"].positive:
        print(obj.sensors)
        print("OK",obj.sensors["Mouse"].hitPosition,obj.sensors["Mouse"].hitObject)