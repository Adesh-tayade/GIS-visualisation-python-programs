import geopandas as gpd

# Define the path to your shapefile
shapefile_path = "C:\\Users\\prath\\Documents\\nn.shp"

# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Check the current CRS
print("Current CRS:", gdf.crs)

if gdf.crs.is_geographic:
    gdf = gdf.to_crs(epsg=4326)  # Reproject to World Mercator (suitable for global area calculations)

# Calculate area in square meters
gdf['area_m2'] = gdf.geometry.area

# Convert area to square kilometers
gdf['area_km2'] = gdf['area_m2'] / 1e6

# Print the area in square kilometers
print(gdf[['geometry', 'area_km2']])

# Optionally, save the result to a new shapefile
gdf.to_file('shapefile_with_area_km2.shp')
