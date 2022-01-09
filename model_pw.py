"""
model_pw.py
clase Model del patrón MVC
"""
#import peewee
from clases import db
from clases import Noticia

class ModelPw:
    """
    Model
    modelo del programa
    """
    def __init__(
        self,
    ):
        if not db.is_closed():
            db.close()

        try:
            db.connect()
            db.create_tables([Noticia])

            print("base y tabla creadas")

        except Exception as exc:
            print(f"Error al iniciar {str(exc)}")

        finally:
            db.close()

    def actualizar(self, treeview):
        """
        actualizar
        refresh de la vista
        """
        # limpieza de tabla
        records = treeview.get_children()
        for element in records:
            treeview.delete(element)

        if not db.is_closed():
            db.close()

        try:
            db.connect()

            noticias = Noticia.select()
            db.close()

            for noticia in noticias:
                print(noticia)
                treeview.insert("", 0, text=noticia.id, values=(noticia.Titulo, noticia.Descripcion, noticia))

            print("registros recuperados")

        except Exception as exc:
            print(f"Error al recuperar registros {str(exc)}")

        finally:
            db.close()

    def alta(self, titulo, descripcion, treeview):
        """
        alta
        crea un registro
        """
        print("alta")
        print(titulo.get(), descripcion.get())

        if not db.is_closed():
            db.close()

        try:
            db.connect()

            Noticia.create(Titulo = titulo.get(), Descripcion = descripcion.get())

        except Exception as exc:
            print(f"Error al crear registro {str(exc)}")

        finally:
            db.close()

        self.actualizar(treeview)

    def baja(self, treeview):
        """
        baja
        elimina un registro
        """
        item = treeview.focus()
        tv_row = treeview.item(item)

        if not db.is_closed():
            db.close()

        try:
            db.connect()
            borrar = Noticia.get(Noticia.id == tv_row["text"])
            borrar.delete_instance()

        except Exception as exc:
            print(f"Error al eliminar registro {str(exc)}")

        finally:
            db.close()

        self.actualizar(treeview)

    def modificar(self, titulo, descripcion, mitreeview):
        """
        modificar
        modifica un registro
        """
        item = mitreeview.focus()
        tw_row = mitreeview.item(item)

        if not db.is_closed():
            db.close()

        try:
            db.connect()
            update = Noticia.update(
                Titulo = titulo.get(), Descripcion = descripcion.get()).where(Noticia.id == tw_row["text"]
                )
            update.execute()

        except Exception as exc:
            print(f"Error al modificar registro {str(exc)}")

        finally:
            db.close()

        self.actualizar(mitreeview)
