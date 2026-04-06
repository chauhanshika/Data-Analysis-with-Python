import numpy as np
from processing import compute_mean, compute_std

def detect_anomalies(data: np.ndarray, threshold: float = 2.0):
    mean = compute_mean(data)
    std = compute_std(data)

    anomalies = []

    for value in data:
        z_score = (value - mean) / std
        if abs(z_score) > threshold:
            anomalies.append(value)

    return np.array(anomalies)
