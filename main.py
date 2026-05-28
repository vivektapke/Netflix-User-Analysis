import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/netflix_titles.csv")
print(df.head())

print(df.info())
print(df.isnull().sum())

df.dropna(inplace=True)

sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.show()

df['listed_in'].value_counts().head(10).plot(kind='bar')
plt.title("Top Genres")
plt.show()

df['release_year'].value_counts().head(10).plot(kind='bar')
plt.title("Release Year Trend")
plt.show()

df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top Countries")
plt.show()

sns.countplot(x='rating', data=df)
plt.xticks(rotation=45)
plt.title("Ratings Distribution")
plt.show()

plt.savefig("images/graph1.png")