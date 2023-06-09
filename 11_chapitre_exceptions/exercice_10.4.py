# Définir un dictionnaire associant chaque nombre de mois à son nom
mois = {1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin",
        7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"}

def determiner_mois(nombre):
    return mois[nombre]

def saisir_valeur(message):
    flag = True
    #Saisie et Validation du mois
    while flag:
        try:
            nombre = int(input(message))
            # Vérifie si le nombre saisi correspond à un mois valide et affiche le nom du mois associé
            if nombre in mois:
                flag = False
            else:
                print("Erreur : Le nombre saisi ne correspond pas à un mois valide.")
        except ValueError:
            print("Erreur : Veuillez saisir un nombre entier.")
    return nombre

if __name__ == '__main__':
    nombre= saisir_valeur("Entrez un nombre correspondant à un mois de l'année : ")
    print("Le mois correspondant au nombre {} est {}".format(nombre, determiner_mois(nombre)))
