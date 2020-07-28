from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox
from datetime import date, datetime

class InformacionVecinos:
  def __init__(self,master, vecino):

    query = "SELECT * FROM vecinos_temporal where id_vecino = '"+vecino+"'"
    
    self.registros = vecinos()
    reg = self.registros.listarVecinos(query)

    master.title("Datos de:"+reg[0][2]+" "+reg[0][4])

    #permitir la tecla intro / enter dentro de la ventana
    master.bind("<Return>", self.focus_next_window)

    self.cuaderno1 = tkrttk.Notebook(master)        
    tkrttk.Style().configure("TNotebook", background="white")
    self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
    self.carga_datos(reg)

  def construir_cadena(self, cadena_1):
      string2_1=cadena_1[0][0]
      string_length=len(string2_1)+60
      string3 = string2_1.ljust(string_length)
      return(string3)

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

  def lista(self,reg, listaTree1):
    listaTree1.delete(*listaTree1.get_children())
    for i in reg:
        listaTree1.insert('','end', value=(i[0],i[2]+" "+i[3],i[4]+" "+i[5], i[28]))

  def callbackFunc(self,event):
    print(self.cmbedif.get())

  def carga_datos(self,reg1):
      self.pagina1 = tkr.Frame(self.cuaderno1, bg="white")
      self.cuaderno1.add(self.pagina1, text="Datos Básicos")
      self.labelframe1=tkr.LabelFrame(self.pagina1)        
      self.labelframe1.configure(bg="#FCFCF9")
      self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

      #linea+=1
      self.labelframe12=tkr.Frame(self.pagina1)
      top_frame = tkr.Frame(self.pagina1, bg='cyan', width=450, height=50, pady=3)
      center = tkr.Frame(self.pagina1, bg='blue', width=650, height=40, padx=3, pady=3)
      #btm_frame = tkr.Frame(self.pagina1, bg='white', width=450, height=45, pady=3)
      #btm_frame2 = tkr.Frame(self.pagina1, bg='lavender', width=450, height=60, pady=3)
      top_frame.grid(column=1, row=0)
      center.grid(column=0, row=1)
      #self.labelframe12.configure(bg="red") #bg="#FCFCF9"
      #self.labelframe12.grid(column=6, row=linea, padx=5, pady=10)


      linea=0
      self.label1=tkr.Label(self.labelframe1, text="Número de Cédula :", bg="#FCFCF9")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.ced=tkr.StringVar()
      self.ced.set(reg1[0][1])
      self.entrynom1=tkr.Entry(self.labelframe1, textvariable=self.ced)
      self.entrynom1.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.label1=tkr.Label(self.labelframe1, text="1er Nombre :", bg="#FCFCF9")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.nom1=tkr.StringVar()
      self.nom1.set(reg1[0][2])
      self.entrynom1=tkr.Entry(self.labelframe1, textvariable=self.nom1)
      self.entrynom1.grid(column=1, row=linea, padx=4, pady=4)

      self.label2=tkr.Label(self.labelframe1, text="2do Nombre :", bg="#FCFCF9")
      self.label2.grid(column=2, row=linea, padx=4, pady=4)
      self.nom2=tkr.StringVar()
      self.nom2.set(reg1[0][3])
      self.entrynom2=tkr.Entry(self.labelframe1, textvariable=self.nom2)
      self.entrynom2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_ape=tkr.Label(self.labelframe1, text="1er Apellido:", bg="#FCFCF9")        
      self.lbl_ape.grid(column=0, row=linea, padx=4, pady=4)
      self.apellido1=tkr.StringVar()
      self.apellido1.set(reg1[0][4])
      self.entryapell1=tkr.Entry(self.labelframe1, textvariable=self.apellido1)
      self.entryapell1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_ape2=tkr.Label(self.labelframe1, text="2do Apellido:", bg="#FCFCF9")        
      self.lbl_ape2.grid(column=2, row=linea, padx=4, pady=4)
      self.apellido2=tkr.StringVar()
      self.apellido2.set(reg1[0][5])
      self.entryapell2=tkr.Entry(self.labelframe1, textvariable=self.apellido2)
      self.entryapell2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_tel1=tkr.Label(self.labelframe1, text="Nro Teléfono(1):", bg="#FCFCF9")        
      self.lbl_tel1.grid(column=0, row=linea, padx=4, pady=4)
      self.tel1=tkr.StringVar()
      self.tel1.set(reg1[0][8])
      self.entrytel1=tkr.Entry(self.labelframe1, textvariable=self.tel1)
      self.entrytel1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_tel2=tkr.Label(self.labelframe1, text="Nro Teléfono(2):", bg="#FCFCF9")        
      self.lbl_tel2.grid(column=2, row=linea, padx=4, pady=4)
      self.tel2=tkr.StringVar()
      self.tel2.set(reg1[0][9])
      self.entrytel2=tkr.Entry(self.labelframe1, textvariable=self.tel2)
      self.entrytel2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_fecn=tkr.Label(self.labelframe1, text="Fecha de Nacimiento:", bg="#FCFCF9")        
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

      self.lbl_email=tkr.Label(self.labelframe1, text="Correo Electrónico:", bg="#FCFCF9")        
      self.lbl_email.grid(column=2, row=linea, padx=4, pady=4)
      self.email=tkr.StringVar()
      self.email.set(reg1[0][10])
      self.entryemail=tkr.Entry(self.labelframe1, textvariable=self.email)
      self.entryemail.grid(column=3, row=linea, padx=4, pady=4)
      
      linea+=1
      self.lbl_prof=tkr.Label(self.labelframe1, text="Oficio/Profesión:", bg="#FCFCF9")        
      self.lbl_prof.grid(column=0, row=linea, padx=4, pady=4)
      self.prof=tkr.StringVar()
      self.prof.set(reg1[0][17])
      self.entryprof=tkr.Entry(self.labelframe1, textvariable=self.prof)
      self.entryprof.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_sexo=tkr.Label(self.labelframe1, text="Femenino/Masculino:", bg="#FCFCF9")        
      self.lbl_sexo.grid(column=0, row=linea, padx=4, pady=4)
      self.sexo=tkr.IntVar()
      self.sexo.set(reg1[0][26])      
      self.entryfem=tkr.Radiobutton(self.labelframe1, text = "Femenino",variable=self.sexo, value="F", bg="#FCFCF9")
      self.entryfem.grid(column=1, row=linea, padx=4, pady=4)
      self.entrymasc=tkr.Radiobutton(self.labelframe1, text = "Masculino",variable=self.sexo, value="M", bg="#FCFCF9")
      self.entrymasc.grid(column=2, row=linea, padx=4, pady=4)

      #Obtener la descripcion de la torre/edificio
      self.idtorre=tkr.IntVar()
      self.idtorre.set(reg1[0][13])
      string2=self.registros.obtener_desc(reg1[0][13])
      string3=self.construir_cadena(string2) 
      #para setear el combo
      string4=string3+str(reg1[0][13])

      #colocar la torre, piso, apto y grupo Familiar lista

      #self.pagina3 = tkr.Frame(self.cuaderno1,bg="white")
      #self.cuaderno1.add(self.pagina3, text="Edificio/Piso/Apto")
      #self.labelframe3=tkr.LabelFrame(self.pagina3, bg="white")        
      #self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

      self.lbl_edif=tkr.Label(top_frame, text="Edificio/Torre:", bg="#FCFCF9")        
      self.lbl_edif.grid(column=0, row=0, padx=4, pady=4)
      self.cmbedif=tkrttk.Combobox(top_frame, state="readonly")
      self.cmbedif["value"]=self.registros.combo_add("TORRE")
      self.cmbedif.set(string4)
      self.cmbedif.bind("<<ComboboxSelected>>", self.callbackFunc)
      self.cmbedif.grid(column=1, row=0, padx=4, pady=4)


      #Obtener la descripcion de la torre/edificio
      self.idpiso=tkr.IntVar()
      self.idpiso.set(reg1[0][14])
      string2=self.registros.obtener_desc(reg1[0][14])
      string3=self.construir_cadena(string2) 
      #para setear el combo
      string4=string3+str(reg1[0][14])


      self.lbl_piso=tkr.Label(top_frame, text="Piso:", bg="#FCFCF9")        
      self.lbl_piso.grid(column=0, row=1, padx=4, pady=4)
      self.cmbpiso=tkrttk.Combobox(top_frame, state="readonly")
      self.cmbpiso["value"]=self.registros.combo_add("PISO")      
      self.cmbpiso.set(string4)
      self.cmbpiso.bind("<<ComboboxSelected>>", self.callbackFunc)
      self.cmbpiso.grid(column=1, row=1, padx=4, pady=4)

      self.lbl_apto=tkr.Label(top_frame, text="Apartamento/Ubicación:", bg="#FCFCF9")        
      self.lbl_apto.grid(column=0, row=2, padx=4, pady=4)
      self.apto=tkr.StringVar()
      self.apto.set(reg1[0][15])
      self.entryapto=tkr.Entry(top_frame, textvariable=self.apto)
      self.entryapto.grid(column=1, row=2, padx=4, pady=4)

      #crear la estructura familiar y el cargo

      #Obtener la descripcion de la torre/edificio
      self.idpiso=tkr.IntVar()
      self.idpiso.set(reg1[0][14])
      string2=self.registros.obtener_desc(reg1[0][6])
      string3=self.construir_cadena(string2) 
      #para setear el combo
      string4=string3+str(reg1[0][6])
      #print(string4)  

      self.labelframe4=tkr.LabelFrame(top_frame,bg="white")        
      self.labelframe4.grid(column=0, columnspan=2, row=3, padx=5, pady=10)
      self.lblrol=tkr.Label(self.labelframe4, text="Rol en la Familia:",bg="white")        
      self.lblrol.grid(column=0, row=0, padx=4, pady=4)
      self.cmbrol=tkrttk.Combobox(self.labelframe4, state="readonly")
      self.cmbrol["value"]=self.registros.combo_add("MIEMBROS")      
      self.cmbrol.set(string4)
      self.cmbrol.grid(column=1, row=0, padx=4, pady=4)

      self.lbl_numfam=tkr.Label(self.labelframe4, text="Nro miembros en la Familia:",bg="white")        
      self.lbl_numfam.grid(column=0, row=1, padx=4, pady=4)
      self.num=tkr.IntVar()
      query = "SELECT count(*) FROM vecinos_temporal tb1 where tb1.grupo_fam= %s" % reg1[0][23]
      string4=self.registros.obtener_cuantos(query)
      self.num.set(string4[0][0])
      self.lbl_numfam_2=tkr.Label(self.labelframe4, textvariable=self.num, text=string4)
      self.lbl_numfam_2.grid(column=1, row=1, padx=4, pady=4)

      #crear listado de los que habian la residencia
      self.labelframe5=tkr.LabelFrame(center)        
      self.labelframe5.grid(column=0, row=3, padx=5, pady=10)

      """ Hacer TREEVIEW lista """
      self.listaTree_rol = tkrttk.Treeview(self.labelframe5, height="14", selectmode='browse')

      self.listaTree_rol["columns"] = ("ID","NOMBRE","APELLIDO","ROL")
      self.listaTree_rol.column("ID", width=80, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("NOMBRE", width=240, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("APELLIDO", width=240, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("ROL", width=80, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("#0", width=0, stretch=False)

      self.listaTree_rol.grid(column=0, row=2, padx=4, pady=4)

      self.listaTree_rol.heading("ID", text="ID")
      self.listaTree_rol.heading("NOMBRE", text="Nombre")
      self.listaTree_rol.heading("APELLIDO", text="Apellido")
      self.listaTree_rol.heading("ROL", text="Rol")

      query = "SELECT vec.*, tb1.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_miembro = tb1.contador where vec.grupo_fam= %s" % reg1[0][23]
      reg = self.registros.listarVecinos(query)
      self.lista(reg, self.listaTree_rol)

      self.pagina2 = tkr.Frame(self.cuaderno1,bg="white")
      self.cuaderno1.add(self.pagina2, text="Observaciones/Medicamentos/Antecedentes")
      self.labelframe2=tkr.LabelFrame(self.pagina2, text=" ")        
      self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
   
      self.lbl_medicam=tkr.Label(self.labelframe2, text="Medicamentos:")        
      self.lbl_medicam.grid(column=0, row=1, padx=4, pady=4)
      #self.medicam=tkr.StringVar()
      #self.prof.set(reg1[0][17])
      self.textmed=tkr.Text(self.labelframe2)
      self.textmed.config(width=130,height=10)
      self.textmed.grid(column=1, row=1, padx=4, pady=4)
