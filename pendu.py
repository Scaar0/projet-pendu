import random

class DiffError(Exception):
    """Exception levée lorsque la difficulté n'est pas 1 ou 2 ou 3"""
    pass

class JeuPenduUnJoueur:
    def __init__(self, vie_restante = 3, diff = 0, mot = ""):
        self.vie_restante = vie_restante
        self.diff = diff
        self.mot = mot
    
    
    def affichage(self):
        pass

    def choix_diff(self):
        while True:
            try:
                diff = int(input("Quelle difficultée (Entrez le chiffre correspondant)? \n1 : Facile, mot de 5 lettres\n2 : Moyen, mot de 6 lettres\n3 : Dur, mot de 7 lettres\n"))
                if diff != 1 or diff != 2 or diff != 3:
                    raise DiffError("Entrer un chiffre valide (1, 2 ou 3)")
                else:
                    break
            except ValueError:
                print("Erreur : Entrer un chiffre valide (1, 2 ou 3)")
            except DiffError as e:
                print(f"Erreur : {e}")
        
        self.diff = diff
    
    def definir_mot(self):
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
        self.mot = tab_mot[random.randint(0, len(tab_mot) - 1)]

    def jouer(self):
        pass

    
        

    

    
    
    
    
