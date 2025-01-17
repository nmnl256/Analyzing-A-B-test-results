import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

z_critical = 1.96
z_points = [1.151040706, -1.151040706]

x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Standard Normal Distribution", color="blue")

plt.fill_between(x, y, where=(x < -z_critical) | (x > z_critical), color="red", alpha=0.3, label="Rejection Region")
plt.fill_between(x, y, where=(-z_critical < x) & (x < z_critical), color="green", alpha=0.2, label="Non-Rejection Region")

plt.axvline(z_critical, color="black", linestyle="--", label=f"Z Critical (+{z_critical})")
plt.axvline(-z_critical, color="black", linestyle="--", label=f"Z Critical (-{z_critical})")

for z in z_points:
    plt.axvline(z, color="orange", linestyle="-.", linewidth=1.5, label=f"Z Point ({z:.2f})")
    plt.text(z, 0.1, f"{z:.2f}", color="orange", fontsize=10, ha="center")

plt.title("Normal Distribution with Z-Critical and Z-Points", fontsize=16)
plt.xlabel("Z-Score", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.legend(loc="upper left")
plt.grid(alpha=0.3)

plt.tight_layout()
file_path = "normal_distribution_with_z_points.png"
plt.savefig(file_path)
plt.show()

file_path
