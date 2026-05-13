# cpf = input("Enter your cpf: ")
# cpf = "123.456.789-00"
cpf = "12345678900"

while True: 

    if len(cpf) == 11: # numbers only 
        try: 
            int(cpf)
            cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            break
        except:
            print("Please, verify if you typed only numbers in your cpf.")
            cpf = input("Enter your cpf: ")
            continue
    
    elif len(cpf) == 14: # with punctuation
        try: 
            int(cpf.replace('.','',).replace('-',''))
            if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
                raise ValueError
            break
        except ValueError:
            print("Please, verify if you typed the cpf with only numbers and the dot and dash are in the right places.")
            cpf = input("Enter your cpf: ")
            continue
            
    else:
        print("Please, verify if you typed the cpf correctly.")
        cpf = input("Enter your cpf: ")


print(f'Your CPF is {cpf}.')
