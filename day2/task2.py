import task1

and_gate = task1.Perceptron(1,1,2)
nand_gate = task1.Perceptron(-1,-1.1,-2)
or_gate = task1.Perceptron(1,1,0.5)
x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]
for i in range(len(x1_list)):
  print("AND(%d, %d) = %d " %(x1_list[i],x2_list[i],and_gate.forward(x1_list[i],x2_list[i])) , end = '')
  print("NAND(%d, %d) = %d " %(x1_list[i],x2_list[i],nand_gate.forward(x1_list[i],x2_list[i])) , end = '')
  print("OR(%d, %d) = %d " %(x1_list[i],x2_list[i],or_gate.forward(x1_list[i],x2_list[i])))