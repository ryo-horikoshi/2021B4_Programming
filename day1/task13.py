def tf(term, doc):
  count = 0
  for i in range(len(doc)):
    if term == doc[i]:
      count += 1
  return(count/len(doc))




docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

