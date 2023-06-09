import tkinter as tk

class Fenetre(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creer_widgets()

    def creer_widgets(self):
        # Création de la liste des couleurs
        self.colors = ["Red", "Green", "Blue", "Yellow", "Purple"]

        # Création de la liste déroulante
        self.color_variable = tk.StringVar(self)
        self.color_variable.set(self.colors[0])  # Valeur initiale de la liste
        self.color_dropdown = tk.OptionMenu(self, self.color_variable, *self.colors)
        self.color_dropdown.pack()

        # Création du bouton pour changer la couleur de fond
        self.change_color_button = tk.Button(self, text="Changer la couleur", command=self.changer_couleur)
        self.change_color_button.pack()

    def changer_couleur(self):
        # Changement de la couleur de fond de la fenêtre
        self.master.configure(bg=self.color_variable.get())

# Création de la fenêtre
root = tk.Tk()
root.geometry('300x100')
root.title('Choix de couleur')
app = Fenetre(master=root)
app.mainloop()