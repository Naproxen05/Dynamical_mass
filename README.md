# Dynamical Mass Estimation of Galaxy Clusters

This project is an academic assignment focused on calculating the **dynamical mass of a galaxy cluster** using observational data, including galaxy redshift and velocity dispersion. The project follows fundamental astrophysical principles and provides a base for future machine learning implementation.

#  📁 Project Structure

📦Dynamical_mass/
┣ 📂data/
┃ ┗ 📄galaxy_cluster_data.csv
┣ 📂notebooks/
┃ ┗ 📄dynamical_mass_calculation.ipynb
┣ 📂results/
┃ ┗ 📄mass_results_summary.csv
┣ 📄README.md
┣ 📄requirements.txt
┗ 📄main.py

## 📌 Objectives

- Compute the **dynamical mass** of a galaxy cluster based on observational velocity dispersion and redshift.
- Explore the **virial theorem** and its application in extragalactic astronomy.
- Evaluate the reliability of mass estimations using available data.

## 🧪 Methodology

The project uses the **virial theorem** in the context of galaxy clusters:


M = (3 x sigma_v^2 x R) / (G)


Where:
-  M : Dynamical Mass
- sigma_v : Velocity Dispersion
-  R : Effective radius (derived from projected separation)
-  G : Gravitational Constant

## 📊 Dataset

The dataset includes:
- Galaxy positions (RA, Dec)
- Spectroscopic redshifts
- Projected distances from cluster center
- Velocity data

📍 *Note*: Data is provided as part of an academic summer internship project.

## 🔍 Results

- Cluster radius: ~0.57 Mpc  
- Velocity dispersion: ~1316.15 km/s  
- Computed dynamical mass: ~\( 3.32 \times 10^{14} \) solar masses

These values are consistent with realistic galaxy clusters such as **Abell 1689** and **Coma**.

## 🤖 Future Work

The next phase of this project will integrate **machine learning** to:
- Train a regression model on velocity dispersion, redshift, and cluster parameters.
- Automatically estimate the dynamical mass with improved accuracy.
- Explore model performance across various real and simulated datasets.

### Planned ML Stack
- Scikit-learn / XGBoost / LightGBM
- Jupyter Notebooks for experimentation
- Dataset curation using SDSS & other catalogs

## 🛠️ Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/dynamical-mass-galaxy-cluster.git
cd dynamical-mass-galaxy-cluster


