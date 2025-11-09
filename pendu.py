import random
import tkinter as tk

class DiffError(Exception):
    """Exception levée lorsque la difficulté n'est pas 1 ou 2 ou 3"""
    pass

class JeuPenduUnJoueur:
    def __init__(self, vie_restante = 3):
        self.vie_restante = vie_restante
        self.diff = self.choix_diff()
        self.mot = self.definir_mot()
        self.lettres_trouvees = ["_" for _ in self.mot]
        self.lettres_ratees = []
    
    def afficher_mot(self):
        return " ".join(self.lettres_trouvees)
    

    def afficher_pendu(self):
        
        match self.vie_restante:
            case 3:
                print(f"Mauvaise lettre ({self.vie_restante} vies restantes)")
                print("________\n" \
                      " |   |\n" \
                      " |   \n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n")
            case 2:
                print(f"Mauvaise lettre ({self.vie_restante} vies restantes)")
                print("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n")
                
            case 1:
                print(f"Mauvaise lettre ({self.vie_restante} vies restantes)")
                print("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " | \n"
                      "_|_ \n")
                
            case 0:
                print(f"Mauvaise lettre ({self.vie_restante} vies restantes)")
                print("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " |   |\n"
                      "_|_ \n")
            case -1:
                print("  ________            ____           _____     _____      ________\n" \
                      " /  ____  \\          /    \\         |     \\   /     |    |  ______|\n" \
                      "/  /    \\__\\        /  /\\  \\        |  |\\  \\_/  /|  |    |  |___\n" \
                      "|  |    ____       /  /__\\  \\       |  | \\     / |  |    |      |\n" \
                      "|  |   |__  \\     /  ______  \\      |  |  \\___/  |  |    |   ___|\n" \
                      "\\  \\_____/  /    /  /      \\  \\     |  |         |  |    |  |_____\n" \
                      " \\_________/    /__/        \\__\\    |__|         |__|    |________|\n")
                print("  _______    ___          ___     ________      ________\n" \
                      " /  ____  \\  \\  \\        /  /    |  ______|    |   __   |\n" \
                      "/  /    \\  \\  \\  \\      /  /     |  |___       |  |__|  | \n" \
                      "|  |    |  |   \\  \\    /  /      |      |      |      __|\n" \
                      "|  |    |  |    \\  \\  /  /       |   ___|      |  |\\  \\ \n" \
                      "\\  \\____/  /     \\  \\/  /        |  |_____     |  | \\  \\\n" \
                      " \\________/       \\____/         |________|    |__|  \\__\\\n")

                print("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " |   |\n"
                      "_|_ / \\ \n")

    def choix_diff(self) -> int :
        while True:
            diff = int(input("Quelle difficultée (Entrez le chiffre correspondant)? \n1 : Facile, mot de 5 lettres\n2 : Moyen, mot de 6 lettres\n3 : Dur, mot de 7 lettres\n"))
            print(diff)
            if not (diff == 1 or diff == 2 or diff == 3):
                print("Entrer un chiffre valide (1, 2 ou 3)")
            else:
                break
        return diff
        
    
    def definir_mot(self) -> str :
        match self.diff:
            case 1 :
                with open("liste5.txt") as liste5:
                    tab_mot = liste5.readlines()
            case 2:
                with open("liste6.txt") as liste6:
                    tab_mot = liste6.readlines()
            case 3:
                with open("liste7.txt") as liste7:
                    tab_mot = liste7.readlines()
            case _:
                raise DiffError("Erreur fatal de difficulté")
        return tab_mot[random.randint(0, len(tab_mot) - 1)].lower()

    def proposer_lettre(self):
        while True:
                lettre = input("Propose une lettre : ")
                lettre = lettre.lower()
                if not lettre.isalpha() or len(lettre) != 1:
                    print("Entre une seule lettre.")
                elif lettre in self.lettres_trouvees or lettre in self.lettres_ratees:
                    print("Lettre déjà proposée.")
                else:
                    break

        if lettre in self.mot:
            for i, l in enumerate(self.mot):
                if l == lettre:
                    self.lettres_trouvees[i] = lettre
            print(f"Bonne lettre ! ({self.afficher_mot()})")
        else:
            self.lettres_ratees.append(lettre)
            self.essais_restants -= 1
            self.afficher_pendu()
            


a = JeuPenduUnJoueur()

    
    
    
    
