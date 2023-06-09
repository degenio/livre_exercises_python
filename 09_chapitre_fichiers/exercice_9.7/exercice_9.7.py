def traiter_fichier(fichier_source):
    with open(fichier_source, "r") as f:
        for ligne in f:
            # Divise la ligne en 3 éléments distincts
            item, quantite, prix = ligne.split()
            prix = float(prix)
            quantite = int(quantite)
            if quantite < 26:
                prix *= 0.8
            item = item.upper()
            # Affiche les éléments sous le format souhaité en utilisant printf
            print(f"Item: {item}, Quantité: {quantite}, Prix: {prix}")