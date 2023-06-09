# Definition du risque
risque = ["Minimum vital", "Athlétique", "En forme", "Moyen", "Obèse"]


def saisir_entier(msg, msg_error):
    valeur = int(input(msg))
    while valeur <= 0:  # Valider que c'est positif
        valeur = int(input(msg_error))
    return valeur


def saisir_sexe(msg, msg_error):
    valeur = int(input(msg))
    while valeur < 0 or valeur > 1:  # Valider que c'est 0 ou 1
        valeur = int(input(msg_error))
    return valeur


def saisir_valeur(msg, msg_error):
    valeur = float(input(msg))
    while valeur <= 0:
        valeur = float(input(msg_error))
    return valeur


def calculer_img(poids, taille, age, sexe):
    # Calcul img selon la regle
    return (1.2 * poids / (taille ** 2)) + (0.23 * age) - (10.8 * sexe) - 5.4


def afficher_img(valeur):
    print("Votre img est :{0:7.2f}".format(valeur))


def determiner_risque(img, sexe):
    # Determination du risque santé
    if sexe == 0:  # femme
        if 10 <= img <= 13:
            index = 0
        elif img <= 20:
            index = 1
        elif img <= 24:
            index = 2
        elif img <= 31:
            index = 3
        else:
            index = 4

    elif sexe == 1:  # homme
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

    return index


def afficher_risque(indice, img):
    print("Votre risque de santé selon IMG:{0:7.2f} est:{1:15s}".format(img, risque[indice]))


def main():
    # saisir le poids
    poids = saisir_valeur("Saisir le poids:", "Saisir le poids > 0:")
    # saisie la taille
    taille = saisir_valeur("Saisir la taille:", "Saisir la taille > 0:")
    # Saisir l'age
    age = saisir_entier("Saisir votre age:","Saisir votre age > 0:")
    # Saisir le sexe
    # On suppose que l'usager nous donne soit 0 ou 1
    sexe = saisir_sexe("Saisir 0 pour femme et 1 pour male:", "Saisir 0 ou 1 seulement:")
    # calculer img
    img = calculer_img(poids, taille, age, sexe)
    # afficher img
    afficher_img(img)
    # determiner indice
    indice = determiner_risque(img, sexe)
    # afficher risque
    afficher_risque(indice, img)


if __name__ == '__main__':
    main()
