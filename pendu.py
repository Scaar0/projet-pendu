class JeuPenduUnJoueur:
    def __init__(self, vie_restante = 3, diff = 0, mot = ""):
        self.vie_restante = vie_restante
        self.diff = diff
        self.mot = mot
    
    
    def affichage(self):
        pass

    def choix_diff(self):
        diff = input("Quelle difficultée (Entrez le chiffre correspondant)? \n1 : Facile, mot de 5 lettres\n2 : Moyen, mot de 6 lettres\n3 : Dur, mot de 7 lettres\n")
        self.diff = diff

    
    
    
    
    
