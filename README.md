### Installation
1. Cloner ou télécharger le projet
```bash
    git clone <repo>
    cd pendu
```
2. Vérifier votre version de Python

Le programme fonctionne sur Python 3.8+.

python --version

3. Préparer les fichiers de mots

Le jeu charge les listes suivantes :

liste5.txt → mots de 5 lettres

liste6.txt → mots de 6 lettres

liste7.txt → mots de 7 lettres

Ils doivent être placés au même niveau que le script Python.

Si vous avez un fichier brut avec accents, utilisez un script de nettoyage (non inclus ici) pour convertir en lettres sans accents.

🚀 Lancer le jeu
python pendu.py

🎯 Règles du jeu

Choisissez une difficulté :

1 : Facile → mot de 5 lettres

2 : Moyen → mot de 6 lettres

3 : Difficile → mot de 7 lettres

Proposez une lettre à chaque tour.

Vous perdez une vie à chaque erreur.

Le pendu se dessine progressivement…

Vous gagnez si toutes les lettres sont trouvées avant d’avoir 0 vie.

🖥️ Fonctionnalités avancées
✔️ Affichage lent (effet machine à écrire)

Le texte est rendu avec un léger délai entre chaque caractère :

def print_slow(texte, delay=0.03, couleur=""):
    ...

✔️ ASCII Art du pendu

Le pendu évolue selon le nombre de vies restantes (3 → 2 → 1 → 0).

✔️ Gestion des couleurs ANSI

Propre, portable et compatible avec la plupart des terminaux.

📚 Organisation du code

JeuPenduUnJoueur : classe principale

print_slow() : affichage immersif

Fonctions dédiées :

choix_diff() → choix difficulté

definir_mot() → sélection d’un mot

demander_lettre() → boucle principale d’entrée utilisateur

afficher_pendu() → ASCII dynamique