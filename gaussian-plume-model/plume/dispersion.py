import numpy as np

def get_dispersion_coefficients(x):
    """
    Neutral atmospheric stability dispersion coefficients.
    """
    sigma_y = 0.08 * x * (1 + 0.0002 * x) ** (-0.5)
    sigma_z = 0.06 * x * (1 + 0.0015 * x) ** (-0.5)
    return sigma_y, sigma_z
