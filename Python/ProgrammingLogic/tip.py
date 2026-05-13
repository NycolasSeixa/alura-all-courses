import random as r

total_value = float(r.randint(30, 120))

tip = input("Enter the tip amount: ") 
while True:
    try:
        tip = float(tip)
        break
    except ValueError:
        print("Only numbers!")
        tip = input("Enter the tip amount in numbers: ") 
        continue

total_tip = total_value + (total_value * (tip / 100))
print(f'Total value: R${total_value}')
print(f'Total value + Tip: R${round(total_tip, 2)}')

print("end video")
