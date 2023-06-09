#Liste pour contenir les nombres lus du fichier
valeurs=[]
# Ouverture du fichier
with open("nombres.txt", "r") as f:
    # Lecture des valeurs
    for tmp in f.readlines():
        print(tmp)
        valeurs.append(float(tmp.strip()))

# Calcul de la moyenne des valeurs
moyenne = sum(valeurs) / len(valeurs)

# Affichage de la moyenne
print("La moyenne des valeurs est: {0:7.2f}  ".format(moyenne))
