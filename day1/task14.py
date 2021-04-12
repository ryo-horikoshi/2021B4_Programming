import numpy as np

def idf(term, docs):
  count = 0
  for i in range(len(docs)):
    if term in docs[i]:
      count += 1

  return(np.log10(len(docs) / count) + 1)




docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

print(idf(terms[1],docs))