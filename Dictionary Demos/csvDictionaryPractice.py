import csv

#Open file
fhand = open('produce.csv')


#Make the dictionary
fruitDict = dict()

#Loop through produce, import the CSV as dictionary
for line in fhand:
    newLine = line.split()
    print(newLine)
    fruitDict[newLine[0]] = newLine[1]
print(fruitDict)