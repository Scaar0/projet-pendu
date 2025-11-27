# Installation
## 1. Cloner ou télécharger le projet
```bash
    git clone <repo>
    cd pendu
```
## 2. Vérifier votre version de Python

Le programme fonctionne sur **Python 3.8+**.

## 3. Préparer les fichiers de mots

Le jeu charge les listes suivantes :

```liste5.txt``` → mots de 5 lettres

```liste6.txt``` → mots de 6 lettres

```liste7.txt``` → mots de 7 lettres

Ils doivent être placés au même niveau que le script Python.

# Lancer le jeu
```bash
    python3.xx pendu.py
```

# Règles du jeu

1. Choisissez une difficulté :

    - **1 : Facile** → mot de 5 lettres

    - **2 : Moyen** → mot de 6 lettres

    - **3 : Difficile** → mot de 7 lettres

2. Proposez une lettre à chaque tour.

3. Vous perdez une vie à chaque erreur.

4. Le pendu se dessine progressivement…

5. Vous gagnez si toutes les lettres sont trouvées avant d’avoir 0 vie.

# Fonctionnalités avancées
## Affichage lent (effet machine à écrire)

Le texte est rendu avec un léger délai entre chaque caractère :
```bash
def print_slow(texte, delay=0.03):
    ...
```

## ASCII Art du pendu

Le pendu évolue selon le nombre de vies restantes (3 → 2 → 1 → 0 → Défaite).

## Gestion des couleurs ANSI

Propre, portable et compatible avec la plupart des terminaux.

# Organisation du code

```JeuPenduUnJoueur``` : classe principale

```print_slow()``` : affichage immersif

```Fonctions dédiées``` :

```choix_diff()``` → choix difficulté

```definir_mot()```→ sélection d’un mot

```demander_lettre``` → boucle principale d’entrée utilisateur

```afficher_pendu()```→ ASCII dynamique