

""""
• pandas for creating the dataframe
• numpy for forming a random number from a range
• Matplotlib.pyplot for displaying graphs
• seaborn for plotting the data
• random for making a choice from a list of items
"""
#libraries, 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random as rd

#1. Create the categories to be observed
Categories = ["Food", "Travel", "Fashion", "Fitness", "Music", "Culture", "Family", "Health"]

#2. Create a dictionary with the following fields: Date, Category, Likes
data = {'Date': pd.date_range('2021-01-01', periods=500), 
        'Category': [rd.choice(Categories) for _ in range(500)], 
        'Likes': np.random.randint(0, 10000, size=500, dtype = int)}

#LOAD AND EXPLORE THE DATA
#3. Create a randomly generated dataframe with pseudo-data, using panda
df = pd.DataFrame(data)

"""
Descriptive statistics:
"""
print(df.head(n=6))
print(df.describe(percentiles = [.25, .4, .6]))
print(df.info())
print(df.value_counts(ascending = True))

"""
#4. CLEAN THE DATA
Remove all the null data
Convert the Date field to a datetime format
Convert the likes to integer
"""
new_df = df.dropna()
df["Category"].fillna("Food", inplace = True)
pd.to_datetime(new_df['Date'])
new_df["Likes"].astype(int, copy = False, errors = 'raise')


"""
5. VISUALIZE THE DATA
view it to observe relationships, perform statistics
1. Create the histograms for Likes
2. Create a boxplot to observe the relationship between Category and Likes
"""
sns.histplot(new_df['Likes'])
plt.show()
sns.boxplot(new_df, x= 'Category', y='Likes')
plt.show()

#group by Category and you return the mean of the likes
print((new_df.groupby('Category')['Likes'].mean()))
#return the overall mean of the likes
print((new_df['Likes'].mean()))



