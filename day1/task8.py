moji = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
li = [tango.strip(".,") for tango in moji.split()]
li2 = [1,5,6,7,8,9,15,16,19]
dic = {}
for i in range(len(li)):
  if i+1 in li2:
    dic[i+1] = li[i][0:1]
  else:
    dic[i+1] = li[i][0:2]
print(dic)