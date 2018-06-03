import numpy as np
import csv
import matplotlib.pyplot as plt


firstNameList = []
interactionList = []


#For First Name CSV
#Open the file
fhand = open("first_names_sajari.csv", 'r')
reader = csv.reader(fhand)
#Read firstName CSV into a list
for row in reader:
    firstNameList.append(row)
#Remove the header
header = firstNameList[0]
withRemovedHeader = firstNameList[1:]


#For Interaction CSV
fhand2 = open("interactions_sajari.csv", 'r')
reader2 = csv.reader(fhand2)
#Read Interactions into list of lists
for row in reader2:
    interactionList.append(row)
#Remove the header
interactionHeader = interactionList[0]
interactionRemovedHeader = interactionList[1:]

#Variable needed for part C
largestWord = 0
theLargestWord = 0

# a) Calculate the average name length
count = 0
sum = 0
for word in withRemovedHeader:
    count = count + 1
    # the '-4' is to correct the format
    wordLength = len(str(word)) - 4
    #For part C
    if wordLength > largestWord:
        largestWord = wordLength
    sum = float(sum + wordLength)
print('The average length of the first names is: ' + str(sum/count))


# b) Calculate the average term length from interactions
count = 0
sum = 0
for row in interactionRemovedHeader:
    count = count + 1
    wordLength = len(str(row[0]))
    # For part C
    if int(wordLength) > int(largestWord):
        largestWord = wordLength
    # For Part B Again
    sum = float(sum + wordLength)
print('The average length of the terms is: ' + str(sum/count))


# c) Largest word across both data sets
print("The largest word from both sets is: " + str(largestWord))

# d) The "Most Positive" word
mostPositive = 0
mostPositiveWord = 0
for row in interactionRemovedHeader:
    positivity = float(row[1]) - float(row[2])
    if positivity > mostPositive:
        mostPositive = positivity
        mostPositiveWord = row[0]
print("The most positive word is: " + str(mostPositiveWord))

# e) The "Most Negative" word
leastPositive = 0
leastPositiveWord = 0;
for row in interactionRemovedHeader:
    positivity = float(row[2]) - float(row[1])
    if positivity > leastPositive:
        leastPositive = positivity
        leastPositiveWord = row[0]
print("The least positive word is: " + str(leastPositiveWord))

#Trying to get this subplot to work
fig, axes = plt.subplots(nrows=1, ncols=2)
ax0, ax1 = axes.flatten()

# 4.a) Plotting Name Lengths
newNameList = []
for word in withRemovedHeader:
    newNameList.append(len(word[0]))
name_data = np.array(newNameList)
ax0.hist(name_data, color = 'firebrick')
ax0.set_title('Name Lengths')

# 4.b) Plotting Term Lengths
#
#
#THERE IS AN ERROR HERE I THINK :(
#I could not figure it out... all of the data is being correctly entered into the histogram but then the plot looks
#super wrong. It must be some tiny error I'm missing, but I just cannot find what it is to save my life...
#
#
newTermList = []
for row in interactionRemovedHeader:
    newTermList.append(len(row[0]))
name_data = np.array(newTermList)
ax1.hist(name_data)
ax1.set_title('Term Lengths')

#Show the subplots
plt.show()


# 4.c) Plot a histogram of Binned terms from interactions.
terms = []
#Binning the terms. Wait, is binning a verb?
for row in interactionRemovedHeader:
    if (float(row[1]) < float(row[2])):
        terms.append(int(-1))
    if (float(row[1]) > float(row[2])):
        terms.append(int(1))
    if (float(row[1]) == float(row[2])):
        terms.append(int(0))
#Convert this list to np array
binned_data = np.array(terms)
#Create the histogram of the binned data
plt.hist(binned_data, color='#875F9A')
plt.title("Number of Negative and Positive Terms: BINNED")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()