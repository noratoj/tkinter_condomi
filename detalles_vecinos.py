from tkinter import StringVar, IntVar, Frame, Label, Entry, Checkbutton, Button
#from tkinter import *
import tkinter as tkr
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox
from datetime import date, datetime

class InformacionVecinos():
  
  grupo_familiar=0
  vecino1=0
  def __init__(self,master, vecino, datos):
    global master_1, vecino1, grupo_familiar
    self.tamagnoletra = ("Arial",10,"bold")
    self.back1="#525252" #8cabbe
    self.button1="#59c9b9"
    self.fore="white"
    self.foreblack="black"
    self.registros = vecinos()
    if vecino != "0":
      master.title("Datos de:"+datos[0][2]+" "+datos[0][4])
      self.vecino1 =vecino
    else:
      vecino1=0
      master.title("Creación de Usuario")

    master.configure(background=self.back1)
    #permitir la tecla intro / enter dentro de la ventana
    master.bind("<Return>", self.focus_next_window)
    master_1 = master
    #master.protocol("WM_DELETE_WINDOW", self.volver)

    self.cuaderno1 = tkrttk.Notebook(master)        
    tkrttk.Style().configure("TNotebook", background=self.back1)
    self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
    self.carga_datos(datos)

  def construir_cadena(self, cadena_1):
      string2_1=cadena_1[0][0]
      string_length=len(string2_1)+60
      string3 = string2_1.ljust(string_length)
      return(string3)

  def volver(self):
      master_1.destroy()

  def focus_next_window(self,event):
    event.widget.tk_focusNext().focus()

  def validar_text(self):

    texto=self.entrynom1.get()

    if texto=="":
      messagebox.showinfo(parent=self.cuaderno1, title="Validación de 1er Nombre", message="1er Nombre no debe estar vacio")
      self.entrynom1.focus()
      return False

    texto=self.entryapell1.get()

    if texto=="":
      messagebox.showinfo(parent=self.cuaderno1, title="Validación de 1er Apellido", message="1er Apellido no debe estar vacio")
      self.entryapell1.focus()
      return False

    texto=self.entryapto.get()

    if texto=="":
      messagebox.showinfo(parent=self.cuaderno1, title="Validación de Sitio o Apartamento", message="Debe asignar el número o sitio del apartamento o ubicación")
      self.entryapto.focus()
      return False

    return True

  def convertirMayus(self, event):
  
    self.nom1.set(self.entrynom1.get().upper())
    self.nom2.set(self.entrynom2.get().upper())
    self.apellido1.set(self.entryapell1.get().upper())
    self.apellido2.set(self.entryapell2.get().upper())
    self.prof.set(self.entryprof.get().upper())
    self.apto.set(self.entryapto.get().upper())
    #self.textant.get("1.0", 'end').upper()

  def inicialiarVariables(self):  
    self.nom1.set("")
    self.nom2.set("")
    self.apellido1.set("")
    self.apellido2.set("")
    self.prof.set("")
    self.ced.set("")
    self.tel1.set("")
    self.tel2.set("")
    self.fecn.set("")
    self.sexo.set("")      
    self.button3.place_forget()
    self.button4 = tkr.Button(self.pagina1,text='Grabar Integrante', command=self.InsertInteg,highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
    self.button4.place(x=900, y=530, height=20)


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
      messagebox.showinfo(parent=self.cuaderno1, title="Validar fecha", message="No es una fecha válida")
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
      messagebox.showinfo(parent=self.cuaderno1, title="Validar fecha", message="No debe contener caracteres")
      self.entryfecn.focus()
      return

    if caract_1 != 2: 
      messagebox.showinfo(parent=self.cuaderno1, title="Validar fecha", message="No esta en el formato de Fecha: D/M/AAAA")
      self.entryfecn.focus()
      return

    day, month, year = texto.split('/')

    if len(year) != 4:
      messagebox.showinfo(parent=self.cuaderno1, title="Validar fecha", message="En el formato de Fecha: D/M/AAAA, el año no es correcto: 4 dígitos")
      self.entryfecn.focus()
      return

    if int(day) not in dayList: # valida sí existe
      messagebox.showinfo(parent=self.cuaderno1, title="Validar fecha", message="En el formato de Fecha: D/M/AAAA, el día no es el rango")
      self.entryfecn.focus()
      return

    if int(month) not in monthList: # valida sí existe
      messagebox.showinfo(parent=self.cuaderno1, message="En el formato de Fecha: D/M/AAAA, el mes no es el rango")
      self.entryfecn.focus()
      return

  def selectItem(self, event):
      curItem = self.listaTree_rol.selection()
      for i in curItem:
          self.vecino1=self.listaTree_rol.item(i,"values")[0]
          #messagebox.showinfo(message=self.vecino1)

          #reaizar el select de la línea seleccionada
          query = "SELECT * FROM vecinos_temporal where id_vecino = '"+self.vecino1+"'"
          self.registros = vecinos()
          reg = self.registros.listarVecinos(query)
          self.ced.set(reg[0][1])
          self.nom1.set(reg[0][2])
          self.nom2.set(reg[0][3])
          self.apellido1.set(reg[0][4])
          self.apellido2.set(reg[0][5])
          self.prof.set(reg[0][17])
          self.tel1.set(reg[0][8])
          self.tel2.set(reg[0][9])
          self.fecn.set(reg[0][16])
          #print(reg1[0][16])
          if reg[0][16] != None and reg[0][16] != "" :
            fecha = datetime.strftime(reg[0][16], '%m-%d-%Y')
            fecha = datetime.strptime(fecha, '%m-%d-%Y')
            formato = '%d/%m/%Y'
            fecha = datetime.strftime(fecha, formato)
          else:
            fecha = ""
          #print(type(fecha))
          #print(fecha)
          self.fecn.set(fecha)
          self.sexo.set(reg[0][26])      



  def updateVec(self):
    texto=self.entryced.get()
    if texto!="":
      query = "SELECT * FROM vecinos_temporal tb1 where tb1.nro_cedula= %s" % texto
      string4=self.registros.listarVecinos(query)
      if len(string4) == 1:
          if int(string4[0][0]) != int(self.vecino1):
            messagebox.showinfo(parent=self.cuaderno1, title="Validación de ID-Cédula", message="NO debe existir un mismo número de ID(Cédula)")
            self.entryced.focus()
            return False

    updateAction=2
    self.informacionGrabar(updateAction)
  
  def InsertInteg(self):
    texto=self.entryced.get()
    if texto!="":
      query = "SELECT * FROM vecinos_temporal tb1 where tb1.nro_cedula= %s" % texto
      string4=self.registros.listarVecinos(query)
      if len(string4) == 1:
          messagebox.showinfo(parent=self.cuaderno1, title="Validación de ID-Cédula", message="No debe existir un mismo número de ID(Cédula)")
          self.entryced.focus()
          return False

    updateAction=3
    self.informacionGrabar(updateAction)

  def InsertVec(self):
    updateAction=1
    self.informacionGrabar(updateAction)

  def informacionGrabar(self, action):
    #print(self.sexo.get())
    valid =self.validar_text()

    if valid == False:
      return
      
    #obtener el id d edificio, piso y rol
    piso= self.cmbpiso.get()[-10:].strip()
    edif= self.cmbedif.get()[-10:].strip()
    rol= self.cmbrol.get()[-10:].strip()
    if self.fecn.get() != "":
        formato = '%Y/%m/%d'
        fecha_ins = datetime.strftime(datetime.strptime(self.fecn.get(),'%d/%m/%Y'), formato)
    else:
      fecha_ins = "1900-01-01"

    if action ==1: #insert
      query = "Select grupo_fam from vecinos_temporal order by grupo_fam DESC limit 1"
      string4=self.registros.obtener_cuantos(query)
      self.grupo_familiar=int(string4[0][0])+1

      datos = (self.ced.get(), self.entrynom1.get(), self.entrynom2.get(), self.entryapell1.get(), self.entryapell2.get(),
           self.entrytel1.get(), self.entrytel2.get(), fecha_ins, self.entryemail.get(), 
           self.entryprof.get(), self.sexo.get(),edif,piso,self.entryapto.get(),rol,self.grupo_familiar,
           self.textmed.get("1.0", 'end'), self.textobs.get("1.0", 'end'), self.textant.get("1.0", 'end'))
    
    if action ==2: #update
      datos = (self.ced.get(), self.entrynom1.get(), self.entrynom2.get(), self.entryapell1.get(), self.entryapell2.get(),
           self.entrytel1.get(), self.entrytel2.get(), fecha_ins, self.entryemail.get(), 
           self.entryprof.get(), self.sexo.get(),edif,piso,self.entryapto.get(),rol,self.grupo_familiar,
           self.textmed.get("1.0", 'end'), self.textobs.get("1.0", 'end'), self.textant.get("1.0", 'end'),self.vecino1)

    if action ==3: #insert integrante
      datos = (self.ced.get(), self.entrynom1.get(), self.entrynom2.get(), self.entryapell1.get(), self.entryapell2.get(),
           self.entrytel1.get(), self.entrytel2.get(), fecha_ins, self.entryemail.get(), 
           self.entryprof.get(), self.sexo.get(),edif,piso,self.entryapto.get(),rol,self.grupo_familiar,
           self.textmed.get("1.0", 'end'), self.textobs.get("1.0", 'end'), self.textant.get("1.0", 'end'))          
      action =1



    if action ==1:
      self.registros.insertvec(datos)
      messagebox.showinfo(parent=self.cuaderno1, title="Guardando Información", message="Registro creado satisfactoriamente")
      query = "Select id_vecino from vecinos_temporal order by id_vecino DESC limit 1"
      string4=self.registros.obtener_cuantos(query)
      self.vecino1=int(string4[0][0])
      print(self.vecino1)
    
    if action ==2: 
      self.registros.updatevec(datos)
      messagebox.showinfo(parent=self.cuaderno1, title="Guardando Información", message="Información actualizada satisfactoriamente")

    query = "SELECT vec.*, tb1.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_miembro = tb1.contador where vec.grupo_fam= %s" % self.grupo_familiar

    reg = self.registros.listarVecinos(query)
    self.lista(reg, self.listaTree_rol)

    return

  def lista(self,reg, listaTree1):
    listaTree1.delete(*listaTree1.get_children())
    for i in reg:
        listaTree1.insert('','end', value=(i[0],i[1],i[2]+" "+i[3],i[4]+" "+i[5], i[28]))

  def callbackFunc(self,event):
    pass

  def carga_datos(self,reg1):
      self.pagina1 = tkr.Frame(self.cuaderno1, background=self.back1)
      self.cuaderno1.add(self.pagina1, text="Datos Básicos")
      self.labelframe1=tkr.LabelFrame(self.pagina1)        
      self.labelframe1.configure( background=self.back1)

      self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

      top_frame = tkr.Frame(self.pagina1, background=self.back1, width=450, height=50, pady=3)
      center = tkr.Frame(self.pagina1, bg=self.back1, width=650, height=40, padx=3, pady=3)
      tkr.Label(center, text="Grupo Familiar", bg=self.button1, width = "30", height="0", font=("Arial",12,"bold")).grid(row=0, column=0)
      top_frame.grid(column=1, row=0)
      center.grid(column=0, row=1)

      linea=0
      self.label1=tkr.Label(self.labelframe1,text="Número de Cédula :", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.ced=tkr.StringVar()
      self.ced.set(reg1[0][1])
      self.entryced=tkr.Entry(self.labelframe1, textvariable=self.ced)      
      self.entryced.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.label1=tkr.Label(self.labelframe1,text="1er Nombre :", bg=self.back1, fg=self.fore, font=self.tamagnoletra, width=20, anchor="e")
      self.label1.grid(column=0, row=linea, padx=4, pady=4)
      self.nom1=tkr.StringVar()
      self.nom1.set(reg1[0][2])
      self.entrynom1=tkr.Entry(self.labelframe1, textvariable=self.nom1)
      self.entrynom1.bind("<FocusOut>", self.convertirMayus)
      self.entrynom1.grid(column=1, row=linea, padx=4, pady=4)

      self.label2=tkr.Label(self.labelframe1, text="2do Nombre :", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.label2.grid(column=2, row=linea, padx=4, pady=4)
      self.nom2=tkr.StringVar()
      self.nom2.set(reg1[0][3])
      self.entrynom2=tkr.Entry(self.labelframe1, textvariable=self.nom2)
      self.entrynom2.bind("<FocusOut>", self.convertirMayus)
      self.entrynom2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_ape=tkr.Label(self.labelframe1, text="1er Apellido:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_ape.grid(column=0, row=linea, padx=4, pady=4)
      self.apellido1=tkr.StringVar()
      self.apellido1.set(reg1[0][4])
      self.entryapell1=tkr.Entry(self.labelframe1, textvariable=self.apellido1)
      self.entryapell1.bind("<FocusOut>", self.convertirMayus)
      self.entryapell1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_ape2=tkr.Label(self.labelframe1, text="2do Apellido:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_ape2.grid(column=2, row=linea, padx=4, pady=4)
      self.apellido2=tkr.StringVar()
      self.apellido2.set(reg1[0][5])
      self.entryapell2=tkr.Entry(self.labelframe1, textvariable=self.apellido2)
      self.entryapell2.bind("<FocusOut>", self.convertirMayus)
      self.entryapell2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_tel1=tkr.Label(self.labelframe1, text="Nro Teléfono(1):", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_tel1.grid(column=0, row=linea, padx=4, pady=4)
      self.tel1=tkr.StringVar()
      self.tel1.set(reg1[0][8])
      self.entrytel1=tkr.Entry(self.labelframe1, textvariable=self.tel1)
      self.entrytel1.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_tel2=tkr.Label(self.labelframe1, text="Nro Teléfono(2):", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_tel2.grid(column=2, row=linea, padx=4, pady=4)
      self.tel2=tkr.StringVar()
      self.tel2.set(reg1[0][9])
      self.entrytel2=tkr.Entry(self.labelframe1, textvariable=self.tel2)
      self.entrytel2.grid(column=3, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_fecn=tkr.Label(self.labelframe1, text="Fecha de Nacimiento:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_fecn.grid(column=0, row=linea, padx=4, pady=4)
      self.fecn=tkr.StringVar()
      self.fecn.set(reg1[0][16])
      #print(reg1[0][16])
      if reg1[0][16] != None and reg1[0][16] != "" :
        fecha = datetime.strftime(reg1[0][16], '%m-%d-%Y')
        fecha = datetime.strptime(fecha, '%m-%d-%Y')
        formato = '%d/%m/%Y'
        fecha = datetime.strftime(fecha, formato)
      else:
        fecha = ""
      #print(type(fecha))
      #print(fecha)
      self.fecn.set(fecha)
      self.entryfecn=tkr.Entry(self.labelframe1, textvariable=self.fecn)
      self.entryfecn.bind("<FocusOut>", self.formatofecha)
      #self.entryfecn.bind("<Key>", self.formatofecha)
      #self.entryfecn.bind("<BackSpace>", lambda _: self.entryfecn.delete(tkr.END))
      self.entryfecn.grid(column=1, row=linea, padx=4, pady=4)

      self.lbl_email=tkr.Label(self.labelframe1, text="Correo Electrónico:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_email.grid(column=2, row=linea, padx=4, pady=4)
      self.email=tkr.StringVar()
      self.email.set(reg1[0][10])
      self.entryemail=tkr.Entry(self.labelframe1, textvariable=self.email)
      self.entryemail.grid(column=3, row=linea, padx=4, pady=4)
      
      linea+=1
      self.lbl_prof=tkr.Label(self.labelframe1, text="Oficio/Profesión:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_prof.grid(column=0, row=linea, padx=4, pady=4)
      self.prof=tkr.StringVar()
      self.prof.set(reg1[0][17])
      self.entryprof=tkr.Entry(self.labelframe1, textvariable=self.prof)
      self.entryprof.bind("<FocusOut>", self.convertirMayus)
      self.entryprof.grid(column=1, row=linea, padx=4, pady=4)

      linea+=1
      self.lbl_sexo=tkr.Label(self.labelframe1, text="Femenino/Masculino:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e") 
      self.lbl_sexo.grid(column=0, row=linea, padx=4, pady=4)
      self.sexo=tkr.StringVar()
      self.sexo.set(reg1[0][26])      
      self.entryfem=tkr.Radiobutton(self.labelframe1, text = "Femenino",variable=self.sexo, value="F", bg="#FCFCF9")
      self.entryfem.grid(column=1, row=linea, padx=4, pady=4)
      self.entrymasc=tkr.Radiobutton(self.labelframe1, text = "Masculino",variable=self.sexo, value="M", bg="#FCFCF9")
      self.entrymasc.grid(column=2, row=linea, padx=4, pady=4)

      #Obtener la descripcion de la torre/edificio
      self.idtorre=tkr.IntVar()
      if reg1[0][13] =="":
        reg1[0][13]=64 #codigo que indica=sin identificar 
      self.idtorre.set(reg1[0][13])
      string2=self.registros.obtener_desc(reg1[0][13])
      if reg1[0][13] != 0:
        string3=self.construir_cadena(string2) 
      else:
        string3=""
      #para setear el combo
      string4=string3+str(reg1[0][13])

      #colocar la torre, piso, apto y grupo Familiar lista

      self.lbl_edif=tkr.Label(top_frame, text="Edificio/Torre:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_edif.grid(column=0, row=0, padx=4, pady=4)
      self.cmbedif=tkrttk.Combobox(top_frame, state="readonly")
      self.cmbedif["value"]=self.registros.combo_add("TORRE", 1)
      self.cmbedif.set(string4)
      self.cmbedif.bind("<<ComboboxSelected>>", self.callbackFunc)
      self.cmbedif.grid(column=1, row=0, padx=4, pady=4)


      #Obtener la descripcion de el piso
      self.idpiso=tkr.IntVar()
      self.idpiso.set(reg1[0][14])
      if reg1[0][14] =="":
        reg1[0][14]=7 #codigo que indica=sin identificar 

      string2=self.registros.obtener_desc(reg1[0][14])
      if reg1[0][14] != 0:
        string3=self.construir_cadena(string2) 
      else:
        string3=""
      #para setear el combo
      string4=string3+str(reg1[0][14])


      self.lbl_piso=tkr.Label(top_frame, text="Piso:", bg=self.back1, fg=self.fore, font=self.tamagnoletra,width=20,anchor="e")
      self.lbl_piso.grid(column=0, row=1, padx=4, pady=4)
      self.cmbpiso=tkrttk.Combobox(top_frame, state="readonly")
      self.cmbpiso["value"]=self.registros.combo_add("PISO", 1)      
      self.cmbpiso.set(string4)
      self.cmbpiso.bind("<<ComboboxSelected>>", self.callbackFunc)
      self.cmbpiso.grid(column=1, row=1, padx=4, pady=4)

      self.lbl_apto=tkr.Label(top_frame, text="Apartamento/Ubicación:", bg=self.back1, fg=self.fore, font=self.tamagnoletra)
      self.lbl_apto.grid(column=0, row=2, padx=4, pady=4)
      self.apto=tkr.StringVar()
      self.apto.set(reg1[0][15])
      self.entryapto=tkr.Entry(top_frame, textvariable=self.apto)
      self.entryapto.bind("<FocusOut>", self.convertirMayus)
      self.entryapto.grid(column=1, row=2, padx=4, pady=4)

      #crear la estructura familiar y el cargo

      #Obtener la descripcion de la estrutura familiar
      self.idmiembro=tkr.IntVar()
      self.idmiembro.set(reg1[0][14])
      
      if reg1[0][6] =="":
        reg1[0][6]=45 #codigo que indica=sin identificar 

      string2=self.registros.obtener_desc(reg1[0][6])
      if reg1[0][6] != 0:
        string3=self.construir_cadena(string2) 
      else:
        string3=""
      #para setear el combo
      string4=string3+str(reg1[0][6])
      #print(string4)  

      self.labelframe4=tkr.LabelFrame(top_frame,bg=self.back1)        
      self.labelframe4.grid(column=0, columnspan=2, row=3, padx=5, pady=10)
      self.lblrol=tkr.Label(self.labelframe4, text="Rol en la Familia:",bg=self.back1,fg=self.fore, font=self.tamagnoletra)
      self.lblrol.grid(column=0, row=0, padx=4, pady=4)
      self.cmbrol=tkrttk.Combobox(self.labelframe4, state="readonly")
      self.cmbrol["value"]=self.registros.combo_add("MIEMBROS", 1)      
      self.cmbrol.set(string4)
      self.cmbrol.grid(column=1, row=0, padx=4, pady=4)

      self.lbl_numfam=tkr.Label(self.labelframe4, text="Nro miembros en la Familia:",bg=self.back1,fg=self.fore, font=self.tamagnoletra)        
      self.lbl_numfam.grid(column=0, row=1, padx=4, pady=4)
      self.num=tkr.IntVar()
      if reg1[0][23] == "":
          reg1[0][23]=0
      query = "SELECT count(*) FROM vecinos_temporal tb1 where tb1.grupo_fam= %s" % reg1[0][23]
      string4=self.registros.obtener_cuantos(query)
      self.num.set(string4[0][0])
      self.lbl_numfam_2=tkr.Label(self.labelframe4, textvariable=self.num, text=string4, bg=self.button1,fg=self.foreblack, font=self.tamagnoletra)
      self.lbl_numfam_2.grid(column=1, row=1, padx=4, pady=4)

      #crear listado de los que habian la residencia
      self.labelframe5=tkr.LabelFrame(center)        
      self.labelframe5.grid(column=0, row=3, padx=5, pady=10)

      """ Hacer TREEVIEW lista """
      self.listaTree_rol = tkrttk.Treeview(self.labelframe5, height="14", selectmode='browse')

      self.listaTree_rol["columns"] = ("ID","CEDULA", "NOMBRE","APELLIDO","ROL")
      self.listaTree_rol.column("ID", width=80, minwidth=270,stretch=False)
      self.listaTree_rol.column("CEDULA", width=80, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("NOMBRE", width=240, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("APELLIDO", width=240, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("ROL", width=80, minwidth=270,stretch=tkr.NO)
      self.listaTree_rol.column("#0", width=0, stretch=False)
      self.listaTree_rol.column("ID", width=0, stretch=False)

      self.listaTree_rol.grid(column=0, row=2, padx=4, pady=4)

      #Boton para actualizar la información
      self.button1 = tkr.Button(self.pagina1,text='Actualizar', command=self.updateVec, highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
      self.button1.place(x=800, y=530, height=20)

      self.button2 = tkr.Button(self.pagina1,text='Grabar', command=self.InsertVec,highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
      self.button2.place(x=900, y=530, height=20)

      self.button3 = tkr.Button(self.pagina1,text='Nuevo Integrante', command=self.inicialiarVariables, highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
      self.button3.place(x=900, y=530, height=20)

      if self.vecino1 == 0:
        self.button1.place_forget()
        self.button3.place_forget()
      
      if self.vecino1 != 0:
        self.button2.place_forget()        

      self.button1 = tkr.Button(self.pagina1,text='Salir', command=self.volver, highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
      self.button1.place(x=680, y=530, height=20)

      #button1.grid(row=5, column=2)

      self.listaTree_rol.heading("ID", text="ID")
      self.listaTree_rol.heading("CEDULA", text="Nro de Cédula")
      self.listaTree_rol.heading("NOMBRE", text="Nombre")
      self.listaTree_rol.heading("APELLIDO", text="Apellido")
      self.listaTree_rol.heading("ROL", text="Rol")

      self.listaTree_rol.bind('<ButtonRelease-1>', self.selectItem)

      query = "SELECT vec.*, tb1.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_miembro = tb1.contador where vec.grupo_fam= %s" % reg1[0][23]
      reg = self.registros.listarVecinos(query)
      self.lista(reg, self.listaTree_rol)

      self.pagina2 = tkr.Frame(self.cuaderno1,bg=self.back1)
      self.cuaderno1.add(self.pagina2, text="Observaciones/Medicamentos/Antecedentes")
      self.labelframe2=tkr.LabelFrame(self.pagina2, bg=self.back1)        
      self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
   
      self.lbl_medicam=tkr.Label(self.labelframe2, text="Medicamentos:",  bg=self.back1, fg=self.fore, font=self.tamagnoletra)
      self.lbl_medicam.grid(column=0, row=1, padx=4, pady=4)
      self.textmed=tkr.Text(self.labelframe2)
      self.textmed.config(width=130,height=10)
      self.textmed.insert(tkr.END, reg1[0][18])
      self.textmed.bind("<FocusOut>", self.convertirMayus)
      self.textmed.grid(column=1, row=1, padx=4, pady=4)

      self.lbl_observa=tkr.Label(self.labelframe2, text="Observaciones:", bg=self.back1, fg=self.fore, font=self.tamagnoletra)
      self.lbl_observa.grid(column=0, row=2, padx=4, pady=4)
      self.textobs=tkr.Text(self.labelframe2)
      self.textobs.config(width=130,height=10)
      self.textobs.insert(tkr.END, reg1[0][19])
      self.textobs.bind("<FocusOut>", self.convertirMayus)
      self.textobs.grid(column=1, row=2, padx=4, pady=4)

      self.lbl_antece=tkr.Label(self.labelframe2, text="Antecedentes:", bg=self.back1, fg=self.fore, font=self.tamagnoletra)
      self.lbl_antece.grid(column=0, row=3, padx=4, pady=4)
      self.textant=tkr.Text(self.labelframe2)
      self.textant.config(width=130,height=10)
      self.textant.insert(tkr.END, reg1[0][20])
      self.textant.bind("<FocusOut>", self.convertirMayus)
      self.textant.grid(column=1, row=3, padx=4, pady=4)
      self.grupo_familiar=reg1[0][23]
      self.entrynom1.focus()