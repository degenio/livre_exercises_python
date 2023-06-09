#Definition du risque
risque =["Minimum vital","Athlétique","En forme","Moyen","Obèse"]

age = int(input("Saisir votre age:"))
# On suppose que l'usager nous donne soit 0 ou 1
sexe = int(input("Saisir 0 pour femme et 1 pour male:"))
poids = float(input("Saisir votre poids:"))
taille = float(input("Saisir votre taille:"))
# Calcul img selon la regle
img = (1.2 * poids / (taille ** 2)) + (0.23 * age) - (10.8 * sexe) - 5.4
print("Votre img est:{0:7.2f}".format(img))

#Determination du risque santé
if sexe == 0 :#femme
            if 10<=img <= 13 :
                index=0
            elif img <= 20 :
                index=1
            elif img<=24:
                index=2
            elif img<=31:
                index=3
            else :
                index=4

elif sexe == 1:#homme
    if 2 <= img <= 5:
        index = 0
    elif img <= 13:
        index = 1
    elif img <= 17:
        index = 2
    elif img <= 24:
        index = 3
    else:
        index = 4

print("Votre risque de santé selon IMG:{0:7.2f} est:{1:15s}".format(img,risque[index]))