from Environnement.Bloc.Case import Case
from Environnement.Bloc.Element import Element
from Environnement.Bloc.Wall import Wall
from Environnement.EnvironnementInterface import EnvironnementInterface
import tkinter as tk
class MapSimple(EnvironnementInterface):
    def __init__(self):
        self.map = [[0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 1],
               [0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1],
               [0, 0, 0, 0, 0, 0]]
        self.root = tk.Tk()
    def show(self):
        size_x = len(self.map)
        size_y = len(self.map[0])
        for i in range(size_x):
            for j in range(size_y):
                element = Wall() if self.map[i][j] == 1 else Case()
                tk.Canvas(self.root, bg=element.color, height=EnvironnementInterface.dimension / size_x, width=EnvironnementInterface.dimension / size_x)\
                    .grid(row=i, column=j)

        self.root.mainloop()
    def update(self):
        pass