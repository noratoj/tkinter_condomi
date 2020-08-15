import tkinter as tkr
from tkinter import StringVar, IntVar, Frame, Label, Entry, Checkbutton, Button, Radiobutton
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox
from views import *

"""
Permite tener todas las actividades referentes a lo relacionado con el CRUD de la tabla TBREFERENCIA.

"""

class VentanaManejoRef(tkr.Toplevel):
    linea1=0
    def __init__(self, parent, usu, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        global linea1
        self.parent = parent
        self.tamagnoletra = ("Arial",10,"bold")
        self.back1="#525252" #8cabbe
        self.button1="#59c9b9"
        self.fore="white"
        self.foreblack="black"
        self.configure(bg="#525252")
        self.registros = vecinos()
        self.title("Administración")
        self.geometry("1400x400+0+0")
        self.protocol("WM_DELETE_WINDOW", self.volver)
        
        self.cuaderno1 = tkrttk.Notebook(self)        
        tkrttk.Style().configure("TNotebook", background=self.back1)

        self.pagina1 = tkr.Frame(self.cuaderno1, background=self.back1)
        self.cuaderno1.add(self.pagina1, text="Administración de tablas")
        self.labelframe1=tkr.LabelFrame(self.pagina1, text="Tablas")        
        self.labelframe1.configure( background=self.back1)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.frameBuscar=Frame(self.labelframe1, bd=1, background=self.back1)
        self.frametabla=Frame(self.labelframe1, bd=1, background=self.back1)

        self.frameBuscar.grid(column=0, row=0, padx=5, pady=10)
        self.frametabla.grid(column=1, row=0, padx=5, pady=10)

        #Hacer un query para llamar la información de las Tores
        query = "SELECT distinct(tabla) FROM tbreferencia"
        registros = vecinos()
        self.ref = registros.listarVecinos(query)

        #mostrar la lista en checkbox las opciones para filtrar por edificio
        self.arreglo=[]
        self.variab=[]
        self.linea1=0

        self.v=StringVar()
        self.v.set("")

        
        for val, period in enumerate(self.ref):            
            Radiobutton(self.frameBuscar, 
                    text=period, 
                    #indicatoron =0,
                    padx=20,
                    variable=self.v, 
                    command=self.selecc, 
                    value=period,
                    highlightbackground=self.back1,
                    background=self.back1, 
                    foreground=self.fore,
                    font=self.tamagnoletra,
                    selectcolor='black').grid(row=self.linea1, column=0, sticky="w")
            self.linea1=self.linea1+1

        #crear el FRame que contendrá los campos de la tabla maestra
        self.labelframe2=tkr.LabelFrame(self.pagina1)        
        self.labelframe2.configure( background=self.back1, highlightbackground=self.back1) #'height=200'
        self.labelframe2.grid(column=1, row=0, padx=5, pady=10)

        linea=0
        self.label1=tkr.Label(self.labelframe2,text="Contador :", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
        self.label1.grid(column=0, row=linea, padx=4, pady=4)
        self.con=tkr.StringVar()
        self.con.set("")
        self.entrycon=tkr.Entry(self.labelframe2, textvariable=self.con)      
        self.entrycon.grid(column=1, row=linea, padx=4, pady=4)

        linea+=1
        self.label1=tkr.Label(self.labelframe2,text="Tabla :", bg=self.back1, fg=self.fore, font=self.tamagnoletra, width=20, anchor="e")
        self.label1.grid(column=0, row=linea, padx=4, pady=4)
        self.tabl=tkr.StringVar()
        self.tabl.set("")
        self.entrytabl=tkr.Entry(self.labelframe2, textvariable=self.tabl)
        self.entrytabl.bind("<FocusOut>", self.convertirMayus)
        self.entrytabl.grid(column=1, row=linea, padx=4, pady=4)

        linea+=1
        self.label2=tkr.Label(self.labelframe2, text="Descripción: ", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
        self.label2.grid(column=0, row=linea, padx=4, pady=4)
        self.desc=tkr.StringVar()
        self.desc.set("")
        self.entrydesc=tkr.Entry(self.labelframe2, textvariable=self.desc)
        self.entrydesc.bind("<FocusOut>", self.convertirMayus)
        self.entrydesc.grid(column=1, row=linea, padx=4, pady=4)


        linea+=1
        self.lbl_ord=tkr.Label(self.labelframe2, text="Orden:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
        self.lbl_ord.grid(column=0, row=linea, padx=4, pady=4)
        self.orden=tkr.StringVar()
        self.orden.set("")
        self.entryorden=tkr.Entry(self.labelframe2, textvariable=self.orden)
        self.entryorden.grid(column=1, row=linea, padx=4, pady=4)

        linea+=1
        #Boton para actualizar la información
        self.button1=tkr.Button(self.labelframe2, command=self.updateReg, text='Actualizar', highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        self.button1.grid(column=0, row=linea, padx=4, pady=4)

        #Boton para eliminar datos de la lista de vecinos seleccionado
        button1elim= tkr.Button(self.labelframe2,text='Eliminar',command=self.eliminarreg, highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
        button1elim.grid(column=1, row=linea, padx=4, pady=4)

        #Boton para CREAR NUEVA información
        self.button3 = tkr.Button(self.labelframe2, command= self.inicialiarVariables, text='Nuevo', highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
        self.button3.grid(row=linea, column=2)
        self.linea1=linea

        #llamar para crear el treeview de los registrs de TBREFERENCIA
        treeview_1 = vistas()
        self.listaTree_rol=treeview_1.treeview_referencia(self.frametabla)

        self.listaTree_rol.bind('<ButtonRelease-1>', self.selectItem)

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

    def selecc(self):
        tabla_sel=self.v.get()
        query = "SELECT ref.*, tb1.campo_des FROM tbreferencia ref left join tbreferencia tb1 on ref.relacionado_con = tb1.contador where ref.tabla= '%s'" % tabla_sel
        reg = self.registros.listarVecinos(query)
        self.listaTree_rol.delete(*self.listaTree_rol.get_children())
        for i in reg:
            self.listaTree_rol.insert('','end', value=(i[0],i[1],i[2],i[3],i[4],i[6]))

    def convertirMayus(self,event):
        self.tabl.set(self.entrytabl.get().upper())
        self.desc.set(self.entrydesc.get().upper())


    def inicialiarVariables(self):
        if self.entrytabl.get() == "":
            self.tabl.set("")
        self.desc.set("")
        self.orden.set("")
        self.con.set("")
        self.entrydesc.focus()
        self.button3.place_forget()
        self.button4 = tkr.Button(self.labelframe2,text='Grabar Campo', command=self.InsertReg,highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
        self.button4.grid(row=self.linea1, column=2)


    def selectItem(self, event):
      curItem = self.listaTree_rol.selection()
      for i in curItem:
          self.contador=self.listaTree_rol.item(i,"values")[0]
          #reaizar el select de la línea seleccionada
          query = "SELECT * FROM tbreferencia where id_contador = '"+self.contador+"'"
          self.registros = vecinos()
          reg = self.registros.listarVecinos(query)
          self.con.set(reg[0][1])
          self.tabl.set(reg[0][2])
          self.desc.set(reg[0][3])
          self.orden.set(reg[0][4])

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def eliminarreg(self):
        
        texto=self.entrycon.get()
        nomb=self.entrydesc.get()
        if texto=="":
            messagebox.showinfo(parent=self.cuaderno1, title="Eliminar registro", message="Debe seleccionar registro maestro a eliminar")
            return
        
        curItem = self.listaTree_rol.selection()
        resp=messagebox.askyesno(parent=self.cuaderno1, message="¿Desea Eliminar a: "+ nomb, title="Eliminar registro")
        
        if resp:
            #reaizar el select de la línea seleccionada 
            datos=(texto,)
            self.registros = vecinos()
            eliminado=self.registros.eliminarref(datos)
            if eliminado == 1:
                messagebox.showinfo(parent=self.cuaderno1, title="Eliminar registro", message="Eliminado satisfactoriamente"+ " " + nomb)
                self.listaTree_rol.delete(curItem)
            else:
                messagebox.showinfo(parent=self.cuaderno1, title="Eliminar registro", message="No se pudo eliminar"+ " " + nomb)



    def InsertReg(self):
        updateAction=1
        self.informacionGrabar(updateAction)


    def updateReg(self):
        updateAction=2
        self.informacionGrabar(updateAction)

    def validar_text(self):

        texto=self.entrytabl.get()

        if texto=="":
            messagebox.showinfo(parent=self.cuaderno1, title="Validación de Tabla", message="Nombre de tabla no debe estar vacio")
            self.entrytabl.focus()
            return False

        texto=self.entrydesc.get()

        if texto=="":
            messagebox.showinfo(parent=self.cuaderno1, title="Validación de Descripción", message="Descripción no debe estar vacio")
            self.entrydesc.focus()
            return False

        texto=self.entryorden.get()

        if texto=="":
            messagebox.showinfo(parent=self.cuaderno1, title="Validación de Orden", message="Orden no debe estar vacio")
            self.entryorden.focus()
            return False

        return True


    def informacionGrabar(self, action):
        #print(self.sexo.get())
        valid =self.validar_text()

        if valid == False:
            return
        
        if action ==1: #insert
            query = "Select id_contador from tbreferencia order by id_contador DESC limit 1"
            string4=self.registros.obtener_cuantos(query)
            self.contador=int(string4[0][0])+1
            self.con.set(self.contador)

            datos = (self.con.get(), self.entrytabl.get(), self.entrydesc.get(), self.entryorden.get(),0)
        
        if action ==2: #update
            datos = (self.entrytabl.get(), self.entrydesc.get(), self.entryorden.get(),self.contador)

        if action ==1:
            self.registros.insertref(datos)
            messagebox.showinfo(parent=self.cuaderno1, title="Guardando Información", message="Información creada satisfactoriamente")
        
        if action ==2: 
            self.registros.updateref(datos)
            messagebox.showinfo(parent=self.cuaderno1, title="Guardando Información", message="Información actualizada satisfactoriamente")

        tabla_sel=self.entrytabl.get()
        query = "SELECT ref.*, tb1.campo_des FROM tbreferencia ref left join tbreferencia tb1 on ref.relacionado_con = tb1.contador where ref.tabla= '%s'" % tabla_sel
        reg = self.registros.listarVecinos(query)
        self.listaTree_rol.delete(*self.listaTree_rol.get_children())
        for i in reg:
            self.listaTree_rol.insert('','end', value=(i[0],i[1],i[2],i[3],i[4],i[6]))

        return
