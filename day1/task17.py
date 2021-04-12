import numpy as np
from nlp import task16
from nlp import task15

def make_terms(li):
  li2 = sum(li,[])
  term = []
  for i in range(len(li2)):
    if li2[i] not in term:
      term.append(li2[i])
  return term

f = open('dataset/data.txt', 'r')
docs = []
while True:
  data = f.readline().rstrip('\n')
  if data:
    docs.append(data.split('と'))
  else:
    break
terms = make_terms(docs)

tfidf = task15.tfidf(terms,docs)

print (tfidf)

ans = []
anss = []
for i in range(len(tfidf)):
  ans = []
  for j in range(len(tfidf)):
    ans.append(task16.cosine_sim(tfidf[i],tfidf[j]))
  anss.append(ans)

print(anss)


