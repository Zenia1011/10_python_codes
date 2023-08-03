#code to check minimum number between three numbers
a = int (input("enter number1: "))
b = int(input("enter number2: "))
c = int (input("enter number3: "))

def minimum(a,b,c):
  if (a <= b) and (a <= c):
        smallest = a

  elif (b <= a) and (b <= c):
        smallest = b

  else:
        smallest = c
        
  return smallest

print("minimum number among the three is: ",minimum(a, b, c))




