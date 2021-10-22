from tkinter import Tk, ttk
from tkinter import *
from database import *

class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        database()
        self.onglet_control = ttk.Notebook(self)

        self.onglet_afficher = ttk.Frame(self.onglet_control)
        self.onglet_ajouter = ttk.Frame(self.onglet_control)
        self.onglet_suppimer = ttk.Frame(self.onglet_control)
        self.onglet_modifier = ttk.Frame(self.onglet_control)

        self.onglet_control.add(self.onglet_afficher, text='Afficher')
        self.onglet_control.add(self.onglet_ajouter, text='Ajouter')
        self.onglet_control.add(self.onglet_suppimer, text='Supprimer')
        self.onglet_control.add(self.onglet_modifier, text='Modifier')

        self.onglet_control.pack(expand=1, fill="both")

        self.remplirAfficher()
        self.remplirAjouter()
        self.remplirsupprimer()
        self.remplirModifier()
    
    def remplirAfficher(self):
        result = lecture()
        ttk.Label()
        for line, i in zip(result, range(len(result)):
            text = line
            ttk.Label(self.onglet_afficher,text=)

    def remplirAjouter(self):
        pass

    def remplirsupprimer(self):
        pass

    def remplirModifier(self):
        pass