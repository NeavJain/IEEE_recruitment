import matplotlib.pyplot as mpl
import numpy as np
import math 
test = np.random.randn(1000)
x = np.mean(test)
y = np.std(test)
z = (1/(y*math.sqrt(2*math.pi))) * np.exp(-((test - x)**2)/(2*y**2))  #normal distribution formula

mpl.figure() 
mpl.title("Normal Distribution")
mpl.scatter(test,z, s=5)   #creates a scatter plot , s means size
mpl.xlabel("Numbers")
mpl.ylabel("Probability density")
mpl.show()