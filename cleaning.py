import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

print("----- ORIGINAL DATA -----")
print(df.head())

# Data Quality Check
print("\n----- DATA ISSUES -----")
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# Cleaning
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Gender'] = df['Gender'].fillna("Unknown")

# Fix inconsistent values
df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df.columns = ['CustomerID', 'Gender', 'Age', 'Income', 'SpendingScore']

# Feature Engineering
df['AgeGroup'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')

# Final Check
print("\n----- CLEANED DATA -----")
print(df.head())

print("\nRemaining Missing Values:\n", df.isnull().sum())
print("Remaining Duplicates:", df.duplicated().sum())

# Save cleaned dataset
df.to_csv("cleaned_customers.csv", index=False)

print("\n✅ Cleaning Completed Successfully")