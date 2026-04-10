from ingestion import load_sensor_data
from processing import (
    compute_mean,
    compute_std,
    min_max_normalize,
    z_score_normalize
)
from analysis import detect_anomalies
from utils import validate_data

def main():
    data = load_sensor_data("../data/sensor_data.csv")
    validate_data(data)

    print("Original Data:", data)
    print("Mean:", compute_mean(data))
    print("Std:", compute_std(data))
    print("Min-Max:", min_max_normalize(data))
    print("Z-Score:", z_score_normalize(data))
    print("Anomalies:", detect_anomalies(data))

if __name__ == "__main__":
    main()
