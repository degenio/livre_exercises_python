import random
# Ouverture du fichier en mode écriture
with open("nombres.txt", "w") as f:
    # Boucle pour écrire 10 lignes dans le fichier
    for i in range(10):
        nombres = []
        # Génération de 4 nombres entier aléatoires par ligne
        for tmp in range(4):
            nombres.append(str(random.randint(1,20)) )
        # Écriture des nombres sur une même ligne dans le fichier
        f.write(" ".join(nombres) + "\n")
