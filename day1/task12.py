def make_terms(li):
  li2 = sum(li,[])
  term = []
  for i in range(len(li2)):
    if li2[i] not in term:
      term.append(li2[i])
  return term

f = open('./dataset/data.txt', 'r')
docs = []
while True:
  data = f.readline().rstrip('\n')
  if data:
    docs.append(data.split('と'))
  else:
    break
  
print(docs)
print(make_terms(docs))