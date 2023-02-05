# From https://pyqtgraph.readthedocs.io/en/latest/getting_started/3dgraphics.html

# TEST COS300 Project 1

import sys
import numpy
from stl import mesh

import OpenGL
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

from PyQt6.QtWidgets import (
	QApplication, QWidget, QPushButton, QLabel, 
	QLineEdit, QHBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QSurfaceFormat
from PyQt6.QtOpenGL import QOpenGLWindow, QOpenGLVersionProfile

import pyqtgraph as pg
import pyqtgraph.opengl as gl


test_mesh = mesh.Mesh.from_file('test_square_stl.stl')

class UI(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("CNC Wire Bending Slicer")
		self.setWindowIcon(QIcon("GhostPipe.jpeg"))
		self.setContentsMargins(10, 10, 10, 10)

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
		model_preview = gl.GLViewWidget()

		# create three grids, add each to the view
		xgrid = gl.GLGridItem()
		ygrid = gl.GLGridItem()
		zgrid = gl.GLGridItem()
		model_preview.addItem(xgrid)
		model_preview.addItem(ygrid)
		model_preview.addItem(zgrid)

		# rotate x and y grids to face the correct direction
		xgrid.rotate(90, 0, 1, 0)
		ygrid.rotate(90, 1, 0, 0)

		# scale each grid differently
		xgrid.scale(0.2, 0.1, 0.1)
		ygrid.scale(0.2, 0.1, 0.1)
		zgrid.scale(0.1, 0.2, 0.1)

		layout.addWidget(model_preview,2)





if __name__ == "__main__":
	app = QApplication(sys.argv)

	ui = UI()
	#mp = Model_Preview()

	ui.show()
	#mp.show()
	sys.exit(app.exec())