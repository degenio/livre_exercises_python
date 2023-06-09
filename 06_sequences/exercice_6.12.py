# création du dictionnaire fruits
fruits = {
    "Pommes": 10,
    "Bananes": 5,
    "Oranges": 8,
    "Fraises": 15
}

# 1. Vérification si le fruit entré par l'utilisateur est présent dans le dictionnaire
fruit = input("Entrez le nom d'un fruit : ")
if fruit in fruits:
    print(f"Le fruit {fruit} a une quantité de {fruits[fruit]}")
else:
    print("Erreur : ce fruit n'est pas dans le dictionnaire")

# 2. Ajout d'un nouveau fruit et sa quantité associée
nouveau_fruit = input("Entrez le nom d'un nouveau fruit : ")
nouvelle_quantite = int(input(f"Entrez la quantité de {nouveau_fruit} : "))
#Verifier si le fruit est dans le dictionnaire
if nouveau_fruit in fruits:
    print(f"Le fruit {fruit} existe et a une quantité de {fruits[fruit]}")
else:
    fruits[nouveau_fruit] = nouvelle_quantite

# 3. Affichage du dictionnaire mis à jour
print("Dictionnaire mis à jour :", fruits)

# 4. Suppression d'un fruit entré par l'utilisateur
fruit_a_supprimer = input("Entrez le nom du fruit à supprimer : ")
if fruit_a_supprimer in fruits:
    del fruits[fruit_a_supprimer]
else:
    print("Erreur : ce fruit n'est pas dans le dictionnaire")
\end{mypython}
\begin{mypython}
# 5. Affichage du dictionnaire mis à jour
print("Dictionnaire mis à jour :", fruits)

# 6. Recherche d'un fruit correspondant à une quantité donnée
quantite = int(input("Entrez une quantité : "))
fruit_trouve = False
for fruit, quant in fruits.items():
    if quant == quantite:
        print(f"Le fruit associé à une quantité de {quantite} est {fruit}")
        fruit_trouve = True
        break
if not fruit_trouve:
    print("Erreur : aucune quantité correspondante trouvée dans le dictionnaire")
