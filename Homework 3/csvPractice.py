import csv

#Declare the list for tuples
fruitList = []
fruitList.append(('Produce', 'Count'))

#Ask the user for a fruit/vegetable and count those items
while 1==1:
    theInput = input("Enter a fruit and count, or type quit\n")

    if theInput == 'quit':
        break

    theTuple = tuple(theInput.split(','))
    fruitList.append(theTuple)

print("Program exited. CSV Saved.")


with open('produce.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(fruitList)