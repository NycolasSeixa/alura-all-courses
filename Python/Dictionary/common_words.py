text1 = "O sol brilha forte no céu azul"
text2 = "O céu azul anuncia um dia de sol intenso"

words1 = text1.split()
words2 = text2.split()

wordsboth = []

for word in words1:
    if word in words2:
        wordsboth.append(word)

print(wordsboth)