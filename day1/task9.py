import sys
import random

args = sys.argv[1:]
for i in range(len(args)):
  if len(args[i]) > 3:
    args[i] = ''.join(random.sample(args[i], len(args[i])))

sr = ' '.join(args)
print(sr)