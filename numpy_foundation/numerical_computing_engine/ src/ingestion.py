import numpy as np

def load_sensor_data(file_path: str) -> np.ndarray:
    try:
        data = np.genfromtxt(file_path, delimiter=",", skip_header=1)
        return data
    except Exception as e:
        raise RuntimeError(f"Failed to load sensor data: {e}")
