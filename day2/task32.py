import numpy as np

class ReLU():
  def __init__(self):
    self.mask = None
  def forward(self, x):
    self.mask = (x<=0)
    z = np.maximum(0, x) 
    return z
  def backprop(self, dz):
    dz[self.mask] = 0
    return dz

x = np.array([-0.5, 0.0, 1.0, 2.0])
task32 = ReLU()
print(task32.forward(x))
print(task32.backprop(np.array([1.0, 1.0, 1.0, 1.0])))
