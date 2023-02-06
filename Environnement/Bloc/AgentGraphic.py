from Environnement.EnvironnementInterface import EnvironnementInterface


class AgentGraphic():

    def __init__(self, color="green"):
        self.color = color

    def __set_corner(self, environnement: EnvironnementInterface):
        return EnvironnementInterface.dimension / environnement.size_x

    def display(self, environnement: EnvironnementInterface, x=0, y=0, corner_x1=None, corner_y1=None):
        if corner_x1 is None:
            corner_x1 = self.__set_corner(environnement)
        if corner_y1 is None:
            corner_y1 = self.__set_corner(environnement)

        return environnement.mapCanvas[x][y].create_oval(5, 5, corner_x1, corner_y1, fill=self.color)

    def move(self, environnement: EnvironnementInterface, old_x, old_y, x, y, corner_x1=None, corner_y1=None):
        if corner_x1 is None:
            corner_x1 = self.__set_corner(environnement)
        if corner_y1 is None:
            corner_y1 = self.__set_corner(environnement)

        environnement.mapCanvas[old_x][old_y].delete("all")
        self.display(environnement, x, y, corner_x1, corner_y1)