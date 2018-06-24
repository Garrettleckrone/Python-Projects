fhand = open('romeo.txt')
wordList = []

for line in fhand:
    newList = line.split()

    for word in newList:
        if word not in wordList:
            wordList.append(word)



wordList.sort()
print(wordList)