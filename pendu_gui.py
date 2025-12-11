import tkinter as tk
from pendu import JeuPenduUnJoueur  # ← adapte le nom du fichier !

class MenuDifficulte:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Choix de difficulté")
        self.root.geometry("400x300")

        tk.Label(self.root, text="Choisis une difficulté", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Facile (5 lettres)", font=("Arial", 14),
                  command=lambda: self.start_game(1)).pack(pady=10)

        tk.Button(self.root, text="Moyen (6 lettres)", font=("Arial", 14),
                  command=lambda: self.start_game(2)).pack(pady=10)

        tk.Button(self.root, text="Difficile (7 lettres)", font=("Arial", 14),
                  command=lambda: self.start_game(3)).pack(pady=10)

        self.root.mainloop()

    def start_game(self, diff):
        self.root.destroy()
        PenduGUI(diff)


class PenduGUI:
    def __init__(self, diff):
        self.jeu = JeuPenduUnJoueur(diff=diff)

        # --- Fenêtre ---
        self.root = tk.Tk()
        self.root.title("Jeu du Pendu")
        self.root.geometry("650x600")
        self.root.resizable(False, False)

        # --- Mot à deviner ---
        self.label_mot = tk.Label(self.root, text=self.jeu.afficher_mot(),
                                  font=("Arial", 32), pady=20)
        self.label_mot.pack()

        # --- Lettres ratées ---
        self.label_ratees = tk.Label(self.root, text="Lettres ratées : ",
                                     font=("Arial", 14))
        self.label_ratees.pack()

        # --- ASCII pendu ---
        self.label_pendu = tk.Label(self.root, text="", font=("Courier", 14), justify="left", anchor="w")
        self.label_pendu.pack(pady=10)
        self.update_pendu()

        # --- Clavier A–Z ---
        frame = tk.Frame(self.root)
        frame.pack(pady=15)

        for i in range(26):
            lettre = chr(ord('a') + i)
            bouton = tk.Button(frame, text=lettre, width=4, height=1,
                               command=lambda l=lettre: self.jouer(l))
            bouton.grid(row=i // 9, column=i % 9, padx=2, pady=2)

        # --- Message de fin ---
        self.label_fin = tk.Label(self.root, text="", font=("Arial", 20), fg="green")
        self.label_fin.pack(pady=10)

        self.root.mainloop()
        
    def jouer(self, lettre):
        """Réagit quand on clique sur une lettre."""
        
        if lettre in self.jeu.lettres_ratees or lettre in self.jeu.lettres_trouvees:
            return
        
        # Même logique que dans ta version console
        if lettre in self.jeu.mot:
            for i, l in enumerate(self.jeu.mot):
                if l == lettre:
                    self.jeu.lettres_trouvees[i] = lettre
        else:
            self.jeu.lettres_ratees.append(lettre)
            self.jeu.vie_restante -= 1
        
        # Mise à jour interface
        self.label_mot.config(text=self.jeu.afficher_mot())
        self.label_ratees.config(text="Lettres ratées : " + ", ".join(self.jeu.lettres_ratees))
        self.update_pendu()

        # Fin du jeu ?
        if self.jeu.est_gagne():
            self.label_fin.config(text=f"🎉 Bravo ! Vous avez gagné !\nLe mot était : {self.jeu.mot}", fg="green")
            self.desactiver_clavier()
        elif self.jeu.est_perdu():
            self.label_fin.config(text=f"💀 Perdu !\nLe mot était : {self.jeu.mot}", fg="red")
            self.desactiver_clavier()
            

    def update_pendu(self):
        pendus = ["________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " |   |\n"
                      "_|_ / \\\n",
                      "________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " |   |\n"
                      "_|_ \n",
                      "________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " | \n"
                      "_|_ \n",
                      "________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n",
                      "________\n" \
                      " |   |\n" \
                      " |   \n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n",
                      "________\n" \
                      " |   \n" \
                      " |   \n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n"
        ]

        index = self.jeu.vie_restante + 1
        self.label_pendu.config(text=pendus[index])
    
    def desactiver_clavier(self):
        """Désactive tous les boutons A–Z."""
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for bouton in widget.winfo_children():
                    bouton.config(state="disabled")

