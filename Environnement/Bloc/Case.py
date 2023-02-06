from Environnement.Bloc.Element import Element
import tkinter as tk


class Case(Element):

    def __init__(self):
        self.color = "white"

    def display(self, root, height, width):
        return tk.Canvas(root, bg=self.color, height=height,
                                                 width=width)
