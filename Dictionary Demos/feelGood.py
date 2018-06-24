import csv

#Open feelgood, else create it
with open('feelGood.csv', 'w', newline='') as csv_file:
        feelGoodDict = dict()

        while 1 == 1:
            feelGoodInput = input("Please enter words that make you feel good. Or just type quit: ")

            if feelGoodInput == 'quit':
                writer = csv.writer(csv_file)

                #Convert Dict to List
                feelGoodList = []
                for key in feelGoodDict:
                    temp = [key, feelGoodDict[key]]
                    feelGoodList.append(temp)

                writer.writerows(feelGoodList)
                break


            #Check if the word has not been entered.
            if feelGoodInput not in feelGoodDict:
                feelGoodDict[feelGoodInput] = 1
                print(feelGoodDict)

            #If it has
            else:
                feelGoodDict[feelGoodInput] = feelGoodDict[feelGoodInput] + 1
                print(feelGoodDict)
