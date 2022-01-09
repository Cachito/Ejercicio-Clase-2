"""
view.py
clase View del patrón VMC
"""
from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import ttk
from clases import Temas
from model import Model

class View:
    """
    View
    vista del programa
    """
    def __init__(self, window):
        self.root = window
        self.titulo = StringVar()
        self.descripcion = StringVar()
        #self.a = IntVar()
        self.opcion = StringVar()
        self.frame = Frame(self.root)
        self.tree = ttk.Treeview(self.frame)
        self.model = Model()

        # Frame
        self.root.title("Tarea Poo")
        self.frame.config(width=1020, height=1020)
        self.frame.grid(row=10, column=0, columnspan=4)

        # Etiquetas
        self.lbl_superior = Label(
            self.root, text="Ingrese sus datos", bg="orchid", fg="white", width=40
        )
        self.lbl_titulo = Label(self.root, text="Titulo")
        self.lbl_descripcion = Label(self.root, text="Descripcion")
        self.lbl_count = Label(
            self.root, text="Mostrar registros existentes", bg="grey", width=40
        )
        self.lbl_temas = Label(
            self.root,
            text="Temas",
            bg="black",
            fg="white",
            height=1,
            width=40,
        )

        self.lbl_superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.lbl_titulo.grid(row=1, column=0, sticky="w")
        self.lbl_descripcion.grid(row=2, column=0, sticky="w")
        self.lbl_count.grid(
            row=3, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.lbl_temas.grid(
            column=0, row=20, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )

        # Entradas
        self.ent_titulo = Entry(self.root, textvariable=self.titulo)
        self.ent_titulo.grid(row=1, column=1)
        self.ent_descripcion = Entry(self.root, textvariable=self.descripcion)
        self.ent_descripcion.grid(row=2, column=1)

        # Frame Unidad 4
        self.frame_rojo_izq = Frame(self.root, width="200", height="80", bg="red")
        self.frame_negro = Frame(self.root, width="80", height="80", bg="black")
        self.frame_rojo_der = Frame(self.root, width="200", height="80", bg="red")

        self.frame_rojo_izq.grid(column=0, row=21)
        self.frame_negro.grid(column=1, row=21)
        self.frame_rojo_der.grid(column=2, row=21)

        # Botones
        self.btn_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.btn_alta.grid(row=6, column=0)

        self.btn_editar = Button(
            self.root, text="Modificar", command=lambda: self.modificar()
        )
        self.btn_editar.grid(row=6, column=1)

        self.btn_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar()
        )
        self.btn_borrar.grid(row=6, column=2)

        self.btn_amarillo = Radiobutton(
            self.frame_negro,
            text="Amarillo",
            variable=self.opcion,
            value="01",
            fg="yellow",
            bg="black",
            command=lambda:Temas.amarillo(self, self.root),
        )
        self.btn_amarillo.grid(column=2, row=21)

        self.btn_blanco = Radiobutton(
            self.frame_negro,
            text="Blanco",
            variable=self.opcion,
            value="02",
            fg="white",
            bg="black",
            command=lambda:Temas.blanco(self, self.root),
        )
        self.btn_blanco.grid(column=2, row=22)

        self.btn_rojo = Radiobutton(
            self.frame_negro,
            text="Rojo",
            variable=self.opcion,
            value="03",
            fg="red",
            bg="black",
            command=lambda:Temas.rojo(self, self.root),
        )
        self.btn_rojo.grid(column=2, row=23)

        # Tree
        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Título")
        self.tree.heading("col2", text="Descripción")
        self.tree.grid(row=10, column=0, columnspan=4)

    def alta(
        self,
    ):
        """
        alta
        crea un registro
        """
        self.model.alta(self.titulo, self.descripcion, self.tree)

    def borrar(
        self,
    ):
        """
        borrar
        elimina un registro
        """
        self.model.baja(self.tree)

    def modificar(
        self,
    ):
        """
        modificar
        modifica un registro
        """
        self.model.modificar(self.titulo, self.descripcion, self.tree)

    def actualizar(
        self,
    ):
        """
        actualizar
        refresh de la vista
        """
        self.model.actualizar(self.tree)
