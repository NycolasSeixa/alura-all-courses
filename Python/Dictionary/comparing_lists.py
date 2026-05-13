list1 = "leite, pão, café, açúcar"
list2 = "pão, café, biscoito, chocolate"

list1 = list1.replace(',', '').split()
list2 = list2.replace(',', '').split()

words = []
words1 = []
words2 = []

for word in list1:
    if word in list2:
        words.append(word)

print(words)

for word in list1:
    if word not in words:
        words1.append(word)

for word in list2:
    if word not in words:
        words2.append(word)

print(words1)
print(words2)