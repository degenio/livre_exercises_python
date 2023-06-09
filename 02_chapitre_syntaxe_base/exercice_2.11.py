nom = input('Saisir votre nom:')
age = int(input('Saisir votre age:'))
taille = float(input('Saisir votre taille:'))

# Formattage de données à l'aide de la méthode format()
message = "Votre nom est: {}, age est: {} ans. Votre taille est {:.2f} mètres.".format(nom, age, taille)

# Affichage du message formatté
print(message)

# Formattage de données à l'aide de la méthode format() en utilisant les index
message = "Votre nom est: {0:12s}, age est: {1:3d} ans. Votre taille est {2:.2f} mètres.".format(nom, age, taille)
print(message)

