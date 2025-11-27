import random
import time

ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU = "\033[34m"
RESET = "\033[0m"  # Réinitialiser la couleur

def print_slow(texte, delay=0.03):
    for c in texte:
        print(f"{c}", end="", flush=True)
        time.sleep(delay)
    print()

class JeuPenduUnJoueur:
    def __init__(self, vie_restante = 4):
        self.vie_restante = vie_restante
        self.diff = self.choix_diff()
        self.mot = self.definir_mot()
        self.lettres_trouvees = ["_" for _ in self.mot]
        self.lettres_ratees = []
        self.t0 = time.time()
    
    def afficher_mot(self):
        return " ".join(self.lettres_trouvees)
    

    def afficher_pendu(self):
        print_slow(ROUGE + "\nMauvaise lettre !! " + RESET+ f"({self.vie_restante} vies restantes)")
        match self.vie_restante:
            case 3:
                print_slow("________\n" \
                      " |   |\n" \
                      " |   \n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n")
            case 2:
                print_slow("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |   \n" \
                      " | \n"
                      "_|_ \n")   
            case 1:
                print_slow("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " | \n"
                      "_|_ \n")         
            case 0:
                print_slow("________\n" \
                      " |   |\n" \
                      " |   ◯\n" \
                      " |  /|\\ \n" \
                      " |   |\n"
                      "_|_ \n")
            

    def choix_diff(self) -> int :
        while True:
            try:
                print_slow("Quelle difficultée (Entrez le " + VERT + "chiffre " + RESET + "correspondant) ?  \n1 : " + VERT + "Facile " + RESET + ": mot de 5 lettres\n2 : " + JAUNE + "Moyen " + RESET + ": mot de 6 lettres\n3 :"+ ROUGE +" Dur "+ RESET +": mot de 7 lettres", 0.02)
                diff = int(input())
                if not (diff == 1 or diff == 2 or diff == 3):
                    print_slow(ROUGE + "############################### \n" \
                "Entrez seulement 1, 2 ou 3 \n" \
                "############################### " + RESET)
                else:
                    break
            except ValueError:
                print_slow(ROUGE + "############################### \n" \
                "ERREUR : Pas de lettre acceptée. \n" \
                "Entrez seulement 1, 2 ou 3 \n" \
                "############################### " + RESET)
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
        return tab_mot[random.randint(0, len(tab_mot) - 1)].strip().lower()

    def demander_lettre(self):
        while True:
                lettre = input("Propose une lettre : ")
                lettre = lettre.lower()
                if not lettre.isalpha() or len(lettre) != 1:
                    print_slow(ROUGE + "############################### \n" \
                        "Entrez seulement une lettre\n" \
                        "############################### " + RESET)
                elif lettre in self.lettres_trouvees or lettre in self.lettres_ratees:
                    print_slow(ROUGE + "############################### \n" \
                        "Lettre déjà proposée\n" \
                        "############################### " + RESET)
                else:
                    break

        if lettre in self.mot:
            for i, l in enumerate(self.mot):
                if l == lettre:
                    self.lettres_trouvees[i] = lettre
            print_slow(VERT + "\nBonne lettre ! " + RESET)
        else:
            self.lettres_ratees.append(lettre)
            self.vie_restante -= 1
            if self.vie_restante >= 0:
                self.afficher_pendu()
    
    def est_gagne(self):
        return "_" not in self.lettres_trouvees

    def est_perdu(self):
        return self.vie_restante < 0
            

if __name__ == "__main__":
    print(BLEU + "======= Jeu du Pendu ======" + RESET)
    jeu = JeuPenduUnJoueur()
    while not (jeu.est_gagne() or jeu.est_perdu()):
        print_slow("\nMot :" + jeu.afficher_mot())
        print_slow("Lettres ratées :" + ", ".join(jeu.lettres_ratees))
        jeu.demander_lettre()

    t = int(time.time() - jeu.t0)
    if jeu.est_gagne():
        print_slow(VERT + 
              "___                    ___    __      _____      __\n" \
              "\\  \\                  /  /   |  |    |     \\    |  |\n" \
              " \\  \\      ____      /  /    |  |    |  |\\  \\   |  |\n" \
              "  \\  \\    /    \\    /  /     |  |    |  | \\  \\  |  |\n" \
              "   \\  \\  /  /\\  \\  /  /      |  |    |  |  \\  \\ |  |\n" \
              "    \\  \\/  /  \\  \\/  /       |  |    |  |   \\  \\|  |\n" \
              "     \\____/    \\____/        |__|    |__|    \\_____|\n" + RESET, 0.005)
        print_slow(f"Temps : {t}s \n")
        print_slow("Bravo ! Le mot était :"+ JAUNE + f" {jeu.mot}" + RESET)
    else:
        print_slow(ROUGE + "  ________            ____           _____     _____      ________\n" \
              " /  ____  \\          /    \\         |     \\   /     |    |  ______|\n" \
              "/  /    \\__\\        /  /\\  \\        |  |\\  \\_/  /|  |    |  |___\n" \
              "|  |    ____       /  /__\\  \\       |  | \\     / |  |    |      |\n" \
              "|  |   |__  \\     /  ______  \\      |  |  \\___/  |  |    |   ___|\n" \
              "\\  \\_____/  /    /  /      \\  \\     |  |         |  |    |  |_____\n" \
              " \\_________/    /__/        \\__\\    |__|         |__|    |________|\n", 0.005)
        print_slow("  _______    ___          ___     ________      ________\n" \
              " /  ____  \\  \\  \\        /  /    |  ______|    |   __   |\n" \
              "/  /    \\  \\  \\  \\      /  /     |  |___       |  |__|  | \n" \
              "|  |    |  |   \\  \\    /  /      |      |      |      __|\n" \
              "|  |    |  |    \\  \\  /  /       |   ___|      |  |\\  \\ \n" \
              "\\  \\____/  /     \\  \\/  /        |  |_____     |  | \\  \\\n" \
              " \\________/       \\____/         |________|    |__|  \\__\\\n " + RESET, 0.005)

        print_slow("________\n" \
              " |   |\n" \
              " |   ◯\n" \
              " |  /|\\ \n" \
              " |   |\n"
              "_|_ / \\ \n")
        print_slow(f"Temps : {t}s \n")
        print_slow("Le mot était : " + JAUNE + f"{jeu.mot}" + RESET)

    
    
    
    
