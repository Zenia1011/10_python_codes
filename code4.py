# Sum of natural numbers up to number
x = int(input("enter a number: "))

if x < 0:
   print("Enter a positive number")
   
else:
   sum = 0
   while(x > 0):
       sum += x
       x -= 1
       
   print("The sum is", sum)

   

   

