def verifier_mot_de_passe(mot_de_passe):
    # Vérification de la longueur
    if len(mot_de_passe) < 12:
        return False

    # Vérification de la présence d'une lettre majuscule
    if not any(char.isupper() for char in mot_de_passe):
        return False

    # Vérification de la présence d'une lettre minuscule
    if not any(char.islower() for char in mot_de_passe):
        return False

    # Vérification de la présence d'un nombre
    if not any(char.isdigit() for char in mot_de_passe):
        return False

    # Toutes les conditions sont satisfaites
    return True

# Demander à l'utilisateur de saisir un mot de passe
mot_de_passe = input("Entrez un mot de passe : ")

# Vérification du mot de passe en appelant la fonction
est_valide = verifier_mot_de_passe(mot_de_passe)

# Affichage du résultat
if est_valide:
    print("Le mot de passe est valide.")
else:
    print("Le mot de passe n'est pas valide.")
