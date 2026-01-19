import numpy as np
import pandas as pd

from plume.coordinates import rotate_coords, lonlat_to_utm
from plume.plume_model import gaussian_plume
from plume.wind import compute_wind

INPUT_FILE = "H:/conference/DAAD/work/test_data.csv"
OUTPUT_FILE = "H:/conference/DAAD/work/GP_Modelled_Concentration.csv"

Z_RECEPTOR = 10.0  # meters
SECONDS_PER_YEAR = 365 * 24 * 60 * 60
UTM_PROJ = "EPSG:32643" 


def run_model(input_csv, output_csv, UTM_PROJ):
    data = pd.read_csv(input_csv)
    data["Time"] = pd.to_datetime(data["Time"])

    results = []

    for time, df in data.groupby("Time"):
        lon = df["Longitude"].values
        lat = df["Latitude"].values
        Q = df["Emi_val"].values
        H = df["H"].values
        hour_time = time.hour 

        wd, ws = compute_wind(df["u_component"].values, df["v_component"].values)

        x_src, y_src = lonlat_to_utm(lon, lat, UTM_PROJ)
        total_conc = np.zeros_like(x_src)

        for i, (sx, sy, Qi) in enumerate(zip(x_src, y_src, Q)):
            dx = x_src - sx
            dy = y_src - sy
            x_rel, y_rel = rotate_coords(dx, dy, wd[i])

            C = gaussian_plume(Qi, x_rel, y_rel, H[i], ws[i], Z_RECEPTOR, hour_time)
            C *= 1e6 / SECONDS_PER_YEAR * 1e6  # unit conversion

            total_conc += C

        for lo, la, c in zip(lon, lat, total_conc):
            results.append([time, lo, la, c])

    pd.DataFrame(
        results,
        columns=["Time", "Longitude", "Latitude", "Modelled_Concentration"],
    ).to_csv(output_csv, index=False)


if __name__ == "__main__":
    run_model(
        input_csv=INPUT_FILE,
        output_csv=OUTPUT_FILE,
        UTM_PROJ=UTM_PROJ,
    )
