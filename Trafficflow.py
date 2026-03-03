import numpy as np

traffic = np.array([
    [100, 50],   # Direction 1 N->S
    [80, 60]     # Direction 2 E->W
])

print("Original Traffic Matrix:\n", traffic)
#Displays the Original Matrix

transform = np.array([[0.7, 0.3],
                      [0.6, 0.4]])
# Transformed Matrix

print("\nTransformation Matrix:\n", transform)
# Displays the Transformed Matrix

new_traffic = np.dot(traffic, transform)
# Dot product of 2 Matrices which provides the optimized result.

print("\nTraffic After Signal Optimization:\n", new_traffic)
# Displays the Optimized Matrix

print("\nTotal traffic per direction:", np.sum(new_traffic, axis=1))
# Displays the Total traffic in each direction

print("Total traffic per phase:", np.sum(new_traffic, axis=0))
# Displays the total traffic per Phase