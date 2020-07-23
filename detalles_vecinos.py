from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox
from datetime import date, datetime

class InformacionVecinos:
  def __init__(self,master, vecino):

    query = "SELECT * FROM vecinos_temporal where id_vecino = '"+vecino+"'"
    
    registros = vecinos()
    reg = registros.listarVecinos(query)

    master.title("Datos de:"+reg[0][2]+" "+reg[0][4])
    master.bind("<Return>", self.focus_next_window)

    self.cuaderno1 = tkrttk.Notebook(master)        
    self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
    self.carga_datos(reg)

  def focus_next_window(self,event):
    event.widget.tk_focusNext().focus()

  def formatofecha(self, event):
    #tener lista de meses y días en números para validar a fecha
    numdays = 31
    nummonth=12
    dayList = []
    monthList = []
    for x in range (0, numdays):
      dayList.append(x+1)
    for x in range (0, nummonth):
      monthList.append(x+1)
    #print(monthList)
  
    texto=self.entryfecn.get()

    if texto=="":
      return

    if len(texto)>10:
      messagebox.showinfo(parent=self.cuaderno1, message="No es una fecha válida")
      self.entryfecn.focus()
      return

    caract_1=0
    caract_11=0
    for i in texto:
      if i == "/":
        caract_1 +=1
        
      if not i.isdigit():    
        if i != "/":
          caract_11=1

    if caract_11==1: 
      messagebox.showinfo(parent=self.cuaderno1, message="No debe contener caracteres")
      self.entryfecn.focus()
      return

    if caract_1 != 2: 
      messagebox.showinfo(parent=self.cuaderno1, message="No esta en el formato de Fecha: D/M/AAAA")
      self.entryfecn.focus()
      return

    day, month, year = texto.split('/')

    if len(year) != 4:
      messagebox.showinfo(parent=self.cuaderno1, message="En el formato de Fecha: D/M/AAAA, el año no es correcto: 4 dígitos")
      self.entryfecn.focus()
      return

    if int(day) not in dayList: # valida sí existe
      messagebox.showinfo(parent=self.cuaderno1, message="En el formato de Fecha: D/M/AAAA, el día no es el rango")
      self.entryfecn.focus()
      return

    if int(month) not in monthList: # valida sí existe
      messagebox.showinfo(parent=self.cuaderno1, message="En el formato de Fecha: D/M/AAAA, el mes no es el rango")
      self.entryfecn.focus()
      return

  def carga_datos(self,reg1):
      self.pagina1 = tkr.Frame(self.cuaderno1)
      self.cuaderno1.add(self.pagina1, text="Datos Básicos")
      self.labelframe1=tkr.LabelFrame(self.pagina1, text=" ")        
      self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
      #self.labelframe1.place(width=300)

      linea=0
      self.label1=tkr.Label(self.labelframe1, text="Número de Cédula :")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.ced=tkr.StringVar()
      self.ced.set(reg1[0][1])
      self.entrynom1=tkr.Entry(self.labelframe1, textvariable=self.ced)
      self.entrynom1.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.label1=tkr.Label(self.labelframe1, text="1er Nombre :")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.nom1=tkr.StringVar()
      self.nom1.set(reg1[0][2])
      self.entrynom1=tkr.Entry(self.labelframe1, textvariable=self.nom1)
      self.entrynom1.grid(column=1, row=linea, padx=4, pady=4)

      self.label2=tkr.Label(self.labelframe1, text="2do Nombre :")
      self.label2.grid(column=2, row=linea, padx=4, pady=4)
      self.nom2=tkr.StringVar()
      self.nom2.set(reg1[0][3])
      self.entrynom2=tkr.Entry(self.labelframe1, textvariable=self.nom2)
      self.entrynom2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_ape=tkr.Label(self.labelframe1, text="1er Apellido:")        
      self.lbl_ape.grid(column=0, row=linea, padx=4, pady=4)
      self.apellido1=tkr.StringVar()
      self.apellido1.set(reg1[0][4])
      self.entryapell1=tkr.Entry(self.labelframe1, textvariable=self.apellido1)
      self.entryapell1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_ape2=tkr.Label(self.labelframe1, text="2do Apellido:")        
      self.lbl_ape2.grid(column=2, row=linea, padx=4, pady=4)
      self.apellido2=tkr.StringVar()
      self.apellido2.set(reg1[0][5])
      self.entryapell2=tkr.Entry(self.labelframe1, textvariable=self.apellido2)
      self.entryapell2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_tel1=tkr.Label(self.labelframe1, text="Nro Teléfono(1):")        
      self.lbl_tel1.grid(column=0, row=linea, padx=4, pady=4)
      self.tel1=tkr.StringVar()
      self.tel1.set(reg1[0][8])
      self.entrytel1=tkr.Entry(self.labelframe1, textvariable=self.tel1)
      self.entrytel1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_tel2=tkr.Label(self.labelframe1, text="Nro Teléfono(2):")        
      self.lbl_tel2.grid(column=2, row=linea, padx=4, pady=4)
      self.tel2=tkr.StringVar()
      self.tel2.set(reg1[0][9])
      self.entrytel2=tkr.Entry(self.labelframe1, textvariable=self.tel2)
      self.entrytel2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_fecn=tkr.Label(self.labelframe1, text="Fecha de Nacimiento:")        
      self.lbl_fecn.grid(column=0, row=linea, padx=4, pady=4)
      self.fecn=tkr.StringVar()
      self.fecn.set(reg1[0][16])
      fecha = datetime.strftime(reg1[0][16], '%m-%d-%Y')
      fecha = datetime.strptime(fecha, '%m-%d-%Y')
      formato = '%d/%m/%Y'
      fecha = datetime.strftime(fecha, formato)
      #print(type(fecha))
      #print(fecha)
      self.fecn.set(fecha)
      self.entryfecn=tkr.Entry(self.labelframe1, textvariable=self.fecn)
      self.entryfecn.bind("<FocusOut>", self.formatofecha)
      #self.entryfecn.bind("<Key>", self.formatofecha)
      #self.entryfecn.bind("<BackSpace>", lambda _: self.entryfecn.delete(tkr.END))
      self.entryfecn.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_email=tkr.Label(self.labelframe1, text="Correo Electrónico:")        
      self.lbl_email.grid(column=2, row=linea, padx=4, pady=4)
      self.email=tkr.StringVar()
      self.email.set(reg1[0][10])
      self.entryemail=tkr.Entry(self.labelframe1, textvariable=self.email)
      self.entryemail.grid(column=3, row=linea, padx=4, pady=4)
      
      linea+=1
      self.lbl_prof=tkr.Label(self.labelframe1, text="Oficio/Profesión:")        
      self.lbl_prof.grid(column=0, row=linea, padx=4, pady=4)
      self.prof=tkr.StringVar()
      self.prof.set(reg1[0][17])
      self.entryprof=tkr.Entry(self.labelframe1, textvariable=self.prof)
      self.entryprof.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_sexo=tkr.Label(self.labelframe1, text="Femenino/Masculino:")        
      self.lbl_sexo.grid(column=0, row=linea, padx=4, pady=4)
      self.sexo=tkr.IntVar()
      self.sexo.set(reg1[0][26])      
      self.entryfem=tkr.Radiobutton(self.labelframe1, text = "Femenino",variable=self.sexo, value="F")
      self.entryfem.grid(column=1, row=linea, padx=4, pady=4)
      self.entrymasc=tkr.Radiobutton(self.labelframe1, text = "Masculino",variable=self.sexo, value="M")
      self.entrymasc.grid(column=2, row=linea, padx=4, pady=4)

      self.obsmedicotro()

  def obsmedicotro(self): 
      self.pagina2 = tkr.Frame(self.cuaderno1)
      self.cuaderno1.add(self.pagina2, text="Observaciones/Medicamentos/Antecedentes")
      self.labelframe2=tkr.LabelFrame(self.pagina2, text=" ")        
      self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
   
      #self.boton1=tkr.Button(self.labelframe1, text="Confirmar", command=self.agregar)
      #self.boton1.grid(column=1, row=2, padx=4, pady=4)
