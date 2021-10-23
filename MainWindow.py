from tkinter import Tk, ttk
from tkinter import *
from database import *

class MainWindow(Tk):

    def __init__(self):
        database()
        Tk.__init__(self)
        self.minsize(400, 400)
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
        results = lecture()
        tableau = ttk.Treeview(self.onglet_afficher, columns=('Num', 'Prenom', 'Nom', 'Note'))
        tableau.heading('Num', text='Numero Etudiant')
        tableau.heading('Prenom', text='Prenom')
        tableau.heading('Nom', text='Nom')
        tableau.heading('Note', text='Note')
        tableau['show'] = 'headings'
        for result in results:
            tableau.insert('', 'end', iid=result[0], 
                    values=(result[1],
                             result[2],
                              result[3],
                              result[4]))

        tableau.pack()

    def remplirAjouter(self):
        pass

    def remplirsupprimer(self):
        pass

    def remplirModifier(self):
        pass