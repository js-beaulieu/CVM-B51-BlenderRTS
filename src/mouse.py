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
    
def select():

    control = logic.getCurrentController()    
    scene = logic.getCurrentScene()
    owner = control.owner
    cam = scene.active_camera

    mouseO = control.sensors["Mouse Over"] 
    mouseL = control.sensors["Mouse LeftClick"]
    x1 = owner["x1"] 
    y1 = owner["y1"]
    x2 = owner["x2"]
    y2 = owner["y2"]

    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_ACTIVATED:
        owner["x1"] = mouseO.hitPosition[0]    # enregistre les coordonees initiales
        owner["y1"] = mouseO.hitPosition[1]
        owner["x2"] = mouseO.hitPosition[0]    # enregistre la position actuelle de la souris
        owner["y2"] = mouseO.hitPosition[1]
        
    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_ACTIVE:
        owner["x2"] = mouseO.hitPosition[0]    # enregistre la position actuelle de la souris
        owner["y2"] = mouseO.hitPosition[1]
        z = mouseO.hitPosition[2] + 0.1

        render.drawLine((x1, y1, z), (x2, y1, z), (1,0,0))    # param((point 1), (point 2), (RGB de 0.00 a 1.00) 
        render.drawLine((x1, y1, z), (x1, y2, z), (1,0,0))
        render.drawLine((x2, y2, z), (x2, y1, z), (1,0,0))
        render.drawLine((x2, y2, z), (x1, y2, z), (1,0,0))     # qui dessine le rectangle tant que la souris est positive

    if logic.mouse.events[logic.KX_MOUSE_BUT_LEFT] == logic.KX_INPUT_JUST_RELEASED:
        if x1 > x2 :
            p = x2
            x2 = x1
            x1 = p

        if y1 > y2 :    # met en ordre croissant
            p = y2
            y2 = y1
            y1 = p

        for obj in scene.objects :    # itere au travers les objets de la scene (pas excellent performances)
            if 'Select' in obj.getPropertyNames() :    # Select = bool in object attributes
                print('select = ', obj.name)
                pos = cam.getScreenPosition(obj)
                x = pos[0] * render.getWindowWidth()    # normalise le format de lecran
                y = pos[1] * render.getWindowHeight()
                if x > x1 and y > y1 and x < x2 and y < y2 :    # si a linterieur du rectangle
                    print('obj inside')
                    obj['Select'] = True
                    
def move():
    cont = logic.getCurrentController()
    owner = cont.owner
    dmouse = cont.sensors["Mouse"]
    cmouse = cont.sensors["Mouse1"]
    obj=logic.getCurrentController() 

    if obj.sensors["Mouse"].positive and obj.sensors["Mouse1"].positive:
        owner.localPosition.x = obj.sensors["Mouse1"].hitPosition[0]
        owner.localPosition.y = obj.sensors["Mouse1"].hitPosition[1]
         
def mousePosition():
    x1 = 0
    y1 = 0
    xt = 0
    yt = 0
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
    if logic.keyboard.events[events.XKEY] == logic.KX_INPUT_JUST_ACTIVATED:
        Game.startclock1 = clock()
    elif logic.keyboard.events[events.XKEY] == logic.KX_INPUT_JUST_RELEASED:
        addobj = control.actuators["Edit Object"]
        addobj.linearVelocity = (-1, 20*(clock() - Game.startclock1), 0)
        control.activate(addobj)
        
def deleteSelect():
    print("okay")
    for ob in context.scene.objects:
        ob.select = ob.type == 'MESH' and ob.name.startswith("Sphe")
        ops.object.delete()
        print("okay2")
        #ob.delete() NNOOOOOOOOOOOOOOOOOO!!!
