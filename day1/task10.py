import sys

def n_gram(st,n):
  gram = []
  for i in range(len(st)-n+1):
    gram.append(st[i:i+n])

  return gram

args = sys.argv[1:]
print("単語bi-gram:",end = ' ')
print(n_gram(args,2))

print("文字bi-gram:",end = ' ')
print(n_gram(''.join(args),2))