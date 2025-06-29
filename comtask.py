import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# List of shapefile paths and corresponding types
shapefile_paths = [
    ("C:\\Users\\prath\\Documents\\nandura.shp", "polygon"),
    ("C:\\Users\\prath\\Documents\\OPEN_SCRUB.shp", "polygon"),
    ("C:\\Users\\prath\\Documents\\ROAD.shp", "road"),
    ("C:\\Users\\prath\\Documents\\Rivers.shp", "river"),
    ("C:\\Users\\prath\\Documents\\RAILWAY LINE.shp", "railway"),
    ("C:\\Users\\prath\\Documents\\OPEN FOREST.shp", "polygon"),
    ("C:\\Users\\prath\Documents\\CITY_OR_VIILAGES.shp","point"),
]

# Read all shapefiles into a list of GeoDataFrames and add type
gdfs = []
for path, gtype in shapefile_paths:
    gdf = gpd.read_file(path)
    gdf['type'] = gtype
    gdfs.append(gdf)

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

# Create a figure and a single axis for plotting
fig, ax = plt.subplots(figsize=(15, 12))

# Plot Points and Polygons
if not points_gdf.empty:
    points_gdf.plot(ax=ax, color='blue', edgecolor='black', marker='o', label='Points')

if not polygons_gdf.empty:
    polygons_gdf.plot(ax=ax, color='white', edgecolor='black', alpha=0.5, label='Polygons')

# Plot LineString categories
if not lines_gdf[lines_gdf['type'] == 'river'].empty:
    lines_gdf[lines_gdf['type'] == 'river'].plot(ax=ax, color='blue', edgecolor='black', linestyle='-', linewidth=1.5, label='Rivers')

if not lines_gdf[lines_gdf['type'] == 'road'].empty:
    lines_gdf[lines_gdf['type'] == 'road'].plot(ax=ax, color='black', edgecolor='black', linestyle='-', linewidth=1.5, label='Roads')

if not lines_gdf[lines_gdf['type'] == 'railway'].empty:
    lines_gdf[lines_gdf['type'] == 'railway'].plot(ax=ax, color='brown', edgecolor='black', linestyle='-', linewidth=1.5, label='Railways')

# Set labels and title
ax.set_title('Geospatial Data')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend()
ax.grid(True)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
