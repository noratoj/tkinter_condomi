import tkinter as tk
import ventana_lista
import administrat
import report
from conexion import *
from tkinter import messagebox, Frame
import hashlib
import os
import tkinter.font as tkf
'''Permite la autnticación o validación del usuario en la aplicación'''

class MainWindow(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.tamagnoletra = ("Arial",10,"bold")
        self.back1="#525252" #8cabbe
        self.fore="white"
        self.parent.title("Autenticar usuario")
        self.configure(background=self.back1) # Color de Fondo

        #permitir la tecla intro / enter dentro de la ventana
        parent.bind("<Return>", self.focus_next_window)
#bba0b2
        lbl_lista= tk.Label(self, text="Autenticarse", bg="#59c9b9", width = "40", height="2", font=("Arial",15,"bold"))
        lbl_lista.grid(column=0, row=0, columnspan=2)

        # Variables
        self.usuario_var = tk.StringVar()
        self.passw_var = tk.StringVar()
        # Caja texto
        linea=1
        self.label1=tk.Label(self,font=self.tamagnoletra, fg= self.fore, background=self.back1 ,text="Usuario :")
        self.label1.grid(column=0, row=linea,padx=10, pady=10)
        self.entryuser=tk.Entry(self,font=self.tamagnoletra, textvariable=self.usuario_var)
        self.entryuser.grid(column=1, row=linea, padx=10, pady=10)

        linea+=1
        self.label1=tk.Label(self, font=self.tamagnoletra, fg= self.fore ,background=self.back1,text="Password :")
        self.label1.grid(column=0, row=linea, padx=10, pady=10)
        self.entrypass=tk.Entry(self, font=self.tamagnoletra,textvariable=self.passw_var, show="*")
        self.entrypass.grid(column=1, row=linea, padx=10, pady=10)

        self.usuario_var.set("7996640")
        self.passw_var.set("7996640")

        # Botones Limpiar y Simular
        boton = tk.Button(self, highlightbackground=self.back1,font=self.tamagnoletra, fg= self.fore ,background=self.back1,text="Registrarse", width=20, command=self.valores_limpiar)
        boton.grid(row=4, column=0, padx=20, pady=30)
        boton = tk.Button(self, highlightbackground=self.back1,font=self.tamagnoletra, fg= self.fore ,background=self.back1,text="Validar Usuario", width=20, command=self.validar)
        boton.grid(row=4, column=1, padx=20, pady=30)
        self.entryuser.focus()

    def focus_next_window(self,event):
        event.widget.tk_focusNext().focus()

    def valores_limpiar(self):
        self.usuario_var.set("")
        self.passw_var.set("")
        self.entryuser.focus()

    def listausuarios(self):
        ventana_lista.VentanaManejoReg(self.parent,
                             self.usuario_var.get())

    def administration(self):
        administrat.VentanaManejoRef(self.parent,
                             self.usuario_var.get())

    def reports(self):
        report.VentanaManejoRep(self.parent,
                             self.usuario_var.get())

    def f_salir(self):
        self.parent.destroy()

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

            # En formato hexadecima
            if (m.hexdigest()==reg1[0][1]):
                self.usuario_var.set("")
                self.passw_var.set("")
                
                self.parent.geometry("500x200")
                frameLista=Frame(self)
                frameLista.config(bg=self.back1, bd=10)
                frameLista.place(relx=0, height=500, relwidth=1.0)
                d = cnx.cursor()
                d.execute('SELECT * FROM modulos')
                mod1=d.fetchall()
                if d.rowcount>0:
                    #messagebox.showinfo(parent=frameLista, message="Colocar las modulos en Botones")          
                    
            # DEFINIR BARRA DE HERRAMIENTAS:
                    app_carpeta = os.getcwd() 
                    self.icono1 = tk.PhotoImage(file=app_carpeta+"/images/vecinos.png")
                    self.icono2 = tk.PhotoImage(file=app_carpeta+"/images/vecinos.png")
                    
                    self.tmi = self.icono1.subsample(3,3)
                    self.tmi2 = self.icono2.subsample(3,3)

                    barraherr = tk.Frame(frameLista,bd=2, background=self.back1)
                    
                    bot1 = tk.Button(barraherr, fg= self.fore ,highlightbackground=self.back1,font = self.tamagnoletra, background=self.back1,text= "Lista de Usuarios",
                                command=self.listausuarios)
                    #bot1.pack(side="left", padx=1, pady=1)
                    bot1.grid(column=0, row=0, padx=15, pady=5)
                    bot1.config(image=self.tmi,compound="right")

                    bot2 = tk.Button(barraherr, highlightbackground=self.back1,fg= self.fore,font = self.tamagnoletra, background=self.back1, text= "Administración",
                                command=self.administration) #command=self.f_salir)                    
                    #bot2.pack(side="left", padx=1, pady=1)
                    bot2.grid(column=1, row=0, padx=5, pady=5)
                    bot2.config(image=self.tmi2,compound="right")

                    bot3 = tk.Button(barraherr, highlightbackground=self.back1,fg= self.fore,text= "Reporte", background=self.back1,
                                command=self.reports)
                    bot3.grid(column=0, row=1, padx=10, pady=10)
                    bot3.config(image=self.tmi2,compound="right")

                    bot4 = tk.Button(barraherr, highlightbackground=self.back1,fg= self.fore,text= "Salir", background=self.back1, command=self.f_salir)
                    bot4.grid(column=1, row=1, padx=10, pady=10)
                    bot4.config(image=self.tmi2,compound="right")

                    barraherr.pack(side="top", fill="x")                    
                    
            else:
                messagebox.showinfo(parent=root, message="Clave Errónea. Intentelo de nuevo")  
        else:
            messagebox.showinfo(parent=root, message="Usuario no esta registrado. Intentelo de nuevo")  

if __name__ == "__main__":
    root = tk.Tk()    
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()