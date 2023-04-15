import random

MIN_VALUE = 0
MAX_VALUE = 100

value = random.randint(MIN_VALUE, MAX_VALUE)
echec = random.randint(1,10)
invoc = random.randint(2,7)
bonneFortune = random.randint(1, 4000) + 4000
mauvaiseFortune = random.randint(250,2000)
found = False
MAX_ATTEMPTS = 6
reponse = 0

print("")

for _ in range(MAX_ATTEMPTS):
        answer = int(input(f"---> Le code est compris entre 1 et 100. Veuilez entrer le code ? il vous reste {6 - reponse} essais:......"))

        if answer == value:
            print("")
            print("     le coffre s'ouvre !!!!")
            print("")
            print(f"     Vous trouvez {bonneFortune} Thrônes !!!")
            print("")
            found = True
            break

        else:

            if answer > value:
                print("")
                print("     c'est inférieur !")
            else:
                print("")
                print("     c'est supérieur !")

            match echec:
                case 1:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Des visions d'horreur vous assaille, vous subissez -10 en Perception jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 2:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     un gaz est libéré, vous subissez -10 en endurance jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 3:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Un flash vous éblouit, vous subissez -10 en intelligence jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 4:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Un liquide vous éclabousse, vous subissez -10 en Charisme jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 5:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Une voix vous hurle dans les oreilles, vous subissez -10 en force mentale jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 6:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Votre vue se trouble, vous subissez -10 en capacité de tir jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 7:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Vos mains deviennent visqueuse, vous subissez -10 en capacité de combat jusqu'au prochain repos dans un lit !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 8:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Des pics sortent du coffre et vous transperse, vous subissez 10 de dégat !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 9:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Nurgle vous obsède, vous subissez un point de folie !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)
                case 10:
                    print("")
                    print("---> Erreur")
                    print("")
                    print("     Vous recentez le touché de Nurgle, vous subissez un point de corruption !")
                    print("")
                    reponse = reponse + 1
                    echec = random.randint(1,10)

else:
    print("")
    print("---> XXX ERREUR XXX ERREUR XXX ERREUR XXX ERREUR XXX ERREUR XXX")
    print(f"---> La bone réponse était {value}")
    print("")
    print("     Le coffre dégage une impulsion vert/jaune !")
    print("")
    print(f"     Trois portails apparaisent autour de vous, {invoc} regeton de Nurgle sortent par portail !")
    print(f"     Vous trouvez {mauvaiseFortune} Thrônes à l'intéreur du coffre.")
    found = True