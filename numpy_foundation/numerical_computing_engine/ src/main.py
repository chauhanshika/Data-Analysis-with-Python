from ingestion import load_sensor_data
from processing import compute_mean, compute_std

def main():
    data = load_sensor_data("../data/sensor_data.csv")

    mean = compute_mean(data)
    std = compute_std(data)

    print("Mean:", mean)
    print("Standard Deviation:", std)

if __name__ == "__main__":
    main()
