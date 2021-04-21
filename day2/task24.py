import numpy as np

class MLP_3Layer:
  def __init__(self,W1,b1,W2,b2,W3,b3):
    self.x = x
    self.W1 = W1
    self.b1 = b1
    self.W2 = W2
    self.b2 = b2
    self.W3 = W3
    self.b3 = b3
  
  def forward(self,x):
    a1 = np.dot(W1.T, x.T).T + b1
    a2 = np.dot(W2.T, a1.T).T + b2
    a3 = np.dot(W3.T, a2.T).T + b3
    return a3

x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

task24 = MLP_3Layer(W1,b1,W2,b2,W3,b3)
print(task24.forward(x))