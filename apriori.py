# Apriori (Association Rule)
#rerferring to apyori class folder
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501): #lower bound included, upper bound is not
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)]) #Just built list containing all transactiosn

#Training Apriori on transactions data
from apyori import apriori #taking file of classes in folder
rules = apriori(transactions, min_support = 21/7500 , min_confidence = 0.2 , min_lift = 3, min_length = 2)
#choosing all the parameters discussed in Apriori theory

#Visualizing Results
results = list(rules)
#Visualizing in string
results_list = []
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]) + '\n' + str(results[i][2]))
#analyze the results list to see most common correlations using support confidence and lift values of two thingd
#revise what support, confidence and lift represent


