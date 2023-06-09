import random

# Demander à l'utilisateur le nombre de valeurs
n = int(input("Saisir le nombre de valeurs: "))

# Initialiser les variables pour les statistiques
nombre_impairs = 0
minimum = 100
maximum = 0

# Générer les nombres aléatoires et mettre à jour les statistiques
for tmp in range(n):
    valeur = random.randint(0, 100)
    if valeur % 2 != 0:
        nombre_impairs += 1
    if valeur < minimum:
        minimum = valeur
    if valeur > maximum:
        maximum = valeur

# Calculer l'étendue
etendue = maximum - minimum

# Afficher les statistiques
print("Nombre de valeurs impaires:".format(nombre_impairs))
print("Valeur minimum:".format(minimum))
print("Valeur maximum:".format(maximum))
print("Étendue:".format(etendue))