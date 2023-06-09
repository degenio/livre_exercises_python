class Etudiant:
    ponderation = {'intra': 0.3,
                   'quiz1': 0.2,
                   'quiz2': 0.15,
                   'final': 0.35
                   }

    def __init__(self, prenom, nom, cours):
        self.prenom = prenom
        self.nom = nom
        self.cours = cours
        self.notes = {}

    def ajouter_note(self, examen, note):
        self.notes[examen] = note

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.cours}, {self.notes})"

    # Calcul se fait en utilisant la structure dict
    def calcul_moyenne(self):
        note_totale = 0
        for k in self.ponderation:
            note_totale += self.ponderation[k] * self.notes[k]

        return note_totale

    def faire_experience(self):
        print('Etudiant effectue une expérience scientifique')

def main():
    etud_science = Etudiant('alain', 'flouflou', 'Biologie 101')
    # Saisie de notes science
    for k in Etudiant.ponderation:
        note = int(input("Ajouter note de l'examen {}:".format(k)))
        etud_science.ajouter_note(k, note)
    # Calculer et Afficher la moyenne
    moyenne = etud_science.calcul_moyenne()
    print("L'etudiant de science a une note de:{}".format(moyenne))

    # appel de methode
    etud_science.faire_experience()

    # Etat de l'objet
    print(etud_science)


if __name__ == '__main__':
    main()