# Code programmed by Eng. Ivan Duran Santos in Volkswagen de Mexico
# This code runs above Python 3.10
# This code does not go on Jupyter Notebooks

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

from matplotlib.widgets import Slider, Button

# We start with the function to plot a big square (just reference)

def Squa_C(tras_x, tras_y, rot_z):
	
	valor_en_x = 8
	valor_en_y = 8
	lon_x = [valor_en_x, valor_en_x, -valor_en_x, -valor_en_x, valor_en_x]
	lon_y = [valor_en_y, -valor_en_y, -valor_en_y, valor_en_y, valor_en_y]
	return (lon_x, lon_y)

# Plot a second square (smaller) -> This is the one that will be manipulated with the sliders
def Squa(tras_x, tras_y, rot_z):
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
ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="b")
ax.plot(Squa_C(0, 0, 0)[0], Squa_C(0, 0, 0)[1], c="0.8")




#Now, we need to plot yhe slider, it's going to be in "horizontal"
plt.subplots_adjust(bottom=0.30)

#We define the dimension and characteristics of the slider
slider_x_plot = plt.axes([0.1, 0.05, 0.8, 0.05])		#Dimensions
slider_y_plot = plt.axes([0.1, 0.1, 0.8, 0.05])		#Dimensions
slider_z_plot = plt.axes([0.1, 0.15, 0.8, 0.05])		#Dimensions
			   #plt.axes([left, bottom, width, height])

# Definition of the properties of the sliders 
#                 label, name, value min, value max, initial value, value of the step
slider_x = Slider(slider_x_plot, "T_x", valmin=-10, valmax=10, valinit=0, valstep=1)#Characteristics
slider_y = Slider(slider_y_plot, "T_y", valmin=-10, valmax=10, valinit=0, valstep=1)#Characteristics
slider_z = Slider(slider_z_plot, "R_z", valmin=-90, valmax=90, valinit=0, valstep=1)#Characteristics


#Finally, we must define the function of UPDATING
def update_x(val_x):
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C(0, 0, 0)[0], Squa_C(0, 0, 0)[1], c="0.8")
	ax.plot(Squa(slider_x.val, slider_y.val, slider_z.val)[0], 
		    Squa(slider_x.val, slider_y.val, slider_z.val)[1])
	plt.draw()

def update_y(val_y):
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C(0, 0, 0)[0], Squa_C(0, 0, 0)[1], c="0.8")
	ax.plot(Squa(slider_x.val, slider_y.val, slider_z.val)[0], 
		    Squa(slider_x.val, slider_y.val, slider_z.val)[1])
	plt.draw()

def update_z(val_z):
	ax.clear()
	ax.axis([-10, 10, -10, 10])
	ax.plot(Squa(0, 0, 0)[0], Squa(0, 0, 0)[1], c="0.8")
	ax.plot(Squa_C(0, 0, 0)[0], Squa_C(0, 0, 0)[1], c="0.8")
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
# It is necessary type **plt.show** at the end because the sliders run apart

