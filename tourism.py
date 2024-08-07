import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Load the dataset
df = pd.read_csv('D:/datasets/Customertravel.csv')

# Descriptive statistics
print(df.describe())

# Frequency distribution of categorical variables
print(df['FrequentFlyer'].value_counts())
print(df['BookedHotelOrNot'].value_counts())
print(df['AccountSyncedToSocialMedia'].value_counts())

# Bar charts for new columns
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(x='BookedHotelOrNot', data=df)
plt.title('Hotel Booked Distribution')

plt.subplot(1, 2, 2)
sns.countplot(x='AccountSyncedToSocialMedia', data=df)
plt.title('Account Synced with Social Media Distribution')
plt.show()


#CLASSIFICATION BASED ON AGE CATAGORY

# Define age categories
bins = [26, 31, 36, 41]
labels = ['26-30', '31-35', '36-40']
df['age_category'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Calculate the frequency of tourism within each age category
# Assuming 'tourism_activity' is a column indicating tourism participation
tourism_counts = df['age_category'].value_counts().sort_index()

# Plotting the results
plt.figure(figsize=(10, 6))
tourism_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Tourism by Age Category (26-40)')
plt.xlabel('Age Category')
plt.ylabel('Number of Travelers')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show plot
plt.show()


# piechart
df['FrequentFlyer'] = df['FrequentFlyer'].apply(lambda x: 1 if x == 'Yes' else 0)

# Calculate the total number of frequent flyers and non-frequent flyers
frequent_flyer_counts = df['FrequentFlyer'].value_counts()

# Define labels for the pie chart
labels = ['Non-Frequent Flyers', 'Frequent Flyers']

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(frequent_flyer_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
plt.title('Proportion of Frequent Flyers')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()



# Data Preprocessing: Convert categorical columns to numeric if necessary
df['AccountSyncedToSocialMedia'] = df['AccountSyncedToSocialMedia'].apply(lambda x: 1 if x == 'Yes' else 0)
df['BookedHotelOrNot'] = df['BookedHotelOrNot'].apply(lambda x: 1 if x == 'Yes' else 0)

# Calculate the counts for each combination
counts = df.groupby(['AccountSyncedToSocialMedia', 'BookedHotelOrNot']).size().reset_index(name='counts')

# Define labels for the plot
labels = ['Not Synced', 'Synced']
booked_labels = ['Not Booked', 'Booked']

# Plotting the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='AccountSyncedToSocialMedia', y='counts', hue='BookedHotelOrNot', data=counts, palette='viridis')
plt.title('Account Synced to Social Media vs Booked Hotel or Not')
plt.xlabel('Account Synced to Social Media')
plt.ylabel('Number of Travelers')
plt.xticks([0, 1], labels)
plt.legend(title='Booked Hotel', labels=booked_labels)

# Show the plot
plt.show()



# Assuming 'ServicesOpted' is the count of services opted for by a user

# Group the data by age and calculate the total number of services opted
age_services = df.groupby('Age')['ServicesOpted'].sum().reset_index()

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(age_services['Age'], age_services['ServicesOpted'], marker='o', linestyle='-', color='b')
plt.title('Total Services Opted vs Age')
plt.xlabel('Age')
plt.ylabel('Total Services Opted')
plt.grid(True)

# Show the plot
plt.show()




# Plotting the violin plot
plt.figure(figsize=(12, 6))
sns.violinplot(x='AnnualIncomeClass', y='ServicesOpted', data=df, palette='viridis')
plt.title('Distribution of Services Opted Across Different Annual Income Classes')
plt.xlabel('Annual Income Class')
plt.ylabel('Services Opted')
plt.grid(True)

# Show the plot
plt.show()