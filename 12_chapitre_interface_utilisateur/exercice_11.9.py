import tkinter as tk
from tkinter import filedialog


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

        # Création du bouton pour lire le texte
        self.btn_lire = tk.Button(self, text="Lire fichier", command=self.open_file)
        self.btn_lire.pack()

    def open_file(self):
        # Ouvre la boîte de dialogue de sélection de fichier
        file_path =  filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        if file_path:
            # Affiche le contenu du fichier dans la zone de texte
            with open(file_path, "r") as f:
                self.zone_texte.delete("1.0", tk.END)
                self.zone_texte.insert(tk.END, f.read())

# Création de la fenêtre
root = tk.Tk()
app = Fenetre(master=root)
app.mainloop()