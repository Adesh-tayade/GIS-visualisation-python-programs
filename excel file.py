import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel file
df = pd.read_excel("d:\ADESH QGIS\dem\corelation of ndvi and c factor.xlsx")

# Display the first few rows of the dataframe
print(df.head())

# Create scatter plot using matplotlib
plt.figure(figsize=(10, 5))
plt.scatter(df['VALUE'], df['VALUE.1'], color='blue', marker='o')
plt.title('Scatter Plot using Matplotlib')
plt.xlabel('VALUE')
plt.ylabel('VALUE.1')
plt.grid(True)
plt.show()

# Create scatter plot using seaborn
plt.figure(figsize=(10, 5))
sns.scatterplot(x='VALUE', y='VALUE.1', data=df)
plt.title('Scatter Plot using Seaborn')
plt.xlabel('VALUE')
plt.ylabel('VALUE.1')
plt.grid(True)
plt.show()
