from mnist import load_mnist
import numpy as np

mnist = load_mnist()

mnist["train_img"] # 訓練データ画像 [60000, 784]
mnist["train_label"] # 訓練データラベル [60000, 10]
mnist["test_img"] # テストデータ画像 [10000, 784]
mnist["test_label"] # テストラベル [10000, 10]

batch_size = 100
epoc_size = 100
learning_rate = 0.0001
standard＿deviation = 0.1

sample = np.random.randint(0, 600000, (100))
print(mnist["train_label"][sample[0]])
