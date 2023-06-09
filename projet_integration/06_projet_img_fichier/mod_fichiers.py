import csv

def enregistrer_img(nom_fichier, pat):
    with open(nom_fichier, "a", newline="\n") as fouc:
        writeur = csv.writer(fouc, quoting=csv.QUOTE_NONNUMERIC)
        writeur.writerow((pat.nom, pat.age, pat.sexe, pat.poids, pat.taille))
