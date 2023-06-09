# Demander à l'utilisateur d'entrer trois nombres entiers
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))

# Calculer la somme des deux premiers nombres et multipliez le résultat par le troisième nombre
resultat1 = (nombre1 + nombre2) * nombre3

# Soustraire le troisième nombre du résultat obtenu à l'étape 1
resultat2 = resultat1 - nombre3

# Diviser le résultat obtenu à l'étape 2 par la somme des trois nombres
resultat_final = resultat2 / (nombre1 + nombre2 + nombre3)

# Afficher le résultat final
print("Le résultat final est :{}".format(resultat_final))
