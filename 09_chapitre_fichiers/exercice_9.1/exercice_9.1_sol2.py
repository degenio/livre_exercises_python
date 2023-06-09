# Ouverture du fichier
with open("nombres.txt", "r") as f:
    # Lecture des valeurs en tant que chaînes de caractères
    valeurs = f.readlines()

# Conversion des chaînes de caractères en nombres réels
valeurs = [float(valeur.strip()) for valeur in valeurs]


# Calcul de la moyenne des valeurs
moyenne = sum(valeurs) / len(valeurs)

# Affichage de la moyenne
print("La moyenne des valeurs est: {0:7.2f}  ".format(moyenne))
