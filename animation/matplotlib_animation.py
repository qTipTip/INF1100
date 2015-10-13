import matplotlib.pyplot as plt
import shutil, glob, os
from numpy import *

def f(x, s):
    """
    The function we wish to animate. Notice that it is vectorized using math
    functions from numpy.
    """
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*(x/s)**2)

x = linspace(-6, 6, 1000)
t = linspace(0, 1, 60)

# In order to avoid cluttering our current folder, we create a new folder
# 'animation' that will store all the image files. We also have to enter
# this new directory
subdir = 'animation'
if os.path.isdir(subdir): # if the directory is already present, remove it
    shutil.rmtree(subdir)
os.mkdir(subdir) # create directory
os.chdir(subdir) # enter new directory

plt.ion() #turn matplotlib interactive mode on
lines = plt.plot(x, zeros_like(x))
plt.axis([x[0], x[-1], -1, 4])

# Here we let the time t vary, and save a new plot for each value of t.
counter = 0
for t_value in t:
    y = f(x, t_value)
    lines[0].set_ydata(y)
    plt.draw()
    plt.savefig('tmp_%04d.png' % counter)
    counter += 1

cmd = 'convert -delay 4 tmp_*.png movie.gif'
os.system(cmd)

# Remove all the image files and change back to previous directory
for a in glob.glob('tmp*.png'):
    os.remove(a)
os.chdir(os.pardir)
