import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# -------- Test Case 1: Boxplot (Student Scores) --------
# Sample student scores dataset
data = {
    'Maths': [78, 85, 90, 76, 88, 92, 95, 89, 100, 65],
    'Science': [72, 80, 85, 70, 90, 88, 91, 87, 95, 60],
    'English': [75, 82, 88, 78, 84, 90, 93, 85, 97, 68]
}

df = pd.DataFrame(data)

plt.figure(figsize=(7, 5))
sns.boxplot(data=df)
plt.title('Boxplot of Student Scores')
plt.show()


# -------- Test Case 2: Heatmap (Car Dataset Correlation) --------
# Sample car dataset
car_data = {
    'Speed': [120, 150, 100, 130, 170],
    'EngineSize': [1.5, 2.0, 1.2, 1.8, 2.2],
    'FuelEfficiency': [18, 15, 20, 17, 14]
}

car_df = pd.DataFrame(car_data)

# Correlation matrix
corr = car_df.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

