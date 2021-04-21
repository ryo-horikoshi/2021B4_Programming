import numpy as np

def softmax(x):
  return np.exp(x) / np.sum(np.exp(x), axis = 1, keepdims = True) 

def cross_entropy_error(y, t) :
  return -np.sum(t * np.log(y))

class SoftmaxCrossEntropy():
  def __init__(self):
    self.x = None
    self.t = None
    self.y = None
    self.z = None

  def forward(self, x, t):
    self.x = x
    self.t = t
    self.y = softmax(x)
    z = cross_entropy_error( self.y , t) / len(x)
    self.z = z
    return z

  def backprop(self):
    dx = self.y - self.t
    return dx

x = np.array([[1.0, 0.5], [-0.4, 0.1]])
t = np.array([[1.0, 0.0], [0.0, 1.0]])

task35 = SoftmaxCrossEntropy()
print(task35.forward(x,t))
print(task35.backprop())