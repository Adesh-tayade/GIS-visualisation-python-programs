import rasterio
import matplotlib.pyplot as plt

# Path to the NDVI raster file
ndvi_file_path = r"D:\ADESH QGIS\ndvi\clipped mask.tif"

# Open the NDVI raster file
with rasterio.open(ndvi_file_path) as src:
    # Read the raster data into a numpy array
    ndvi_array = src.read(1, masked=True)  # Read the first band with masking
    
    # Print metadata
    print("Raster Metadata:")
    print(f"Width: {src.width}")
    print(f"Height: {src.height}")
    print(f"CRS: {src.crs}")
    print(f"Transform: {src.transform}")
    
    # Displaying statistics
    print("Statistics:")
    print(f"Min value: {ndvi_array.min()}")
    print(f"Max value: {ndvi_array.max()}")
    print(f"Mean value: {ndvi_array.mean()}")
    print(f"Standard deviation: {ndvi_array.std()}")
    
    # Define a custom green colormap
    colors = [(0, 0.2, 0), (0, 0.8, 0)]  # RGB values: dark green (0, 0.2, 0) to bright green (0, 0.8, 0)
    cmap_green = plt.cm.colors.LinearSegmentedColormap.from_list('custom_green', colors, N=256)
    
    # Plotting the NDVI raster with the custom green colormap
    plt.figure(figsize=(10, 8))
    plt.imshow(ndvi_array, cmap=cmap_green, vmin=-1, vmax=1)  # Adjust the colormap and vmin/vmax as needed
    plt.colorbar(label='NDVI Value')
    plt.title('NDVI Raster')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.show()
