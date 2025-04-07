
import pandas as pd 
import numpy as np  
from matplotlib import pyplot as plt 

# Importing the dataset from CSV file
df = pd.read_csv('/home/arnav/Polygence/death-rates-from-air-pollution.csv')

df.head()

df.isna().sum()

df[df['Code'].isna()]['Entity'].unique()

region = ['Andean Latin America', 'Australasia', 'Caribbean', 'Central Asia', 'Central Europe', 
          'Central Europe, Eastern Europe, and Central Asia', 'Central Latin America', 
          'Central Sub-Saharan Africa', 'East Asia', 'Eastern Europe', 'Eastern Sub-Saharan Africa',
          'Latin America and Caribbean', 'North Africa and Middle East', 'North America', 
          'Oceania', 'Scotland', 'South Asia', 'Southeast Asia', 'Southeast Asia, East Asia, and Oceania',
          'Southern Latin America', 'Southern Sub-Saharan Africa','Sub-Saharan Africa', 
          'Tropical Latin America', 'Western Europe', 'Western Sub-Saharan Africa']
constituent_country = ['England', 'Northern Ireland', 'Wales']
income = ['High-income', 'High-income Asia Pacific']
sdis = ['High SDI', 'High-middle SDI', 'Middle SDI', 'Low-middle SDI', 'Low SDI']

# Creating a new dataframe for the different regions
regions = df[df['Entity'].isin(region)].copy(deep=True)
# Dropping the 'Code' column
regions.drop('Code', axis=1, inplace=True)

# Creating a new dataframe for the constituent countries
constituent_countries = df[df['Entity'].isin(constituent_country)].copy(deep=True)
# Dropping the 'Code' column
constituent_countries.drop('Code', axis=1, inplace=True)

# Creating a new dataframe for the different high-income countries
high_income = df[df['Entity'].isin(income)].copy(deep=True)
# Dropping the 'Code' column
high_income.drop('Code', axis=1, inplace=True)

# Creating a new dataframe from the different SDI levels
sdi = df[df['Entity'].isin(sdis)].copy(deep=True)
# Dropping the 'Code' column
sdi.drop('Code', axis=1, inplace=True)

# Copying the original dataframe
countries = df.copy(deep=True)
# Dropping the rows with missing values
countries.dropna(inplace=True)

# First summing the number of missing values from each dataframe, then adding those values together
print('Total Number of Missing Values:', \
      sum(countries.isna().sum().values) + \
      sum(regions.isna().sum().values) + \
      sum(constituent_countries.isna().sum().values) + \
      sum(high_income.isna().sum().values) + \
      sum(sdi.isna().sum().values)
     )

plt.figure(figsize=(15,10))  # Increasing the plot size

# Using a loop to add lines for each region
for r in region:
    plt.plot(regions[regions['Entity'] == r].groupby('Year').mean().iloc[:,0], label = r)

plt.xlabel('Year', size=16)  # Labeling the x-axis
plt.ylabel('Deaths Per 100k', size=16)  # Labeling the y-axis
plt.title('Total Air Pollution Deaths by Region', size=20,fontfamily='sans-serif', fontweight='bold')  # Adding a title
plt.legend(bbox_to_anchor=(1,1), loc="upper left", prop={'size': 15})
plt.style.use('fivethirtyeight')  # Using a plot style to include gridlines

