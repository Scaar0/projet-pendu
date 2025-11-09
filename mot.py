import unicodedata

def enlever_accents(texte):
    # Normalise le texte et supprime les accents
    texte_normalise = unicodedata.normalize('NFD', texte)
    return ''.join(c for c in texte_normalise if unicodedata.category(c) != 'Mn')


with open("liste_francais.txt", "r", encoding="latin-1") as f:
    mots_bruts = f.readlines()

tab5 = []
tab6 = []
tab7 = []
for elt in mots_bruts:
    mot = elt.strip().lower()
    mot = enlever_accents(mot)         # enlève les accents
    if len(mot) == 5:
        tab5.append(mot)
    elif len(mot) == 6:
        tab6.append(mot)
    elif len(mot) == 7:
        tab7.append(mot)

with open("liste5.txt", "w", encoding="utf‑8") as liste5:
    for elt in tab5:
        liste5.write(elt + "\n")

with open("liste6.txt", "w", encoding="utf‑8") as liste6:
    for elt in tab6:
        liste6.write(elt + "\n")

with open("liste7.txt", "w", encoding="utf‑8") as liste7:
    for elt in tab7:
        liste7.write(elt + "\n")