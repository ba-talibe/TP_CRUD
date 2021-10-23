from tkinter import Tk, ttk
from tkinter import *
from database import *

class MainWindow(Tk):

    def __init__(self):
        database()
        Tk.__init__(self)
        self.minsize(400, 400)
        self.maxsize(800, 400)
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
        print (self.winfo_width())
        print (self.winfo_height())
    
    def remplirAfficher(self):
        results = lecture()
        tableau = ttk.Treeview(self.onglet_afficher,
                                     columns=('Num', 'Prenom', 'Nom', 'Note'))
        
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
        """num = IntVar()
        prenom = StringVar()
        nom = StringVar()"""

        Label(self.onglet_ajouter, text="Numero Etudiant : ").grid(column=0, row=0, padx=10, pady=10, sticky=W)
        champNum = Entry(self.onglet_ajouter, width=70).grid(column=1, row=0)

        Label(self.onglet_ajouter, text="Prenom : ").grid(column=0, row=1, padx=10, pady=10, sticky=W)
        champPrenom = Entry(self.onglet_ajouter, width=70).grid(column=1, row=1, padx=10, pady=10,)

        Label(self.onglet_ajouter, text="Nom : ").grid(column=0, row=2, padx=10, pady=10, sticky=W)
        champNom = Entry(self.onglet_ajouter, width=70)
        champNom.grid(column=1, row=2, padx=10, pady=10)

        Label(self.onglet_ajouter, text="Note : ").grid(column=0, row=3, padx=10, pady=10, sticky=W)
        champNote = Entry(self.onglet_ajouter, width=70).grid(column=1, row=3, padx=10, pady=10)
        AjoutButton = Button(self.onglet_ajouter, text='Ajouter')
        AjoutButton.grid(row= 4, column=1)


    def remplirsupprimer(self):
        pass

    def remplirModifier(self):
        pass