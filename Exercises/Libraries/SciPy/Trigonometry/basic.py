import numpy as np 

angle = np.pi/2

# takes angle and returns in radians
print(np.sin(angle))
print(np.cos(angle))
print(np.tan(angle))

# takes values and returns in radians
print(np.arcsin(1))
print(np.arccos(0))
print(np.arctan(1))

# degrees to radians
radians = np.radians(90) # can also use deg2rad
print(np.sin(radians))

# radians to degrees
ang = np.pi
print(ang)
print(np.rad2deg(ang))

# hyperbolic
print(np.sinh(1))
print(np.cosh(0))
print(np.tanh(0))