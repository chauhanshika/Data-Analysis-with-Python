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


def min_max_normalize(data: np.ndarray) -> np.ndarray:
    min_val = data[0]
    max_val = data[0]

    for value in data:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    normalized = []
    for value in data:
        normalized.append((value - min_val) / (max_val - min_val))

    return np.array(normalized)


def z_score_normalize(data: np.ndarray) -> np.ndarray:
    mean = compute_mean(data)
    std = compute_std(data)

    normalized = []
    for value in data:
        normalized.append((value - mean) / std)

    return np.array(normalized)
