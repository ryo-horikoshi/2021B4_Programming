from dataset.mnist import load_mnist
import numpy as np
import task41
import matplotlib.pyplot as plt

def make_onehot(labels):
  one_hot_labels = np.zeros((10))
  one_hot_labels[labels] = 1
  return one_hot_labels


(train_images, train_labels), (test_images, test_labels)  = load_mnist()

bias = 0
batch_size = 100
epoc_size = 100
learning_rate = 0.0001
standard＿deviation = 0.1
learning_num = 30

in_size = 784
hide_size = 500
out_size = 10

sample = np.random.randint(0, 60000, (100,))
ans_label = make_onehot(train_labels[0])
print(ans_label.shape)

NeuralNetwork = task41.NeuralNetwork(bias,standard＿deviation,in_size,hide_size,out_size)

for i in range(learning_num):
  print("%d週目" %(i+1))
  NeuralNetwork.acc = 0
  NeuralNetwork.nums = 0    
  x = np.empty((784,), float)
  t = np.empty((10,), int)
  sample = np.random.randint(0, 10000, (100,))
  for j in range(len(sample)):
    t = np.append(t,make_onehot(train_labels[sample[j]].T) , axis=0)
    x = np.append(x,train_images[sample[j]].T , axis=0)
  x = np.delete(x.reshape(101,784), 0, 0)
  t = np.delete(t.reshape(101,10), 0, 0)
  for k in range(epoc_size):
    #NeuralNetwork.forward(x)
    #NeuralNetwork.loss(x,t)
    #NeuralNetwork.backprop(x,t)

    NeuralNetwork.sgd(x,t,learning_rate)
  print(NeuralNetwork.losscost)
  print(NeuralNetwork.acc / NeuralNetwork.nums * 100)

##########テスト用############
#plt.imshow(x[0].reshape(28, 28), cmap='Greys')
#plt.show()

NeuralNetwork.acc = 0
NeuralNetwork.nums = 0    
x = np.empty((784,), float)
t = np.empty((10,), int)
sample = np.random.randint(0, 60000, (100,))
for j in range(len(sample)):
  t = np.append(t,make_onehot(test_labels[sample[j]].T) , axis=0)
  x = np.append(x,test_images[sample[j]].T , axis=0)
x = np.delete(x.reshape(101,784), 0, 0)
t = np.delete(t.reshape(101,10), 0, 0)
NeuralNetwork.sgd(x,t,learning_rate)
print("テスト")
print(NeuralNetwork.losscost)
print(NeuralNetwork.acc / NeuralNetwork.nums * 100)


