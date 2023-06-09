def traiter_fichier(fichier_source):
    with open(fichier_source, "r") as f:
        for ligne in f:
            # Divise la ligne en 3 éléments distincts
            item, quantite, prix = ligne.split()
            # Affiche les éléments sous le format souhaité en utilisant printf
            print(f"Item: {item}, Quantité: {quantite}, Prix: {prix}")

if __name__ == '__main__':
    traiter_fichier("produits.txt")
