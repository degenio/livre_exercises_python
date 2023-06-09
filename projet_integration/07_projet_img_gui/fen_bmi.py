from tkinter import *
from tkinter import ttk

from mod_classes import Patient
from mod_fichiers import enregistrer_img
from mod_main import risque, determiner_risque

def quit():
    root.destroy()

def main_calcul():
    patient = Patient(nom.get(), int(age.get()),int(choix_sexe.get()), float(poids.get()), float(taille.get()))
    #Appel pour le calcul IMC
    img = patient.calculer_img()
    #Afficher IMG, risque
    lbl_img.config(text="{0:5.2f}".format(img))
    indice = determiner_risque(img,patient.sexe)
    lbl_risque.config(text=str(risque[indice]))


def enregistrer():
    personne = Patient(nom.get(), int(age.get()),int(choix_sexe.get()), float(poids.get()), float(taille.get()))
    #Sauvegarde csv
    enregistrer_img("sortie_img.csv", personne)

#Creation de la fenetre princicpale
root = Tk()
root.title("Calcul de l'indice de masse de graisse")
root.geometry("380x400")
#Variable pour le suivi selection de sexe patient
choix_sexe =  StringVar()
choix_sexe.set(0)  # init
#Creation d'un frame pour le titre
frame_titre = Frame(root)
titre_font = ('arial', 20, 'bold')
label_titre = Label(frame_titre, text='Saisie des données Patient', font=titre_font)
label_titre.grid(row=1, column=1,   padx=5, pady=5 )

#Creation d'un frame pour les composants graphiques
frame_compo = Frame(root)
Label(frame_compo , text='Nom').grid(row=1, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Age').grid(row=2, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Sexe').grid(row=3, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Poids').grid(row=4, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Taille').grid(row=5, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='IMG:').grid(row=6, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Risque de santé:').grid(row=7, column=1, sticky=E, padx=5, pady=5)

nom = Entry(frame_compo , width=40)
nom.grid(row=1, column=2, columnspan=4, sticky=W)
age = Entry(frame_compo , width=10)
age.grid(row=2, column=2, columnspan=4, sticky=W)

val_sexe = [("Femme", 0),
           ("Home", 1)]
#  valeurs
i = 2
for s_k, val in val_sexe:
    Radiobutton(frame_compo,
                   text=s_k,
                   padx=5,
                   variable=choix_sexe,
                   value=val).grid(row=3, column=i, sticky=W)
    i += 1

poids = Entry(frame_compo , width=20)
poids.grid(row=4, column=2, columnspan=4, sticky=W)
taille = Entry(frame_compo , width=20)
taille.grid(row=5, column=2, columnspan=4, sticky=W)
lbl_img = Label(frame_compo  )
lbl_img.grid(row=6, column=2,  sticky=W)
lbl_risque = Label(frame_compo )
lbl_risque.grid(row=7, column=2, sticky=W)

#Creation d'un frame pour les boutons
frame_boutons = Frame(root)
btn_calculer = Button(frame_boutons, text='Calculer', width=15, command=main_calcul)
btn_calculer.grid(row=1, column=1, padx=5, pady=5)
btn_enregistrer = Button(frame_boutons, text='Enregistrer', width=15, command=enregistrer)
btn_enregistrer.grid(row=1, column=2, padx=5, pady=5)
btn_cancel = Button(frame_boutons, text='Quitter', width=15, command=quit)
btn_cancel.grid(row=1, column=3)
#Placement des frames
frame_titre.grid(row=1, column=1,columnspan=3,   padx=5, pady=5 )
frame_compo.grid(row=2, column=1,   padx=5, pady=5 )
frame_boutons.grid(row=3, column=1,  padx=5, pady=5 )

root.mainloop()
