import task33
import task34
import task35
import numpy as np

class NeuralNetwork:
  def __init__(self,bias,standard＿deviation,in_size,hide_size,out_size):
    self.params = {}
    self.grads = {}
    self.params['W1'] = standard＿deviation *  np.random.randn(in_size,hide_size)
    self.params['b1'] = np.zeros(hide_size)
    self.params['W2'] = standard＿deviation *  np.random.randn(in_size,hide_size)
    self.params['b2'] = np.zeros(hide_size)
    self.grads['W2'] = None
    self.grads['b2'] = None
    self.grads['W1'] = None
    self.grads['b1'] = None
    self.acc = 0
    self.Sigmoid = task33.Sigmoid()
    self.Affine = task34.Affine()
    self.SoftmaxCrossEntropy = task35.SoftmaxCrossEntropy()

  def forward(self, x):
    W1, W2 = self.params['W1'],self.params['W2']
    b1, b2 = self.params['b1'],self.params['b2']
    a1 = Affine.forward(x,W1,b1)
    z1 = Sigmoid.forward(a1)
    a2 = Affine.forward(z1,W2,b2)
    z2 = Sigmoid.forward(a2)
    return z2

  def loss(self, x, t):
    y = forward(x)
    y_class = np.argmax(task35.softmax(y))
    y_class = y_class.astype("int8")
    ans = np.identity(10, dtype = "int8")[y_class]
    if(np.allclose(ans, t)):
      self.acc += 1
    return SoftmaxCrossEntropy(y,t)

  def backprop(self, x, t):
    loss(x,t)
    dx1 = SoftmaxCrossEntropy.backprop()
    dx2 = Sigmoid.backprop(dx1)
    dx3 = Affine.backprop(dx2)[0]
    self.grads['W2']  = Affine.backprop(dx2)[1]
    self.grads['b2']  = Affine.backprop(dx2)[2]
    dx4 = Sigmoid.backprop(dx3)
    dx5 = Affine.backprop(dx4)[0]
    self.grads['W1']  = Affine.backprop(dx4)[1]
    self.grads['b1']  = Affine.backprop(dx4)[2]

  def sgd(self, x, t, learning_rate):
    backprop(x,t)
    for key in params.keys():
      params[key] -= self.learning_rate * grads[key]

