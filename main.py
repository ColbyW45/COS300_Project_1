# COS300 Project 1

import sys
import numpy as np
from stl import mesh

from PyQt6.QtWidgets import (
	QApplication, QWidget, QPushButton, QLabel, 
	QLineEdit, QHBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QSurfaceFormat
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLVersionProfile

import pyqtgraph as pg
import pyqtgraph.opengl as gl


class STL_Model():

	def __init__(self, stl_file):
		self.model = stl_file

	def mesh(self):
		self.mesh = mesh.Mesh.from_file(self.model)
		return self.mesh


def Model_Preview_Parameters():
	model_preview = gl.GLViewWidget()

	# Add Axis Grids
	xGrid = gl.GLGridItem()
	yGrid = gl.GLGridItem()
	zGrid = gl.GLGridItem()
	model_preview.addItem(xGrid)
	model_preview.addItem(yGrid)
	model_preview.addItem(zGrid)

	# rotate x and y grids to face the correct direction
	xGrid.rotate(90, 0, 1, 0)
	yGrid.rotate(90, 1, 0, 0)

	# scale each grid differently
	xGrid.scale(0.2, 0.1, 0.1)
	yGrid.scale(0.2, 0.1, 0.1)
	zGrid.scale(0.1, 0.2, 0.1)

	# Add Mesh
	#m = gl.GLMeshItem(Model.mesh())
	#model_preview.addItem(m)

	return model_preview


class Window(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("CNC Wire Bending Slicer")
		# Set window Icon (Curently placeholder)
		self.setWindowIcon(QIcon("icon.jpeg"))
		self.setContentsMargins(5, 5, 5, 5)

		# Set Qt layout type 
		layout = QHBoxLayout()
		self.setLayout(layout)

		button = QPushButton("Test Button")
		layout.addWidget(button)

		stylesheet = ("""
			QWidget {
				font-family: "Helvetica";
			}

		""")

		self.setStyleSheet(stylesheet)


		# Model Preview
		layout.addWidget(Model_Preview_Parameters(),2)


def st_test():
	from mpl_toolkits import mplot3d
	from matplotlib import pyplot

	test_mesh = Model.mesh

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


if __name__ == "__main__":

	Model = STL_Model('test_square_stl.stl')

	print(Model.mesh)

	# PyQt Window
	app = QApplication(sys.argv)

	window = Window()

	window.show()
	sys.exit(app.exec())