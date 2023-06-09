import random

# Demander à l'utilisateur le nombre de valeurs souhaitées
n = int(input("Saisir le nombre de valeurs souhaitées: "))

# Générer la suite de nombres aléatoires
valeurs = [random.randint(0, 100) for _ in range(n)]#utiliser _ pour la variable temporaire

# Afficher la suite de nombres aléatoires
print("Suite de nombres aléatoires:".format(valeurs))

# Calculer le nombre de valeurs impaires
impaires = [v for v in valeurs if v % 2 != 0]
nombre_impaires = len(impaires)

# Afficher le nombre de valeurs impaires
print("Nombre de valeurs impaires :".format(nombre_impaires))

# Calculer la valeur minimum et maximum
min_valeur = min(valeurs)
max_valeur = max(valeurs)

# Afficher la valeur minimum et maximum
print("Valeur minimale:".format(min_valeur))
print("Valeur maximale:".format(max_valeur))

# Calculer l'étendue
etendue = max_valeur - min_valeur

# Afficher l'étendue
print("Étendue:".format(etendue))
