# COS300 Project 1

import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

test_mesh = mesh.Mesh.from_file('test_square_stl.stl')

# Create a new plot
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

# Load the STL files and add the vectors to the plot
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(test_mesh.vectors))

# Auto scale to the mesh size
scale = test_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()
