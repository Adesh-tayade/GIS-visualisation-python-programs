import geopandas as gpd
import matplotlib.pyplot as plt

# Define the path to your shapefile
shapefile_path = "D:\\ADESH QGIS\\georeferencing image\\nn tq toposheet.shp"  # Replace this with the actual path to your shapefile

# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Check if CRS is set
print("Original CRS:", gdf.crs)

# Set the CRS manually if it's not set (assuming WGS 84 for this example)
# Replace 'EPSG:4326' with the correct EPSG code if you know the actual CRS
if gdf.crs is None:
    gdf.set_crs(epsg=4326, inplace=True)

# Print the CRS after setting it
print("CRS after setting:", gdf.crs)

# Define the UTM CRS you want to convert to, for example, UTM Zone 43N
# Make sure to replace 'EPSG:32643' with the correct EPSG code for your UTM zone
utm_crs = 'EPSG:32643'

# Reproject the GeoDataFrame to UTM
gdf_utm = gdf.to_crs(utm_crs)

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the reprojected GeoDataFrame
gdf_utm.plot(ax=ax, color='white', edgecolor='black')

# Set the title
ax.set_title('ADESH TQ (UTM)')

# Display the plot
plt.show()
