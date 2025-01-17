import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Parameters
n_control = 5000  # number of users in the control group
n_test = 5000  # number of users in the test group
conversion_rate_control = 0.25  # base conversion rate for the control group
lift = 0.1  # expected lift in the test group

# Generate control group data
control_group = pd.DataFrame({
    "user_id": range(1, n_control + 1),
    "group": "Control",
    "conversion": np.random.choice([0, 1], size=n_control, p=[1 - conversion_rate_control, conversion_rate_control]),
    "date": pd.date_range(start="2025-01-01", periods=n_control // 100, freq="D").repeat(100)[:n_control]
})

# Generate test group data
test_group = pd.DataFrame({
    "user_id": range(n_control + 1, n_control + n_test + 1),
    "group": "Test",
    "conversion": np.random.choice([0, 1], size=n_test, p=[1 - conversion_rate_control * (1 + lift), conversion_rate_control * (1 + lift)]),
    "date": pd.date_range(start="2025-01-01", periods=n_test // 100, freq="D").repeat(100)[:n_test]
})

# Combine data
ab_test_data = pd.concat([control_group, test_group], ignore_index=True)

# Save to CSV
file_path = "ab_test_results.csv"
ab_test_data.to_csv(file_path, index=False)
file_path