from Norms.Norm import Norm


class EnvironnementInterface:
    dimension = 500
    map = None
    root = None
    mapCanvas = None
    mapObject = None
    size_x = None
    size_y = None
    norms = []
    def __init__(self):
        pass

    def __show(self):
        pass

    def addAgent(self, agent):
        pass

    def addNorm(self, norm: Norm):
        self.norms.append(norm)