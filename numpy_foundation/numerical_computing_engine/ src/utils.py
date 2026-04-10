import numpy as np

def validate_data(data):
    if data is None:
        raise ValueError("Data is None")

    if len(data) == 0:
        raise ValueError("Empty dataset")

    if not isinstance(data, np.ndarray):
        raise TypeError("Data must be a NumPy array")
