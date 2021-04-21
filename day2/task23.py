import task22
import numpy as np

class SingleLayer:
  def __init__(self,x,W,b):
    self.x = x
    self.W = W
    self.b = b
  
  def calc(self):
    return task22.relu(np.dot(W.T,x) + b)

x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])
task23 = SingleLayer(x,W,b)
print(task23.calc())