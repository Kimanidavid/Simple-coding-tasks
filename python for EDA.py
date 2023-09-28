import csv
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtl

"""with open(".\world population 2020.csv", 'r') as file:
    data = csv.reader(file, delimiter= ';')
    
    for row in data:
        print(row)"""


df = pd.read_csv('world population 2020.csv') 
print(df.head(10))

#check the last 10 items
print(df.tail(10))

#checking the shape of data(no of rows and columns)
print(df.shape)

#check the info of your data(the information of the dataframe)
print(df.info())

#description of data in the dataframe
print(df.describe())

#check correlation(the relationship btwn each columnin the data set)
#print(df.corr(2))

#check missing values(dataset is clean and contains no missing values)
print(df.isnull().sum())

#DATA PROCESSING
data = df.copy()
print(data)
#renaming 'Country (or dependency)' to 'Country'
newdata = data.rename(columns={'Country (or dependency)':'Country'}, inplace=True)
print(newdata)

for col in data.columns:
    if 'County (or dependency)'and '0' in col:
        data.rename(columns={col: col.split(' ')[0]})
print(data.head(3))

#check to see how many null objects we have in the data set
print(data.isnull().sum())

#looking for duplicates in the dataset
print(data.duplicated().sum())

# getting aquainted with our dataset
print(data.info())

print(data.nunique())

#converting the column names into strings
data.columns = list(map(str, data.columns))
print(data.columns)

#lets view our statistical summary
# this line shows the measures of central tedencies, percentiles and the max
summary = data.describe().T.sort_values(ascending=0, by='mean')
print(summary)

#creating dataframe for 'population data by country name'
population_data = data.groupby(by='Country').sum()
population_data.head(3)
print(population_data)

