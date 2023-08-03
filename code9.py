#code to check if a number is an armstrong number
x = int(input("Enter a number: "))

sum = 0
temp = x

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if x == sum:
   print(x,"is an Armstrong number")
   
else:
   print(x,"is not an Armstrong number")

   

   
