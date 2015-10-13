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
res_x = 512
res_y = 512

# Create the image
image = Image.new('RGB', (res_x, res_y), 'black')
pixels = image.load()

# Region of the complex plane we want to visualize
start_x = -2
start_y = -1.5
end_x = 2
end_y = 0.5

dx = float(end_x - start_x) / res_x
dy = float(end_y - start_y) / res_y

# Initial complex number
c = complex(-0.4, 0.6)

complex_grid_x = np.linspace(start_x, end_y, res_x)
compley_grid_y = np.linspace(start_y, end_y, res_y)

for iterations in range(10, 250, 10):
    print iterations
    for i, a in enumerate(complex_grid_x):
        for j, b in enumerate(complex_grid_x):
            z = complex(a, b)
            z_new = z
            for n in range(iterations):
                if abs(z_new) >= 2:
                    color = iteration_count_coloring(n, iterations)
                    pixels[i, j] = (int(255*(1 - color)), int(255*(1 - color)), int(255*(1 - color)))
                    break
                else:
                    z_new = complex_function(z_new, c)
            else:
                color = 0
                pixels[i, j] = (int(255*(1 - color)), int(255*(1 - color)), int(255*(1 - color)))
    
    image.save('tmp_%04d.png' % iterations)

os.system('convert -delay 4 tmp_*.png movie.gif')
