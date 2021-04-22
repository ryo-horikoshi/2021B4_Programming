import numpy as np

class Sigmoid():
  def __init__(self):
    self.x = None
  def forward(self, x):
    
    z = 1/(1 + np.exp(-x))
    self.x = z
    return z
  def backprop(self, dz):

    dx = dz * (1.0 - self.x) * self.x

    return dx

x = np.array([-0.5, 0.0, 1.0, 2.0])

task33 = Sigmoid()
print(task33.forward(x))
print(task33.backprop(np.array([1.0, 1.0, 1.0, 1.0])))