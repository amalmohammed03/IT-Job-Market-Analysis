import pandas as pd

df = pd.read_csv("data/ai_jobs.csv")

print(df.head(10))
print (df.info())
print(df.isnull().sum())
df.columns = df.columns.str.lower()
print(df.head)
df['avg_salary'] = (df['salary_min_usd'] + df['salary_max_usd']) / 2
print(df.head(5))
print(df['job_title'].value_counts().head(10))
print(df.groupby('job_title')['avg_salary'].mean().sort_values(ascending=False).head(10))
print(df.groupby('experience_level')['avg_salary'].mean())
print(df.groupby('remote_work')['avg_salary'].mean())
print(df.groupby('country')['avg_salary'].mean().sort_values(ascending=False).head(10))
df = df[df['country'] != 'Global']
print(df['country'].unique())
print(df.groupby('country')['avg_salary'].mean().sort_values(ascending=False).head(10))


import seaborn as sns
import matplotlib.pyplot as plt

#Top Job Roles
plt.figure(figsize=(10,6))
sns.countplot(y='job_title', data=df, order=df['job_title'].value_counts().index)

plt.title("Top Job Roles Demand")
plt.xlabel("Count")
plt.ylabel("Job Title")

plt.show()



#Experience vs Salary
plt.figure(figsize=(8,5))
sns.barplot(x='experience_level', y='avg_salary', data=df)

plt.title("Average Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary")

plt.show()


#Country vs Salary
top_countries = df.groupby('country')['avg_salary'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries by Average Salary")
plt.xlabel("Country")
plt.ylabel("Average Salary")

plt.xticks(rotation=45)

plt.show()


#Demand vs Salary
plt.figure(figsize=(10,6))

sns.scatterplot(
    x='demand_score',
    y='avg_salary',
    hue='job_category',      # color by job category
    size='demand_score',     # size shows demand strength
    data=df
)

plt.title("Demand vs Salary by Job Category")
plt.xlabel("Demand Score")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()
