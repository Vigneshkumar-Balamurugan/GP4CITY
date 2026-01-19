import numpy as np
from .dispersion import get_dispersion_coefficients

def gaussian_plume(Q, x, y, H, u, z, hour_time):
    """
    Gaussian plume concentration model.
    """
    C = np.zeros_like(x)
    mask = x > 0

    if np.any(mask):
        sigma_y, sigma_z = get_dispersion_coefficients(x[mask], u, hour_time)

        C[mask] = (
            Q / (2 * np.pi * u * sigma_y * sigma_z)
            * np.exp(-y[mask] ** 2 / (2 * sigma_y ** 2))
            * (
                np.exp(-(z - H) ** 2 / (2 * sigma_z ** 2))
                + np.exp(-(z + H) ** 2 / (2 * sigma_z ** 2))
            )
        )
    return C
