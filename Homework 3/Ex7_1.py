#Prompt the user to input filename
fileName = input("Please enter the filename ")

#Open the filename
fhand = open(fileName)

#Read through file and look for lines of the form X-DSPAM-Confidence:0.8475
targetString = 'X-DSPAM-Confidence:'
count = 0
total = 0

for line in fhand:
    if line.startswith(targetString):
        #Increment Counter
        count = count + 1
        value = line[20:]
        value = float(value)
        total = total + value

print("The number of occurrences is", count)
print("The total spam confidence is", total)
print("The average spam confidence is", total/count)


