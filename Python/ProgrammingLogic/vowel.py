string = "abcdefghijklmnopqrstuvwxyz"

count = 0
pos = 1

for char in string:
    if char in 'aáâãeéêiíoóôuú':
        print(f'{char} found in pos {pos}')
        count+=1
    pos += 1
    
print(f'{count} vowels in total.')
