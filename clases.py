"""
clases.py
a falta de otra explicación,
las clases van acá
"""

from peewee import *

db = SqliteDatabase('mi_base_pw.db')
class BaseModel(Model):
    """
    modelo de base de datos
    """
    class Meta:
        """
        metadata
        """
        database = db

class Noticia(BaseModel):
    """
    tabla Noticias
    """
    class Meta:
        """
        metadata
        """
        Database = db
        table_name = "Noticias"

    Titulo = CharField(unique = True)
    Descripcion = TextField()

    def __str__(self):
        return f'{self.Titulo} {self.Descripcion}'

db.connect()
db.create_tables([Noticia])
class Temas:
    """
    temas de color
    """
    def amarillo(self, root):
        """
        tema amarillo
        """
        fondo = "yellow"
        root.configure(background=fondo)
        return root

    def blanco(self, root):
        """
        tema blanco
        """
        fondo = "white"
        root.configure(background=fondo)
        return root

    def rojo(self, root):
        """
        tema rojo
        """
        fondo = "red"
        root.configure(background=fondo)
        return root
