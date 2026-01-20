# Gaussian Plume Model

This repository provides a Python implementation of a Gaussian plume model for simulating pollutant dispersion in urban environments. The model processes emission and meteorological data to estimate pollutant concentrations at receptor points (grid points).
---

## 📂 Repository Structure
```text
gaussian-plume-model/
│
├─ data/
│  ├─ test_data.csv
│
├─ plume/
│  ├─ coordinates.py    # Functions to convert and rotate coordinates
│  ├─ dispersion.py     # Functions to calculate dispersion coefficients
│  ├─ plume_model.py    # Gaussian plume calculations
│  └─ wind.py           # Wind speed and direction calculations
│
├─ scripts/
│  └─ run_model.py      # Main script to run the model

```
---

⚡ Usage

The main script for running the model is `run_model.py`, located in the `scripts/` directory.

Before executing the script, update the required configuration parameters in `run_model.py` as needed:

- **`Z_RECEPTOR = 10.0`**  
  Height of the receptor (i.e., the elevation at which air pollutant concentrations are modelled), in meters.

- **`SECONDS_PER_YEAR = 365 * 24 * 60 * 60`**  
  Total number of seconds in one year.

- **`UTM_PROJ = "EPSG:32643"`**  
  UTM coordinate reference system used for the study region.

After configuring these parameters, run the model using:

```bash
python -m scripts.run_model
```

### Input Data

The input CSV file should contain the following columns:

| **Field** | **Description** | 
|-----------|----------------|
| Time |	Timestamp (YYYY-MM-DD HH:MM:SS) of each grid point (receptor)|
| Longitude |	Source longitude (degrees) of each grid point (receptor) |
| Latitude |	Source latitude (degrees) of each grid point (receptor) |
| Emi_val |	Emission rate (kt/year) of pollutant of each grid point (receptor) |
| H |	Stack height (m) of each grid point (receptor) |
| u_component |	Wind speed in x-direction (m/s) of each grid point (receptor) |
| v_component | Wind speed in y-direction (m/s) of each grid point (receptor) |

### Output

The output CSV file contains:

| **Field** | **Description** | 
|-----------|----------------|
| Time |	Timestamp (YYYY-MM-DD HH:MM:SS)  of each grid point (receptor)|
| Longitude |	Source longitude (degrees)  of each grid point (receptor)|
| Latitude |	Source latitude (degrees)  of each grid point (receptor)|
| Modelled_Concentration | Modelled concentration of each grid point (receptor) in μg/m³|
