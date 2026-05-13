import random as r

win = False

print("Type [1] for Rock")
print("Type [2] for Paper")
print("Type [3] for Scissors")

while True:
    
    try: 
        player_choice = int(input("Enter your choice: "))
        bot_choice = r.randint(1, 3)    
        print(f'Bot choice: {"Rock" if bot_choice == 1 else "Paper" if bot_choice == 2 else "Scissors"}')
        match player_choice:
            case 1:
                if(bot_choice == 1):
                    print("Draw")
                elif(bot_choice == 2):
                    print("You lost")
                else:
                    raise TypeError
            case 2:
                if(bot_choice == 1):
                    raise TypeError
                elif(bot_choice == 2):
                    print("Draw")
                else:
                    print("You Lost")
            case 3: 
                if(bot_choice == 1):
                    print("You Lost")
                elif(bot_choice == 2):
                    raise TypeError
                else:
                    print("Draw")
            case _:     
                raise ValueError
    except ValueError: 
        print("You must enter a valid choice!")
    except TypeError:
        print("You Win")
        break
