from ingestion import load_sensor_data
from processing import (
    compute_mean,
    compute_std,
    min_max_normalize,
    z_score_normalize
)

def main():
    data = load_sensor_data("../data/sensor_data.csv")

    print("Original Data:", data)
    print("Min-Max Normalized:", min_max_normalize(data))
    print("Z-Score Normalized:", z_score_normalize(data))

if __name__ == "__main__":
    main()
