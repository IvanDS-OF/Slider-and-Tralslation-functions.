# Slider-and-Tralslation-functions.

This code combines the power between the sliders _(From MatPlotLib)_ and the Traslation functions. 

This program helps us to realize the importance of simulations. 

## Program

First at all, we need to call all the libraries:

```
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
``` 

This last is the most important because this is the one that gives us the Slider options. 

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













Then, the program 






https://www.tutorialspoint.com/computer_graphics/2d_transformation.htm
