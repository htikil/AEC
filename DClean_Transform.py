import pandas as pd

# -------------------------------
# TEST CASE 1: Handle Missing Data
# -------------------------------

# Company dataset
df = pd.read_csv("company_salary.csv") # Read CSV file

print("Before Filling Missing Salaries:")
print(df)

mean_salary = df['Salary'].mean() # Calculate mean salary


df['Salary'] = df['Salary'].fillna(mean_salary) # Replace missing values with mean

df.index = df.index + 1 # Reset index to start from 1 instead of 0

print("After Filling Missing Salaries:")
print(df)

# -------------------------------
# TEST CASE 2: Remove Duplicates
# -------------------------------

# E-commerce dataset
df2 = pd.read_csv("Ecommerce.csv") # Read CSV file

print("\nBefore Removing Duplicates:")
print(df2)

df2_cleaned = df2.drop_duplicates() # Remove duplicate rows

df2_cleaned.index = df2_cleaned.index + 1 # Reset index to start from 1 instead of 0

print("\nAfter Removing Duplicates:")
print(df2_cleaned)