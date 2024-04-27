#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy pandas seaborn statsmodels')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.formula.api import ols

# Load the dataset
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
boston_df = pd.read_csv(URL)

# 1. Boxplot for "Median value of owner-occupied homes"
plt.figure(figsize=(8, 6))
sns.boxplot(x='MEDV', data=boston_df)
plt.title('Boxplot of Median value of owner-occupied homes')
plt.xlabel('Median value ($1000s)')
plt.show()

# 2. Bar plot for the Charles river variable
plt.figure(figsize=(8, 6))
sns.countplot(x='CHAS', data=boston_df)
plt.title('Bar plot of Charles River variable')
plt.xlabel('Bounded by Charles River')
plt.ylabel('Count')
plt.show()

# 3. Boxplot for MEDV vs AGE variable
boston_df['AGE_group'] = pd.cut(boston_df['AGE'], bins=[0, 35, 70, float('inf')], labels=['35 years and younger', 'between 35 and 70 years', '70 years and older'])
plt.figure(figsize=(8, 6))
sns.boxplot(x='AGE_group', y='MEDV', data=boston_df)
plt.title('Boxplot of Median value vs Age of houses')
plt.xlabel('Age group')
plt.ylabel('Median value ($1000s)')
plt.show()

# 4. Scatter plot for Nitric oxide concentrations vs proportion of non-retail business acres per town
plt.figure(figsize=(8, 6))
sns.scatterplot(x='NOX', y='INDUS', data=boston_df)
plt.title('Scatter plot of Nitric oxide vs Non-retail business acres')
plt.xlabel('Nitric oxide concentration (pp 10m)')
plt.ylabel('Proportion of non-retail business acres')
plt.show()


# In[ ]:




