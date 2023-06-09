class Utilisateur:
    def __init__(self, nom, prenom, age, tel):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.tel = tel

class Kiosque:
    def __init__(self):
        # Initialisation de la liste pour stocker les informations
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
        # Si la liste atteint la taille de 5, afficher les informations contenues dans la liste
        if len(self.utilisateurs) == 5:
            print("="*50)
            self.afficher_utilisateurs()
            self.utilisateurs = []

    def afficher_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(f"Nom: {utilisateur.nom}")
            print(f"Prénom: {utilisateur.prenom}")
            print(f"Age: {utilisateur.age}")
            print(f"Téléphone: {utilisateur.tel}")
            print("-----------")

    # Définition de la fonction pour demander les informations à l'utilisateur
    def demander_infos(self):
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")
        age = int(input("Entrez votre âge : "))
        telephone = input("Entrez votre numéro de téléphone : ")
        return Utilisateur(nom, prenom, age, telephone)

# Exemple d'utilisation
kiosque = Kiosque()
infos_utilisateur = kiosque.demander_infos()
kiosque.ajouter_utilisateur(infos_utilisateur)
#Pour tester, appeler 5 fois la méthode d'ajout