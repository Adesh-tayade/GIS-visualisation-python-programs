import geopandas as gpd
import matplotlib.pyplot as plt

# List of shapefile paths and corresponding types
shapefile_paths = [
    ("C:\\Users\\prath\\Documents\\nandura.shp", "polygon"),
    ("C:\\Users\\prath\\Documents\\OPEN_SCRUB.shp", "polygon"),
    ("C:\\Users\\prath\\Documents\\ROAD.shp", "road"),
    ("C:\\Users\\prath\\Documents\\Rivers.shp", "river"),
    ("C:\\Users\\prath\\Documents\\RAILWAY LINE.shp", "railway"),
    ("C:\\Users\\prath\\Documents\\OPEN FOREST.shp", "polygon"),
]

# Read all shapefiles into a list of GeoDataFrames and add type
gdfs = []
for path, gtype in shapefile_paths:
    gdf = gpd.read_file(path)
    gdf['type'] = gtype
    gdfs.append(gdf)

# Combine all GeoDataFrames into a single GeoDataFrame
combined_gdf = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Define a common CRS (choose one that fits your data needs)
common_crs = 'EPSG:4326'  # WGS 84, or another appropriate CRS

# Reproject all GeoDataFrames to the common CRS
if combined_gdf.crs != common_crs:
    combined_gdf = combined_gdf.to_crs(common_crs)

# Filter GeoDataFrames by geometry type
points_gdf = combined_gdf[combined_gdf.geometry.type == 'Point']
lines_gdf = combined_gdf[combined_gdf.geometry.type == 'LineString']
polygons_gdf = combined_gdf[combined_gdf.geometry.type == 'Polygon']

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plot Points
if not points_gdf.empty:
    points_gdf.plot(ax=ax, color='blue', markersize=5, label='Points')

# Plot Polygons
if not polygons_gdf.empty:
    polygons_gdf.plot(ax=ax, color='white', edgecolor='black', alpha=0.5, label='Polygons')

# Plot Lines
# Rivers
if not lines_gdf[lines_gdf['type'] == 'river'].empty:
    lines_gdf[lines_gdf['type'] == 'river'].plot(ax=ax, color='blue', linewidth=1.5, label='Rivers')

# Roads
if not lines_gdf[lines_gdf['type'] == 'road'].empty:
    lines_gdf[lines_gdf['type'] == 'road'].plot(ax=ax, color='black', linewidth=1.5, label='Roads')

# Railways
if not lines_gdf[lines_gdf['type'] == 'railway'].empty:
    lines_gdf[lines_gdf['type'] == 'railway'].plot(ax=ax, color='brown', linewidth=1.5, label='Railways')

# Set labels, legend, and grid
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Combined Plot of Points, Polygons, and Lines')
ax.legend()
ax.grid(True)

# Display the plot
plt.show()
