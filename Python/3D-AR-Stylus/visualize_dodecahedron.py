import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

# data = pd.read_csv('markers/model_points_4x4.csv') 
data = pd.read_csv('markers/model_points_MIP_36h12.csv') 
row, column = data.shape        # Check the number of row & column

# Create a 3D scatter plot
# -- Plots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Adjust axes to blender axes
ax.axes.set_xlim3d(30,-30)
ax.axes.set_ylim3d(-30,30)
ax.axes.set_zlim3d(bottom=30, top=-30)
ax.scatter(data['x'], data['y'], data['z'])

# line=art3D.Line3D([x始点, x終点], [y始点, y終点], [z始点, z終点])
for i in range(0,row,4):
    for j in range(4):
        # print(i, i+j, i+j+1)
        if((i+j)<row):
            if(j<3):
                line = art3d.Line3D([data['x'][i+j], data['x'][i+j+1]],
                                    [data['y'][i+j], data['y'][i+j+1]],
                                    [data['z'][i+j], data['z'][i+j+1]])
            else:
                line = art3d.Line3D([data['x'][i + j], data['x'][i]],
                                    [data['y'][i + j], data['y'][i]],
                                    [data['z'][i + j], data['z'][i]])

        ax.add_line(line)

# Put data into a 2D-list
cols_to_combine = ['x', 'y', 'z']
test = data[cols_to_combine].values.tolist()
print(test)

# Convert a 2D list to a 3D list using K-slice
# https://www.geeksforgeeks.org/python-convert-2d-list-to-3d-at-k-slicing/
# initializing K
K = 4   # number of 2D data in a group
test_list = iter(test)
temp = [test_list] * K
model_list = [list(ele) for ele in zip(*temp)]
print(model_list)

# Use deque to append (faster)
from collections import deque
new_list = deque()
for i in range(4):
    new_list.append(model_list[0][i])
print(new_list)
for i in range(4):
    new_list.append(model_list[1][i])
print(new_list)

# Convert list to numpy array
import numpy as np
result = np.array(new_list)
print(result)

# -- Labels
for i in range(row):
    ax.text(data['x'][i], data['y'][i], data['z'][i], data['label'][i])
plt.show()
