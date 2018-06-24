import numpy as np

#Create the NumPy Array using a List
theList = ([1,1,1,1,1],[1,2,1,1,1],[1,1,3,1,1],[1,1,1,4,1],[1,1,1,5,1])
theArray = np.array(theList)

#Calculate the row sums
print("The Row Sums: ", np.sum(theArray[0][:]))

#Multiply Matrix Elements x2 and Print
print("Matrix*2: ")
print(theArray * 2)

#Multiply with Identity Matrix
print("Multiplied with Identity Matrix:")

#Creating an Identity Matrix
b = np.eye(5)
print(theArray * b)

#Dot Product
print("Dot Multiplied with the Supplied Matrix")
thereHasToBeAnEasierWay = ([1],[2],[3],[4],[5])
newArray = np.array(thereHasToBeAnEasierWay)
print(np.dot(theArray,newArray))
