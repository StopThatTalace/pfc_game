import random
import sys

score_bot = 0
score_j1 = 0

def end_game():
    print("Fin du jeu.")
    sys.exit()  

while score_bot != 2 and score_j1 != 2:
    bot = random.choice(["pierre", "feuille", "ciseaux"])
    
    joueur1 = input("pierre, feuille ou ciseaux ? : ")

    if (bot == "pierre" and joueur1 == "ciseaux") or (bot == "feuille" and joueur1 == "pierre") or (bot == "ciseaux" and joueur1 == "feuille"):
        print("Dommage! Vous avez perdu cette manche!")
        print("Le bot a choisi:", bot)
        score_bot += 1
        print("Le score est de", score_j1, ":", score_bot)
    elif (joueur1 == "pierre" and bot == "ciseaux") or (joueur1 == "feuille" and bot == "pierre") or (joueur1 == "ciseaux" and bot == "feuille"):
        print("Vous avez gagné !!")
        score_j1 += 1
        print("Le score est de", score_j1, ":", score_bot)
    else:
        print("Mince.. c'est une égalité!")
        print("Le score est de", score_j1, ":", score_bot)
    
    exit = input("Vous souhaitez continuez la partie (Y/n)")

    if exit == "n":
        end_game()
        

if score_bot == 2:
    print("Vous avez perdu la partie...")
    print("Le score final:", score_j1, ":", score_bot)
if score_j1 == 2:
    print("Félicitations, vous avez gagné la partie!")
    print("Le score final:", score_j1, ":", score_bot)

