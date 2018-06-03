import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

#This project will focus on making a predictive model for the game League of Legends.
#League of legends is a competitive game where two teams with 5 players compete, and only one team can win.
#Because only one team can win, we will try to predict if team Red or team Blue will win.
#First, we need to see if there is a correlation between winning the game and any of the metrics.
#If there is a correlation, we will use stats such as First Baron in order to predict who will win.

#Read the data
data = pd.read_csv('Games.csv')

#Print the head to get an idea for the dataset
#print(data.head())


#We will first use a Heatmap in Seaborn to see correlations between winning and taking first game objectives.
#Create the figure.
fig = plt.figure(figsize=(12, 12))

#Heatmap showing the total number of objectives taken for each team and the correlation to winning
sns.heatmap(data[['t1_towerKills','t1_inhibitorKills','t1_dragonKills','t1_baronKills', 't1_riftHeraldKills',
                  't2_towerKills','t2_inhibitorKills','t2_dragonKills','t2_baronKills', 't2_riftHeraldKills','winner']].corr(),
            annot=True, square=True)
plt.title("Correlation Heatmap of Total Objectives Taken and Winner")
plt.tight_layout()
plt.show()

#Heatmap showing the correlation between first team to take objective and winning
sns.heatmap(data[['firstBlood', 'firstTower', 'firstInhibitor', 'firstDragon', 'firstRiftHerald', 'winner']].corr(), annot=True, square=True)
plt.title("First Objective Taken vs Winner")
plt.tight_layout()
plt.show()

#Lets clean up the data
#0 means that neither team took the objective
#1 means that blue side took the objective
#2 means that redside took the objective
cleanData = data.replace([0,1,2], ['neither', 'blue', 'red'])

#Put it in a DataFrame
df = pd.DataFrame(cleanData)
#Drop unnecessary columns, such as gameID, creationTime, gameDuration, and seasonID
#Although these could be useful in another analysis, we are looking only at the first objectives taken
#and how they correlate to winning the game
df.drop(df.columns[[0,1,2,3]], axis=1, inplace=True)
#print(df.head())

#Graph the total blue wins vs total red wins in a pie chart
df['winner'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['cyan', 'firebrick'])
plt.tight_layout()
plt.title("Who Wins More? Red vs Blue")
plt.show()



#Begin the machine learning!
#First, we must use SkiKit Learn to separate our data into a Training dataset and a Test Dataset.
#We are going to run a few different logistic regression analyses, to look at the predictions based on different factors
#First, let's use the number of neutral objectives taken by each team
#We will use the Baron Nashor kills, which give a buff that empowers the team
#And we will use dragon kills, which give a unique permanent buff depending on the element of the dragon
#Because the element of the dragon is not listed in the data, we will consider all dragons to be a Dragon.
X = data[['t1_baronKills', 't1_dragonKills', 't2_baronKills', 't2_dragonKills']]
y = data['winner']
#We split the data into training and test data. We use one third of the total data for our test data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

#Now that the logistic regression model is fitted with the training data,
#let's use it to predict the winner for our test data.
winnerPrediction = logmodel.predict(X_test)
#We use the classification report function, provided by SKLearn, in order to analyze the results.
print("Predicting the winner using the total baron and dragon kills for each team:")
print(classification_report(y_test, winnerPrediction))


#Now we will use different objects in order to predict the winner, to determine if these are better features.
#This time, lets see how the total number of towers killed and inhibitors killed affects the ability to predict the winner
X = data[['t1_towerKills','t1_inhibitorKills','t2_towerKills','t2_inhibitorKills']]
y = data['winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

#Predict again, and print a classification report
predictions = logmodel.predict(X_test)
print("Predicting the winner using the total tower and inhibitor kills for each team:")
print(classification_report(y_test, predictions))

#Now lastly, let's determine how the first team to take objectives can predict the winner
X = data[['firstBlood', 'firstTower', 'firstInhibitor', 'firstDragon', 'firstRiftHerald']]
y = data['winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

#Predict again, and print a classification report
predictions = logmodel.predict(X_test)
print("Predicting the winner using the first objectives taken for each team:")
print(classification_report(y_test, predictions))

#Make conclusion about the analyses
print("Conclusion:")
print("-These analyses have shown that the first team to take objectives is not certain to win the game.")
print("-Also, the total number of neutral objectives does not conclusively determine the winning team.")
print("-Lastly, the total number of towers and inhibitors killed is a reliable indicator for the winning team.")
print("We can see that based on the total number of towers and inhibitors killed, we can predict the winner of the game.")







