from random import randint
import time

print('''Willkommen bei einem kleinem Rate Spiel.
Ich denke an eine Zahl von 1 bis 100''')

BL_vermuten = 0
BL_vermutungen = 0
BL_zahl = randint(1, 100)

while BL_vermutungen != BL_zahl:
    BL_vermutungen +=1
    BL_vermuten = int(input("Was ist deine Vermutung? "))

    if BL_vermuten > BL_zahl:
        print("Zu Hoch")
    elif BL_vermuten < BL_zahl:
        print("Zu Tief")
    elif BL_vermuten == BL_zahl:
        print("Du hast die Zahl erraten und", BL_vermutungen, "versuche gebraucht.")
        time.sleep(3)
        exit()