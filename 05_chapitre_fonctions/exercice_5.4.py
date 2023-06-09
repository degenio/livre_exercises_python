def calculer_factorielle(nombre):
    factorielle = 1
    for i in range(1, nombre + 1):
        factorielle *= i

    return  factorielle

# Appel de la fonction principale
if __name__ == '__main__':
    # Demande à l'utilisateur de saisir une valeur
    valeur = int(input("Entrez une valeur positive : "))

    # Vérifie si la valeur est strictement positive
    while valeur < 0:
        print("Erreur : La valeur doit être strictement positive.")
        valeur = int(input("Entrez une valeur positive : "))

    resultat = calculer_factorielle(valeur)
    print('La factorielle de {} est: {}'.format(valeur, resultat))
