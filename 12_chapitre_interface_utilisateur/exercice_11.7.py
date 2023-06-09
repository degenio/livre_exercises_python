import tkinter as tk

class Converter:
    def __init__(self, master):
        self.master = master
        master.title("Convertisseur de poids")
        master.geometry('260x150')

        # Création des widgets
        self.lbl_kg = tk.Label(master, text="Kilogrammes:")
        self.lbl_lb = tk.Label(master, text="Livres:")
        self.entry_kg = tk.Entry(master)
        self.entry_lb = tk.Entry(master)
        self.btn_kg_to_lb = tk.Button(master, text="Convertir kg en lb", command=self.convert_kg_to_lb)
        self.btn_lb_to_kg = tk.Button(master, text="Convertir lb en kg", command=self.convert_lb_to_kg)

        # Placement des widgets
        self.lbl_kg.grid(row=0, column=0)
        self.entry_kg.grid(row=0, column=1)
        self.btn_kg_to_lb.grid(row=1, column=0, columnspan=2, pady=10)
        self.lbl_lb.grid(row=2, column=0)
        self.entry_lb.grid(row=2, column=1)
        self.btn_lb_to_kg.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_kg_to_lb(self):
        try:
            kg = float(self.entry_kg.get())
            lb = kg * 2.2
            self.entry_lb.delete(0, tk.END)
            self.entry_lb.insert(0, round(lb, 2))
        except ValueError:
            self.entry_lb.delete(0, tk.END)
            self.entry_lb.insert(0, "Erreur")

    def convert_lb_to_kg(self):
        try:
            lb = float(self.entry_lb.get())
            kg = lb / 2.2
            self.entry_kg.delete(0, tk.END)
            self.entry_kg.insert(0, round(kg, 2))
        except ValueError:
            self.entry_kg.delete(0, tk.END)
            self.entry_kg.insert(0, "Erreur")

root = tk.Tk()
converter = Converter(root)
root.mainloop()
