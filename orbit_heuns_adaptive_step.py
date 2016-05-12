#!/usr/bin/env python
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

T = 12500.
earth_mass = 5.97e24 
spacecraft_mass = 1.
gravitational_constant = 6.67e-11 

M = earth_mass
m = spacecraft_mass
G = gravitational_constant
steps = 20000
h = 5.0

def gravity(location):
	return - G * M * m * location / np.linalg.norm(location) ** 3

x = np.zeros(2)
v = np.zeros(2)
x[0] = 15e6
x[1] = 1e6    
v[0] = 2e3
v[1] = 4e3
plt.scatter(x[0], x[1], s = 4)
t = 0.
h = 100. 
h_new = h 
tolerance = 5e5

while t < T:
    g = gravity(x)    
    xE = x + h * v
    vE = v + h * g
    xH = x + h * 0.5 * (v + vE)
    vH = v + h * 0.5 * (g + gravity(xE))
    x = xH
    v = vH

    error = np.linalg.norm(xE - xH) + T * np.linalg.norm(vE - vH)
    h_new =  math.sqrt(tolerance / error)

    plt.scatter(x[0], x[1], s = 1)
    t += h
    h = h_new

plt.axis('equal')
plt.scatter(0., 0.) 
axes = plt.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')
plt.show()




