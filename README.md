# Slider-and-Tralslation-functions.

This code combines the power between the sliders **(From MatPlotLib)** and the Traslation functions. 

This program helps us to realize the importance of simulations. 

## Program

### Functions

First at all, we need to call all the libraries:

```
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
``` 

This last is the most important because this is the one that gives us the Slider options. 

### Functions

Then I will define the initial functions that can do the next: 

**Squa_C**: This is just for draw a big square with dimentions of 8 each side. 

**Squa**: This is the main function. We start giving the shape of the swuare _(3 x 3)_, then I write functions to transform the radiants to grades using $`a = argument * pi / 180`$. Then I define the sqare using two lists of 5 points in X and Y. I create the 1's vector and define the square matrix. Then I build the X and Y traslation matrix: 


```
[
[1, 0, X_movement] #List
[0, 1, Y_movement] #List
[0, 0, 1] #List
]
```

Later, the Rotation movement matrix: 

```
[
[Cos(angle), Sin(angle), 0]
[-Sin(angle), Cos(angle), 0]
[0, 0, 1]
]
```

> Remember: these matrix are jsut for a 2 Dimentions Transformation

[If you need more information about the Movement Transformation, you can find them here](https://www.tutorialspoint.com/computer_graphics/2d_transformation.htm)

At the end of the function, it is necessary to combine the previous matrices using the Numpy **dot** operator, 


### Initial figure

We need to define a figure using: 

```
fig, ax = plt.subplots()    # From Matplotlib
```

Then, I will plot the big gray square (from the first function) and then the other gray and blue smaller (from the 2nd function). Since tha area where the squares are plotted is fixed on top of the figure. 

For the slider characteristics, first each slider need to be defined. There will be 3 sliders (One for rotation transformation, and 2 for X and Y traslation movement). The sintaxis of the slider properties are the next: 

```
Slider(Label, "name", valmin=, valmax=, valinit=, valstep=)
```

[For more information about the Sliders](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)


### Updating functions. 

Finaly, it is necesary create the updating functions. The logic is the next: 

> Clear the figure
> Fix the axis, one more time
> Plot the big square
> Plot the small gray square
> Update the blue square using the current values from the sliders position inside the **Squa** function. 

This process is replied 3 times, because there are 3 sliders and the position of each slider needs to be saved and at the same time recognized by the others.



At the end, we need to write the **on_changed** from the sliders. 


