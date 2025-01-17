import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parameters
z_critical = 1.96  # Critical Z value for alpha = 0.05 (two-tailed)
z_points = [1.151040706, -1.151040706]  # Points to mark on the curve

# X range for the standard normal distribution
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plot the normal distribution
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Standard Normal Distribution", color="blue")

# Highlight rejection regions
plt.fill_between(x, y, where=(x < -z_critical) | (x > z_critical), color="red", alpha=0.3, label="Rejection Region")
plt.fill_between(x, y, where=(-z_critical < x) & (x < z_critical), color="green", alpha=0.2, label="Non-Rejection Region")

# Add Z-critical lines
plt.axvline(z_critical, color="black", linestyle="--", label=f"Z Critical (+{z_critical})")
plt.axvline(-z_critical, color="black", linestyle="--", label=f"Z Critical (-{z_critical})")

# Add points for the given Z values
for z in z_points:
    plt.axvline(z, color="orange", linestyle="-.", linewidth=1.5, label=f"Z Point ({z:.2f})")
    plt.text(z, 0.1, f"{z:.2f}", color="orange", fontsize=10, ha="center")

# Labels and title
plt.title("Normal Distribution with Z-Critical and Z-Points", fontsize=16)
plt.xlabel("Z-Score", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.legend(loc="upper left")
plt.grid(alpha=0.3)

# Save and display the plot
plt.tight_layout()
file_path = "normal_distribution_with_z_points.png"
plt.savefig(file_path)
plt.show()

file_path
