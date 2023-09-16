# Code programmed by Eng. Ivan Duran Santos in Volkswagen de Mexico
# This code runs above Python 3.10
# This code does not go on Jupyter Notebooks
 
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Slider, Button

# We start with the function to plot a big square (just reference)

def Squa_C():
	"""
	This function just draws an 8x8 square. No arguments required
	"""
	valor_en_x = 8
	valor_en_y = 8
	lon_x = [valor_en_x, valor_en_x, -valor_en_x, -valor_en_x, valor_en_x]
	lon_y = [valor_en_y, -valor_en_y, -valor_en_y, valor_en_y, valor_en_y]
	return (lon_x, lon_y)

# Plot a second square (smaller) -> This is the one that will be manipulated with the sliders
def Squa(tras_x, tras_y, rot_z):
	"""
	This function draws a 3x3 square and modifies its position with three arguments
 	The way to modify the position of the square is by implementing a translation matrix
  	and a rotation matrix, and multiply them using np.dot to obtain a matrix
   	with the same initial shape. 

 	Arguments: 
  
	tras_x (float): This modifies the x position of the square
 	tras_y (float): This modifies the y position of the square
	rot_z (float): This modifies the z angle of the square

 	Returns:
  
  	S1[0] (list): It is a list of the x points of the squared 
    S1[1] (list): It is a list of the y points of the squared 
 
	"""
	valor_en_x = 3
	valor_en_y = 3
	a = rot_z * np.pi / 180
	lon_x = [valor_en_x, valor_en_x, -valor_en_x, -valor_en_x, valor_en_x]
	lon_y = [valor_en_y, -valor_en_y, -valor_en_y, valor_en_y, valor_en_y]
	mat_uno = [1, 1, 1, 1, 1]
	C = [lon_x, lon_y, mat_uno]
	P1 = [[1, 0, tras_x], [0, 1, tras_y], [0, 0, 1]]
	P2 = [[np.cos(a), np.sin(a), 0], 
          [-np.sin(a), np.cos(a), 0], 
          [0, 0, 1]]
	S1 = np.dot(np.dot(P1, P2), C)
	return (S1[0], S1[1])

# First, we must draw the figure like a subplot
fig, ax = plt.subplots()

# we need to start ploting the initial values, square in 0, 0
# We need to start plotting the initial values, square in 0, 0
ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="b")
ax.plot(Squa_C()[0], Squa_C()[1], c="0.8")

#Now, we need to plot yhe slider, it's going to be in "horizontal"
plt.subplots_adjust(bottom=0.30)

#We define the dimension and characteristics of the slider
slider_x_plot = plt.axes([0.1, 0.05, 0.8, 0.05])	#Dimensions
slider_y_plot = plt.axes([0.1, 0.1, 0.8, 0.05])		#Dimensions
slider_z_plot = plt.axes([0.1, 0.15, 0.8, 0.05])	#Dimensions
#plt.axes([left, bottom, width, height])

# Definition of the properties of the sliders 
#                 label, name, value min, value max, initial value, value of the step
slider_x = Slider(slider_x_plot, "T_x", valmin=-10, valmax=10, valinit=0, valstep=1)#Characteristics
slider_y = Slider(slider_y_plot, "T_y", valmin=-10, valmax=10, valinit=0, valstep=1)#Characteristics
slider_z = Slider(slider_z_plot, "R_z", valmin=-90, valmax=90, valinit=0, valstep=1)#Characteristics


#Finally, we must define the function of UPDATING
def update_x(val_x):
	"""
	This function displays the changes from slider X using the val_x slicer as input
	"""
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C()[0], Squa_C()[1], c="0.8")
	ax.plot(Squa(slider_x.val, slider_y.val, slider_z.val)[0], 
		    Squa(slider_x.val, slider_y.val, slider_z.val)[1])
	plt.draw()

def update_y(val_y):
	"""
	This function displays the changes from slider Y using the val_x slicer as input
 	"""
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C()[0], Squa_C()[1], c="0.8")
	ax.plot(Squa(slider_x.val, slider_y.val, slider_z.val)[0], 
		    Squa(slider_x.val, slider_y.val, slider_z.val)[1])
	plt.draw()


def update_z(val_z):
	"""
	This function displays the changes from slider Z using the val_x slicer as input
 	"""
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C()[0], Squa_C()[1], c="0.8")
	ax.plot(Squa(slider_x.val, slider_y.val, slider_z.val)[0], 
		    Squa(slider_x.val, slider_y.val, slider_z.val)[1])
	plt.draw()


# We write the command to update the plot, like that: 
slider_x.on_changed(update_x)
slider_y.on_changed(update_y)
slider_z.on_changed(update_z)

# We should define the axis. 
ax.axis([-10, 10, -10, 10])
plt.show()

# Note: This code should be improved using the OOP paradigm 
