import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
a, b = 0.5, 0.5
u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Parametric equations
x = np.exp(b * v) * np.cos(v) + np.exp(a * v) * np.cos(u) * np.cos(v)
y = np.exp(b * v) * np.sin(v) + np.exp(a * v) * np.cos(u) * np.sin(v)
z = np.exp(a * v) * np.sin(u)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set transparent background
fig.patch.set_alpha(0)
ax.set_facecolor('none')

# Surface plot with gradient colors
ax.plot_surface(x, y, z, cmap='plasma', edgecolor='none')

# Labels in white for better contrast
ax.set_xlabel('X', color='white')
ax.set_ylabel('Y', color='white')
ax.set_zlabel('Z', color='white')

# Make tick numbers yellow
ax.tick_params(axis='x', colors='yellow')
ax.tick_params(axis='y', colors='yellow')
ax.tick_params(axis='z', colors='yellow')

# Add title at the top center
plt.title("Cross Cup Surface", color='white', fontsize=14, pad=20)

# Save with transparent background
plt.savefig("crossCupSurface.png", transparent=True, dpi=300)
                  plt.show()
