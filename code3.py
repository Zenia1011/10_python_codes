#code to check if a number is a prime number
x = int(input("enter number1: "))
y = int(input("enter number2: "))
print("The prime numbers between", x, "and", y, "are:")

for z in range(x, y + 1):
   if z > 1:
       for i in range(2,z):
           if (z % i) == 0:
               break
       else:
           print(z)
           

           
