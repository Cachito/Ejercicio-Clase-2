import sqlite3


class Abmc:
    def __init__(
        self,
    ):
        try:
            con = sqlite3.connect("mibase.db")
            cursorObj = con.cursor()
            cursorObj.execute(
                "CREATE TABLE noticias(id integer PRIMARY KEY, titulo text, descripcion text)"
            )
            con.commit()
        except:
            print("Error conexión")

    def conexion(
        self,
    ):
        con = sqlite3.connect("mibase.db")
        return con

    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        # Consiguiendo datos
        sql = "SELECT * FROM noticias ORDER BY id ASC"

        con = self.conexion()
        cursorObj = con.cursor()
        datos = cursorObj.execute(sql)
        con.commit()

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreeview.insert("", 0, text=fila[0], values=(fila[1], fila[2]))

    def cerrar_conexion(
        self,
    ):
        print("cerrar_conexion")

    def alta(self, titulo, descripcion, mitreeview):
        print("alta")
        print(self, titulo, descripcion, mitreeview)
        print(titulo.get())
        print(descripcion.get())
        print(mitreeview)
        datos = (titulo.get(), descripcion.get())

        con = self.conexion()
        print(con)
        sql = "INSERT INTO noticias(titulo, descripcion) VALUES(?,?) "
        cur = con.cursor()
        cur.execute(sql, datos)
        con.commit()
        self.actualizar_treeview(mitreeview)

    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        con = self.conexion()
        cursor = con.cursor()
        sql = "DELETE FROM noticias WHERE id=?"
        datos = (valor_id["text"],)
        print(datos, sql)
        cursor.execute(sql, datos)
        con.commit()
        self.actualizar_treeview(mitreeview)

    def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        con = self.conexion()

        cursor = con.cursor()
        sql = "UPDATE noticias SET (titulo, descripcion)=(?,?) WHERE id=?"
        datos = (titulo.get(), descripcion.get(), valor_id["text"])
        cursor.execute(sql, datos)
        con.commit()
        print(sql, datos)

        self.actualizar_treeview(mitreeview)
