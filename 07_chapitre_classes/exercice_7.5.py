class RegistreFruit:
    def __init__(self):
        self.dictionnaire_fruits = {}

    def ajouter_fruit(self, fruit):
        if fruit.nom in self.dictionnaire_fruits:
            self.dictionnaire_fruits[fruit.nom].quantite += fruit.quantite
        else:
            self.dictionnaire_fruits[fruit.nom] = fruit

    def supprimer_fruit(self, nom):
        if nom in self.dictionnaire_fruits:
            del self.dictionnaire_fruits[nom]
        else:
            print(f"{nom} n'est pas présent dans le dictionnaire.")

    def verifier_fruit(self, nom):
        if nom in self.dictionnaire_fruits:
            print(f"{nom} : {self.dictionnaire_fruits[nom]}")
        else:
            print(f"{nom} n'est pas présent dans le dictionnaire.")

    def supprimer_fruit_utilisateur(self):
        nom = input("Entrez le nom du fruit à supprimer : ")
        self.supprimer_fruit(nom)

    def afficher_dictionnaire(self):
        print('=' * 40)
        for k, v in self.dictionnaire_fruits.items():
            print(k, ':', v)


class Fruit:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def __str__(self):
        return "{}, {}".format(self.nom,self.quantite)


if __name__ == '__main__':
    # Creation du registre
    fruits = RegistreFruit()

    # Création d'un fruit
    pomme = Fruit("Pommes", 10)
    fruits.ajouter_fruit(pomme)

    # Creation d'un fruit
    banane = Fruit("Bananes", 5)
    fruits.ajouter_fruit(banane)

    # Ajout d'un fruit existant
    pomme = Fruit("Pommes", 22)
    fruits.ajouter_fruit(pomme)

    # Affichage du dictionnaire de fruits
    fruits.afficher_dictionnaire()

    # Suppression d'un fruit existant
    fruits.supprimer_fruit("Pommes")

    # Suppression d'un fruit non existant
    fruits.supprimer_fruit("Caroube")

    # Vérification de la présence d'un fruit
    fruits.verifier_fruit("Oranges")

    # Affichage du dictionnaire de fruits à la fin des opérations
    fruits.afficher_dictionnaire()
