import matplotlib.pyplot as plt
import numpy as np

def read_file(filename):
    """
    reads the output of lnsum.py
    and extracts numbers corresponding to epsilon, exact error
    and n.
    """
    epsilon = []
    exact_error = []
    n = []
    with open(filename, 'r') as infile:
        for line in infile:
            if 'epsilon' in line:
                line = line.split()
                epsilon.append(float(line[1].strip(',')))
                exact_error.append(float(line[4].strip(',')))
                n.append(float(line[-1].strip('=n')))
                
    return np.array(epsilon), np.array(exact_error), np.array(n)

eps, exact, n = read_file('lnsum.dat')

plt.semilogy(n, eps, 'ro-', n, exact, 'bo-')
plt.xlabel('n')
plt.title('epsilon and exact error versus n on a semi-log scale')
plt.legend(['epsilon', 'exact error'])
plt.show()
