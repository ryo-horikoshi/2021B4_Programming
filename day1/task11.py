f = open('./dataset/data.txt', 'r')
while True:
  data = f.readline()
  if data:
    print(data,end='')
  else:
    break