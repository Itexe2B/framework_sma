from Environnement.Bloc.AgentGraphic import AgentGraphic
from Environnement.EnvironnementInterface import EnvironnementInterface
import random as rd

class AgentRandomMove:
    def __init__(self, env: EnvironnementInterface, color="green"):
        self.env = env
        self.x = 2
        self.y = 3
        self.graphic = AgentGraphic(color=color)
        env.addAgent(self)
        self.__display()

    def __display(self):
        self.graphic.display(self.env, self.x, self.y)

    def __getPosiblePosition(self):
        position_possible = []
        if self.x > 0:
            position_possible.append((self.x - 1, self.y))
        if self.x < self.env.size_x - 1:
            position_possible.append((self.x + 1, self.y))
        if self.y > 0:
            position_possible.append((self.x, self.y - 1))
        if self.y < self.env.size_y - 1:
            position_possible.append((self.x, self.y + 1))
        return position_possible
    def move(self):
        x, y = rd.sample(self.__getPosiblePosition(), 1)[0]
        self.graphic.move(self.env, self.x, self.y, x, y)
        self.x = x
        self.y = y

