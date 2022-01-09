"""
model.py
clase Model del patrón MVC
"""
import sqlite3


class Model:
    """
    Model
    modelo del programa
    """
    def __init__(
        self,
    ):
        try:
            con = sqlite3.connect("mibase.db")

            drop_qry = """
                DROP TABLE IF EXISTS Noticias
                """
            create_qry = """
                CREATE TABLE IF NOT EXISTS Noticias(
                    Id INTEGER PRIMARY KEY,
                    Titulo text,
                    Descripcion text
                    )
                """
            cursor_obj = con.cursor()

            cursor_obj.execute(drop_qry)
            cursor_obj.execute(create_qry)

            con.commit()

        except Exception as exc:
            print(f"Error conexión {str(exc)}")

    def conexion(
        self,
    ):
        """
        conexion
        devuelve una conexión a la base de datos
        """
        con = sqlite3.connect("mibase.db")
        return con

    def actualizar(self, treeview):
        """
        actualizar
        refresh de la vista
        """
        # limpieza de tabla
        records = treeview.get_children()
        for element in records:
            treeview.delete(element)

        sql = """
            SELECT *
            FROM Noticias
            ORDER BY id ASC
            """

        con = self.conexion()
        cursor_obj = con.cursor()
        data = cursor_obj.execute(sql)
        con.commit()

        data_rows = data.fetchall()
        for data_row in data_rows:
            print(data_row)
            treeview.insert("", 0, text=data_row[0], values=(data_row[1], data_row[2]))

    def cerrar_conexion(
        self,
    ):
        """
        ?
        cerrar_conexion
        cierra la conexión a base de datos
        """
        print("cerrar_conexion")

    def alta(self, titulo, descripcion, treeview):
        """
        alta
        crea un registro
        """
        print("alta")
        print(self, titulo, descripcion, treeview)
        print(titulo.get())
        print(descripcion.get())
        print(treeview)
        datos = (titulo.get(), descripcion.get())

        con = self.conexion()
        print(con)
        sql = """
            INSERT INTO Noticias(Titulo, Descripcion)
                VALUES(?, ?)
            """
        cur = con.cursor()
        cur.execute(sql, datos)
        con.commit()
        self.actualizar(treeview)

    def baja(self, treeview):
        """
        baja
        elimina un registro
        """
        item = treeview.focus()
        tv_row = treeview.item(item)
        datos = (tv_row["text"],)
        sql = """
            DELETE FROM Noticias
            WHERE id = ?
        """
        print(datos, sql)

        con = self.conexion()
        cursor = con.cursor()

        cursor.execute(sql, datos)

        con.commit()

        self.actualizar(treeview)

    def modificar(self, titulo, descripcion, mitreeview):
        """
        modificar
        modifica un registro
        """
        item = mitreeview.focus()
        tw_row = mitreeview.item(item)
        datos = (titulo.get(), descripcion.get(), tw_row["text"])
        sql = """
            UPDATE Noticias SET
                (Titulo, Descripcion) = (?, ?)
            WHERE Id = ?
        """
        print(sql, datos)

        con = self.conexion()

        cursor = con.cursor()

        cursor.execute(sql, datos)
        con.commit()

        self.actualizar(mitreeview)
