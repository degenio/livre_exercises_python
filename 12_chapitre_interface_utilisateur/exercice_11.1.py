import tkinter as tk

class Fenetre(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creer_widgets()

    def creer_widgets(self):
        # Création de la première zone de texte
        self.area_src = tk.Text(self)
        self.area_src.pack()

        # Création de la deuxième zone de texte
        self.area_dest = tk.Text(self)
        self.area_dest.pack()

        # Création du bouton pour copier le texte
        self.btn_copy = tk.Button(self, text="Copier", command=self.copier_texte)
        self.btn_copy.pack()
 
    def copier_texte(self):
        # Copie du texte de la première zone de texte dans la deuxième zone de texte
        text = self.area_src.get("1.0", "end-1c")  # Récupération du texte de la première zone de texte
        self.area_dest.delete("1.0", "end")  # Effacement du texte de la deuxième zone de texte
        self.area_dest.insert("1.0", text)  # Copie du texte dans la deuxième zone de texte

# Création de la fenêtre
root = tk.Tk()
app = Fenetre(master=root)
app.mainloop()