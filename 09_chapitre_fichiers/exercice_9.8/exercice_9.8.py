def traiter_fichier(fichier_source, fichier_destination):
    with open(fichier_source, "r") as f:
        with open(fichier_destination, 'w') as f_dest:
            for ligne in f:
                # Divise la ligne en 3 éléments distincts
                item, quantite, prix = ligne.split()
                prix = float(prix)
                quantite = int(quantite)
                if quantite < 26:
                    prix *= 0.8
                item = item.upper()
                # Sauvegarder dans le fichier destination
                f_dest.write(f"{item}|{quantite}|{prix:.2f}\n")


if __name__ == '__main__':
    traiter_fichier("produits.txt", 'sortie.txt')
