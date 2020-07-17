from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox

def ShowChoice1():
    for Mostrar in arreglo:
        #print(variab[arreglo.index(Mostrar)].get())
        if variab[arreglo.index(Mostrar)].get()==1:
            contador=(ref[arreglo.index(Mostrar)])[1]
            print(contador)

def referencia(ref_campo):
    q2 = ref_campo
    query = "SELECT tb1.campo_des, tb1.contador FROM tbreferencia tb1 where tabla LIKE '%"+q2+"%' order by campo_des"    
    registros = vecinos()
    reg_1 = registros.listarVecinos(query)
    return(reg_1)
    #for i in reg_1:
    #    print(str(i[0])+" "+str(i[1]))        
    

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
i_1=IntVar()
linea1=IntVar()
#v = IntVar()
#v.set(1)  # inicializar el choice del listado de torres

frameLista=Frame(ventana)
frameLista.config(bg="gray", bd=10)

lbl_lista= Label(frameLista, text="Lista de Vecinos del Condominio", bg="green")
lbl_lista.place(relx=0.5,rely=0, anchor="center")
#lbl_lista.pack()

frameBuscar=Frame(ventana, bd=1, bg="gray")

split = 0.5
frameBuscar.place(relx=0, relheight=1, relwidth=0.2)
frameLista.place(relx=0.201, relheight=1, relwidth=1.0)

""" Hacer TREEVIEW lista """
listaTree = tkrttk.Treeview(frameLista, height="24", selectmode='browse')

listaTree["columns"] = ("ID","NOMBRE","APELLIDO","PISO","APTO","TORRE")
listaTree.column("ID", width=80, minwidth=270,stretch=tkr.NO)
listaTree.column("NOMBRE", width=240, minwidth=270,stretch=tkr.NO)
listaTree.column("APELLIDO", width=240, minwidth=270,stretch=tkr.NO)
listaTree.column("PISO", width=80, minwidth=270,stretch=tkr.NO)
listaTree.column("APTO", width=80, minwidth=270,stretch=tkr.NO)
listaTree.column("TORRE", width=260, minwidth=270,stretch=tkr.NO)
listaTree.column("#0", width=0, stretch=False)

#show ="headings", height="24")

listaTree.pack()
#posicionar el treevie en su lado mas a la izquierda
listaTree.place(relx=0, relwidth=0.80, y=15)
#scroll para el tree
vsb = tkrttk.Scrollbar(frameLista, orient="vertical", command=listaTree.yview)

vsb.place(x=935, y=16, height=498)

listaTree.configure(yscrollcommand=vsb.set)

listaTree.heading("ID", text="ID")
listaTree.heading("NOMBRE", text="Nombre")
listaTree.heading("APELLIDO", text="Apellido")
listaTree.heading("PISO", text="Piso")
listaTree.heading("APTO", text="Apto")
listaTree.heading("TORRE", text="Torre")

lista(reg)

#Hacer un query para llamar la información de las Tores
ref=referencia("TORRE")
i_1=3
#para armar el buscar por nombre, apllido, cedula, torre, piso
lbl = Label(frameBuscar, text="Buscar: ").grid(row=0)
#lbl.place(relx=0, relheight=1, relwidth=0.2)

#lbl.pack(side=tkr.LEFT, padx=10)
textBUscar = Entry(frameBuscar, textvariable=q)
textBUscar.grid(row=0, column=1)

arreglo=[]
variab=[]
linea1=5
for int in ref:
    variab.append(IntVar())
    arreglo.append(Checkbutton(frameBuscar, command=ShowChoice1, text=int[0],variable=variab[ref.index(int)]))


for mostrar in arreglo:
    linea1=linea1+1
    mostrar.grid(row=linea1, column=0, sticky="w")

#textBUscar.pack(side=tkr.LEFT, padx=6)
btn = Button(frameBuscar, text="Buscar", command = buscar)
btn.grid(row=2, column=0)
#btn.pack(side=tkr.LEFT, padx=6)

tkr.mainloop()