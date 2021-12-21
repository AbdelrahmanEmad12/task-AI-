# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:28:55 2021

@author: workstation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.head()
dataset.describe()

print(dataset.info())

#Clean the data (null, duplications)
dataset.isnull().sum()
dataset.duplicated().sum()
duplicates=dataset.duplicated()
dataset[duplicates]
#drop_duplicated_data
dataset.drop_duplicates(inplace=True)

# What are the most demanding companies for jobs?
demanding_companies = dataset['Company'].value_counts().head(15)
dataset[demanding_companies]

# Show step 4 in a pie chart
demanding_companies.plot(kind='pie' , figsize=(7,7))

# Find out what are the most popular job titles
popular_job = dataset['Title'].value_counts().head(15)
dataset[popular_job]

# Show step 6 in bar chart
popular_job.plot(kind='bar',figsize=(7,7))

# Find out the most popular areas?
popular_area = dataset['Country'].value_counts().head(15)
dataset[popular_area]

# Show step 8 in bar chart
popular_area.plot(kind='bar',figsize=(7,7))

#Print skills one by one and how many each repeated and order the output to find out the most important skills required? 
from collections import Counter
MyList = dataset['Skills'].value_counts()
c = Counter(MyList)
print(c)

dataset['Skills'].value_counts().head(15)












