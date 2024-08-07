import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('D:/datasets/cereal.csv')


#  Histogram for Calories
plt.figure(figsize=(10, 6))
sns.histplot(df['calories'], bins=10, kde=True)
plt.title('Distribution of Calories')
plt.show()

#  Box Plot for Calories
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['calories'])
plt.title('Box Plot of Calories')
plt.show()

#  Histogram for Protein
plt.figure(figsize=(10, 6))
sns.histplot(df['protein'], bins=10, kde=True)
plt.title('Distribution of Protein')
plt.show()



#  Histogram for Fat
plt.figure(figsize=(10, 6))
sns.histplot(df['fat'], bins=10, kde=True)
plt.title('Distribution of Fat')
plt.show()


#  Histogram for Sodium
plt.figure(figsize=(10, 6))
sns.histplot(df['sodium'], bins=10, kde=True)
plt.title('Distribution of Sodium')
plt.show()



#  Histogram for Fiber
plt.figure(figsize=(10, 6))
sns.histplot(df['fiber'], bins=10, kde=True)
plt.title('Distribution of Fiber')
plt.show()



#  Histogram for Carbohydrates
plt.figure(figsize=(10, 6))
sns.histplot(df['carbo'], bins=10, kde=True)
plt.title('Distribution of Carbohydrates')
plt.show()


#  Histogram for Sugars
plt.figure(figsize=(10, 6))
sns.histplot(df['sugars'], bins=10, kde=True)
plt.title('Distribution of Sugars')
plt.show()




#  Pie Chart for Shelf Distribution
plt.figure(figsize=(10, 6))
df['shelf'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Shelf Distribution')
plt.show()



# Create a treemap
fig = px.treemap(df, path=['name'], values='rating', title='Treemap of Ratings by Item')

# Show the treemap
fig.show()

# Create a scatter plot with a regression line
plt.figure(figsize=(10, 6))

# Scatter plot with regression line
sns.regplot(x='weight', y='calories', data=df, scatter_kws={'s':100, 'color':'blue'}, line_kws={'color':'red'})

# Adding title and labels
plt.title('Calories vs. Weight')
plt.xlabel('Weight')
plt.ylabel('Calories')

# Show the plot
plt.grid(True)
plt.show()

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='cups', y='protein', data=df, s=100, color='green')

# Adding title and labels
plt.title('Protein vs. Cups')
plt.xlabel('Cups')
plt.ylabel('Protein')

# Show the plot
plt.grid(True)
plt.show()


# Create an area chart
plt.figure(figsize=(12, 6))

# Plot Protein
plt.fill_between(df['type'], df['protein'], color='blue', alpha=0.5, label='Protein')

# Plot Cups
plt.fill_between(df['type'], df['cups'], color='orange', alpha=0.5, label='Cups')

# Adding title and labels
plt.title('Area Chart of Protein and Cups')
plt.xlabel('Item')
plt.ylabel('Value')

# Adding a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()