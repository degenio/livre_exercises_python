def calculer_factorielle(nombre):
    # Cas de base : factorielle de 0 est 1
    if nombre == 0:
        return 1

    # Récursion : calcul de la factorielle en appelant la fonction avec n-1
    return nombre * calculer_factorielle(nombre - 1)

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
