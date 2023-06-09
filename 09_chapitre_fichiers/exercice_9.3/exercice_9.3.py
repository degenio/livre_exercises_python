# solution avec retour de la longueur 
def calcul_fichier_longueur(fichier):
    # Initialisation de la variable pour stocker la ligne la plus longue
    ligne_maximum = ""
    input = open(fichier)
    for ligne in input:
        if len(ligne) > len(ligne_maximum):
            # Stockage de la nouvelle ligne la plus longue
            ligne_maximum = ligne
    input.close()
    return len(ligne_maximum)

# solution avec retour de la longueur et la phrase elle meme
def calcul_fichier_stats(fichier):
    # Initialisation de la variable pour stocker la ligne la plus longue
    ligne_maximum = ""
    input = open(fichier)
    for ligne in input:
        if len(ligne) > len(ligne_maximum):
            # Stockage de la nouvelle ligne la plus longue
            ligne_maximum = ligne
    input.close()
    return len(ligne_maximum), ligne_maximum

def main():
    maximus = calcul_fichier_longueur("stats.txt")
    print("Longueur maximum:", maximus)

    maximus, ligne_max = calcul_fichier_stats("stats.txt")
    print("Longueur maximum:", maximus)
    print("Ligne avec longueur maximum:", ligne_max)

if __name__ == '__main__':
    main()