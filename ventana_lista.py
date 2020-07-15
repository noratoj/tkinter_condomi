from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox


def lista(reg):
    listaTree.delete(*listaTree.get_children())
    for i in reg:
        #listaTree.insert('','end', value=(i[0])) 
        listaTree.insert('','end', value=(i[0],i[2]+" "+i[3],i[4]+" "+i[5], i[28], i[15], i[29]))
        #print(str(i[0])+" "+str(i[4]))        

def buscar():
    q2 = q.get()
    query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador where nombre1 LIKE '%"+q2+"%' or apellido_1 LIKE '%"+q2+"%' order by id_torre,id_piso,apto,id_miembro"    
    registros = vecinos()
    reg = registros.listarVecinos(query)
    lista(reg)
    
query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador order by id_torre,id_piso,apto,id_miembro"
registros = vecinos()
reg = registros.listarVecinos(query)


""" Creando la ventana con la lista de vecinos"""
ventana = tkr.Tk()
ventana.geometry("1200x600")
q = StringVar()

frameLista=LabelFrame(ventana, text="Lista Vecinos")
frameBuscar=LabelFrame(ventana, text="Buscar...")

frameBuscar.pack(fill="both", expand="yes", padx=20, pady=10)
frameLista.pack(fill="both", expand="yes", padx=20, pady=10)

""" Hacer TREEVIEW lista """
listaTree = tkrttk.Treeview(frameLista, height="24")
scrollbar = tkr.Scrollbar(listaTree, orient="vertical")
listaTree["columns"] = ("ID","NOMBRE","APELLIDO","PISO","APTO","TORRE")
listaTree.column("ID", width=80, minwidth=270,stretch=tkr.NO)
listaTree.column("NOMBRE", width=240, minwidth=270,stretch=tkr.NO)
listaTree.column("APELLIDO", width=240, minwidth=270,stretch=tkr.NO)
listaTree.column("PISO", width=120, minwidth=270,stretch=tkr.NO)
listaTree.column("APTO", width=170, minwidth=270,stretch=tkr.NO)
listaTree.column("TORRE", width=260, minwidth=270,stretch=tkr.NO)
listaTree.column("#0", width=0, stretch=False)

#show ="headings", height="24")

listaTree.pack()

listaTree.heading("ID", text="ID")
listaTree.heading("NOMBRE", text="Nombre")
listaTree.heading("APELLIDO", text="Apellido")
listaTree.heading("PISO", text="Piso")
listaTree.heading("APTO", text="Apto")
listaTree.heading("TORRE", text="Torre")

listaTree.configure(yscroll = scrollbar.set, selectmode="browse")
scrollbar.config(command=listaTree.yview)

lista(reg)

#para armar el buscar por nombre, apllido, cedula, torre, piso
lbl = Label(frameBuscar, text="Buscar: ")
lbl.pack(side=tkr.LEFT, padx=10)
textBUscar = Entry(frameBuscar, textvariable=q)
textBUscar.pack(side=tkr.LEFT, padx=6)
btn = Button(frameBuscar, text="Buscar", command = buscar)
btn.pack(side=tkr.LEFT, padx=6)

tkr.mainloop()