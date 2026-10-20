import random

random_numb: int = random.randint(1, 1000)  # für zahlen 1 bis 1000: randrange(1, 1001) oder randint(1, 1000)
try_counter: int = 0
start_numb: int = 0
guess_numb = start_numb

print("\nVersuch mal meine (Ganz-)zahl zwischen 1 und 1000 zu erraten\n Ich wette, dass du es nich in unter 8 Versuchen schaffst :3\n\n")


while guess_numb != random_numb:

    while True:
        try:
            guess_numb: int = int(input())
            break
        except ValueError:
            print("Das ist \033[3m\033[1mkeine ganzzahl\033[0m\033[0m")
    
    try_counter = try_counter + 1
    
    if guess_numb > random_numb:
            print("Das ist nicht meine Zahl. Probiers nochmal!\n\033[1mMeine Zahl ist \033[3mkleiner\033[0m\033[0m")
    elif guess_numb < random_numb:
            print ("Das ist nicht meine Zahl. Probiers nochmal!\n\033[1mMeine Zahl ist \033[3mgrößer\033[0m\033[0m")

    print(f"\nBisherige Versuche: {try_counter}\n\n")

print (f"GLÜCKWUNSCH !!! \nDu hast meine Zahl erraten: {random_numb} war meine Zahl.")

if try_counter <= 8:
     print(f"UUUND DUU hast sogar nur {try_counter} Versuche gebraucht ^^.\nDu bist KRASS!!!\nHast mich wohl geschlagen, Glückwunsch!")
else:
     print(f"Du hast {try_counter} Versuche gebraucht, ist noch nicht ganz 8.\nVersuch es nochmal und vielleicht schlägst du mich dann ^^")