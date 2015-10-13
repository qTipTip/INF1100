import shutil, os, glob

from scitools.std import plot, movie
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
if os.path.isdir(subdir): # if already present, remove the directory
    shutil.rmtree(subdir)
os.mkdir(subdir) # create directory
os.chdir(subdir) # enter new directory

# Here we let the time t vary, and save a new plot for each value of t.
counter = 0
for t_value in t:
    y = f(x, t_value)
    plot(x, y, 'r-', axis=[x[0], x[-1], -1, 4], xlabel="x", ylabel="y",
         t="%2.2f" % t_value, savefig="tmp%04d" % counter) # saves as png by default
    counter += 1

movie('tmp*.png', encode='convert', fps=24, output_file='animation.gif')

# Remove all the image files and change back to previous directory
for a in glob.glob('tmp*.png'):
    os.remove(a)
os.chdir(os.pardir)
