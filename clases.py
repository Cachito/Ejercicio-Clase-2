"""
clases.py
a falta de otra explicación,
las clases van acá
"""


class Temas:
    """
    temas de color
    """
    def amarillo(self, root):
        """
        tema amarillo
        """
        #self.root = root
        fondo = "yellow"
        root.configure(background=fondo)
        return root

    def blanco(self, root):
        """
        tema blanco
        """
        #self.root = root
        fondo = "white"
        root.configure(background=fondo)
        return root

    def rojo(self, root):
        """
        tema rojo
        """
        #self.root = root
        fondo = "red"
        root.configure(background=fondo)
        return root
