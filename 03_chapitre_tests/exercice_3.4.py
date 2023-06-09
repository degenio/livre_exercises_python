TAUX_CHANGE = 1.21
# Demander à l'utilisateur de saisir 0 pour convertir des dollars américains
# en dollars canadiens et 1 pour convertir des dollars canadiens en dollars américains
choix = int(input("Entrez 0 pour convertir des dollars américains en dollars canadiens \n ou 1 pour convertir des dollars canadiens en dollars américains: "))

# Demander à l'utilisateur de saisir le montant à convertir
montant = float(input("Entrez le montant à convertir: "))

if choix == 0:
    # Conversion de dollars américains en dollars canadiens
    taux = TAUX_CHANGE  # taux de change actuel USD/CAD
    montant_converti = montant * taux
    print("${0:,.2f} USD est égal à ${1:,.2f} CAD".format(montant, montant_converti))
elif choix == 1:
    # Conversion de dollars canadiens en dollars américains
    taux = 1/TAUX_CHANGE  # taux de change actuel CAD/USD
    montant_converti = montant * taux
    print("${:,.2f} CAD est égal à ${:,.2f} USD".format(montant, montant_converti))
else:
    print("Choix invalide. Veuillez entrer 0 ou 1 pour choisir la conversion désirée.")
