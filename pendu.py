import random

class JeuPenduUnJoueur:
    def __init__(self, diff=1, vie_restante=4):
        self.vie_restante = vie_restante
        self.diff = diff
        self.mot = self.definir_mot()
        self.lettres_trouvees = ["_" for _ in self.mot]
        self.lettres_ratees = []
    
    def afficher_mot(self):
        return " ".join(self.lettres_trouvees)    
    
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
    
    def est_gagne(self):
        return "_" not in self.lettres_trouvees

    def est_perdu(self):
        return self.vie_restante < 0
            

    
    
    
    
