import tkinter as tkr
from tkinter import StringVar, IntVar, Frame, Label, Entry, Checkbutton, Button
import tkinter.ttk as tkrttk
from lista_vecinos import *
from views import *
from tkinter import messagebox
from vista import *

from typing import re


class VentanaManejoReg(tkr.Toplevel):
    PAD = 5
    def __init__(self, parent, usu, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.tamagnoletra = ("Arial",10,"bold")
        self.back1="#525252" #8cabbe
        self.button1="#59c9b9"
        self.fore="white"
        self.foreblack="black"
        self.title("Lista de Vecinos")

        self.config(bg='white', borderwidth=1)

        # Frame Principal
        self.frm_main = ttk.Frame(self, relief='ridge')
        self.frm_main.pack(padx=self.PAD, pady=self.PAD, fill="both", expand='yes')

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w = sw * 0.7
        h = sh * 0.7
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.attributes('-zoomed', True)

        self.protocol("WM_DELETE_WINDOW", self.volver)
        
        info = tkr.Label(self, text="Usuario: {}".format(usu), font=self.tamagnoletra, background=self.back1)
        info.pack()

        tkr.Button(self, text="Volver", command=self.volver).pack()
        self.parent.withdraw()

        self.IdVec=0
        self.q = StringVar()
        query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador order by id_torre,id_piso,apto,id_miembro"
        registros = vecinos()
        reg = registros.listarVecinos(query)
            
        #self.geometry("1200x600")

        self.frameLista=Frame(self)
        self.frameLista.config(background=self.back1, bd=10)

        lbl_lista= tkr.Label(self.frameLista, text="Lista de Vecinos del Condominio", bg=self.button1, width = "40", height="2", font=("Arial",12,"bold"))
        lbl_lista.grid(row=0, column=0)
        #lbl_lista.place(relx=0.5,rely=0, anchor="center")

        frameBuscar=Frame(self, bd=1, background=self.back1)
        
        #split = 0.5
        frameBuscar.place(relx=0, relheight=1, relwidth=0.2)
        self.frameLista.place(relx=0.201, relheight=1, relwidth=1.0)
        self.framebtns=Frame(self.frameLista, bd=1, background=self.back1) 
        self.framebtns.place(x=100, y= 540,relheight=0.1, relwidth=0.5)
        
        #llamar para crear el treeview de los registrs de vecinos_temporal
        treeview_1 = vistas()
        self.listatree2 = treeview_1.treeview_registros(self.frameLista)
        self.listatree2.bind('<ButtonRelease-1>', self.selectItem)
        """ Hacer TREEVIEW lista """
        self.lista(reg, self.listatree2)
        

        #Boton para consultar datos de la lista de vecinos seleccionado
        button1 = tkr.Button(self.framebtns,text='Consultar Datos',command=self.show_window2, highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        button1.grid(row=0,column=1, padx=10, pady=10)

        buttonagregfam = tkr.Button(self.framebtns,text='Crear grupo Familiar',command=self.show_grupofamnuevo, highlightbackground=self.button1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        buttonagregfam.grid(row=0,column=2, padx=10, pady=10)

        #Boton para eliminar datos de la lista de vecinos seleccionado
        button1elim= tkr.Button(self.framebtns,text='Eliminar',command=self.EliminarVec, highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        button1elim.grid(row=0,column=3, padx=10, pady=10)


        #para armar el buscar por nombre, apllido, cedula, torre, piso
        self.lbl = Label(frameBuscar, text="Buscar: ", bg=self.back1, fg=self.fore, font=self.tamagnoletra)
        self.lbl.grid(row=0, column=0)

        #lbl.pack(side=tkr.LEFT, padx=10)
        self.textBUscar = Entry(frameBuscar, textvariable=self.q)
        self.textBUscar.grid(row=0, column=1)

        #Hacer un query para llamar la información de las Tores
        self.ref = registros.combo_add("TORRE",0)

        #mostrar la lista en checkbox las opciones para filtrar por edificio
        self.arreglo=[]
        self.variab=[]
        self.linea1=5

        for int in self.ref:
            self.variab.append(IntVar())
            self.arreglo.append(Checkbutton(frameBuscar, command=self.ShowChoice1, highlightbackground=self.back1,relief="flat", bg=self.back1, fg=self.fore, font=self.tamagnoletra,text=int[0],variable=self.variab[self.ref.index(int)]))

        for mostrar in self.arreglo:
            self.linea1=self.linea1+1
            mostrar.grid(row=self.linea1, column=0, sticky="w")

        #textBUscar.pack(side=tkr.LEFT, padx=6)
        btn = Button(frameBuscar, text="Buscar", command = self.buscar, highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        btn.grid(row=2, column=0)

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def lista(self,reg, listaTree2):
        listaTree2.delete(*listaTree2.get_children())
        ii=0
        for i in reg:
            ii+=1
            if (i[23] % 2):
                listaTree2.insert('','end', value=(i[0],i[1],i[2]+" "+i[3],i[4]+" "+i[5], i[28], i[15], i[29]),)
            else:
                listaTree2.insert('','end', value=(i[0],i[1],i[2]+" "+i[3],i[4]+" "+i[5], i[28], i[15], i[29]), tag='gray')              
            listaTree2.tag_configure('gray', background='#cccccc')

    def selectItem(self, event):
        curItem = self.listatree2.selection()
        for i in curItem:
            #print (self.listaTree.item(i,"values")[0])
            self.IdVec=self.listatree2.item(i,"values")[0]
            #messagebox.showinfo(message=self.IdVec)

    def buscar(self):
        q2 = self.q.get()
        query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador where nombre1 LIKE '%"+q2+"%' or apellido_1 LIKE '%"+q2+"%' order by id_torre,id_piso,apto,id_miembro"    
        registros = vecinos()
        reg = registros.listarVecinos(query)
        self.lista(reg, self.listaTree2)

    def ShowChoice1(self):
        for Mostrar in self.arreglo:
            #print(variab[arreglo.index(Mostrar)].get())
            if self.variab[self.arreglo.index(Mostrar)].get()==1:
                contador=(self.ref[self.arreglo.index(Mostrar)])[1]

    def EliminarVec(self):
        if self.IdVec==0:
            messagebox.showinfo(parent=self, title="Eliminar registro", message="Debe seleccionar vecino a eliminar")
            return

        curItem = self.listaTree2.selection()
        for i in curItem:
            nomb=self.listaTree2.item(i,"values")[2] + " " + str(self.listaTree2.item(i,"values")[3])

        resp=messagebox.askyesno(message="¿Desea Eliminar a: "+ nomb, title="Eliminar registro")
        
        if resp:
            #reaizar el select de la línea seleccionada 
            datos=(self.IdVec,)
            self.registros = vecinos()
            eliminado=self.registros.eliminarreg(datos)
            if eliminado == 1:
                messagebox.showinfo(parent=self, title="Eliminar registro", message="Eliminado satisfactoriamente"+ " " + nomb)
                self.listaTree2.delete(curItem)
            else:
                messagebox.showinfo(parent=self, title="Eliminar registro", message="No se pudo eliminar"+ " " + nomb)


    def show_window2(self):
        
        if self.IdVec==0:
            messagebox.showinfo(parent=self, title="Seleccionar registro", message="Debe seleccionar registro a consultar")
            return
        
        #reaizar el select de la línea seleccionada
        query = "SELECT * FROM vecinos_temporal where id_vecino = '"+self.IdVec+"'"
        self.registros = vecinos()
        reg = self.registros.listarVecinos(query)
        
        #hacer matriz-arreglo con la información del select
        datos=[]
        for i in reg:
            datos.append(i)

        #print(len(datos[0]))


        from detalles_vecinos import InformacionVecinos
        t=tkr.Toplevel()
        t.configure(bg="#FCFCF9", bd=10)
        t.transient(self)
        InformacionVecinos(t, self.IdVec, datos)

    def show_grupofamnuevo(self):

        datos=[["" for j in range(28)] for i in range(1)]

        #print(datos[0][15])

        self.IdVec=0
        from detalles_vecinos import InformacionVecinos
        #messagebox.showinfo(message=self.IdVec)
        t=tkr.Toplevel()
        t.configure(bg="#FCFCF9", bd=10)
        t.transient(self)
        InformacionVecinos(t, str(self.IdVec), datos)
