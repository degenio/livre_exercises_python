def calculer_carre(valeur):
    return valeur ** 2

def calculer_cube(valeur):
    return valeur ** 3

def calculer_factorielle(valeur):
     if valeur == 0:
        return 1

    factorielle = 1
    for i in range(1, valeur + 1):
        factorielle *= i

    return factorielle

def choix_operation():
    valeur = int(input("Entrez une valeur : "))
    choix = 0
    while not 1 <= choix <= 3:
        choix = int(input("Choisissez l'opération à effectuer (1.carre, 2.cube, 3.factorielle) : "))

    if choix == 1:
        resultat = calculer_carre(valeur)
    elif choix == 2:
        resultat = calculer_cube(valeur)
    elif choix == 3:
        while valeur < 0:
            print("Erreur : La valeur doit être strictement positive.")
            valeur = int(input("Entrez une valeur positive : "))
        resultat = calculer_factorielle(valeur)

    return resultat


# Appel de la fonction principale
if __name__ == '__main__':
    resultat = choix_operation()
    print("Le résultat de l'opération est:{}".format(resultat))
