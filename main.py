import tkinter as tk
import ventana_lista
from conexion import *
from tkinter import messagebox, Frame
import hashlib
import os
'''Permite la autnticación o validación del usuario en la aplicación'''

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Autenticar usuario")
        self.configure(background='light grey') # Color de Fondo

        lbl_lista= tk.Label(self, text="Usuario a Autenticarse", bg="LightGreen", width = "40", height="2", font=("Calibri",13))
        lbl_lista.grid(column=0, row=0, columnspan=2)

        # Variables
        self.usuario_var = tk.StringVar()
        self.passw_var = tk.StringVar()
        # Caja texto
        linea=1
        self.label1=tk.Label(self, text="Usuario :")
        self.label1.grid(column=0, row=linea,padx=10, pady=10)
        self.entryuser=tk.Entry(self, textvariable=self.usuario_var)
        self.entryuser.grid(column=1, row=linea, padx=10, pady=10)

        linea+=1
        self.label1=tk.Label(self, text="Password :")
        self.label1.grid(column=0, row=linea, padx=10, pady=10)
        self.entrypass=tk.Entry(self, textvariable=self.passw_var, show="*")
        self.entrypass.grid(column=1, row=linea, padx=10, pady=10)

        self.usuario_var.set("7996640")
        self.passw_var.set("7996640")

        # Botones Limpiar y Simular
        boton = tk.Button(self, text="Regstrarse", width=20, command=self.valores_limpiar)
        boton.grid(row=4, column=0, padx=20, pady=30)
        boton = tk.Button(self, text="Validar Usuario", width=20, command=self.validar)
        boton.grid(row=4, column=1, padx=20, pady=30)


    def valores_limpiar(self):
        self.usuario_var.set("")
        self.passw_var.set("")
        self.entryuser.focus()

    def listausuarios(self):
        ventana_lista.VentanaSimulacion(self.parent,
                             self.usuario_var.get())

    def validar(self):
        if self.usuario_var.get()=="":
            messagebox.showwarning(parent=root, message="Debe introducir su identificador de usuario")
            return

        if self.passw_var.get() =="":
            messagebox.showwarning(parent=root, message="Debe introducir la contraseña(password)")
            return

        usser=self.usuario_var.get()
        passw=self.passw_var.get()

        cnx = Conexion.conectar(self)
        c = cnx.cursor()
        c.execute('SELECT id_cedula, contrasena FROM usuarios WHERE id_cedula = %s' % usser)
        reg1=c.fetchall()
        #print(len(reg1))
        #print(c.rowcount)
        if c.rowcount==1:
            m = hashlib.sha256(passw.encode('utf-8'))

            # En formato hexadecimal
            if (m.hexdigest()==reg1[0][1]):
                self.usuario_var.set("")
                self.passw_var.set("")
                #root.geometry("1200x600")
                frameLista=Frame(self)
                frameLista.config(bg="light grey", bd=10)
                frameLista.place(relx=0, relheight=1, relwidth=1.0)
                d = cnx.cursor()
                d.execute('SELECT * FROM modulos')
                mod1=d.fetchall()
                #reg1=registros.fetchall()
                #print(len(mod1))
                #print(mod1.rowcount)
                #mod1=d.fetchall()
                if d.rowcount>0:
                    #messagebox.showinfo(parent=frameLista, message="Colocar las modulos en Botones")          
                    
            # DEFINIR BARRA DE HERRAMIENTAS:
                    app_carpeta = os.getcwd() 
                    self.icono1 = tk.PhotoImage(file=app_carpeta+"/images/vecinos.png")
                    self.icono2 = tk.PhotoImage(file=app_carpeta+"/images/vecinos.png")
                    
                    self.tmi = self.icono1.subsample(3,3)
                    self.tmi2 = self.icono2.subsample(3,3)

                    barraherr = tk.Frame(frameLista,bd=2, bg="#E5E5E5")
                    
                    bot1 = tk.Button(barraherr, text= "Lista de Usuarios",
                                command=self.listausuarios)
                    #bot1.pack(side="left", padx=1, pady=1)
                    bot1.grid(column=0, row=0, padx=10, pady=10)
                    bot1.config(image=self.tmi,compound="right")

                    bot2 = tk.Button(barraherr, text= "Lista de Usuarios") #command=self.f_salir)                    
                    #bot2.pack(side="left", padx=1, pady=1)
                    bot2.grid(column=1, row=0, padx=10, pady=10)
                    bot2.config(image=self.tmi2,compound="right")

                    bot3 = tk.Button(barraherr, text= "Salir") #command=self.f_salir)                    
                    #bot3.pack(side="left", padx=1, pady=1)
                    bot3.grid(column=0, row=1, padx=10, pady=10)
                    bot3.config(image=self.tmi2,compound="right")

                    barraherr.pack(side="top", fill="x")                    
                    
            else:
                messagebox.showinfo(parent=root, message="Clave Errónea. Intentelo de nuevo")  
        else:
            messagebox.showinfo(parent=root, message="Usuario no esta registrado. Intentelo de nuevo")  

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()