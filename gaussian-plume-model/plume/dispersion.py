import numpy as np

def get_dispersion_coefficients(x, u, hour_time):
    """
    atmospheric stability dispersion coefficients.
    """

    is_day = 6 <= hour_time <= 18

    if u <= 2:
        sigma_y = 0.32 * x * (1 + 0.0004 * x) ** -0.5
        sigma_z = 0.24 * x * (1 + 0.001 * x) ** -0.5
    elif 2 < u <= 4:
        if is_day:
            sigma_y = 0.32 * x * (1 + 0.0004 * x) ** -0.5
            sigma_z = 0.24 * x * (1 + 0.001 * x) ** -0.5
        else:
            sigma_y = 0.11 * x * (1 + 0.0004 * x) ** -0.5
            sigma_z = 0.08 * x * (1 + 0.0015 * x) ** -0.5
    elif u > 4:
        if is_day:
            sigma_y = 0.22 * x * (1 + 0.0004 * x) ** -0.5
            sigma_z = 0.20 * x
        else:
            sigma_y = 0.16 * x * (1 + 0.0004 * x) ** -0.5
            sigma_z = 0.14 * x * (1 + 0.0003 * x) ** -0.5
    else:
        # fallback, should never happen
        sigma_y = sigma_z = np.nan

    return sigma_y, sigma_z
