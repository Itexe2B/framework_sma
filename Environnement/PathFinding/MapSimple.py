from Environnement.Bloc.AgentGraphic import AgentGraphic
from Environnement.Bloc.Case import Case
from Environnement.Bloc.Element import Element
from Environnement.Bloc.Wall import Wall
from Environnement.EnvironnementInterface import EnvironnementInterface
import tkinter as tk
import random as rd
from copy import deepcopy

from Simulation.RandomMove import RandomMove


class MapSimple(EnvironnementInterface):
    def __init__(self):
        self.map = [[0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 1],
               [0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1],
               [0, 0, 0, 0, 0, 0]]

        self.mapCanvas = deepcopy(self.map)
        self.mapObject = deepcopy(self.map)

        self.root = tk.Tk()
        self.root.title("MapSimple")
        self.size_x = len(self.map)
        self.size_y = len(self.map[0])
        self.agent = None
        self.__show()
    def __show(self):
        '''
        Show the map
        :return:
        '''
        for i in range(self.size_x):
            for j in range(self.size_y):
                height = EnvironnementInterface.dimension / self.size_x
                width = EnvironnementInterface.dimension / self.size_x

                if self.map[i][j] == 1:
                    wall = Wall()
                    self.mapObject[i][j] = wall
                    self.mapCanvas[i][j] = wall.display(self.root, height, width)
                else:
                    case = Case()
                    self.mapObject[i][j] = case
                    self.mapCanvas[i][j] = case.display(self.root, height, width)

                #self.mapCanvas[i][j] = Wall().display(self.root, height, width) if self.map[i][j] == 1 else \
                #    Case().display(self.root, height, width)s

                #self.mapObject[i][j] = Wall() if self.map[i][j] == 1 else Case()

                self.mapCanvas[i][j].grid(row=i, column=j)

        #Button pour tester le déplacement de l'agent
        button = tk.Button(self.root, text="Start Simulation", command= lambda: self.root.after_idle(RandomMove(self.agent).run), height=2)
        button.grid(row=self.size_x + 1, column=0, columnspan=self.size_y)
    def addAgent(self, agent):
        self.agent = agent