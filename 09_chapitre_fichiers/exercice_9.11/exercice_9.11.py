import csv


def traiter_inventaire(fichier_source, fichier_destination):
    with open(fichier_source, 'r') as f:
        # lire le fichier
        lecteur = csv.DictReader(f)
        items = []
        for ligne in lecteur:
            items.append((ligne['item'], ligne['prix'], ligne['quantite']))

        with open(fichier_destination, mode='w', newline='') as f_dest:
            writer = csv.writer(f_dest, delimiter=';')
            writer.writerow(['item', 'prix', 'quantite'])
            for item in items:
                writer.writerow([item[0], item[1], item[2]])


if __name__ == '__main__':
    traiter_inventaire("inventaire.csv", "sortie.csv")
