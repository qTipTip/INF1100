# Animating fractals

This python program is ment as a supplement to the animation programs in given
in the book and mostly for fun. It gives an example of other ways we can
visualize mathematical concepts using animation and python.
This program uses the Python Image Library (PIL), which is another way of visualizing
things in Python. We can, using this library, generate an image by specifiying the color
of each pixel.

In this program we visualize the effect of increasing the number of iterations
under fractal computation.

## What is a fractal?

A fractal is located in the complex plane. The most famous fractal is the
Mandelbrot fractal. In a fractal, we look at a function f and iterated evaluations
of this function. In our example program, we use the function f(z, c) = z^2 +
c. We wish to assign a color to each point in the complex plane.

We let z be a complex number, and plug it into the function.  We get a new complex
number w1. Take this w1 and plug it into the same function and we get a new complex
number w3. Keep doing this n times.

This sequence of complex numbers either **diverges** or **converges**. If it
diverges, we assign it a color. If it converges we leave it as is.

## How do we implement this?

We want to look at a **region** in the complex plane. We obviously can't look
at every single complex number, so we **discretize** this region. This
essentially means we just create a grid of points in the complex plane.  Just
as we **discretize** functions when plotting them, since we cant plot for every
single real number in an interval. 

We therefore create an array of x-coordinates, and an array of y-coordinates
which defines a set of points in the complex planes. This is done using
`np.linspace`. We can now loop over points in our grid using two for loops.
The number of elements in these arrays directly correspond to the number of
pixels in our image.

For each complex number we iterate over, we want to apply the function to this
complex value several times. Obviously, we can't do this for ever, so we define
a maximum number of iterations. The larger the number of iterations is, the
better the fractal looks.


