import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")
print("Data loaded successfully")
print(df.head())

# TASK 1: Population & Sample
population = df
print("Population size:", len(population))

sample = df.sample(frac=0.1, random_state=42)
print("Sample size:", len(sample))


# TASK 2: Sampling Techniques
population_mean = df['Sales'].mean()

random_sample = df.sample(n=100, random_state=1)
random_mean = random_sample['Sales'].mean()

systematic_sample = df.iloc[::10]
systematic_mean = systematic_sample['Sales'].mean()

print("Population Mean:", population_mean)
print("Random Sample Mean:", random_mean)
print("Systematic Sample Mean:", systematic_mean)



# TASK 3: CLT
sample_means = []

for i in range(100):
    sample = df['Sales'].sample(30)
    sample_means.append(sample.mean())

plt.hist(sample_means, bins=20)
plt.title("Sampling Distribution of Sample Means")
plt.show()



# TASK 3: Central Limit Theorem (CLT)

sample_means = []

for i in range(100):
    sample = df['Sales'].sample(30)
    sample_means.append(sample.mean())



plt.hist(sample_means, bins=20)
plt.title("Sampling Distribution of Sample Means (CLT)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()



# TASK 4: Normal Distribution

mean = df['Sales'].mean()
std = df['Sales'].std()

print("Mean:", mean)
print("Standard Deviation:", std)



plt.hist(df['Sales'], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()



# TASK 5: Z-Score Calculation

df['Z_Score'] = (df['Sales'] - mean) / std
print(df[['Sales', 'Z_Score']].head())

outliers = df[(df['Z_Score'] > 3) | (df['Z_Score'] < -3)]
print("Outliers:")
print(outliers)




# TASK 6: Business Insights

"""
1. Sampling is required because it reduces time and cost when working with large datasets.
2. Central Limit Theorem helps us estimate population behavior using sample statistics.
3. Normal distribution is important because many statistical tests assume data is normally distributed.
4. Z-Score helps identify unusual or extreme values in the data.
"""
plt.savefig("clt_distribution.png")
plt.savefig("sales_distribution.png")

