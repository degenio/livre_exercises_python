# Définir un dictionnaire associant chaque nombre de mois à son nom
mois = {1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin",
        7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"}

# Demander à l'utilisateur de saisir un nombre correspondant à un mois
numero = int(input("Entrez un nombre entre 1 et 12 : "))

# Vérifier si le nombre correspond à un mois valide
if numero in mois:
    # Afficher le nom du mois correspondant
    print("Le mois correspondant au nombre {} est {}".format( numero,mois[numero]))
else:
    # Afficher un message d'erreur
    print("Le nombre {} ne correspond à aucun mois valide.".format(numero))
