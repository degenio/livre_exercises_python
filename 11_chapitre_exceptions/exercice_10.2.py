class NombreComplexe:
    def __init__(self, real, imaginaire):
        try:
            self.reel = float(real)
            self.imaginaire = float(imaginaire)
        except ValueError:
            raise ValueError("Valeurs invalides. Saisir des nombres pour la partie réelle et imaginaire.")

    def __str__(self):
        if self.imaginaire < 0:
            return f"{self.reel} {self.imaginaire}j"
        else:
            return f"{self.reel}+{self.imaginaire}j"

    def conjugate(self):
        return NombreComplexe(self.reel, -self.imaginaire)

    def __add__(self, other):
        return NombreComplexe(self.reel + other.reel, self.imaginaire + other.imaginaire)

    def __sub__(self, other):
        return NombreComplexe(self.reel - other.reel, self.imaginaire - other.imaginaire)

    def __mul__(self, other):
        return NombreComplexe(self.reel * other.reel - self.imaginaire * other.imaginaire,
                              self.reel * other.imaginaire + self.imaginaire * other.reel)

if __name__ == '__main__':
    # création de deux nombres complexe
    z1 = NombreComplexe(3, 4)
    z2 = NombreComplexe(1, -2)

    # affichage des nombres complexes
    print(z1)  # affiche "3+4j"
    print(z2)  # affiche "1-2j"

    # calcul du conjugué et du module d'un nombre complexe
    print(z1.conjugate())  # affiche "3-4j"

    # opérations arithmétiques sur deux nombres complexes
    print(z1 + z2)  # affiche "4+2j"
    print(z1 - z2)  # affiche "2+6j"
    print(z1 * z2)  # affiche "11-2j"

    #Valeurs invalides
    z2 = NombreComplexe(1, 'toto')

