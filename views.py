
import tkinter.ttk as tkrttk
from tkinter import scrolledtext, NSEW, W

#Realizar el diseño de todas las TREVIEW y otros elementos relacionados con la vista que
#se requiera y se repita dentro del sistema
class vistas():
    
    #Arbol - treeview para registros relacionados con la VECINOS
    def treeview_registros(self, frame1):
        self.listaTree = tkrttk.Treeview(frame1, style="Treeview",height="24", selectmode='browse')

        self.listaTree["columns"] = ("ID","CEDULA","NOMBRE","APELLIDO","PISO","APTO","TORRE")
        self.listaTree.column("ID", width=80, minwidth=270,stretch=False)
        self.listaTree.column("CEDULA", width=90, minwidth=90)
        self.listaTree.column("NOMBRE", width=240, minwidth=270)
        self.listaTree.column("APELLIDO", width=240, minwidth=270)
        self.listaTree.column("PISO", width=50, minwidth=50)
        self.listaTree.column("APTO", width=70, minwidth=80)
        self.listaTree.column("TORRE", width=230, minwidth=240)
        self.listaTree.column("#0", width=0, stretch=False)
        self.listaTree.column("ID", width=0, stretch=False)

        self.listaTree.heading("ID", text="ID")
        self.listaTree.heading("CEDULA", text="Nro Cédula")
        self.listaTree.heading("NOMBRE", text="Nombre")
        self.listaTree.heading("APELLIDO", text="Apellido")
        self.listaTree.heading("PISO", text="Piso")
        self.listaTree.heading("APTO", text="Apto")
        self.listaTree.heading("TORRE", text="Torre")

        self.listaTree.grid(row=1, column=0, sticky=NSEW)
        
        vsb_a = tkrttk.Scrollbar(frame1, orient="vertical", command=self.listaTree.yview)
        vsb_a.grid(row=1, column=1, sticky=NSEW)
        hsb_a = tkrttk.Scrollbar(frame1, orient="horizontal", command=self.listaTree.xview)
        hsb_a.grid(row=2, column=0, sticky=NSEW)
        self.listaTree.configure(xscrollcommand=hsb_a.set, yscrollcommand=vsb_a.set)
        return self.listaTree

    #Arbol - treeview para registros relacionados con la VECINOS
    def treeview_referencia(self, frame1):
        self.listaTree_rol = tkrttk.Treeview(frame1, height="14", selectmode='browse')

        self.listaTree_rol["columns"] = ("ID","CONTADOR", "TABLA","DESCRIPCION","ORDEN","PADRE")
        self.listaTree_rol.column("ID", width=80, minwidth=270,stretch=False)
        self.listaTree_rol.column("CONTADOR", width=60, minwidth=80)
        self.listaTree_rol.column("TABLA", width=130, minwidth=130)
        self.listaTree_rol.column("DESCRIPCION", width=260, minwidth=270)
        self.listaTree_rol.column("ORDEN", width=60, minwidth=70)
        self.listaTree_rol.column("PADRE", width=220, minwidth=230)
        self.listaTree_rol.column("#0", width=0, stretch=False)
        self.listaTree_rol.column("ID", width=0, stretch=False)

        self.listaTree_rol.grid(column=1, row=0, padx=4, pady=4)

        self.listaTree_rol.heading("ID", text="ID")
        self.listaTree_rol.heading("CONTADOR", text="id campo")
        self.listaTree_rol.heading("TABLA", text="Tabla Maestra")
        self.listaTree_rol.heading("DESCRIPCION", text="Descripcion")
        self.listaTree_rol.heading("ORDEN", text="Orden")
        self.listaTree_rol.heading("PADRE", text="Padre (Relacionado con)")
        return self.listaTree_rol