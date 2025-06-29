import geopandas as gpd
import matplotlib.pyplot as plt

# Define the path to your shapefile
shapefile_path = "C:\\Users\\prath\\Documents\\nandura bdy n.shp"  # Replace this with the actual path to your shapefile

# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the GeoDataFrame
gdf.plot(ax=ax, color='white', edgecolor='black')

# Set the title
ax.set_title('ADESH TQ')

# Display the plot
plt.show()