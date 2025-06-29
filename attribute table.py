import geopandas as gpd
import matplotlib.pyplot as plt

# Define the path to your shapefile
shapefile_path = "C:\\Users\\prath\\Documents\\Rivers.shp"  # Replace this with the actual path to your shapefile

# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Print the attribute table (first 5 rows)
print("Attribute Table:")
print(gdf.head())

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the GeoDataFrame
gdf.plot(ax=ax, color='blue', edgecolor='black')

# Set the title
ax.set_title('Taluka Map with Coordinates')

# Display the plot
plt.show()
