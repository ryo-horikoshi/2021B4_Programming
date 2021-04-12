for i in range(1,31):
  fizz = 1 if i % 3 == 0 else 0
  buzz = 1 if i % 5 == 0 else 0
  if(fizz and buzz):
    print("FizzBuzz")
  elif(fizz):
    print("Fizz")
  elif(buzz):
    print("Buzz")
  else:
    print(i)
  print("\n")