import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/datasets/ds_salaries.csv')

# Group by Currency Type and calculate mean Salary in USD
currency_salary = df.groupby('salary_currency')['salary_in_usd'].mean().sort_values(ascending=False)

# Plotting the impact of currency on salary
plt.figure(figsize=(10, 5))
currency_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary in USD by Currency Type')
plt.xlabel('Currency Type')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Group by Company Location and calculate mean Salary in USD
location_salary = df.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False)

# Plotting the geographical salary differences
plt.figure(figsize=(12, 6))
location_salary.plot(kind='bar', color='red')
plt.title('Average Salary in USD by Company Location')
plt.xlabel('Company Location')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Group by Company Size and calculate mean Salary in USD
size_salary = df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)

# Plotting the company size influence on salary
plt.figure(figsize=(10, 5))
size_salary.plot(kind='bar', color='green')
plt.title('Average Salary in USD by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




# Group by Job Title and calculate mean Salary in USD
role_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

# Plotting the role-specific salary insights
plt.figure(figsize=(12, 6))
role_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary in USD by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Count the occurrences of each Job Title
role_counts = df['job_title'].value_counts()

# Plotting the frequency of each job title
plt.figure(figsize=(12, 6))
role_counts.plot(kind='bar', color='salmon')
plt.title('Frequency of Each Job Title')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Group by Job Title and calculate average salary by Company Size
role_size_salary = df.groupby(['job_title', 'company_size'])['salary_in_usd'].mean().unstack()

# Plotting the average salary by job title and company size
role_size_salary.plot(kind='bar', figsize=(12, 6), colormap='viridis')
plt.title('Average Salary in USD by Job Title and Company Size')
plt.xlabel('Job Title')
plt.ylabel('Average Salary in USD')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Company Size')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 8))
df['company_size'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Number of Employees by Company Size')
plt.ylabel('')
plt.tight_layout()
plt.show()



import seaborn as sns

# Convert 'salary_in_usd' to numeric and 'company_size' to category
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
df['company_size'] = df['company_size'].astype('category')

# Drop rows with missing salary_in_usd or company_size
df = df.dropna(subset=['salary_in_usd', 'company_size'])

# Set the style of the visualization
sns.set(style="whitegrid")

# Create a histogram to compare salaries by company size
plt.figure(figsize=(12, 6))
ax = sns.histplot(data=df, x='salary_in_usd', hue='company_size', multiple='stack', palette="Set3", binwidth=10000)
ax.set_title('Salary Distribution by Company Size')
ax.set_xlabel('Salary in USD')
ax.set_ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# Line Chart: Average Salary by Work Year
plt.figure(figsize=(12, 6))
sns.lineplot(x='work_year', y='salary_in_usd', data=df, marker='o', color='purple')
plt.title('Average Salary by Work Year')
plt.xlabel('Work Year')
plt.ylabel('Average Salary in USD')
plt.grid(True)
plt.show()



# Convert 'Salary in USD' to numeric and 'Work Year' to numeric for correlation
df['salary_in_usd'] = pd.to_numeric(df['salary_in_usd'], errors='coerce')
df['work_year'] = pd.to_numeric(df['work_year'])

# Calculate correlation matrix
correlation_matrix = df[['work_year', 'salary_in_usd']].corr()

# Set the style of the visualization
sns.set(style="whitegrid")

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Creating cumulative salary data
cumulative_salary = df.groupby('work_year')['salary_in_usd'].sum().cumsum()

# Area Chart
plt.figure(figsize=(12, 6))
plt.fill_between(cumulative_salary.index, cumulative_salary.values, color="skyblue", alpha=0.4)
plt.plot(cumulative_salary.index, cumulative_salary.values, color="Slateblue", alpha=0.6, linewidth=2)
plt.title('Cumulative Salary Over Years')
plt.xlabel('Work Year')
plt.ylabel('Cumulative Salary in USD')
plt.grid(True)
plt.show()