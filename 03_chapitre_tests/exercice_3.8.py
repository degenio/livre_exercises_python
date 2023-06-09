salaire = float(input('Saisir votre salaire:'))
if salaire < 0:
    print("Erreur: le salaire ne peut pas être négatif.")
else:
    if salaire >= 100000:
        taux_imposition = 0.45
    elif salaire >= 70000:
        taux_imposition = 0.32
    elif salaire >= 40000:
        taux_imposition = 0.18
    else:
        taux_imposition = 0.1

    impot = salaire * taux_imposition
    print(f"Pour un salaire de {salaire:.2f}$, l'impôt sur le revenu est de {impot:.2f}$.")

