class Participant:
    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nom} {self.prenom}"


class Etudiant(Participant):
    ANNEES = ["1ere année", "2ieme année", "3ieme année", "4ieme année"]

    def __init__(self, nom, prenom, email, annee):
        super().__init__(nom, prenom, email)
        self.annee = annee

    def __str__(self):
        return super().__str__() + f" ({self.annee})"


class Employe(Participant):
    def __init__(self, nom, prenom, email, bureau, salaire, date_embauche):
        super().__init__(nom, prenom, email)
        self.bureau = bureau
        self.salaire = salaire
        self.date_embauche = date_embauche

    def __str__(self):
        return super().__str__() + f" ({self.__class__.__name__})"


class Enseignant(Employe):
    def __init__(self, nom, prenom, email, bureau, salaire, date_embauche, rang, horaires_bureau):
        super().__init__(nom, prenom, email, bureau, salaire, date_embauche)
        self.rang = rang
        self.horaires_bureau = horaires_bureau

    def __str__(self):
        return super().__str__() + f", {self.rang}"


class Staff(Employe):
    def __init__(self, nom, prenom, email, bureau, salaire, date_embauche, titre):
        super().__init__(nom, prenom, email, bureau, salaire, date_embauche)
        self.titre = titre

    def __str__(self):
        return super().__str__() + f", {self.titre}"


if __name__ == '__main__':
    # création d'un objet Participant
    part = Participant("Flouflou", "Alain", "alain.flouflou@smail.com")
    print(part)  # Participant

    # création d'un objet Etudiant
    etud = Etudiant("Flouclair", "Abdel", "abdel.flouclair@smail.com", "2ieme année")
    print(etud)  # Etudiant: Smith John (
