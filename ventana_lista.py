import tkinter as tkr
from tkinter import StringVar, IntVar, Frame, Label, Entry, Checkbutton, Button
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox


class VentanaSimulacion(tkr.Toplevel):
    def __init__(self, parent, usu, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.title("Simulación")
        self.geometry("400x200+0+0")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        
        info = tkr.Label(self, text="Usuario: {}".format(usu))
        info.pack()

        tkr.Button(self, text="Volver", command=self.volver).pack()
        self.parent.withdraw()

        self.IdVec=0
        self.q = StringVar()
        query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador order by id_torre,id_piso,apto,id_miembro"
        registros = vecinos()
        reg = registros.listarVecinos(query)
            
        self.geometry("1200x600")

        frameLista=Frame(self)
        frameLista.config(bg="gray", bd=10)

        lbl_lista= Label(frameLista, text="Lista de Vecinos del Condominio", bg="green")
        lbl_lista.place(relx=0.5,rely=0, anchor="center")

        frameBuscar=Frame(self, bd=1, bg="gray")

        #split = 0.5
        frameBuscar.place(relx=0, relheight=1, relwidth=0.2)
        frameLista.place(relx=0.201, relheight=1, relwidth=1.0)

        """ Hacer TREEVIEW lista """
        self.listaTree = tkrttk.Treeview(frameLista, height="24", selectmode='browse')

        self.listaTree["columns"] = ("ID","CEDULA","NOMBRE","APELLIDO","PISO","APTO","TORRE")
        self.listaTree.column("ID", width=80, minwidth=270,stretch=False)
        self.listaTree.column("CEDULA", width=80, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("NOMBRE", width=240, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("APELLIDO", width=240, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("PISO", width=80, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("APTO", width=80, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("TORRE", width=260, minwidth=270,stretch=tkr.NO)
        self.listaTree.column("#0", width=0, stretch=False)
        self.listaTree.column("ID", width=0, stretch=False)

        self.listaTree.pack()
        #posicionar el treevie en su lado mas a la izquierda
        self.listaTree.place(relx=0, relwidth=0.80, y=15)
        #scroll para el tree
        vsb = tkrttk.Scrollbar(frameLista, orient="vertical", command=self.listaTree.yview)

        vsb.place(x=935, y=16, height=498)

        self.listaTree.configure(yscrollcommand=vsb.set)

        self.listaTree.heading("ID", text="ID")
        self.listaTree.heading("CEDULA", text="Nro Cédula")
        self.listaTree.heading("NOMBRE", text="Nombre")
        self.listaTree.heading("APELLIDO", text="Apellido")
        self.listaTree.heading("PISO", text="Piso")
        self.listaTree.heading("APTO", text="Apto")
        self.listaTree.heading("TORRE", text="Torre")

        self.listaTree.bind('<ButtonRelease-1>', self.selectItem)

        self.lista(reg, self.listaTree)

        #Hacer un query para llamar la información de las Tores
        self.ref = registros.referencia("TORRE")

        button1 = tkr.Button(frameLista,text='Consultar Datos',command=self.show_window2)
        button1.pack()
        button1.place(x=90, y=520, height=20)

        #para armar el buscar por nombre, apllido, cedula, torre, piso
        self.lbl = Label(frameBuscar, text="Buscar: ")
        self.lbl.grid(row=0)

        #lbl.pack(side=tkr.LEFT, padx=10)
        self.textBUscar = Entry(frameBuscar, textvariable=self.q)
        self.textBUscar.grid(row=0, column=1, padx=2)

        #mostrar la lista en checkbox las opciones para filtrar por edificio
        self.arreglo=[]
        self.variab=[]
        self.linea1=5

        for int in self.ref:
            self.variab.append(IntVar())
            self.arreglo.append(Checkbutton(frameBuscar, command=self.ShowChoice1,bg="gray", text=int[0],variable=self.variab[self.ref.index(int)]))

        for mostrar in self.arreglo:
            self.linea1=self.linea1+1
            mostrar.grid(row=self.linea1, column=0, sticky="w")

        #textBUscar.pack(side=tkr.LEFT, padx=6)
        btn = Button(frameBuscar, text="Buscar", command = self.buscar)
        btn.grid(row=2, column=0)

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def lista(self,reg, listaTree1):
        listaTree1.delete(*listaTree1.get_children())
        ii=0
        for i in reg:
            ii+=1
            if (i[24] % 2):
                listaTree1.insert('','end', value=(i[0],i[1],i[2]+" "+i[3],i[4]+" "+i[5], i[28], i[15], i[29]),)
            else:
                listaTree1.insert('','end', value=(i[0],i[1],i[2]+" "+i[3],i[4]+" "+i[5], i[28], i[15], i[29]), tag='gray')              
            listaTree1.tag_configure('gray', background='#cccccc')

    def selectItem(self, event):
        curItem = self.listaTree.selection()
        for i in curItem:
            #print (self.listaTree.item(i,"values")[0])
            self.IdVec=self.listaTree.item(i,"values")[0]
            #messagebox.showinfo(message=self.IdVec)

    def buscar(self):
        q2 = self.q.get()
        query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador where nombre1 LIKE '%"+q2+"%' or apellido_1 LIKE '%"+q2+"%' order by id_torre,id_piso,apto,id_miembro"    
        registros = vecinos()
        reg = registros.listarVecinos(query)
        self.lista(reg, self.listaTree)

    def ShowChoice1(self):
        for Mostrar in self.arreglo:
            #print(variab[arreglo.index(Mostrar)].get())
            if self.variab[self.arreglo.index(Mostrar)].get()==1:
                contador=(self.ref[self.arreglo.index(Mostrar)])[1]
                print(contador)


    def show_window2(self):
        
        if self.IdVec==0:
            messagebox.showinfo(parent=self, message="Debe seleccionar vecino a consultar")
            return
        
        from detalles_vecinos import InformacionVecinos
        #messagebox.showinfo(message=self.IdVec)
        t=tkr.Toplevel()
        t.configure(bg="#FCFCF9", bd=10)
        t.transient(self)
        InformacionVecinos(t, self.IdVec)
