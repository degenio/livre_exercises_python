import csv

def rechercher_produit(fichier_source,nom_prd):
    with open(fichier_source, 'r') as f:
        lecteur = csv.DictReader(f)
        print("{:<10} {:<10} {}".format('item', 'prix', 'quantité'))
        print("=" * 30)
        for ligne in lecteur:
            if ligne['item'] == nom_prd:
                print("{:<10} {:<10} {}".format(ligne['item'], ligne['prix'], ligne['quantite']))


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
    print("=" * 30)
    rechercher_produit("inventaire.csv", "stylo")
