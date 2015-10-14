import numpy as np
import os
from PIL import Image

def complex_function(z, c):
    return z*z + c

def iteration_count_coloring(iterations, max_iterations):
    return iterations / float(max_iterations)

bailout_value = 2

res_x = 1024
res_y = 1024

image = Image.new('RGB', (res_x, res_y), 'black')
pixels = image.load()

c = complex(-0.4, 0.6)

start_x = -0.4 - 2 
start_y = 0.6 - 2
end_x = -0.4 + 2
end_y = 0.6 + 2

complex_grid_x = np.linspace(start_x, end_y, res_x)
compley_grid_y = np.linspace(start_y, end_y, res_y)

for iterations in range(10, 250, 10):
    print 'Computing fractal for %d iterations' % iterations

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
                pass

    image.save('tmp_%04d.png' % iterations)

os.system('convert -delay 4 tmp_*.png movie.gif')
