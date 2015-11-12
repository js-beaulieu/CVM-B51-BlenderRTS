from bge import logic, render
import bgl

def init():
    scene = logic.getCurrentScene()
    scene.post_draw = [write]
    print('ok')

def write():
    """write on screen"""
    scene = logic.getCurrentScene()
    width = render.getWindowWidth()
    height = render.getWindowHeight()

    # OpenGL setup
    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glLoadIdentity()
    bgl.gluOrtho2D(0, width, 0, height)
    bgl.glMatrixMode(bgl.GL_MODELVIEW)
    bgl.glLoadIdentity()
 
    #draw a 2D rectangle to make the fonts stand out
    bgl.glEnable(bgl.GL_BLEND)# Enable alpha blending
    bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA)
    view_buf = bgl.Buffer(bgl.GL_INT, 4)
    bgl.glGetIntegerv(bgl.GL_VIEWPORT, view_buf)
    view = view_buf
    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glLoadIdentity()
    bgl.gluOrtho2D(0, view[2], 0, view[3])
    bgl.glMatrixMode(bgl.GL_MODELVIEW)
    bgl.glLoadIdentity()
    bgl.glBegin(bgl.GL_QUADS)
    bgl.glColor4f(.4, 0, 0, 0.4)
    bgl.glVertex2f(5, (height/2))
    bgl.glVertex2f(width -5, (height/2))
    bgl.glVertex2f(width - 5, (height/2) + 21)
    bgl.glVertex2f(5, int(height/2) + 21)
    bgl.glEnd()

def main(cont):
    own = cont.owner
    if not "init" in own:
        own["init"] = True
        init()