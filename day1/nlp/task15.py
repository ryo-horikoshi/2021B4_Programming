import task13
import task14
import numpy as np

def tfidf(terms,docs):
  ans = np.zeros((len(terms),len(docs)))
  idf = []
  tf = []
  for i in range(len(terms)):
    idf.append(task14.idf(terms[i],docs))

  for i in range(len(terms)):
    tfs = []
    for j in range(len(docs)):
      tfs.append(task13.tf(terms[j],docs[i]))
    tf.append(tfs)
  np_idf = np.array(idf)
  np_tf = np.array(tf)
  return np_tf*np_idf



docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]
