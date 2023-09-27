#Convert a collection of text documents to a matrix of token counts.
from sklearn.feature_extraction.text import CountVectorizer as CV
#Split arrays or matrices into random train and test subsets.
from sklearn.model_selection import train_test_split as TTS
'''1. Versatile (MultinomialNB): Suits Continuous & Discrete Data, Handles Big Datasets, Multilabel Classification, Ideal for NLP Model Training
   2. Effective Multiclass Classification (MultinomialNB): Calculates Probabilities for Each Label, Outputs Highest Probability Label for Text Classification'''
from sklearn.naive_bayes import MultinomialNB
#Pandas for Cleaning and EDA
import pandas as PD
#NumPy for numerical operations, in this project we are using it for array creation for the model creation.
import numpy as NP

#Step_1: Load data from csv file. I used the Kaggele dataset for this project.
df = PD.read_csv("language_detection.csv")
#print(df.head(5))

#We couldn't find any null value in this data set.
print("Null Check")
print("__________", end = "\n")
print(df.isnull().sum(), end = "\n \n")

#Total language sample in a chosen dataset
print("Distinct Language count : ",len(PD.unique(df['language'])), end ="\n \n")

#Total text sample for each language is 1000 in a chosen dataset
print("Distinct Language sample's count :- ")
print("_________________________________", end = "\n")
print(df['language'].value_counts(), end ="\n \n")

# Using numpy array we have split the text and language value into 2 parameters for further ML test and train purpose
x = NP.array(df['language'])
y = NP.array(df['Text'])
# print(x)
# print(y)

#Using CV() create a object cv, it helps to convert a collection of text documents to a matrix of token counts.
cv = CV()
Y = cv.fit_transform(y)
Y_train,Y_test,x_train,x_test = TTS(Y,x,test_size = 0.20,random_state = 50)

#From this model we got 0.9593 as accuracy rate it's nearly 95.93(~96)%
ML_model = MultinomialNB()
ML_model.fit(Y_train,x_train)
accuracy = ML_model.score(Y_test,x_test)
print("Model Accuracy : ", accuracy, end = "\n \n")

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
language = ML_model.predict(data)
print("Given text is written with language: ", language)
print("This model created with only 1000 texts samples for each language. If you need more accuracy you need more data to train the model to get better outcome, Thank you for using this")
