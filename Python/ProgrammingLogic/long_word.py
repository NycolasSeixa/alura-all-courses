min_char = 5
count = 1
long_word = ""

sentence = "A purple pig and a green donkey danced under the neon moonlight while eating cheese."
sentence.replace('-','').replace('.','').replace('_','')

for word in sentence.split(' '):
    if len(word) > min_char:
        print(f'"{word}" is a long word, with {len(word)} characters. Pos: {count}')
        if len(word) > len(long_word):
            long_word = word
            long_pos = count
    count+=1 

print(f'The longest word found is {long_word} with {len(long_word)} characters, in pos {long_pos}.')
