import random as r

min, max = 1, 10
number = r.randint(min, max)

print(f'Try to guess what the secret number is! ({min} - {max})')

while True:
    try:
        choice = float(input("Choice: "))
        if(choice < number):
            print("choice < number")
        elif(choice > number):
            print("choice > number")
        else:
            break
    except:
        print("Type a valid number!")
        continue

print("You got it!")
