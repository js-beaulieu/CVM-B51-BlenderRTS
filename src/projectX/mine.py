import bge


class Mine(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.material = 10000
        bge.c.game.mines.append(self)
