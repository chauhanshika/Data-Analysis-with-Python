import numpy as np

def compute_mean(data: np.ndarray) -> float:
    total = 0.0
    for value in data:
        total += value
    return total / len(data)


def compute_std(data: np.ndarray) -> float:
    mean = compute_mean(data)
    variance_sum = 0.0

    for value in data:
        variance_sum += (value - mean) ** 2

    variance = variance_sum / len(data)
    return variance ** 0.5
