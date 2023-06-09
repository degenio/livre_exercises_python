age = int(input("Saisir votre age:"))
# On suppose que l'usager nous donne soit 0 ou 1
sexe = int(input("Saisir 0 pour femme et 1 pour male:"))
poids = float(input("Saisir votre poids:"))
taille = float(input("Saisir votre taille:"))
# Calcul img selon la regle
img = (1.2 * poids / (taille ** 2)) + (0.23 * age) - (10.8 * sexe) - 5.4
print("Votre img est:{0:7.2f}".format(img))
