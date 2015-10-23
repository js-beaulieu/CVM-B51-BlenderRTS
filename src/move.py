import bge

cont = bge.logic.getCurrentController()
owner = cont.owner

mouse = cont.sensors["Mouse"]
width = bge.render.getWindowWidth()
width = width / 2

pos = mouse.position

posX = width - pos[0] 
posX = posX * 0.02 
owner.localPosition.x = posX
print(posX)


