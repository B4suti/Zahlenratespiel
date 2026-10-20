import random

random_numb = random.randrange(1,100)
guess_numb = 0

print ("Hallooo, Wilkommen in meinem Spiel\nIch werde mir eine (ganze) Zahl zwischen 1 und 100 ausdenken und du musst sie dann erraten, okayy?\n\nSupii, dann lass uns gleich loslegen ^^\nWelche Zahl habe ich mir überlegt? :3")

while guess_numb != random_numb:

    while True:
        try:
            guess_numb = int(input())
            break
        except ValueError:
            print("Das ist keine Ganzzahl xD\nVersuchs nochmal")

    if guess_numb == random_numb:
        print(f"Jaaaaa meine Zahl ist {random_numb} xxD\nHerzlichen Glückwunsch!!!\nDas hast du supii gemacht ^^")
    elif guess_numb < 1:
        print("Du hast eine Zahl, die kleiner als 1 ist eingegeben -_-\nMeine Zahl ist aber im Bereich von 1 bis 100\nVersuchs nochmal")
    elif guess_numb > 100:
        print("Du hast eine Zahl, die größer als 100 ist eingegeben -_-\nMeine Zahl ist aber im Bereich von 1 bis 100\nVersuchs nochmal")

    if 100 > abs(random_numb - guess_numb) >= 80:
        print("Absoluter Schneesturm\nProbiers nochmal")
    elif 80 > abs(random_numb - guess_numb) >= 60:
            print("sehr sehr kalt\nVersuchs nochmal")
    elif 60 > abs(random_numb - guess_numb) >= 40:
            print("kalt\nNoch ein Versuch schadet nich")
    elif 40 > abs(random_numb - guess_numb) >= 30:
            print("ein klitzekleines Bisschen Warm, aber noch ein langer Weg xD")
    elif 30 > abs(random_numb - guess_numb) >= 20:
            print("schon wärmer, langsam wirds")
    elif 20 > abs(random_numb - guess_numb) >= 15:
            print("schon sehr warm\nDu bist schon sehr sehr nah dran jetzt")
    elif 15 > abs(random_numb - guess_numb) >= 10:
            print("langsam ist sogar schon ein T-Shirt zu viel \nNoch ein Versuch schadet nicht sag ich xD")
    elif 10 > abs(random_numb - guess_numb) >= 5:
            print("sehr heiß inzwischen\nNicht aufgeben!! Du bist sehr nah dran")
    elif 5 > abs(random_numb - guess_numb) >= 3:
            print("sind wir auf der Sonne oder warum ist es jetzt plötzlich zu heiß??!??\nVersuchs nochmal und wir findens raus")
    elif 3 > abs(random_numb - guess_numb) >= 1:
            print("Fühlt sich an wie in einer Supernova\nDu bist sehr sehr nah dran")

## du musst die anderen grenzen noch setzen, damit nicht alle auf einmal anspringeeen..
##dann musst du testen ob das wirklich so geil dann ist, evlt ist ja ein punktescore dann auch myb besser
#wäre crazy wenn du den auf einer funktion basieren könntest wo dann je nach abstand sich die temperatur ändert
    