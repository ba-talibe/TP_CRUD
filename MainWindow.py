from tkinter import Tk, ttk
from tkinter import *
from database import *
from tkinter.messagebox import *

database()
class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.minsize(400, 400)
        self.maxsize(800, 400)
        self.onglet_control = ttk.Notebook(self)


        self.onglet_afficher = ttk.Frame(self.onglet_control)
        masteur = ttk.Frame(self.onglet_control)
        self.onglet_suppimer = ttk.Frame(self.onglet_control)
        self.onglet_modifier = ttk.Frame(self.onglet_control)

        self.onglet_control.add(self.onglet_afficher, text='Afficher')
        self.onglet_control.add(masteur, text='Ajouter')

        self.onglet_control.pack(expand=1, fill="both")
        
        self.remplirAfficher()
        self.remplirAjouter()
        self.remplirsupprimer()
        self.remplirModifier()
        print (self.winfo_width())
        print (self.winfo_height())
    
    def remplirAfficher(self) -> None:
        results = lecture()
        self.tableau = ttk.Treeview(self.onglet_afficher,
                                     columns=('Num', 'Prenom', 'Nom', 'Note'))
        
        self.tableau.heading('Num', text='Numero Etudiant')
        self.tableau.heading('Prenom', text='Prenom')
        self.tableau.heading('Nom', text='Nom')
        self.tableau.heading('Note', text='Note')
        self.tableau['show'] = 'headings'
        
        for result in results:
            self.tableau.insert('', 'end', iid=result[1], 
                    values=(result[1],
                             result[2],
                              result[3],
                              result[4]))

        self.tableau.grid(row=0, column=0, columnspan=4)
        Button(self.onglet_afficher, text='Supprimer',
                         command=self.supprimerLigne
                         ).grid(row=1, column=1, sticky=W)

        Button(self.onglet_afficher, text='Modifier',
                         command=self.modifierLigne
                         ).grid(row=1, column=2, sticky=E)
        

    def remplirAjouter(self, masteur):
        self.num = IntVar()
        self.prenom = StringVar()
        self.nom = StringVar()
        self.note = StringVar()

        Label(masteur, text="Numero Etudiant : ").grid(column=0, row=0, padx=10, pady=10, sticky=W)
        champNum = Entry(masteur,
                                textvariable=self.num,
                                width=70).grid(column=1, row=0)

        Label(masteur, text="Prenom : ").grid(column=0, row=1, padx=10, pady=10, sticky=W)
        champPrenom = Entry(masteur,
                                textvariable=self.prenom,
                                width=70).grid(column=1, row=1, padx=10, pady=10,)

        Label(masteur, text="Nom : ").grid(column=0, row=2, padx=10, pady=10, sticky=W)
        champNom = Entry(masteur, 
                                textvariable=self.nom,
                                width=70)

        champNom.grid(column=1, row=2, padx=10, pady=10)

        Label(masteur, text="Note : ").grid(column=0, row=3, padx=10, pady=10, sticky=W)
        champNote = Entry(masteur, 
                                textvariable=self.note,
                                width=70).grid(column=1, row=3, padx=10, pady=10)

        AjoutButton = Button(masteur, text='Ajouter', command=self.verifierAjout)
        AjoutButton.grid(row= 4, column=1)


    def remplirsupprimer(self):
        pass

    def remplirModifier(self):
        pass

    def verifierAjout(self):
        result = getNum()
        [num, prenom, nom, note] = [self.num.get(), self.prenom.get(), self.nom.get(), self.note.get()]
        if (num, ) in result:
            showwarning("Error Saisie", "Le numero Saisie existe deja")
            return
        
        if len(note) ==0 or not (0 <= int(note) <= 20):
             showwarning("Erreur de Saisie", "La Note Saisie est Incorrcte")
             return

        if len(prenom) == 0 or len(nom) == 0:
            showwarning("Erreur de Saisie", "Les champs prenom et nom ne peuveut etre vide")
            return

        inserer(num, prenom, nom, note)
        self.tableau.insert('', 'end', iid=num,
                    values=  (num,
                              prenom,
                              nom,
                              note))

        showinfo("Reussi", "Transaction Effectué")
        
    def supprimerLigne(self):
        if askyesno('Confirmation de Suppression', "Etes vous sûr de vouloir surpprimmer cette note ?"):
            for ligne in self.tableau.selection():
                delete(ligne)
                self.tableau.delete(ligne)
        else:
            return

    def modifierLigne(self):
        ligne = self.tableau.selection()
        [num, prenom, nom, note] = list(self.tableau.item(ligne)['values'])
        fenModif = Tk()
        fenModif.title("Modifier Note")

        