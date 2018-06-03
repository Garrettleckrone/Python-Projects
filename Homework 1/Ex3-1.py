# Second Example From Homework 1
# Garrett Leckrone
# Fall 2017

#Input the score from the user
answer = input('Enter a score between 0.0 and 1.0\n')
answer = float(answer)

#If the answer is not in the correct range
if answer < 0.0 or answer > 1.0:
    print('An Error Message')

#Assign the grade and print
if answer <= 1.0 and answer >= .90:
    print('A')
if answer < .90 and answer >= .80:
    print('B')
if answer < .80 and answer >= .70:
    print('C')
if answer < .70 and answer >= .60:
    print('D')
if answer < .60:
    print('F')

# Example of Results:
# Enter a score between 0.0 and 1.0
# .95
# A

# Example of Results:
# Enter a score between 0.0 and 1.0
# 1.1
# An Error Message