import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the tetrahedron
vertices = [
    [0, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(vertices)

# Define the triangular faces (vertex indices)
faces = [
    [0, 1, 3],
    [1, 2, 3]
]

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the tetrahedron
ax.add_collection3d(Poly3DCollection([
    [vertices[i] for i in face] for face in faces
], facecolors='cyan', edgecolor='k'))

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set plot title
ax.set_title('3D Tetrahedron')

# Show the plot
plt.show()