import numpy as np
import os
from PIL import Image

def complex_function(z, c):
    return z*z + c

def iteration_count_coloring(iterations, max_iterations):
    return iterations / float(max_iterations)

# Fractal Properties

bailout_value = 2

# Image dimensions
res_x = 1024
res_y = 1024

"""
We create a new image, with the RGB color space (this will determine how we
color the image later), with resolution (res_x X res_y), and we set the default
pixel color to be black.
"""
image = Image.new('RGB', (res_x, res_y), 'black')
pixels = image.load()

"""
Initial complex number: this number determines the fractal we get as output.
"""
c = complex(-0.4, 0.6)

"""
Region of the complex plane we want to visualize in this case the region is the
rectangle with bottom left vertex (-2.4, -1.4), upper right vertex (1.6, 2.6)

The reason we chose this specific rectangle is so it includes the whole fractal
we are visualizing.
"""

start_x = -0.4 - 2 
start_y = 0.6 - 2
end_x = -0.4 + 2
end_y = 0.6 + 2

"""
The discrete grid - We create points in our rectangle. The goal is to have one
point per pixel in the image, hence we need as many points as the resolution of
the image.
"""
complex_grid_x = np.linspace(start_x, end_y, res_x)
compley_grid_y = np.linspace(start_y, end_y, res_y)

"""
We want to create one image for each number of n, in order to see what happens
with the fractal as the number of iterations increase.
"""
for iterations in range(10, 250, 10):
    print 'Computing fractal for %d iterations' % iterations

    """
    We now for each point z = a + ib in the complex plane compute f(z)
    iteratively and see whether it converges or not. If the absolute value of
    z_new is larger than 2, then it must converge, since we are taking powers
    of two.
    """
    for i, a in enumerate(complex_grid_x):
        for j, b in enumerate(complex_grid_x):

            z = complex(a, b)
            z_new = z

            for n in range(iterations):
                if abs(z_new) >= 2:
                    """
                    The functions diverge for the current point z = a + ib.  We
                    calculate a number 'color' between 0 and 1 corresponding to
                    the 'rate of divergence'. This is computed by taking the
                    ratio between current number of iterations n, and the
                    maximum number of iterations.  and set the pixel
                    corresponding to the point z = a + ib to be equal to this
                    color.

                    This is done in the RGB color space.

                    In the case where the functions diverge, we can break the
                    for loop, and continue with the next point z.
                    """
                    color = iteration_count_coloring(n, iterations)
                    pixels[i, j] = (int(255*(1 - color)), int(255*(1 - color)), int(255*(1 - color)))
                    break
                else:
                    """
                    The function has not 'diverged' yet, so we keep iterating.
                    """
                    z_new = complex_function(z_new, c)
            else:
                """
                If the function didnt diverge after the maximum number of iterations,
                then we consider the point as convergent, and chose to not color it.
                """
                pass

    """
    We save the image file with file name including the max number of iterations
    """
    image.save('tmp_%04d.png' % iterations)

# We convert all the tmp_*.png files to a gif
os.system('convert -delay 4 tmp_*.png movie.gif')
