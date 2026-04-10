import numpy as np
from ingestion import load_sensor_data
from processing import (
    compute_mean,
    compute_std,
    min_max_normalize,
    z_score_normalize
)
from analysis import detect_anomalies
from utils import validate_data


def save_to_csv(data, file_path):
    try:
        np.savetxt(file_path, data, delimiter=",")
    except Exception as e:
        raise RuntimeError(f"Failed to save data: {e}")


def run_pipeline():
    data = load_sensor_data("../data/sensor_data.csv")
    validate_data(data)

    mean = compute_mean(data)
    std = compute_std(data)

    minmax = min_max_normalize(data)
    zscore = z_score_normalize(data)
    anomalies = detect_anomalies(data)

    # Save outputs
    save_to_csv(minmax, "../outputs/minmax_normalized.csv")
    save_to_csv(zscore, "../outputs/zscore_normalized.csv")
    save_to_csv(anomalies, "../outputs/anomalies.csv")

    print("Pipeline executed successfully")
    print(f"Mean: {mean}, Std: {std}")
    print(f"Anomalies: {anomalies}")


if __name__ == "__main__":
    run_pipeline()
