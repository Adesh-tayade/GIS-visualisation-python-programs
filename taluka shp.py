import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# List of shapefile paths
shapefile_paths = [
    "C:\\Users\\prath\\Documents\\nandura.shp",
    "C:\\Users\\prath\\Documents\\OPEN_SCRUB.shp",
    "C:\\Users\\prath\\Documents\\ROAD.shp",
    "C:\\Users\\prath\\Documents\\Rivers.shp",
    "C:\\Users\\prath\\Documents\\RAILWAY LINE.shp",
    "C:\\Users\\prath\\Documents\\OPEN FOREST.shp",
]

# Read all shapefiles into a list of GeoDataFrames
gdfs = [gpd.read_file(path) for path in shapefile_paths]

# Print CRS for debugging
for i, gdf in enumerate(gdfs):
    print(f"CRS of shapefile {i}: {gdf.crs}")

# Define a common CRS (choose one that fits your data needs)
common_crs = 'EPSG:4326'  # WGS 84, or another appropriate CRS

# Reproject all GeoDataFrames to the common CRS
for i in range(len(gdfs)):
    if gdfs[i].crs != common_crs:
        gdfs[i] = gdfs[i].to_crs(common_crs)

# Combine all GeoDataFrames into a single GeoDataFrame
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Filter GeoDataFrames by geometry type, handling empty cases
points_gdf = combined_gdf[combined_gdf.geometry.type == 'Point']
lines_gdf = combined_gdf[combined_gdf.geometry.type == 'LineString']
polygons_gdf = combined_gdf[combined_gdf.geometry.type == 'Polygon']

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 10))

# Plot Points
if not points_gdf.empty:
    points_gdf.plot(ax=ax, color='blue', edgecolor='black', marker='o', label='Points')

# Plot Lines
if not lines_gdf.empty:
    lines_gdf.plot(ax=ax, color='green', edgecolor='black', linestyle='-', linewidth=1.5, label='Lines')

# Plot Polygons
if not polygons_gdf.empty:
    polygons_gdf.plot(ax=ax, color='white', edgecolor='black', alpha=0.5, label='Polygons')

# Set the title and labels
ax.set_title('Combined Geometries')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Add a legend
ax.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
