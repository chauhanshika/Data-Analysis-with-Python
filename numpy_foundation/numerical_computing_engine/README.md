# Numerical Computing Engine

## Overview

The Numerical Computing Engine is a lightweight data preprocessing system designed to handle raw sensor data and prepare it for downstream analytics.

It focuses on building core statistical and normalization logic from scratch using NumPy, without relying on high-level abstractions. This approach ensures transparency, control, and a deeper understanding of data transformation pipelines.

---

## Problem Statement

Sensor-generated data (e.g., IoT devices, monitoring systems) is often:

* Noisy and inconsistent
* Containing extreme outliers
* Difficult to directly use for analysis or modeling
  

Without proper preprocessing, such data leads to inaccurate insights and unreliable systems.

---

## Solution

This system provides a structured preprocessing pipeline that:

* Computes statistical measures manually
* Normalizes data for consistency
* Detects anomalies using statistical methods

It acts as a foundational layer before analytics or machine learning workflows.

---

## Key Features

### 1. Statistical Computation

* Manual implementation of:

  * Mean
  * Standard Deviation
* Avoids direct reliance on NumPy shortcuts to demonstrate core logic

### 2. Data Normalization

* Min-Max Normalization
* Z-Score Normalization

Ensures data is scaled and comparable across different ranges.

### 3. Anomaly Detection

* Z-score based detection
* Identifies extreme sensor readings

### 4. Input Validation

* Handles:

  * Empty datasets
  * Invalid data types
* Improves system robustness

---

## System Architecture

```bash
src/
├── ingestion.py        # Data loading
├── processing.py       # Core computations
├── analysis.py         # Anomaly detection
├── utils.py            # Validation utilities
├── main.py             # Pipeline execution
```

---

## Data Flow

```text
Raw Sensor Data → Validation → Processing → Analysis → Output
```

---

## Example Dataset

The system uses simulated sensor data containing normal values and anomalies:

* Normal range: 12–35
* Outliers: 100, 400

---

## Key Findings

* Detected anomalies: **100, 400**
* Data distribution shows significant skew due to extreme values
* Normalization stabilizes scale for further processing

---

## Outputs

The system can generate:

* Normalized datasets
* Detected anomaly values
* Processed numerical arrays

(Stored in the `outputs/` directory)

---

## Tech Stack

* Python
* NumPy

---

## Real-World Applications

* IoT sensor data preprocessing
* Industrial monitoring systems
* Data cleaning pipelines before analytics
* Preprocessing layer for machine learning systems

---

## Future Improvements

* Batch data processing support
* Integration with data pipelines
* Performance optimization for large-scale datasets
* Extension to multi-dimensional data

---

## Conclusion

This project demonstrates how foundational numerical systems can be built from scratch using NumPy, emphasizing clarity, control, and real-world applicability.

It serves as a base layer for scalable data processing and analytics systems.
