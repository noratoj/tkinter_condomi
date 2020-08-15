import os
import sys
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import scrolledtext, NSEW, W
from typing import re


class Vista(tk.Tk):

    def treeview_paises_fun(self, frame1):
        self.treeview_paises = ttk.Treeview(self.frame1, style="Treeview", columns=('Nº', 'ISO', 'País', 'Codigo'))
        self.treeview_paises.heading('#0', text='Nº')
        self.treeview_paises.heading('#1', text='ISO')
        self.treeview_paises.heading('#2', text='País')
        self.treeview_paises.heading('#3', text='Código')
        self.treeview_paises.column('#0', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#1', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#2', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#3', minwidth=100, width=100, stretch=True, anchor="c")

        self.treeview_paises.tag_bind("item", '<<TreeviewSelect>>', self.selecciono_pais)
        self.treeview_paises.tag_bind('item', "<Double-Button-1>", self.selecciono_pais)

        self.treeview_paises.grid(row=0, column=0, sticky=NSEW)

        vsb_a = ttk.Scrollbar(self.frm_cpf, orient="vertical", command=self.treeview_paises.yview)
        vsb_a.grid(row=0, column=1, sticky=NSEW)
        hsb_a = ttk.Scrollbar(self.frm_cpf, orient="horizontal", command=self.treeview_paises.xview)
        hsb_a.grid(row=1, column=0, sticky=NSEW)
        self.treeview_paises.configure(xscrollcommand=hsb_a.set, yscrollcommand=vsb_a.set)

    def treeview_referencia_fun(self):
        self.treeview_paises = ttk.Treeview(self.frm_cpf, style="Treeview", columns=('Nº', 'ISO', 'País', 'Codigo'))
        self.treeview_paises.heading('#0', text='Nº')
        self.treeview_paises.heading('#1', text='ISO')
        self.treeview_paises.heading('#2', text='REfreencia')
        self.treeview_paises.heading('#3', text='Código')
        self.treeview_paises.column('#0', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#1', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#2', minwidth=80, width=80, stretch=True, anchor="c")
        self.treeview_paises.column('#3', minwidth=100, width=100, stretch=True, anchor="c")

        self.treeview_paises.tag_bind("item", '<<TreeviewSelect>>', self.selecciono_pais)
        self.treeview_paises.tag_bind('item', "<Double-Button-1>", self.selecciono_pais)

        self.treeview_paises.grid(row=0, column=0, sticky=NSEW)

        vsb_a = ttk.Scrollbar(self.frm_cpf, orient="vertical", command=self.treeview_paises.yview)
        vsb_a.grid(row=0, column=1, sticky=NSEW)
        hsb_a = ttk.Scrollbar(self.frm_cpf, orient="horizontal", command=self.treeview_paises.xview)
        hsb_a.grid(row=1, column=0, sticky=NSEW)
        self.treeview_paises.configure(xscrollcommand=hsb_a.set, yscrollcommand=vsb_a.set)


    def main(self):
        self.mainloop()

    def salir(self):
        #self.master.salir()
        self.destroy()
        os._exit(0)
        sys.exit(0)

    def on_closing(self):
        self.withdraw()

    def selecciono_pais(self, event):
        print('Seleccionado pais')
        item = self.treeview_paises.identify('item', event.x, event.y)
        print("you clicked on", self.treeview_paises.item(item, "text"))

    def filter(self, tree, col, descending):
        print ('Row: {} & Column: {} '.format(
            re.sub('I00', '', str(tree.identify_row(tree.winfo_pointerxy()[1] - tree.winfo_rooty()))),
            re.sub(r'#', '', str(tree.identify_column(tree.winfo_pointerxy()[0] - tree.winfo_rootx())))))

    def administration(self):
        self.VentanaManejoRef()
    