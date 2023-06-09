# Demande à l'utilisateur le nom du produit, le poids et le prix pour chaque format
nom_produit = input("Entrez le nom du produit : ")
poids1 = float(input("Entrez le poids du premier format : "))
prix1 = float(input("Entrez le prix du premier format : "))
poids2 = float(input("Entrez le poids du deuxième format : "))
prix2 = float(input("Entrez le prix du deuxième format : "))

# Calcul du prix par unité de poids pour chaque format
prix_unite1 = prix1 / poids1
prix_unite2 = prix2 / poids2

# Comparaison des deux prix par unité de poids pour déterminer le format le moins cher
if prix_unite1 < prix_unite2:
    format_choisi = "Format 1"
    prix_format = prix_unite1
else:
    format_choisi = "Format 2"
    prix_format = prix_unite2

# Affichage du format choisi
print("Le format le moins cher pour {} est {} à un prix de {}$ par unité de poids.".format(nom_produit,format_choisi,prix_format))
