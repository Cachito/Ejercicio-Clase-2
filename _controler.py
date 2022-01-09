from tkinter import Tk
import _vista

# from modelo import *


class Controller:
    """
    Está es la clase principal
    """

    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = _vista.Ventanita(self.root_controler)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)

    application.objeto_vista.actualizar()
    root_tk.mainloop()
