import json
from rich.console import Console
from rich.table import Table
import pandas as pd
import os

console = Console()

def load_results(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def display_results(results):
    table = Table(title="🔭 Galaxy Cluster Mass Summary", style="bold cyan")
    table.add_column("Parameter", style="magenta")
    table.add_column("Value", justify="right", style="green")

    table.add_row("Cluster Redshift", f"{results['cluster_redshift']:.5f}")
    table.add_row("Velocity Dispersion", f"{results['velocity_dispersion']:.2f} km/s")
    table.add_row("Diameter", f"{results['diameter_mpc']:.3f} Mpc")
    table.add_row("Dynamical Mass", f"{results['dynamical_mass']:.2e} solar masses")
    table.add_row("Luminous Mass (r-band)", f"{results['luminous_mass_r']:.2e} solar masses")
    table.add_row("Mass-to-Light-ratio", f"{results['mass-to-light-ratio']:.2f}")

    console.print(table)

def save_summary_to_csv(results, file_path):
    df = pd.DataFrame([{
        "Cluster Redshift": results["cluster_redshift"],
        "Velocity Dispersion (km/s)": results["velocity_dispersion"],
        "Diameter (Mpc)": results["diameter_mpc"],
        "Dynamical Mass (Solar Masses)": results["dynamical_mass"],
        "Luminous Mass (r-band) (Solar Masses)": results["luminous_mass_r"],
        "Mass-to-Light-ratio": results["mass-to-light-ratio"]
    }])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"[✔] Results saved to: {file_path}")

def main():
    results = load_results("final_results.json")
    display_results(results)
    save_summary_to_csv(results, "Results/mass_results_summary.csv")

if __name__ == "__main__":
    main()
