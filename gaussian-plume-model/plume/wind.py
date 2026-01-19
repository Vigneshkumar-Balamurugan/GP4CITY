from metpy.calc import wind_direction, wind_speed
from metpy.units import units

def compute_wind(u, v):
    """
    Compute wind direction and speed from components.
    """
    wd = wind_direction(u * units("m/s"), v * units("m/s"))
    ws = wind_speed(u * units("m/s"), v * units("m/s"))
    return wd.magnitude, ws.magnitude
