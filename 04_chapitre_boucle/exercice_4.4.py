frais_premiere_annee = 2500  # Frais de scolarité de la première année
TAUX_INFLATION = 0.035  # Taux d'inflation annuel
annees_etudes = 4  # Durée des études en années

montant_total = frais_premiere_annee  # Montant total initialisé avec les frais de la première année

for annee in range(2, annees_etudes + 1):  # Ne pas oublie que l'index de fin n'est pas pris en compte
    frais_annee = frais_premiere_annee * (1 + TAUX_INFLATION) ** (annee - 1)
    montant_total += frais_annee

print("Le montant total payé à la fin des études est de :{:.2f}".format(montant_total))
