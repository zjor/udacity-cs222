#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

earth_mass = 5.97e24 # kg
spacecraft_mass = 30000. # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

M = earth_mass
m = spacecraft_mass
G = gravitational_constant
steps = 20000
h = 5.0

def gravity(location):
	return - G * M * m * location / np.linalg.norm(location) ** 3

x = np.zeros((steps + 1, 2))
v = np.zeros((steps + 1, 2))

x[0, 0] = 15e6
x[0, 1] = 1e6
v[0, 0] = 2e3
v[0, 1] = 4e3

for i in range(steps):
	x[i + 1] = x[i] + h * v[i]
	v[i + 1] = v[i] + h * gravity(x[i + 1]) / m

plt.plot(x[:, 0], x[:, 1])
plt.scatter(0, 0)
plt.show()



