import numpy as np

class Affine():
  def __init__(self):
    self.z = None
    self.x = None
    self.W = None
    self.b = None
  def forward(self, x, W, b):
    z = np.dot(x,W) + b
    self.z = z
    return z
  def backprop(self, dz):
    dx = np.dot(dz, W.T)
    dw = np.dot(x.T, dz)
    db = np.sum(dz, axis=0)
    return [dx,dw,db]

x = np.array([[1.0, 0.5], [-0.4, 0.1]])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

task34 = Affine()
print(task34.forward(x,W,b))
print(task34.backprop([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]))