ventes = float(input("Entrez le montant total des ventes pour le mois : "))

if ventes < 0:
    print("Erreur: le montant des ventes ne peut pas être négatif.")
else:
    if ventes < 1000:
        taux_commission = 0.025
    elif  ventes <= 5000:
        taux_commission = 0.05
    else:
        taux_commission = 0.075

    commission = ventes * taux_commission
    remuneration = commission + 5000  # 5000 $ est le salaire de base
    print("La rémunération du vendeur est de {0:.2f}$".format(remuneration))
