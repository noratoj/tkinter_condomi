import tkinter as tk
import ventana_lista
from conexion import *
from tkinter import messagebox
import hashlib

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

        # Botones Limpiar y Simular
        boton = tk.Button(self, text="Limpiar", width=20, command=self.valores_limpiar)
        boton.grid(row=4, column=0, padx=20, pady=30)
        boton = tk.Button(self, text="Simular", width=20, command=self.valores_simular)
        boton.grid(row=4, column=1, padx=20, pady=30)


    def valores_limpiar(self):
        self.usuario_var.set("")
        self.passw_var.set("")
        self.entryuser.focus()

    def valores_simular(self):
        if self.usuario_var.get()=="":
            messagebox.showinfo(parent=root, message="Debe introducir el usuario a entrar")
            return

        if self.passw_var.get() =="":
            messagebox.showinfo(parent=root, message="Debe introducir la contraseña/password")
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
                ventana_lista.VentanaSimulacion(self.parent,
                                     self.usuario_var.get())
            else:
                messagebox.showinfo(parent=root, message="Clave Errónea. Intentelo de nuevo")  
        else:
            messagebox.showinfo(parent=root, message="Usuario no esta registrado. Intentelo de nuevo")  

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(side="top", fill="both", expand=True)
    root.mainloop()