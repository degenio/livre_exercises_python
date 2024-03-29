import tkinter as tk
import random
from tkinter import NW

# Liste de fruits
fruits = ["poire", "orange", "fraise", "citron", "cerise"]

# Fonction pour vérifier la réponse
def verifier_reponse():
    global essais
    fruit_dev = entry.get().lower()
    essais += 1
    if fruit_dev == fruit_actuel:
        lbl_resultat.config(text="Bravo! Vous avez deviné le fruit en {} essai(s)".format(essais), fg="green")
        changer_fruit()
    else:
        lbl_resultat.config(text="Désolé, ce n'est pas le bon fruit. Réessayez!", fg="red")
        entry.delete(0, tk.END)

    lbl_nb_essais.config(text="Nombre d'essais: " + str(essais))

# Fonction pour changer le fruit
def changer_fruit():
    global fruit_actuel
    global essais
    essais = 0
    fruit_actuel = random.choice(fruits)
    img.config(file = 'photos/'+fruit_actuel + ".gif")
    # lbl_fruit.config(text=fruit_actuel)
    entry.delete(0, tk.END)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Devinez le fruit!")
#Création du canvas pour l'image
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
img = tk.PhotoImage()
canvas.create_image(20, 20, anchor=NW, image=img)
# Création des widgets
# lbl_fruit = tk.Label(root, text="", font=("Arial", 14))
# lbl_fruit.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=1, column=0, columnspan=2, padx=10)

btn_verifier = tk.Button(root, text="Vérifier!", command=verifier_reponse)
btn_verifier.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

lbl_resultat = tk.Label(root, text="")
lbl_resultat.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")

essais = 0
lbl_nb_essais = tk.Label(root, text="Nombre d'essais: " + str(essais))
lbl_nb_essais.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Lancement du jeu
changer_fruit()

# Boucle principale de la fenêtre
root.mainloop()
