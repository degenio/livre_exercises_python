class ConvertisseurPoids:
    def __init__(self, valeur, unite):
        if not isinstance(valeur, (int, float)):
            raise ValueError("La valeur doit être un numérique.")
        if valeur < 0:
            raise ValueError("La valeur doit être positive.")
        self.valeur = valeur
        self.unite = unite

    def to_grammes(self):
        if self.unite == "gramme":
            return self.valeur
        elif self.unite == "kilogramme":
            return self.valeur * 1000
        elif self.unite == "pound":
            return self.valeur * 453.592
        elif self.unite == "ounce":
            return self.valeur * 28.3495
        else:
            raise ValueError("Unité invalide.")

    def to_kilogrammes(self):
        return self.to_grammes() / 1000

    def to_pounds(self):
        return self.to_grammes() / 453.592

    def to_ounces(self):
        return self.to_grammes() / 28.3495

if __name__ == '__main__':
    try:
        converter = ConvertisseurPoids(10, "kilogramme")
        wc = converter
        print(wc.to_grammes())  # prints 10000.0
        print(wc.to_pounds())  # prints 22.04622621875

        wc = ConvertisseurPoids(1000, "gramme")
        print(wc.to_kilogrammes())  # prints 1.0
        print(wc.to_ounces())  # prints 35.27396194958041

        wc = ConvertisseurPoids(-1, "pound")  # raises ValueError
    except ValueError as e:
        print(e)  # print "La valeur doit être positive."
