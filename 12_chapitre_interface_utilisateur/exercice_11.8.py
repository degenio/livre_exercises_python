import tkinter as tk

class Fenetre(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creer_widgets()

    def creer_widgets(self):
        # Création de la zone de texte
        self.zone_texte = tk.Text(self)
        self.zone_texte.pack()

        # Création du bouton pour enregistrer le texte
        self.btn_sauvegarder = tk.Button(self, text="Enregistrer", command=self.save_text)
        self.btn_sauvegarder.pack()

    def save_text(self):
        # Récupération du texte de la zone de texte
        text = self.zone_texte.get("1.0", "end-1c")

        # Enregistrement du texte dans un fichier texte
        with open("sortie.txt", "w") as f:
            f.write(text)

# Création de la fenêtre
root = tk.Tk()
app = Fenetre(master=root)
app.mainloop()