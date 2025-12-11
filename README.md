# 🎮 Jeu du Pendu - Projet Python CY Tech

Un jeu du Pendu interactif développé en Python dans le cadre d'un projet académique à CY Tech. Le jeu propose une interface en ligne de commande avec affichage ASCII art et plusieurs niveaux de difficulté.

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Règles du jeu](#-règles-du-jeu)
- [Auteur](#-auteur)

## ✨ Fonctionnalités

- 🎯 **Trois niveaux de difficulté** : Facile (5 lettres), Moyen (6 lettres), Difficile (7 lettres)
- 📝 **Dictionnaires de mots** personnalisés par difficulté

## 🔧 Prérequis

- Python 3.8 ou supérieur

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Scaar0/projet-pendu.git
cd projet-pendu
```

### 2. Vérifier votre installation Python

```bash
python --version
# ou
python3 --version
```

Le projet nécessite Python 3.8+.

### 3. Structure des fichiers

Assurez-vous que tous les fichiers sont présents :

```
projet-pendu/
│
├── main.py              # Point d'entrée du jeu
├── pendu.py             # Logique principale du jeu
├── mot.py               # Gestion des mots
├── pendu_gui.py         # Interface graphique
│
├── liste5.txt           # Dictionnaire - mots de 5 lettres
├── liste6.txt           # Dictionnaire - mots de 6 lettres
├── liste7.txt           # Dictionnaire - mots de 7 lettres
└── liste_francais.txt   # Dictionnaire général
```

## 🚀 Utilisation

### Lancer le jeu en mode console

```bash
python main.py
```

ou

```bash
python3 main.py
```

## 📁 Structure du projet

### `main.py`
Point d'entrée principal qui initialise et lance le jeu.

### `pendu.py`
Contient la classe `JeuPenduUnJoueur` avec toutes les mécaniques du jeu :
- Gestion des vies
- Logique de jeu (vérification des lettres, gestion des victoires/défaites)

### `mot.py`
Gestion de la sélection et du chargement des mots depuis les fichiers texte.

### `pendu_gui.py`
Interface graphique.

### Fichiers de données
- `liste5.txt` : Mots de 5 lettres
- `liste6.txt` : Mots de 6 lettres
- `liste7.txt` : Mots de 7 lettres
- `liste_francais.txt` : Dictionnaire complet

## 🎮 Règles du jeu

1. **Choisir la difficulté** :
   - `1` : Facile (mot de 5 lettres)
   - `2` : Moyen (mot de 6 lettres)
   - `3` : Difficile (mot de 7 lettres)

2. **Deviner le mot** :
   - Proposez une lettre à chaque tour
   - Si la lettre est dans le mot, elle s'affiche
   - Sinon, vous perdez une vie et le pendu se dessine

3. **Conditions de victoire** :
   - ✅ Vous gagnez si vous trouvez toutes les lettres avant d'avoir 0 vie
   - ❌ Vous perdez si vous n'avez plus de vie


### Architecture orientée objet

Le jeu est structuré autour de la classe `JeuPenduUnJoueur` qui encapsule toute la logique du jeu, facilitant la maintenance et l'évolution du code.

## 👨‍💻 Auteur

**Scaar0**
- GitHub : [@Scaar0](https://github.com/Scaar0)
**anes931**
- GitHub : [@anes931](https://github.com/anes931)

## 📝 Licence

Projet académique réalisé dans le cadre d'un cours Python à CY Tech.

---
