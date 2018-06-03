import csv
import numpy as np

def convertToTuples(listData):
    convertList = []
    for row in listData:
        newTuple = tuple(row)
        convertList.append(newTuple)
    return convertList

#Read CSV in
with open('X:\Programs\PyCharm IDE\Homework 3\produce.csv', newline='') as csv_file:
    fruitReader = csv.reader(csv_file)
    fruitList = []

    for row in fruitReader:
        fruitList.append(row)

    # remove header
    removedHeader = fruitList[1:]
    headerRow = fruitList[0:1][0]

    #Using Instructors Syntax
    type_spec = np.dtype([(headerRow[0][0], 'U30'), (headerRow[0][1], 'i4')])

    listConvert = convertToTuples(fruitList[1:])

    finalArray = np.array(listConvert, type_spec)

    print(finalArray)
