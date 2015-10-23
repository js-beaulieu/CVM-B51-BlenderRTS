import bge


from Display import *
from Model import *

class Controller():
    def __init__(self):
        self.frame = 0
        self.model = Model(1) # mapNb 1
        self.model.createUnit()
        self.display = Display(self)
        #self.play()

    def play(self):
        #self.model.update()
        #todo


if __name__ == '__main__':
    bge.controller = Controller()