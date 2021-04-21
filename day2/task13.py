import task11

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

def xor(x1,x2):
  and_gate = task11.Perceptron(1,1,2)
  nand_gate = task11.Perceptron(-1,-1.1,-2)
  or_gate = task11.Perceptron(1,1,0.5)

  return(and_gate.forward( nand_gate.forward( x1 , x2 ) , or_gate.forward( x1 , x2 ) ))


for i in range(len(x1_list)):
  print("XOR(%d, %d) = %d " %(x1_list[i],x2_list[i], xor(x1_list[i],x2_list[i])))