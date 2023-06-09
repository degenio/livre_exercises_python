import csv

def traiter_inventaire(fichier_source):
    with open(fichier_source, 'r') as f:
        # lire le fichier
        lecteur = csv.reader(f)
        # lire le header
        headers = next(lecteur)
        print("{:<10} {:<10} {}".format(headers[0], headers[1], headers[2]))
        print("=" * 30)
        for ligne in lecteur:
            item, prix, quantite = ligne
            print("{:<10} {:<10} {}".format(item, prix, quantite))


if __name__ == '__main__':
    traiter_inventaire("inventaire.csv")
