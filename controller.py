"""
controller.py
clase Controller del patrón MVC
"""
from tkinter import Tk
import view


class Controller:
    """
    Está es la clase principal
    """
    def __init__(self, root):
        self.root_controler = root
        self.view = view.View(self.root_controler)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)

    application.view.actualizar()
    root_tk.mainloop()
