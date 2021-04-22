import task32
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
    self.params['W2'] = standard＿deviation *  np.random.randn(hide_size,out_size)
    self.params['b2'] = np.zeros(out_size)
    self.grads['W2'] = None
    self.grads['b2'] = None
    self.grads['W1'] = None
    self.grads['b1'] = None
    self.acc = 0
    self.nums = 0
    self.losscost = 0
    self.Sigmoid = task33.Sigmoid()
    #self.Sigmoid2 = task33.Sigmoid()
    self.ReLU = task32.ReLU()
    self.Affine = task34.Affine()
    self.Affine2 = task34.Affine()
    self.SoftmaxCrossEntropy = task35.SoftmaxCrossEntropy()

  def softmax(self,x):
    return np.exp(x) / np.sum(np.exp(x), axis = 0, keepdims = True) 

  def forward(self, x):
    W1, W2 = self.params['W1'],self.params['W2']
    b1, b2 = self.params['b1'],self.params['b2']
    a1 = self.Affine.forward(x,W1,b1)
    z1 = self.ReLU.forward(a1)
    a2 = self.Affine2.forward(z1,W2,b2)
    #z2 = self.Sigmoid2.forward(a2)
    return a2

  def loss(self, x, t):
    y = self.forward(x)
    ans = np.copy(y)
    for i in range(len(y)):
      #print(self.softmax(ans[i]))
      ansnum = np.argmax(self.softmax(ans[i]))
      #print(ansnum)
      ans[i] = np.identity(10, dtype = "int8")[ansnum]
      self.nums += 1
      if(np.allclose(ans[i], t[i])):
        self.acc += 1
    self.losscost = self.SoftmaxCrossEntropy.forward(y,t)

  def backprop(self, x, t):
    self.loss(x,t)
    dx1 = self.SoftmaxCrossEntropy.backprop()
    #dx2 = self.Sigmoid2.backprop(dx1)
    dx3 = self.Affine2.backprop(dx1)[0]
    self.grads['W2']  = self.Affine2.backprop(dx1)[1]
    self.grads['b2']  = self.Affine2.backprop(dx1)[2]
    dx4 = self.ReLU.backprop(dx3)
    dx5 = self.Affine.backprop(dx4)[0]
    self.grads['W1']  = self.Affine.backprop(dx4)[1]
    self.grads['b1']  = self.Affine.backprop(dx4)[2]

  def sgd(self, x, t, learning_rate):
    self.backprop(x,t)
    for key in self.params.keys():
      self.params[key] -= learning_rate * self.grads[key]
    

