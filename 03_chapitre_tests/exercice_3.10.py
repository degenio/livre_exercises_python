# Définition des constantes pour le calcul du minimum à payer
MINIMUM_1 = 50
MINIMUM_2 = 295
TAUX_MINIMUM_3 = 0.25

# Lecture des entrées utilisateur
solde_precedent = float(input("Entrez le solde précédent du compte : "))
versement = float(input("Entrez le versement effectué par le client : "))
achats = float(input("Entrez le montant total des charges additionnelles (achats) : "))

# Calcul du solde courant et de l'intérêt dû
solde_courant = solde_precedent - versement
if solde_courant <= 0:
    frais_interet = 0
else:
    frais_interet = (solde_courant + achats) * 0.05

# Calcul du nouveau solde et du minimum à payer
nouveau_solde = solde_courant + achats + frais_interet
if nouveau_solde < MINIMUM_1:
    minimum_a_payer = nouveau_solde
elif nouveau_solde < MINIMUM_2:
    minimum_a_payer = MINIMUM_1
else:
    minimum_a_payer = nouveau_solde * TAUX_MINIMUM_3

# Affichage du relevé mensuel des charges
print("MasterPop International")
print("Relevé mensuel des charges")
print("Solde précédent :", format(solde_precedent, ".2f"), "$")
print("Versement :", format(versement, ".2f"), "$")
print("Solde courant :", format(solde_courant, ".2f"), "$")
print("Frais d'intérêt :", format(frais_interet, ".2f"), "$")
print("Achats :", format(achats, ".2f"), "$")
print("Nouveau solde :", format(nouveau_solde, ".2f"), "$")
print("Minimum à payer :", format(minimum_a_payer, ".2f"), "$")