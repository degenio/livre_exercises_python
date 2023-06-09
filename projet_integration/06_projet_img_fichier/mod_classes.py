class Patient:  # Classe entité ou domaine
    def __init__(self, nom: str, age: int, sexe: int, poids: float, taille: float):
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.poids = poids
        self.taille = taille

    def __str__(self):
        return "Nom:{}, age:{}, sexe:{}, poids:{}, taille:{}".format(self.nom,
        self.age, self.sexe, self.poids, self.taille)

    def calculer_img(self):  # On peut utiliser cette méthode pour le calcul IMG
        return (1.2 * self.poids / (self.taille ** 2)) + (0.23 * self.age) - (10.8 * self.sexe) - 5.4
