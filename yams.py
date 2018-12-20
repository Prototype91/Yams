#On importe le module nécessaire au lancé de dé :
from random import randint

#Création des caractéristiques des joueurs :
joueur_A = {
    "brelan": False,
    "full": False,
    "carré": False,
    "winner": False
}

joueur_B = {
    "brelan": False,
    "full": False,
    "carré": False,
    "winner": False
}

#fonction dans laquelle le joueur A lance le dé :
def roll_dice_joueur_A():

    #compteur des faces apparues :
    counter_A = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    #Liste dans laquelle sont compris les résultats de dés :
    l = []

    for i in range(1, 6):
        result = randint(1, 6)
        l.append(result)
    print(l)

    #On compte les dés à même chiffre :
    for k in l:
        if k == 6:
            counter_A[6] += 1
        if k == 5:
            counter_A[5] += 1
        if k == 4:
            counter_A[4] += 1
        if k == 3:
            counter_A[3] += 1
        if k == 2:
            counter_A[2] += 1
        if k == 1:
            counter_A[1] += 1

    #On détermine la combinaison de dés :
    if set(counter_A.values()) == {0, 5}:
        print("Vous avez un Yams")

    if set(counter_A.values()) == {0, 1, 4}:
        print("Vous avez un carré")
        joueur_A["carré"] = True

    if set(counter_A.values()) == {0, 2, 3}:
        print("Vous avez un Full")
        joueur_A["full"] = True

    if set(counter_A.values()) == {0, 1, 3}:
        print("Vous avez un Brelan")
        joueur_A["brelan"] = True

    if set(counter_A.values()) == {0, 1}:
        print("Vous n'avez rien")

    if set(counter_A.values()) == {0, 1, 2}:
        print("Vous avez au moins une paire")

    #Cas où le joueur A à gagné :
    if joueur_A["carré"] == True and joueur_A["full"] == True and joueur_A["brelan"] == True:
        joueur_A["winner"] = True
        print("Joueur A est le vainqueur !")

#fonction dans laquelle le joueur B lance le dé :
def roll_dice_joueur_B():

    #compteur des faces apparues :
    counter_B = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    #Liste dans laquelle sont compris les résultats de dés :
    l = []

    for i in range(1, 6):
        result = randint(1, 6)
        l.append(result)
    print(l)

    #On compte les dés à même chiffre :
    for k in l:
        if k == 6:
            counter_B[6] += 1
        if k == 5:
            counter_B[5] += 1
        if k == 4:
            counter_B[4] += 1
        if k == 3:
            counter_B[3] += 1
        if k == 2:
            counter_B[2] += 1
        if k == 1:
            counter_B[1] += 1
    
    #On détermine la combinaison de dés :
    if set(counter_B.values()) == {0, 5}:
        print("Vous avez un Yams")

    if set(counter_B.values()) == {0, 1, 4}:
        print("Vous avez un carré")
        joueur_B["carré"] = True

    if set(counter_B.values()) == {0, 2, 3}:
        print("Vous avez un Full")
        joueur_B["full"] = True

    if set(counter_B.values()) == {0, 1, 3}:
        print("Vous avez un Brelan")
        joueur_B["brelan"] = True

    if set(counter_B.values()) == {0, 1}:
        print("Vous n'avez rien")

    if set(counter_B.values()) == {0, 1, 2}:
        print("Vous avez au moins une paire")

    #Cas où le joueur B à gagné :
    if joueur_B["carré"] == True and joueur_B["full"] == True and joueur_B["brelan"] == True:
        joueur_B["winner"] = True
        print("Joueur B est le vainqueur !")

#On créer une fonction pour le jeu :
def game():
    roll_dice_joueur_A()
    roll_dice_joueur_B()

#Boucle de jeu :
while joueur_A["winner"] == False and joueur_B["winner"] == False:
    game()
