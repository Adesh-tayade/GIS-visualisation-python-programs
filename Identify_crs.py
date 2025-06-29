import geopandas as gpd

# Define the path to your shapefile
shapefile_path = "C:\\Users\\prath\\Documents\\OPEN_SCRUB.shp"
# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Print the CRS
print("CRS:", gdf.crs)
