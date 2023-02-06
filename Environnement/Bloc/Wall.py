from Environnement.Bloc.Element import Element
import tkinter as tk

class Wall(Element):

    def __init__(self):
        self.color = "red"

    def display(self, root, height, width):
        return tk.Canvas(root, bg=self.color, height=height,
                  width=width)
