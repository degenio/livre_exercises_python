mois = [
    "Janvier", "Février", "Mars", "Avril",
    "Mai", "Juin", "Juillet", "Aout",
    "Septembre", "Octobre", "Novembre", 
    "Decembre"
]
jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Saisir le mois
num_mois = int(input("Saisir un numéro de mois (1-12): "))

#Valider la valeur saisie
if not 1 <= num_mois <= 12:
    print("Numéro du mois invalide")
else:
    nom_mois = mois[num_mois-1]
    print("Name:", nom_mois)
    print("Days:", jours[num_mois - 1])

