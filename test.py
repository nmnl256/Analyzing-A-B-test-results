import pandas as pd
import numpy as np

np.random.seed(42)


n_control = 5000
n_test = 5000
conversion_rate_control = 0.25
lift = 0.01

control_group = pd.DataFrame({
    "user_id": range(1, n_control + 1),
    "group": "Control",
    "conversion": np.random.choice([0, 1], size=n_control, p=[1 - conversion_rate_control, conversion_rate_control]),
    "date": pd.date_range(start="2025-01-01", periods=n_control // 100, freq="D").repeat(100)[:n_control]
})

test_group = pd.DataFrame({
    "user_id": range(n_control + 1, n_control + n_test + 1),
    "group": "Test",
    "conversion": np.random.choice([0, 1], size=n_test, p=[1 - conversion_rate_control * (1 + lift), conversion_rate_control * (1 + lift)]),
    "date": pd.date_range(start="2025-01-01", periods=n_test // 100, freq="D").repeat(100)[:n_test]
})

ab_test_data = pd.concat([control_group, test_group], ignore_index=True)

file_path = "ab_test_results.csv"
ab_test_data.to_csv(file_path, index=False)
file_path
