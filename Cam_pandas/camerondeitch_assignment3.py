# -*- coding: utf-8 -*-
"""CameronDeitch_Assignment3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KzgosVsjww84GlHYQjwCBwFempzGMAcO

Cameron Deitch

Assignment 3

Numpy and Panda applications
"""

from sklearn.linear_model import LinearRegression
import sklearn.datasets as datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Q1
df = pd.read_csv('nycflights.csv')
air_time = df['air_time']
distance = df['distance']
dep_time = df['dep_time']
dep_delay = df['dep_delay']
arr_time = df['arr_time']
arr_delay = df['arr_delay']
tailnum = df['tailnum']
dest = df['dest']
month = df['month']
dfquery = df.query('air_time > 120 and distance > 700')
print(dfquery)

#Q2
df1 = df.filter({'dep_time', 'dep_delay', 'arr_time', 'arr_delay', 'tailnum', 'dest'})
print(df1)

#Q3
df1 = df1.assign(total_delay=df1['dep_delay']+df1['arr_delay'])
print(df1)

#Q4
df = df.groupby(['month']).agg({'air_time' : 'mean', 'distance': 'max'})
print(df)

#Q5
dfSTU = pd.read_csv('student-por.csv')
studytime = dfSTU['studytime']
absences = dfSTU['absences']
G1 = dfSTU['G1']
G2 = dfSTU['G2']
G3 = dfSTU['G3']
print(dfSTU)

"""data set has 16 features"""

#Q6
x = np.array(studytime).reshape(-1,1)
y = np.array(G1)
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between study time and G1: {r_sq}")
y = np.array(G2)
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between study time and G2: {r_sq}")

"""study time and G2 had the best performance"""

#Q7
x = np.array(absences).reshape(-1,1)
y = np.array(G1)
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between absences and G1: {r_sq}")
x = np.array(absences).reshape(-1,1)
y = np.array(G2)
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between absences and G2: {r_sq}")

"""there is a relationship between both pairs"""

#Q8
x = dfSTU[['studytime', 'absences']]
y = G3
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between study time, absences and G3: {r_sq}")
x = dfSTU[['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']]
y = G3
model = LinearRegression()
model.fit(x,y)
r_sq = model.score(x,y)
print(f"coeficient of determination between all features and G3: {r_sq}")

"""performance was much better when adding more features because as you add more features that sum to the total grade, all it is doing is getting closer to that number"""

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# jupyter nbconvert --to html /content/CameronDeitch_Assignment3.ipynb