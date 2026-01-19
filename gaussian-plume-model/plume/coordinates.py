import numpy as np
from pyproj import Transformer

def rotate_coords(dx, dy, wind_dir_deg):
    """
    Rotate coordinates into wind-aligned reference frame.
    """
    theta = np.radians(-wind_dir_deg)
    x_rot = dx * np.cos(theta) - dy * np.sin(theta)
    y_rot = dx * np.sin(theta) + dy * np.cos(theta)
    return x_rot, y_rot


def lonlat_to_utm(lon, lat, epsg="EPSG:32643"):
    """
    Convert lon/lat to UTM coordinates.
    """
    transformer = Transformer.from_crs("EPSG:4326", epsg, always_xy=True)
    return transformer.transform(lon, lat)
