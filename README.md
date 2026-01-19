# Gaussian Plume Model

This repository provides a Python implementation of a Gaussian plume model for simulating pollutant dispersion in urban environments. The model processes emission and meteorological data to estimate pollutant concentrations at receptor points (grid points).
---

## 📂 Repository Structure
gaussian-plume-model/
│
├─ plume/
│ ├─ coordinates.py # Functions to convert and rotate coordinates
│ ├─ dispersion.py # Functions to calculate dispersion co-efficients
│ ├─ plume_model.py # Gaussian plume calculations
│ └─ wind.py # Wind speed and direction calculations
├─ scripts/
│ └─ run_model.py # Main script to run the model
---

⚡ Usage

The main script is run_model.py located in scripts/. You can run the model using your own input CSV file:
python scripts/run_model.py


### Input Data

The input CSV file should contain the following columns:

| **Field** | **Description** | 
| Time |	Timestamp (YYYY-MM-DD HH:MM:SS) of each grid point (receptor)|
| Longitude |	Source longitude (degrees) of each grid point (receptor) |
| Latitude |	Source latitude (degrees) of each grid point (receptor) |
| Emi_val |	Emission rate of pollutant of each grid point (receptor) |
|H |	Stack height (m) of each grid point (receptor) |
|u_component|	Wind speed in x-direction (m/s) of each grid point (receptor) |
|v_component | Wind speed in y-direction (m/s) of each grid point (receptor) |

### Output

The output CSV file contains:

| **Field** | **Description** | 
| Time |	Timestamp (YYYY-MM-DD HH:MM:SS)  of each grid point (receptor)|
| Longitude |	Source longitude (degrees)  of each grid point (receptor)|
| Latitude |	Source latitude (degrees)  of each grid point (receptor)|
| Modelled_Concentration | Modelled concentration of each grid point (receptor) in μg/m^3|
