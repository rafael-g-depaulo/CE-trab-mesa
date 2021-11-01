import numpy as np
import random

# Creating a Function.
def normal_dist(x, mean, sd):
  prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
  return prob_density

def randomColor():
  r = lambda: random.randint(0,255)
  return '#%02X%02X%02X' % (r(),r(),r())
