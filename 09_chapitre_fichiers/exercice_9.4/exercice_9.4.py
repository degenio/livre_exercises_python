#Solution de base
def traiter_casse_op1(nom_fichier_source, nom_fichier_destination):
    # Ouverture des deux fichiers en mode lecture et écriture, respectivement
    f_destination = open(nom_fichier_destination, "w")
    f_source = open(nom_fichier_source)
    # Boucle pour lire chaque ligne du fichier source
    for ligne in f_source:
        print(ligne.strip())
        if not ligne.strip()[0] in "abcdefghijklmnopqrstuvwxyz":
            f_destination.write(ligne.strip() + '\n')
    f_destination.close()
    f_source.close()


#Solution 2 avec la fonction built-in isupper()
def traiter_casse_op2(nom_fichier_source, nom_fichier_destination):
    # Ouverture des deux fichiers en mode lecture et écriture, respectivement
    f_destination = open(nom_fichier_destination, "w")
    input_f = open(nom_fichier_source)
    # Boucle pour lire chaque ligne du fichier source
    for ligne in input_f:
        if ligne.strip()[0].isupper():
            f_destination.write(ligne.strip() + '\n')
    f_destination.close()
    input_f.close()


#Solution 3  avec with open sur les deux fichiers
def traiter_casse_op3(nom_fichier_source, nom_fichier_destination):
    # Ouverture des deux fichiers en mode lecture et écriture, respectivement
    with open(nom_fichier_source, "r") as f_source, open(nom_fichier_destination, "w") as f_destination:
        # Boucle pour lire chaque ligne du fichier source
        for ligne in f_source:
            # Si la première lettre de la ligne est une majuscule, on la copie dans le fichier de destination
            if ligne.strip()[0].isupper():
                f_destination.write(ligne.strip() + '\n')


if __name__ == '__main__':
    traiter_casse_op1("stats.txt", "sortie1.txt")
    traiter_casse_op2("stats.txt", "sortie2.txt")
    traiter_casse_op3("stats.txt", "sortie3.txt")
