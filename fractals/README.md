# Animating fractals

This python program is ment as a supplement to the animation programs in given
in the book and mostly for fun. 

In this program we visualize the effect of increasing the number of iterations
under fractal computation.

## What is a fractal?

A fractal is located in the complex plane. The most famous fractal is the
Mandelbrot set. In a fractal, we look at a function f and iterated evaluations
of this function. In our example program, we use the function f(z, c) = z^2 +
c.  We wish to assign a color to each point in the complex plane. 

Let z be a complex number, and plug it into the function.  We get a new complex
number w1. Take this w1 and plug it into the function and we get a new complex
number w3. Keep doing this n times.

This sequence of complex numbers either **diverges** or **converges**. If it
diverges, we assign it a color. If it converges we leave it as is.
