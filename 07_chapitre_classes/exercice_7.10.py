class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __str__(self):
        return str(self.x) + " " + str(self.y)


A = Vecteur(10, 20)
B = Vecteur(5, 15)
# Créer le vecteur C
C = A + B
print(C)
