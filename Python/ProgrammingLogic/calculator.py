def sum(a, b):
    return a + b

def sub(a , b):
    return a - b

def mul(a , b):
    return a * b

def div(a , b):
    return a / b

while True:
    try: 
        a = float(input("Number[a]: "))
        op = input("Operation: ")
        b = float(input("Number[b]: "))
        match (op):
            case '+': print(f'Result: {sum(a,b)}')
            case '-': print(f'Result: {sub(a,b)}')
            case '*': print(f'Result: {mul(a,b)}')
            case '/': print(f'Result: {div(a,b)}')
            case _: print("Invalid operation!")
            
    except:
        print("Invalid operation!")
