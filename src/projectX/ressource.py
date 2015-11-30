import bge


class Ressource(bge.types.KX_GameObject):

    def __init__(self, parent):
        self.material = 10000


class Mine(Ressource):

    def __init__(self, parent):
        super(Mine, self).__init__(parent)
        self.material = 10000


class Tree(Ressource):

    def __init__(self, parent):
        super(Tree, self).__init__(parent)
        self.material = 10000


class Crystal(Ressource):

    def __init__(self, parent):
        super(Crystal, self).__init__(parent)
        self.material = 10000


