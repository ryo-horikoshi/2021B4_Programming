import numpy as np
import task24

def softmax(x):
  return np.exp(x) / np.sum(np.exp(x), axis = 1, keepdims = True)

class MLP_3Layer(task24.MLP_3Layer):
  def forward(self,x):
    a1 = np.dot(W1.T, x.T).T + b1
    a2 = np.dot(W2.T, a1.T).T + b2
    a3 = np.dot(W3.T, a2.T).T + b3
    return softmax(a3)
  
x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

task25 = MLP_3Layer(W1,b1,W2,b2,W3,b3)
print(task25.forward(x))


