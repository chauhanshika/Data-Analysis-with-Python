from ingestion import load_sensor_data

def main():
    data = load_sensor_data("../data/sensor_data.csv")
    print("Raw Sensor Data:", data)

if __name__ == "__main__":
    main()
