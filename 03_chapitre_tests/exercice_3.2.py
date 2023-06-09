# Demande à l'utilisateur d'entrer un nombre entier
nombre = int(input("Entrez un nombre entier : "))

# Vérifie si le nombre est pair et compris entre 10 et 100
if nombre % 2 == 0 and nombre >= 10 and nombre <= 100:
    print("Le nombre est pair et compris entre 10 et 100.")
else:
    print("Le nombre n'est pas pair et/ou n'est pas compris entre 10 et 100.")
