import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel files using raw strings to avoid escape character issues
df1 = pd.read_excel(r"d:\ADESH QGIS\dem\NDVI data.xlsx")
df2 = pd.read_excel(r"d:\ADESH QGIS\dem\NDVI data2.xlsx")

# Display the first few rows of the dataframes
print(df1.head())
print(df2.head())

# Create scatter plot using matplotlib
plt.figure(figsize=(10, 5))
plt.scatter(df1['NDVI'], df1['C Factor'], color='blue', marker='o', label='Data from file 1')
plt.scatter(df2['NDVI'], df2['C Factor'], color='red', marker='x', label='Data from file 2')
plt.title('Scatter Plot from Two Excel Files')
plt.xlabel('NDVI')
plt.ylabel('C Factor')
plt.legend()
plt.grid(True)
plt.show()

# Add a column to identify the source of data
df1['Source'] = 'File 1'
df2['Source'] = 'File 2'

# Combine the two DataFrames
combined_df = pd.concat([df1, df2])

# Create scatter plot using seaborn
plt.figure(figsize=(10, 5))
sns.scatterplot(x='NDVI', y='C Factor', hue='Source', style='Source', data=combined_df)
plt.title('Scatter Plot from Two Excel Files')
plt.xlabel('NDVI')
plt.ylabel('C Factor')
plt.grid(True)
plt.show()
